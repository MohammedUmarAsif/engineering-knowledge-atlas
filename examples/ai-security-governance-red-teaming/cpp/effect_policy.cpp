#include <functional>
#include <iostream>
#include <optional>
#include <string>

enum class Risk { Low, High };
enum class Denial { Identity, Tenant, Scope, Expired, Approval };

struct Effect {
    std::string principal;
    std::string tenant;
    std::string tool;
    std::string target;
    std::string payload;
    Risk risk;

    [[nodiscard]] std::size_t binding() const {
        // Demonstration only: std::hash is not a cryptographic approval signature.
        const std::string material = principal + '\x1f' + tenant + '\x1f' + tool + '\x1f' +
                                     target + '\x1f' + payload + '\x1f' +
                                     (risk == Risk::High ? "high" : "low");
        return std::hash<std::string>{}(material);
    }
};

struct Capability {
    std::string principal;
    std::string tenant;
    std::string tool;
    std::string target;
    int expires_at;
};

struct Approval { std::size_t action_binding; };
struct Decision { bool allowed; std::optional<Denial> denial; };

Decision authorize(const Effect& effect, const Capability& capability, int now,
                   const std::optional<Approval>& approval = std::nullopt) {
    if (effect.principal != capability.principal) return {false, Denial::Identity};
    if (effect.tenant != capability.tenant) return {false, Denial::Tenant};
    if (effect.tool != capability.tool || effect.target != capability.target) {
        return {false, Denial::Scope};
    }
    if (now >= capability.expires_at) return {false, Denial::Expired};
    if (effect.risk == Risk::High &&
        (!approval || approval->action_binding != effect.binding())) {
        return {false, Denial::Approval};
    }
    return {true, std::nullopt};
}

int main() {
    const Capability capability{"user-7", "studio-a", "publish_note", "repo/game-docs", 200};
    const Effect proposed{"user-7", "studio-a", "publish_note", "repo/game-docs",
                          "Review draft", Risk::High};

    std::cout << "without approval: " << (authorize(proposed, capability, 100).allowed ? "allow" : "deny") << '\n';
    const Approval approval{proposed.binding()};
    std::cout << "exact approved effect: "
              << (authorize(proposed, capability, 100, approval).allowed ? "true" : "false") << '\n';

    const Effect changed{"user-7", "studio-a", "publish_note", "repo/game-docs",
                         "Changed after review", Risk::High};
    std::cout << "changed payload: "
              << (authorize(changed, capability, 100, approval).allowed ? "allow" : "deny") << '\n';
}
