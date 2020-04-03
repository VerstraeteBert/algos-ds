//C++17-compatibele lijst. Ontbrekende elementen: move en copy, iterator
#ifndef __LIJST_H
#define __LIJST_H

//
// speciale code voor debuggen
//
#define DEBUG

//
//speciale code voor iteratoren
//
#define ITERATOR

#include <algorithm>
#include <cassert>
#include <fstream>
#include <iostream>
#include <memory>
#include <sstream>
#include <string>
#include <vector>
#include "./IsolationRange.h"
using std::endl;
using std::ofstream;
using std::ostream;
using std::string;

template <class T>
class Lijstknoop;
template <class T>
class Lijst;

template <class T>
using Lijstknoopptr = std::unique_ptr<Lijstknoop<T>>;
template <class T>
ostream& operator<<(ostream& os, const Lijst<T>& l);

template <class T>
class Lijst : private Lijstknoopptr<T>
{
public:
    //toekenning, constructoren
    //overname constructoren van unique_ptr

    using std::unique_ptr<Lijstknoop<T>>::operator=;
    using std::unique_ptr<Lijstknoop<T>>::swap;

    Lijst() = default;
    Lijst(const Lijst& andere);
    Lijst(Lijst&& andere);
    Lijst& operator=(const Lijst& andere);
    Lijst& operator=(Lijst&& andere);
    bool operator==(const Lijst& andere);
    bool operator!=(const Lijst& andere);
    virtual ~Lijst() = default;

    //operaties
    //duplicaten zijn toegelaten.

    void voegToe(const T&);
    //geefaantal geeft het aantal keer dat de sleutel voorkomt.
    //gebruikt de zoekfunctie om door de lijst te lopen!
    //zonder argument: geef lengte lijst
    int geefAantal(const T&) const;
    int geefAantal() const;
    //verwijder verwijdert slechts het eerste exemplaar met de gegeven
    //T, en geeft geen fout als de T niet gevonden wordt.
    //gebruik de zoekfunctie om door de lijst te lopen!
    void verwijder(const T&);
    //verwijder eerste knoop.
    void verwijderEerste();    
    bool isClone(const Lijst<T>&) const;
    void applySocialDistancing(const T& N, const T& isolationKey);
    
    //uitschrijf- en tekenoperaties
    //dotformaat:

    void teken(const char* bestandsnaam) const;
    //uitschrijven: voor elke knoop de T-waarde, gescheiden door komma's
    friend ostream& operator<<<>(ostream& os, const Lijst& l);
    void schrijf(ostream& os) const;

private:
    Lijstknoop<T>* identifyNextSublist(Lijstknoop<T>*, IsolationRange<T>& range);
    void addIsolationKeys(Lijstknoop<T>* node_ptr, int num, const T& key);

    //iterator; gaat ervan uit dat alles const is
    class iterator
    {
    private:
        Lijstknoop<T>* lkptr;

    public:
        iterator(Lijstknoop<T>* lkptr = nullptr);

        const T& operator*() const;
        const iterator& operator++();
        bool operator==(const iterator& andere);
        bool operator!=(const iterator& andere);
    };

    iterator begin() const;
    iterator end() const;

protected:
    // zoek geeft een pointer naar de Lijst die de sleutelwaarde bevat,
    // en geeft een pointer naar de lege lijst op het einde als de sleutel niet
    // voorkomt.
    const Lijst* zoek(const T&) const;
    Lijst* zoek(const T&);
    //preconditie zoekgesorteerd: lijst is gesorteerd
    //teruggeefwaarde: wijst naar Lijst waar sleutel staat/zou moeten staan.
    Lijst<T>* zoekGesorteerd(const T& sleutel);
};

template <class T>
class Lijstknoop
{
    friend class Lijst<T>;
    friend ostream& operator<<<>(ostream& os, const Lijst<T>& l);

public:
    Lijst<T> volgend;
    Lijstknoop(const T&);
#ifdef DEBUG
    ~Lijstknoop();
#endif
protected:
    T sleutel;
#ifdef DEBUG
public:
    static bool controle(int gemaakt, int verwijderd);

protected:
    static int aantalGemaakt;
    static int aantalVerwijderd;
#endif
};

template <class T>
int Lijstknoop<T>::aantalGemaakt = 0;
template <class T>
int Lijstknoop<T>::aantalVerwijderd = 0;

