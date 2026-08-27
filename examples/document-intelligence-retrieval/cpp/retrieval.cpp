// Small retrieval mechanics demo. C++20, standard library only.

#include <algorithm>
#include <cctype>
#include <cmath>
#include <iostream>
#include <span>
#include <sstream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

struct Document {
    std::string id;
    std::string tenant;
    std::string text;
    std::vector<double> embedding;
};

using Ranking = std::vector<std::pair<std::string, double>>;
using Postings = std::unordered_map<std::string, std::unordered_set<std::string>>;

std::vector<std::string> tokenize(const std::string& text) {
    std::istringstream input{text};
    std::vector<std::string> tokens;
    std::string token;
    while (input >> token) {
        std::ranges::transform(token, token.begin(), [](unsigned char value) {
            return static_cast<char>(std::tolower(value));
        });
        tokens.push_back(token);
    }
    return tokens;
}

Postings build_inverted_index(const std::vector<Document>& documents) {
    Postings postings;
    for (const auto& document : documents) {
        for (const auto& term : tokenize(document.text)) {
            postings[term].insert(document.id);
        }
    }
    return postings;
}

void sort_ranking(Ranking& ranking) {
    std::ranges::sort(ranking, [](const auto& left, const auto& right) {
        return left.second == right.second ? left.first < right.first
                                           : left.second > right.second;
    });
}

Ranking lexical_search(
    const std::string& query,
    const std::vector<Document>& documents,
    const Postings& postings,
    const std::string& tenant
) {
    std::unordered_set<std::string> allowed;
    for (const auto& document : documents) {
        if (document.tenant == tenant) allowed.insert(document.id);
    }

    std::unordered_map<std::string, double> scores;
    for (const auto& term : tokenize(query)) {
        const auto found = postings.find(term);
        if (found == postings.end()) continue;
        for (const auto& id : found->second) {
            if (allowed.contains(id)) scores[id] += 1.0;
        }
    }

    Ranking ranking{scores.begin(), scores.end()};
    sort_ranking(ranking);
    return ranking;
}

double cosine(std::span<const double> left, std::span<const double> right) {
    if (left.size() != right.size()) throw std::invalid_argument("dimensions differ");
    double dot = 0.0;
    double left_squared = 0.0;
    double right_squared = 0.0;
    for (std::size_t index = 0; index < left.size(); ++index) {
        dot += left[index] * right[index];
        left_squared += left[index] * left[index];
        right_squared += right[index] * right[index];
    }
    if (left_squared == 0.0 || right_squared == 0.0) {
        throw std::invalid_argument("cosine is undefined for a zero vector");
    }
    return dot / (std::sqrt(left_squared) * std::sqrt(right_squared));
}

Ranking dense_search(
    std::span<const double> query,
    const std::vector<Document>& documents,
    const std::string& tenant
) {
    Ranking ranking;
    for (const auto& document : documents) {
        if (document.tenant == tenant) {
            ranking.emplace_back(document.id, cosine(query, document.embedding));
        }
    }
    sort_ranking(ranking);
    return ranking;
}

Ranking reciprocal_rank_fusion(const std::vector<Ranking>& rankings, int constant = 60) {
    std::unordered_map<std::string, double> scores;
    for (const auto& ranking : rankings) {
        for (std::size_t index = 0; index < ranking.size(); ++index) {
            scores[ranking[index].first] += 1.0 / (constant + index + 1.0);
        }
    }
    Ranking fused{scores.begin(), scores.end()};
    sort_ranking(fused);
    return fused;
}

void print_ranking(const std::string& name, const Ranking& ranking) {
    std::cout << name << '\n';
    for (const auto& [id, score] : ranking) std::cout << "  " << id << " " << score << '\n';
}

int main() {
    const std::vector<Document> documents{
        {"d1", "tenant-a", "Refund requests must be idempotent", {0.9, 0.2}},
        {"d2", "tenant-a", "Timeouts need reconciliation before retry", {0.8, 0.5}},
        {"d3", "tenant-b", "Private refund escalation policy", {1.0, 0.1}},
    };
    const auto postings = build_inverted_index(documents);
    const auto lexical = lexical_search("refund timeout", documents, postings, "tenant-a");
    const std::vector<double> query{0.85, 0.35};
    const auto dense = dense_search(query, documents, "tenant-a");
    const auto fused = reciprocal_rank_fusion({lexical, dense});

    print_ranking("lexical", lexical);
    print_ranking("dense", dense);
    print_ranking("fused", fused);
}
