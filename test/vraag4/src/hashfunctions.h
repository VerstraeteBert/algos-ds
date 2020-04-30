#ifndef HASHFUNCTIONS_H
#define HASHFUNCTIONS_H

#include <string>

unsigned int worst_hash(const std::string &word)
{
    return 0;
}

unsigned int bad_hash(const std::string &word)
{
    return word.size();
}

unsigned int other_bad_hash(const std::string &word)
{
    unsigned int result = 0;

    for (const auto &c : word)
    {
        result += c;
    }

    return result;
}

unsigned int horner_hash(const std::string &word)
{
    unsigned int horner = 0;

    for (const auto &c : word)
    {
        horner = (horner * 256 + c);
    }

    return horner;
}

unsigned int good_hash(const std::string &word)
{
    unsigned int horner = 0;

    for (const char c : word)
    {
        horner = (horner * 131 + c);
    }

    return horner;
}

unsigned int djb2(const std::string &word) {
    unsigned int hash = 5381;

    for (const char c : word) {
        hash = ((hash << 5) + hash) + c; /* hash * 33 + c */
    }

    return hash;
}

unsigned int sdbm(const std::string &word) {
    unsigned int hash = 0;

    for (const char c : word) {
        hash = c + (hash << 6) + (hash << 16) - hash;
    }

    return hash;
}

unsigned int jenkins_one_bit_at_a_time(const std::string& word) {
    unsigned int hash = 0;
    for (const char c : word) {
        hash += c;
        hash += hash << 10;
        hash ^= hash >> 6;
    }
    hash += hash << 3;
    hash ^= hash >> 11;
    hash += hash << 15;
    return hash;
}

#endif