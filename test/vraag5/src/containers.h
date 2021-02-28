#ifndef CONTAINERS_H
#define CONTAINERS_H

#include <iostream>
#include <list>

template <class T>
std::ostream& operator<<(std::ostream& os, const std::list<T>& list) {
    auto itr = list.cbegin();

    if (itr != list.cend()) {
        os << *itr++;
    }

    while (itr != list.cend()) {
        os << ", " << *itr++;
    }

    return os;
}

#endif // CONTAINERS_H
