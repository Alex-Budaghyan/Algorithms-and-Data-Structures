//
// Created by Dell on 12/16/2023.
//

#include "TrieTree.h"


int main() {
    TrieTree<char> trie;  // Specify the template parameter as char
    TrieTree<char> prefix;
    // Insert words into the trie
    trie.insert("apple");
    trie.insert("app");
    trie.insert("bat");
    trie.insert("batman");
    trie.insert("batwoman");

    // Search for words and prefixes
    std::cout << "Search results:" << std::endl;
    std::cout << "Search 'app': " << (trie.search_word("app") ? "Found" : "Not Found") << std::endl;
    std::cout << "Search 'apple': " << (trie.search_word("apple") ? "Found" : "Not Found") << std::endl;
    std::cout << "Search 'orange': " << (trie.search_word("orange") ? "Found" : "Not Found") << std::endl;
    std::cout << "Search prefix 'bat': " << (trie.search_prefix("bat") ? "Found" : "Not Found") << std::endl;

    // Remove a word
    trie.removeR("batman");

    // Level-order traversal
    std::cout << "Level-order traversal:" << std::endl;
    trie.levelorder();

    // Find the longest common prefix
    std::vector<std::basic_string<char>> words = {"flower", "flow", "flight"};
    std::basic_string<char> commonPrefix = prefix.longestCommonPrefix(words);

    std::cout << "Longest Common Prefix: " << commonPrefix << std::endl;

    return 0;
}

#include <iostream>

int main()
{
    std :: cout << "Hello world" << std::endl;

    return 0;
}

