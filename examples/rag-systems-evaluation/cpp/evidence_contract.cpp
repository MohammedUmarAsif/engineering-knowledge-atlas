// Minimal evidence/citation contract. C++20, standard library only.

#include <algorithm>
#include <cctype>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

struct Evidence {
    std::string id;
    std::string source;
    std::string text;
};

struct Claim {
    std::string text;
    std::vector<std::string> evidence_ids;
};

std::unordered_set<std::string> terms(const std::string& text) {
    std::istringstream input{text};
    std::unordered_set<std::string> result;
    std::string word;
    while (input >> word) {
        std::ranges::transform(word, word.begin(), [](unsigned char value) {
            return static_cast<char>(std::tolower(value));
        });
        if (word.size() > 3) result.insert(word);
    }
    return result;
}

void validate_claim(const Claim& claim, const std::vector<Evidence>& evidence) {
    std::unordered_map<std::string, const Evidence*> by_id;
    for (const auto& item : evidence) by_id[item.id] = &item;
    if (claim.evidence_ids.empty()) throw std::runtime_error("claim has no evidence");

    std::string support_text;
    for (const auto& id : claim.evidence_ids) {
        const auto found = by_id.find(id);
        if (found == by_id.end()) throw std::runtime_error("unknown evidence id: " + id);
        support_text += " " + found->second->text;
    }

    const auto claim_terms = terms(claim.text);
    const auto support_terms = terms(support_text);
    std::size_t overlap = 0;
    for (const auto& term : claim_terms) if (support_terms.contains(term)) ++overlap;
    if (overlap < 2) throw std::runtime_error("claim lacks minimal lexical support");
}

std::string render(const Claim& claim, const std::vector<Evidence>& evidence) {
    validate_claim(claim, evidence);
    std::unordered_map<std::string, const Evidence*> by_id;
    for (const auto& item : evidence) by_id[item.id] = &item;
    std::string output = claim.text + " [";
    for (std::size_t index = 0; index < claim.evidence_ids.size(); ++index) {
        if (index > 0) output += ", ";
        output += by_id.at(claim.evidence_ids[index])->source;
    }
    return output + "]";
}

int main() {
    const std::vector<Evidence> evidence{{"e1", "Policy p.4", "Refunds require manager approval."}};
    const Claim claim{"A refund requires manager approval.", {"e1"}};
    std::cout << render(claim, evidence) << '\n';
}
