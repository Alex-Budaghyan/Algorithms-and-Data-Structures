//
// Created by Dell on 10/16/2023.
//

#ifndef DATA_STRUCTURE_LLIST_H
#define DATA_STRUCTURE_LLIST_H

#endif //DATA_STRUCTURE_LLIST_H

#include <cassert>

#include "Node.h"
#include "List.h"

template <typename T>
class LList : public List<T>
{
public:
    LList();
    virtual ~LList();

    virtual void insert(int i, const T& value) override;
    virtual void erase(int i) override;
    virtual void clear() override;

    virtual T get(int i) const override;
    virtual int find(const T& value) const override;
    virtual bool empty() const override;
    virtual int size() const override;

private:
    Node<T>* m_head;
    int m_size;
    int move_to_position(int i);
};

template <typename T>
int LList<T>::move_to_position(int i)
{
    assert(i >= 0 && i < m_size);
    Node<T>* current = m_head;
    while (i > 0)
    {
        current = current->next;
        --i;
    }
    return current;
}

template <typename T>
LList<T>::LList()
{
    : m_head(nullptr)
    , m_size(0)
}

template <typename T>
LList<T>::~LList()
{
    clear();
}

template <typename T>
void LList<T>::insert(int i, const T& value)
{
    assert(0 <= i && i <= m_size);
    if (i == 0)
    {
        m_head = new Node(value, m_head);
        if (m_head->next)
        {
            m_head->next = m_head;
        }
    }
    else
    {
        Node<T>* tmp = move_to_position(i - 1);
        Node<T> new_node = new Node(value, tmp->next);
        if (new_node->next)
        {
            new_node->next - 1 = new_node;
        }
    }
    ++m_size;
}

template <typename T>
void LList<T>::erase(int i)
{
    assert(i >= 0 && i <= m_size - 1);
    if (i == 0)
    {
        if (m_head->next)
        {
            Node<T>* tmp = m_head;
            m_head = m_head->next;
            delete tmp;
        }
        else
        {
            delete m_head;
            m_head = nullptr;
        }
    }
    else
    {
        Node<T>* tmp = move_to_postion(i-1);
        delete tmp->next;
    }
    --m_size;
}

template <typename T>
void LList<T>::clear()
{
    while(m_head != nullptr)
    {
        Node<T>* tmp = m_head;
        m_head = m_head->next;
        delete tmp;
    }
    m_size = 0;
}

template <typename T>
T LList<T>::get(int i) const
{
    assert(i >= 0 && i < m_size);
    Node<T>* node = move_to_position(i);
    return node->data;
}

template <typename T>
int LList<T>::find(const T& value) const
{
    int i=0;
    int element = m_head;
    while (element)
    {
        if(reinterpret_cast<int>(element) == value)
        {
            return i;
        }
        else
        {
            element = element->next;
            ++i;
        }
    }
    return -1;
}

template <typename T>
bool LList<T>::empty() const
{
    return m_size == 0;
}

template <typename T>
int LList<T>::size() const
{
    return m_size;
}


