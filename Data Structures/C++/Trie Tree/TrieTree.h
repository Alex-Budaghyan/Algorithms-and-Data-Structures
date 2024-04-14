//
// Created by Dell on 12/16/2023.
//

#ifndef DATA_STRUCTURE_C_TRIETREE_H
#define DATA_STRUCTURE_C_TRIETREE_H

#endif //DATA_STRUCTURE_C_TRIETREE_H

#include "TrieNode.h"

#include <unordered_map>
#include <string>
#include <queue>
#include <iostream>
template <typename T>
class TrieTree
{
public:
    TrieTree();

    // Iterative
    void insert(const std::basic_string<T>& word) const;

    bool search_prefix(const std::basic_string<T>& prefix) const;
    bool search_word(const std::basic_string<T>& word) const;
    void levelorder() const;
    std::basic_string<T> longestCommonPrefix(const std::vector<std::basic_string<T>>& strs) const;

    // Recursive
    void removeR(const std::basic_string<T>& word);
    void insertR(const std::basic_string<T>& word);

private:
    TrieNode<T>* insertHelper(TrieNode<T>* p, const std::basic_string<T>& word, int index);
    bool removeHelper(TrieNode<T>* p, const std::basic_string<T>& word, int index);

private:
    TrieNode<T>* m_root;
};

// Template definition for TrieTree
template <typename T>
TrieTree<T>::TrieTree()
{
    m_root = new TrieNode<T>();
}

template <typename T>
void TrieTree<T>::insert(const std::basic_string<T>& word) const {
    TrieNode<T>* curr = m_root;
    for (int i = 0; i < word.length(); ++i)
    {
        if (curr->children.find(word[i]) == curr->children.end())
        {
            curr->children[word[i]] = new TrieNode<T>();
        }
        curr = curr->children[word[i]];
    }
    curr->isWord = true;
}

template <typename T>
void TrieTree<T>::insertR(const std::basic_string<T>& word)
{
    insertHelper(m_root, word, 0);
}

template <typename T>
TrieNode<T>* TrieTree<T>::insertHelper(TrieNode<T>* p, const std::basic_string<T>& word, int index)
{
    if (index == word.length())
    {
        p->isWord = true;
        return p;
    }

    T ch = word[index];
    TrieNode<T>* node = p->children[ch];
    if (node == nullptr) {
        node = new TrieNode<T>();
        p->children[ch] = node;
    }

    // Fix the recursive call by incrementing the index
    return insertHelper(node, word, index + 1);
}

template <typename T>
bool TrieTree<T>::search_prefix(const std::basic_string<T>& prefix) const
{
    TrieNode<T>* current = m_root;

    for (T ch : prefix)
    {
        if (current->children.find(ch) == current->children.end()) {
            return false;
        }
        current = current->children[ch];
    }

    return true;
}

template <typename T>
bool TrieTree<T>::search_word(const std::basic_string<T>& word) const
{
    TrieNode<T>* current = m_root;

    for (T ch : word)
    {
        if (current->children.find(ch) == current->children.end()) {
            return false;
        }
        current = current->children[ch];
    }
    return current->isWord;
}

template <typename T>
void TrieTree<T>::removeR(const std::basic_string<T>& word)
{
    removeHelper(m_root, word, 0);
}

template <typename T>
bool TrieTree<T>::removeHelper(TrieNode<T>* p, const std::basic_string<T>& word, int index)
{
    if (p == nullptr) {
        return false;  // Word not found in the Trie
    }

    if (index == word.length()) {
        if (!p->isWord) {
            return false;  // Word not found in the Trie
        }
        p->isWord = false;

        // If p has no other children, it can be safely removed
        return p->children.empty();
    }

    T ch = word[index];
    if (removeHelper(p->children[ch], word, index + 1)) {
        // Remove the child node
        delete p->children[ch];
        p->children.erase(ch);

        // If p has no other children and is not the end of another word, it can be safely removed
        return p->children.empty() && !p->isWord;
    }

    return false;
}

template <typename T>
void TrieTree<T>::levelorder() const {
    if (!m_root) {
        return;
    }

    std::queue<TrieNode<T>*> q;
    q.push(m_root);

    while (!q.empty()) {
        size_t levelSize = q.size();

        for (size_t i = 0; i < levelSize; ++i) {
            TrieNode<T>* current = q.front();
            q.pop();

            std::cout << "{ ";
            for (const auto& child : current->children) {
                std::cout << child.first << " ";
                q.push(child.second);
            }
            std::cout << "} ";
        }

        std::cout << std::endl;
    }
}


template <typename T>
std::basic_string<T> TrieTree<T>::longestCommonPrefix(const std::vector<std::basic_string<T>>& strs) const
{
    if (strs.empty()) {
        return std::basic_string<T>();
    }

    for (const std::basic_string<T>& word : strs) {
        insert(word);  // Insert each word into the Trie
    }

    TrieNode<T>* current = m_root;
    std::basic_string<T> commonPrefix;

    // Traverse the Trie until a node has more than one child or reaches the end of a word
    while (current->children.size() == 1 && !current->isWord) {
        for (const auto& child : current->children) {
            commonPrefix.push_back(child.first);
            current = child.second;
        }
    }

    return commonPrefix;
}