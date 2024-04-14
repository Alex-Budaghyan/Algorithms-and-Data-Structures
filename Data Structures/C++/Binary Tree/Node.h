//
// Created by Dell on 11/14/2023.
//

#ifndef DATA_STRUCTURE_C_NODE_H
#define DATA_STRUCTURE_C_NODE_H

#endif //DATA_STRUCTURE_C_NODE_H

template <typename T>
struct Node
{
    Node(const T& d, Node<T>* l = nullptr, Node<T>* r = nullptr)
            : data(d)
            , left(l)
            , right(r)
    {
    }

    T data;
    Node<T>* left;
    Node<T>* right;
};