////////////////////////////////////////////////////////////////////////////////

template <class T>
Lijst<T>::Lijst(const Lijst& andere)
{
    if (this == &andere)
    {
        return;
    }

    const Lijst* it_andere = &andere;
    Lijst* it_this = this;

    while (it_andere && *it_andere)
    {
        *it_this = std::make_unique<Lijstknoop<T>>((*it_andere)->sleutel);

        it_andere = &((*it_andere)->volgend);
        it_this = &((*it_this)->volgend);
    }
}

template <class T>
Lijst<T>::Lijst(Lijst&& andere) : std::unique_ptr<Lijstknoop<T>>{std::move(andere)}
{
}

template <class T>
Lijst<T>& Lijst<T>::operator=(const Lijst& andere)
{
    if (this != &andere)
    {
        Lijst temp{andere};
        swap(temp);
    }

    return (*this);
}

template <class T>
Lijst<T>& Lijst<T>::operator=(Lijst&& andere)
{
    // swap(andere); // of
    // this->reset(andere.release()); // of
    std::unique_ptr<Lijstknoop<T>>::operator=(std::move(andere));

    return (*this);
}

////////////////////////////////////////////////////////////////////////////////

template <class T>
Lijst<T>::iterator::iterator(Lijstknoop<T>* lkptr) : lkptr{lkptr}
{
}

template <class T>
const T& Lijst<T>::iterator::operator*() const
{
    return lkptr->sleutel;
}

template <class T>
const typename Lijst<T>::iterator &Lijst<T>::iterator::operator++()
{
    lkptr = (lkptr->volgend).get();

    return *this;
}

template <class T>
bool Lijst<T>::iterator::operator==(const iterator& andere)
{
    return (lkptr == andere.lkptr);
}

template <class T>
bool Lijst<T>::iterator::operator!=(const iterator& andere)
{
    return !(*this == andere);
}

template <class T>
typename Lijst<T>::iterator Lijst<T>::begin() const
{
    return iterator(this->get());
}

template <class T>
typename Lijst<T>::iterator Lijst<T>::end() const
{
    return nullptr;
}

////////////////////////////////////////////////////////////////////////////////

template <class T>
Lijstknoop<T>::Lijstknoop(const T& _sl) : sleutel(_sl)
{
    //    std::cerr<<"Knoop met sleutel "<<sleutel<<" wordt gemaakt\n";
    aantalGemaakt++;
}
#ifdef DEBUG

template <class T>
Lijstknoop<T>::~Lijstknoop()
{
    //    std::cerr<<"Knoop met sleutel "<<sleutel<<" wordt verwijderd\n";
    aantalVerwijderd++;
}
template <class T>
bool Lijstknoop<T>::controle(int gemaakt, int verwijderd)
{
    if (aantalGemaakt == gemaakt && aantalVerwijderd == verwijderd)
        return true;
    else
    {
        std::cerr << "Fout bij controle:\n";
        std::cerr << "Aantal gemaakte knopen   : " << aantalGemaakt << " (moet zijn: " << gemaakt << ")\n";
        std::cerr << "Aantal verwijderde knopen: " << aantalVerwijderd << " (moet zijn: " << verwijderd << ")\n";
        throw "Mislukte controle";
    };
};
#endif

template <class T>
ostream& operator<<(ostream& os, const Lijst<T>& l)
{
#ifdef ITERATOR
    for (auto&& sleutel : l)
        os << sleutel << ", ";
#else
    if (l.get())
    {
        os << l.get()->sleutel << ", ";
        os << l.get()->volgend;
    }
#endif
    return os;
}

template <class T>
void Lijst<T>::schrijf(ostream& os) const
{
#ifdef ITERATOR
    if (this->get() != 0)
    {
        os << this->get()->sleutel;
        std::for_each(++begin(), end(), [&](const T& sleutel) { os << " . " << sleutel; });
    }
#else
    {
        Lijstknoop<T>* kn = this->get();
        if (kn != 0)
        {
            os << kn->sleutel;
            kn = kn->volgend.get();
        };
        while (kn != 0)
        {
            os << " . " << kn->sleutel;
            kn = kn->volgend.get();
        };
    }
#endif
}
//oplossing:

