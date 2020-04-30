#ifndef CONTAINERS_H
#define CONTAINERS_H

#include <set>
#include <iostream>

template<class T>
std::ostream& operator<<(std::ostream& out, const std::set<T>& s) {
    auto it = s.cbegin();
    out << " { ";
    if (it != s.cend()) {
        out << "\"" << *it++ << "\"";
        while (it != s.cend()) {
            out << ", \"" << *it++ << "\"";
        }
    }
    out << " } ";
    return out;
}

#endif
