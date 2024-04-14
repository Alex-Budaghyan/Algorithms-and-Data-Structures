//
// Created by Dell on 10/10/2023.
//

#ifndef DATA_STRUCTURE_LIST_H
#define DATA_STRUCTURE_LIST_H

#endif //DATA_STRUCTURE_LIST_H

template <typename T>
class List
{
    List() {}
    virtual ~ List() {}

    virtual void insert(int i, T* value) = 0;
    virtual void erase(int i) = 0;
    virtual void clear() = 0;

    virtual T get(int i) const = 0;
    virtual int find(const T& value) const = 0;
    virtual bool empty() const = 0;
    virtual int size() const = 0;
};