template <class T>
bool Lijst<T>::isClone(const Lijst<T>& ander) const
{
    const Lijst<T>*l1 = this, *l2 = &ander; //twee lopers
    while (*l1 && *l2 && (*l1)->sleutel == (*l2)->sleutel)
    {
        l1 = &((*l1)->volgend);
        l2 = &((*l2)->volgend);
    };
    return (!(*l1) && !(*l2));
};

template <class T>
const Lijst<T>* Lijst<T>::zoek(const T& sleutel) const
{
    const Lijst<T>* pl = this;
    while (*pl && pl->get()->sleutel != sleutel)
        pl = &(pl->get()->volgend);
    return pl;
}

template <class T>
int Lijst<T>::geefAantal(const T& sleutel) const
{
    int aantal = 0;
    const Lijst<T>* pl = this;
    while (*pl)
    {
        if (sleutel == (*pl)->sleutel)
            ++aantal;
        pl = &(pl->get()->volgend);
    };
    return aantal;
};

template <class T>
int Lijst<T>::geefAantal() const
{
    int aantal = 0;
    const Lijst<T>* pl = this;
    while (*pl)
    {
        ++aantal;
        pl = &(pl->get()->volgend);
    };
    return aantal;
};

template <class T>
Lijst<T>* Lijst<T>::zoek(const T& sleutel)
{
    Lijst* pl = this;
    while (*pl && pl->get()->sleutel != sleutel)
        pl = &(pl->get()->volgend);
    return pl;
}

template <class T>
void Lijst<T>::voegToe(const T& sleutel)
{
    Lijstknoopptr<T> nieuw = std::make_unique<Lijstknoop<T>>(sleutel);
    Lijstknoopptr<T>::swap(nieuw->volgend);
    *this = std::move(nieuw);
}

template <class T>
void Lijst<T>::verwijderEerste()
{
    if (this->get() != 0)
    {
        Lijstknoopptr<T> staart(std::move(this->get()->volgend));
        this->reset();
        Lijstknoopptr<T>::swap(staart);
    }
}

template <class T>
void Lijst<T>::verwijder(const T& sleutel)
{
    zoek(sleutel)->verwijderEerste();
}

template <class T>
Lijst<T>* Lijst<T>::zoekGesorteerd(const T& sleutel)
{
    Lijst* plaats = this;
    while (*plaats && plaats->get()->sleutel < sleutel)
        plaats = &plaats->get()->volgend;
    return plaats;
};

template <class T>
void Lijst<T>::teken(const char* bestandsnaam) const
{
    ofstream uit(bestandsnaam);
    assert(uit);
    uit << "digraph {\nrankdir=\"LR\";\n\"0\"[label=\"\",shape=diamond];\n\"0\" -> \"1\";\n";
    int knoopteller = 1; //knopen moeten een eigen nummer krijgen.
    const Lijst<T>* loper = this;
    while (*loper)
    {
        uit << "subgraph cluster_" << knoopteller << " {\nrankdir=\"LR\";\n";
        uit << "\"" << knoopteller << "\" [label=\"" << (*loper)->sleutel << "\",color=white];\n";
        uit << "\"" << knoopteller << "v\" [shape=diamond,label=\"\"];\n";
        uit << "\"" << knoopteller << "\" -> \"" << knoopteller << "v\" [color=white];\n";

        uit << "}\n";
        uit << "\"" << knoopteller << "v\" -> \"" << knoopteller + 1 << "\" [lhead=cluster_" << knoopteller
            << " ltail=cluster_" << knoopteller + 1 << "];\n";
        loper = &((*loper)->volgend);
        knoopteller++;
    };
    uit << "\"" << knoopteller << "\" [shape=point];\n";
    uit << "}";
};

