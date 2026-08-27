#include <chrono>
#include <iostream>
#include <memory>
#include <mutex>
#include <optional>
#include <stdexcept>
#include <string>
#include <unordered_map>

enum class Rejection { Expired, TooLarge, TenantBusy, Overloaded };

struct Request {
    std::string tenant;
    int input_tokens;
    int max_output_tokens;
    std::chrono::steady_clock::time_point deadline;
};

class AdmissionController;

class Lease {
  public:
    Lease(AdmissionController& controller, std::string tenant);
    Lease(const Lease&) = delete;
    Lease& operator=(const Lease&) = delete;
    Lease(Lease&& other) noexcept;
    Lease& operator=(Lease&&) = delete;
    ~Lease();

  private:
    AdmissionController* controller_;
    std::string tenant_;
};

struct Decision {
    std::unique_ptr<Lease> lease;
    std::optional<Rejection> rejection;
    [[nodiscard]] bool accepted() const { return lease != nullptr; }
};

class AdmissionController {
  public:
    AdmissionController(int global_limit, int tenant_limit, int token_limit)
        : global_limit_(global_limit), tenant_limit_(tenant_limit), token_limit_(token_limit) {
        if (global_limit <= 0 || tenant_limit <= 0 || token_limit <= 0) {
            throw std::invalid_argument("limits must be positive");
        }
    }

    Decision admit(const Request& request, std::chrono::steady_clock::time_point now) {
        if (request.deadline <= now) return {nullptr, Rejection::Expired};
        if (request.input_tokens + request.max_output_tokens > token_limit_) {
            return {nullptr, Rejection::TooLarge};
        }
        std::lock_guard<std::mutex> guard(mutex_);
        const int tenant_count = tenant_in_flight_[request.tenant];
        if (tenant_count >= tenant_limit_) return {nullptr, Rejection::TenantBusy};
        if (global_in_flight_ >= global_limit_) return {nullptr, Rejection::Overloaded};
        ++global_in_flight_;
        tenant_in_flight_[request.tenant] = tenant_count + 1;
        return {std::make_unique<Lease>(*this, request.tenant), std::nullopt};
    }

    void release(const std::string& tenant) noexcept {
        std::lock_guard<std::mutex> guard(mutex_);
        auto it = tenant_in_flight_.find(tenant);
        if (it == tenant_in_flight_.end() || global_in_flight_ <= 0) {
            std::terminate();  // Internal invariant violation; destructors must not throw.
        }
        if (--it->second == 0) tenant_in_flight_.erase(it);
        --global_in_flight_;
    }

  private:
    int global_limit_;
    int tenant_limit_;
    int token_limit_;
    int global_in_flight_{0};
    std::unordered_map<std::string, int> tenant_in_flight_;
    std::mutex mutex_;
};

Lease::Lease(AdmissionController& controller, std::string tenant)
    : controller_(&controller), tenant_(std::move(tenant)) {}

Lease::Lease(Lease&& other) noexcept
    : controller_(other.controller_), tenant_(std::move(other.tenant_)) {
    other.controller_ = nullptr;
}

Lease::~Lease() {
    if (controller_) controller_->release(tenant_);
}

int main() {
    AdmissionController controller(2, 1, 4096);
    const auto now = std::chrono::steady_clock::now();
    auto first = controller.admit({"studio-a", 800, 500, now + std::chrono::seconds(2)}, now);
    if (!first.accepted()) return 1;

    auto blocked = controller.admit({"studio-a", 200, 100, now + std::chrono::seconds(2)}, now);
    std::cout << "second request: "
              << (blocked.rejection == Rejection::TenantBusy ? "tenant_busy" : "unexpected")
              << '\n';
    first.lease.reset();

    auto retried = controller.admit({"studio-a", 200, 100, now + std::chrono::seconds(2)}, now);
    std::cout << "retry after release: " << (retried.accepted() ? "accepted" : "rejected") << '\n';
}
