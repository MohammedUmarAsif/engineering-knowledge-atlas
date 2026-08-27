#include <functional>
#include <iostream>
#include <optional>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

enum class RunStatus { Running, WaitingApproval, Completed, Failed, BudgetExhausted };

struct Proposal {
    std::string tool;
    std::unordered_map<std::string, std::string> arguments;
    std::string idempotency_key;
};

struct ToolSpec {
    std::unordered_set<std::string> required_arguments;
    bool writes;
    std::function<std::string(const std::unordered_map<std::string, std::string>&)> execute;
};

struct RunState {
    std::string goal;
    int steps_left;
    RunStatus status{RunStatus::Running};
    std::vector<std::string> observations;
    std::unordered_set<std::string> completed_keys;
    std::optional<Proposal> pending;
};

class Runtime {
  public:
    explicit Runtime(std::unordered_map<std::string, ToolSpec> tools)
        : tools_(std::move(tools)) {}

    void apply(RunState& state, const Proposal& proposal, bool approved = false) const {
        if (state.status != RunStatus::Running && state.status != RunStatus::WaitingApproval) {
            throw std::logic_error("run is terminal");
        }
        if (state.steps_left <= 0) {
            state.status = RunStatus::BudgetExhausted;
            return;
        }
        const auto tool_it = tools_.find(proposal.tool);
        if (tool_it == tools_.end()) {
            fail(state, "unknown tool: " + proposal.tool);
            return;
        }
        for (const auto& key : tool_it->second.required_arguments) {
            if (!proposal.arguments.contains(key)) {
                fail(state, "missing argument: " + key);
                return;
            }
        }
        if (state.completed_keys.contains(proposal.idempotency_key)) {
            state.observations.push_back("duplicate logical operation ignored");
            state.status = RunStatus::Running;
            state.pending.reset();
            return;
        }
        if (tool_it->second.writes && !approved) {
            state.status = RunStatus::WaitingApproval;
            state.pending = proposal;
            return;
        }

        --state.steps_left;
        try {
            const std::string result = tool_it->second.execute(proposal.arguments);
            state.completed_keys.insert(proposal.idempotency_key);
            state.observations.push_back(proposal.tool + ": " + result);
            state.pending.reset();
            state.status = RunStatus::Running;
        } catch (const std::exception& error) {
            fail(state, std::string("tool error: ") + error.what());
        }
    }

    static void complete(RunState& state, const std::function<bool(const RunState&)>& verifier) {
        state.status = verifier(state) ? RunStatus::Completed : RunStatus::Failed;
    }

  private:
    std::unordered_map<std::string, ToolSpec> tools_;

    static void fail(RunState& state, const std::string& message) {
        state.observations.push_back(message);
        state.pending.reset();
        state.status = RunStatus::Failed;
    }
};

int main() {
    std::unordered_map<std::string, ToolSpec> tools{
        {"read_lore", {std::unordered_set<std::string>{"entry_id"}, false, [](const auto& args) {
            return "canon[" + args.at("entry_id") + "] = The bridge opens at dawn";
        }}},
        {"record_note", {std::unordered_set<std::string>{"text"}, true, [](const auto& args) {
            return "stored note: " + args.at("text");
        }}},
    };
    Runtime runtime(std::move(tools));

    RunState state{"read canon and record a verified note", 3};
    runtime.apply(state, {"read_lore", {{"entry_id", "bridge"}}, "read-bridge-1"});
    const Proposal write{"record_note", {{"text", "The bridge opens at dawn"}}, "note-bridge-1"};
    runtime.apply(state, write);
    if (state.status != RunStatus::WaitingApproval || !state.pending) return 1;
    runtime.apply(state, *state.pending, true);
    runtime.apply(state, write, true);
    Runtime::complete(state, [](const RunState& run) {
        for (const auto& item : run.observations) {
            if (item.find("stored note") != std::string::npos) return true;
        }
        return false;
    });

    std::cout << (state.status == RunStatus::Completed ? "completed" : "failed") << '\n';
    for (const auto& item : state.observations) std::cout << "- " << item << '\n';
}
