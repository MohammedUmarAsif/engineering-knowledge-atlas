// Provider-neutral model and tool contracts. C++20, standard library only.

#include <iostream>
#include <stdexcept>
#include <string>
#include <unordered_set>

struct GenerationRequest {
    std::string task;
    std::string user_input;
    std::string tenant_id;
};

struct ModelResult {
    std::string text;
    std::string model;
    std::string finish_reason;
};

class ModelAdapter {
public:
    virtual ~ModelAdapter() = default;
    virtual ModelResult generate(const GenerationRequest& request) = 0;
};

class FakeModelAdapter final : public ModelAdapter {
public:
    ModelResult generate(const GenerationRequest& request) override {
        return {
            .text = "Summary: " + request.user_input,
            .model = "fake-model-v1",
            .finish_reason = "stop",
        };
    }
};

std::string validate_answer(const ModelResult& result) {
    if (result.finish_reason != "stop") {
        throw std::runtime_error("incomplete generation: " + result.finish_reason);
    }
    if (!result.text.starts_with("Summary:")) {
        throw std::runtime_error("result violates the domain response contract");
    }
    if (result.text.size() > 500) {
        throw std::runtime_error("result exceeds the product limit");
    }
    return result.text;
}

struct ToolProposal {
    std::string name;
    std::string order_id;
    std::string idempotency_key;
};

class RefundExecutor {
public:
    std::string execute(
        const ToolProposal& proposal,
        const std::string& authenticated_tenant,
        const std::string& order_tenant,
        bool approved
    ) {
        if (proposal.name != "refund_order") {
            throw std::invalid_argument("unsupported tool");
        }
        if (authenticated_tenant != order_tenant) {
            throw std::runtime_error("cross-tenant access denied");
        }
        if (!approved) {
            throw std::runtime_error("refund requires approval");
        }
        if (completed_.contains(proposal.idempotency_key)) {
            return "already_completed";
        }

        // A real implementation would use a database transaction and unique key.
        completed_.insert(proposal.idempotency_key);
        return "refunded:" + proposal.order_id;
    }

private:
    std::unordered_set<std::string> completed_;
};

int main() {
    FakeModelAdapter adapter;
    const GenerationRequest request{
        .task = "summarize",
        .user_input = "A model proposal is not authorization.",
        .tenant_id = "tenant-a",
    };
    std::cout << validate_answer(adapter.generate(request)) << '\n';

    RefundExecutor executor;
    const ToolProposal proposal{
        .name = "refund_order",
        .order_id = "order-42",
        .idempotency_key = "refund-order-42-v1",
    };
    std::cout << executor.execute(proposal, "tenant-a", "tenant-a", true) << '\n';
    std::cout << executor.execute(proposal, "tenant-a", "tenant-a", true) << '\n';
}
