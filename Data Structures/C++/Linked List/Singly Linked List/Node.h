//
// Created by Dell on 10/16/2023.
//

#ifndef DATA_STRUCTURE_NODE_H
#define DATA_STRUCTURE_NODE_H

#endif //DATA_STRUCTURE_NODE_H

template <typename T>
struct Node
{
    Node(const T& d, Node<T>* n = nullptr)
    : data(d)
    , next(n)
    {
    }
    T data;
    Node<T>* next;
};