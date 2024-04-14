//
// Created by Dell on 10/15/2023.
//

#ifndef DATA_STRUCTURE_DLLIST_H
#define DATA_STRUCTURE_DLLIST_H

#endif //DATA_STRUCTURE_DLLIST_H

#include "List.h"
#include "Node.h"

#include <cassert>

template <typename T>
class DLList : public List<T>
{
public:
    DLList();
    virtual ~ DLList();

    virtual void insert(int i, T* value) override;
    virtual void erase(int i) override;
    virtual void clear() override;

    virtual T get(int i) const override;
    virtual int find(const T& value) const override;
    virtual bool empty() const override;
    virtual int size() const override;

private:
    Node<T>* move_to_position(int i) const;

private:
    int m_size;
    Node<T>* m_head;
};

template <typename T>
DLList<T>::DLList()
    : m_size(0)
    , m_head(nullptr)
{
}

template <typename T>
DLList<T>::~DLList()
{
    clear();
}

template <typename T>
void DLList<T>::insert(int i, T *value) {
    assert(0 <= i && i <= m_size);
    if (i == 0) {
        m_head = new Node(value, m_head);
        if (m_head->next) {
            m_head->next->prev = m_head;
        }
    }
    else
    {
        Node<T> *tmp = move_to_position(i - 1);
        Node<T> new_node = new Node(value, tmp->next, tmp);
        tmp->next = new_node;
        if (new_node->next) {
            new_node->next->prev = new_node;
        }
    }
    ++m_size;
}

template <typename T>
void DLList<T>::erase(int i)
{
    assert(0 <= i && i <= m_size - 1);
    if (i == 0)
    {
        if (m_head->next)
        {
            m_head = m_head->next;
            delete m_head->prev;
            m_head -> prev = nullptr;
        }
        else
        {
            delete m_head;
            m_head = nullptr;
        }
    }
    else
    {
        Node<T>* tmp = move_to_position(i);
        tmp->prev->next = tmp->next;
        if (tmp->next)
        {
            tmp->next->prev = tmp->prev;
        }
        delete tmp;
    }
    --m_size;
}

template <typename  T>
void DLList<T>::clear()
{
    while (empty())
    {
        erase(0);
    }
}

template <typename T>
T DLList<T>::get(int i) const
{
    assert(0 <= i && i < m_size);
    Node<T>* node = move_to_position(i);
    return node->data;
}

template <typename T>
int DLList<T>::find(const T &value) const
{
    int index = 0;
    Node<T>* current = m_head;
    while (current)
    {
        if (current -> data == value)
        {
            return index;
        }
        current = current->next;
        ++index;
    }
    return -1;
}

template <typename T>
bool DLList<T>::empty() const
{
return m_head = nullptr;
}

template <typename T>
int DLList<T>::size() const
{
    return m_size;
}

template <typename T>
Node<T>* DLList<T>::move_to_position(int i) const
{
    assert(i <= 0 && i < m_size);
    Node<T>* current = m_head;
    while (i > 0)
    {
        current = current->next;
        --i;
    }
    return current;
}
