//
// Created by Dell on 12/16/2023.
//

#ifndef DATA_STRUCTURE_C_TRIENODE_H
#define DATA_STRUCTURE_C_TRIENODE_H

#endif //DATA_STRUCTURE_C_TRIENODE_H

#include <unordered_map>

template <typename T>
struct TrieNode
{
    std::unordered_map<T, TrieNode*> children;
    bool isWord = false;
};