/**
 * Takes list as input and forms sublists;
 *      With the min of the sublist having a max distance of N to the maximum of the sublist
 *      Moreover, isolation keys are added between adjecent sublists.
 *
 * The number of isolation keys depends overlapping ranging of the sublists
 *      If there are K overlapping elements -> K isolating keys are added between the adjecent sublists
 *      If there are no overlapping elements -> only one key is added
 *
 * Parameter const T& N -> max range distance within a sublist
 * Parameter const T& isolationKey -> the key that's added between adjacent sublists
 *
 * The general idea is to linearly loop over the list
 *      1. identifying new sublists and saving their respective ranges
 *      2. whenever a pair of adjacent sublists is made
 *              -> fill isolation keys between them, depending on their overlap
 *
 * Implementation:
 *  1. Form the first sublist:
 *       - keeping a reference to the tail node of the sublist (prev_tail_ptr)
 *       - saving the range of the sublist in prev_range
 *       - curr_ptr is set to the head of the second sublist (prev_tail_ptr->next)
 *  2. Identify new sublist and add K isolating keys between the previous sublist and the newly formed sublist
 *      - identify the next sublist:
 *          - saving its tail to curr_ptr
 *          - saving its range in curr_range
 *      - calculate the number of overlaps between the previous and current sublist
 *          and add isolating keys (more info at its function declaration)
 *          - if number of overlaps is 0 -> add 1 isolating key between the two groups
 *          - else add number of overlaps times an isolating key between the two groups
 *      - Prepare for next iteration
 *          - the previous sublist is now fully processed
 *          - the new sublist now becomes the previous sublist for the next iteration
 *              - save the range of the new sublist into the range of the previous
 *              - set previous tail pointer to the tail pointer of the new sublist
 *              - set curr_ptr to the head of the next sublist to be processed
 *      - As long as there are nodes left that are left to be grouped goto 2
 */
template <class T>
void Lijst<T>::applySocialDistancing(const T& N, const T& isolationKey) {
    if (this->get() == nullptr) {
        return;
    }

    Lijstknoop<T>* curr_ptr = this->get();
    Lijstknoop<T>* prev_tail_ptr = nullptr;

    IsolationRange<T> curr_range = IsolationRange<T>(N);
    IsolationRange<T> prev_range = IsolationRange<T>(N);

    prev_tail_ptr = identifyNextSublist(curr_ptr, prev_range);
    curr_ptr = prev_tail_ptr->volgend.get();

    while (curr_ptr) {
        curr_ptr = identifyNextSublist(curr_ptr, curr_range);
        int num_overlap = curr_range.calculateNumberOverlaps(prev_range);

        if (num_overlap == 0) {
            addIsolationKeys(prev_tail_ptr, 1, isolationKey);
        } else {
            addIsolationKeys(prev_tail_ptr, num_overlap, isolationKey);
        }

        prev_range = std::move(curr_range);
        prev_tail_ptr = curr_ptr;
        curr_ptr = prev_tail_ptr->volgend.get();
    }
}

/**
 * Identifies the next sublist and saves its range
 *  - Adds the next node to the sublist as long as
 *      1. there's nodes left to add
 *      2. the node is within the valid range of the sublist
 *  - Sets the passed IsolationRange<T>& to the range of the identified sublist
 *  - Returns a pointer to the tail of the identified sublist
 */
template <class T>
Lijstknoop<T>* Lijst<T>::identifyNextSublist(Lijstknoop<T>* curr_ptr, IsolationRange<T>& range) {
    if (curr_ptr == nullptr) {
        return nullptr;
    }

    range.min = &(curr_ptr->sleutel);
    range.max = &(curr_ptr->sleutel);

    while (curr_ptr->volgend != nullptr && range.ensureValidBoundsAndUpdate(curr_ptr->volgend->sleutel)) {
        curr_ptr = curr_ptr->volgend.get();
    }

    return curr_ptr;
}

/**
 * Adds N new nodes between supplied node and its next node
 * note why I'm not passing int as ref -> trivially copyable
 */
template <class T>
void Lijst<T>::addIsolationKeys(Lijstknoop<T>* node_ptr, int num, const T& key) {
    auto tmp = move(node_ptr->volgend);
    for (int i = 0; i < num; i++) {
        node_ptr->volgend = make_unique<Lijstknoop<T>>(key);
        node_ptr = node_ptr->volgend.get();
    }
    node_ptr->volgend = move(tmp);
}

/**
 * Member functie lijst == toegevoegd voor testing
 */
template<class T>
bool Lijst<T>::operator==(const Lijst<T>& andere) {
    auto this_iter = this->begin();
    auto andere_iter = andere.begin();

    while (this_iter != this->end() && andere_iter != andere.end()) {
        if (*this_iter != *andere_iter) {
            return false;
        }
        ++this_iter; ++andere_iter;
    }
    return (this_iter == this->end() && andere_iter == andere.end());
}

template<class T>
bool Lijst<T>::operator!=(const Lijst<T>& andere) {
    return !(*this == andere);
}

#endif
