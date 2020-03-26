// Ontbrekende elementen: move en copy, iterator
#ifndef __LIJST17_H
#define __LIJST17_H
//
// speciale code voor debuggen
//
#define DEBUG
//
//
//speciale code voor iteratoren
#define ITERATOR

#include <iostream>
#include <fstream>
#include <memory>
#include <cassert>
#include <algorithm>
#include <string>
#include <sstream>
using std::string;
using std::endl;
using std::ostream;
using std::ofstream;

using namespace std;
template<class T>
class Lijstknoop;
template<class T>
class Lijst;

template<class T>
using Lijstknoopptr=std::unique_ptr<Lijstknoop<T> >;
template<class T>
ostream& operator<<(ostream& os, const Lijst<T>& l);

template<class T>
class Lijst: private Lijstknoopptr<T>{
public:
    using std::unique_ptr<Lijstknoop<T>>::operator=;
    using std::unique_ptr<Lijstknoop<T>>::swap;

    // default constructor
    Lijst () = default;
    // default destructor (enige member var is unique_ptr, deze wordt automatisch opgeschort :-) )
    // altijd marken als virtual hé
    virtual ~Lijst() = default;

    Lijst(const Lijst<T>&);
    Lijst<T>& operator=(const Lijst<T>&);

    Lijst<T>& operator=(Lijst<T>&& pl) noexcept;

    Lijst(Lijst<T>&& pl) noexcept;

    private: void copy(const Lijst<T>&);
//    private: void copyRec(const Lijstknoop<T>* ptr);

    //duplicaten zijn toegelaten.
    public: void voegToe(const T&);

    //geefaantal geeft het aantal keer dat de sleutel voorkomt.
    //gebruikt de zoekfunctie om door de lijst te lopen!
    //zonder argument: geef lengte lijst
    public: int geefAantal(const T&) const;
    public: int geefAantal() const;

    //verwijder verwijdert slechts het eerste exemplaar met de gegeven
    //T, en geeft geen fout als de T niet gevonden wordt.
    //gebruik de zoekfunctie om door de lijst te lopen!
    public: void verwijder(const T&);

    //verwijder eerste knoop.
    public: void verwijderEerste();

    public: void insertionsort();

    public: bool isClone(const Lijst<T>&) const;

    // zoek geeft een pointer naar de Lijst die de sleutelwaarde bevat,
    // en geeft een pointer naar de lege lijst op het einde als de sleutel niet
    // voorkomt.
    protected: const Lijst* zoek(const T&) const;
    protected: Lijst* zoek(const T&);

    //preconditie zoekgesorteerd: lijst is gesorteerd
    //teruggeefwaarde: wijst naar Lijst waar sleutel staat/zou moeten staan.
    protected: Lijst<T>* zoekGesorteerd(const T& sleutel);

    //uitschrijf- en tekenoperaties
    //dotformaat:
    public: void teken(const char * bestandsnaam)const;
    //uitschrijven: voor elke knoop de T-waarde, gescheiden door komma's
    friend ostream& operator<< <>(ostream& os, const Lijst& l);
    public: void schrijf(ostream & os) const;

    //iterator; gaat ervan uit dat alles const is
    public: class iterator{
        private:
            Lijstknoop<T>* itr;
        public:
            iterator(Lijstknoop<T>* l=0);
            const T& operator*() const;
            const iterator& operator++();
            bool operator!=(const iterator& rhs);
    };
    iterator begin() const;
    iterator end() const;
};

/**
 * COPY & MOVE
 */
template <class T>
Lijst<T>::Lijst(const Lijst<T>& pl) {
    copy(pl);
}

template <class T>
Lijst<T>& Lijst<T>::operator=(const Lijst<T>& pl) {
    if (&pl != this) {
        copy(pl);
    }
    return *this;
}

template <class T>
Lijst<T>& Lijst<T>::operator=(Lijst<T>&& pl) noexcept {
    if (&pl != this) {
        this->swap(pl);
        pl.reset();
    }
    return *this;
}

template <class T>
Lijst<T>::Lijst(Lijst<T>&& pl) noexcept {
    this->swap(pl);
}

/**
 Trivial recursive implementation
 O(N) runtime; O(N) memory

template <class T>
void Lijst<T>::copy(const Lijst<T>& pl) {
    this->reset();
    copyRec(pl.get());
}

template<class T>
void Lijst<T>::copyRec(const Lijstknoop<T>* ptr) {
    if (!ptr) return;
    copyRec(ptr->volgend.get());
    voegToe(ptr->sleutel);
}
*/

// O(N) Runtime, O(1) Memory
template <class T>
void Lijst<T>::copy(const Lijst<T>& pl) {
    this->reset();
    if (pl) {
        auto curr_cp = pl.get();
        voegToe(curr_cp->sleutel);
        curr_cp = curr_cp->volgend.get();

        auto curr_new = this->get();

        while (curr_cp) {
            curr_new->volgend = make_unique<Lijstknoop<T>>(curr_cp->sleutel);
            curr_new = curr_new->volgend.get();
            curr_cp = curr_cp->volgend.get();
        }
    }
}

/**
 * ITERATOR CODE
 */
template<class T>
Lijst<T>::iterator::iterator(Lijstknoop<T> *l) : itr(l) {}

template<class T>
const T& Lijst<T>::iterator::operator*() const {
    return itr->sleutel;
}

template<class T>
bool Lijst<T>::iterator::operator!=(const Lijst::iterator &rhs) {
    return itr != rhs.itr;
}

template<class T>
const typename Lijst<T>::iterator& Lijst<T>::iterator::operator++() {
    itr = itr->volgend.get();
    return *this;
}

template<class T>
typename Lijst<T>::iterator Lijst<T>::begin() const {
    return Lijst::iterator(this->get());
}

template<class T>
typename Lijst<T>::iterator Lijst<T>::end() const {
    return nullptr;
}

template<class T>
class Lijstknoop {
    friend class Lijst<T>;
    friend ostream& operator<< <>(ostream& os, const Lijst<T>& l);
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
        static bool controle (int gemaakt, int verwijderd);
protected:
        static int aantalGemaakt;
        static int aantalVerwijderd;
#endif
};

template<class T>
int Lijstknoop<T>::aantalGemaakt=0;
template<class T>
int Lijstknoop<T>::aantalVerwijderd=0;

template<class T>
Lijstknoop<T>::Lijstknoop(const T& _sl):sleutel(_sl){
//    std::cerr<<"Knoop met sleutel "<<sleutel<<" wordt gemaakt\n";
    aantalGemaakt++;
}
#ifdef DEBUG

template<class T>
Lijstknoop<T>::~Lijstknoop(){
//    std::cerr<<"Knoop met sleutel "<<sleutel<<" wordt verwijderd\n";
    aantalVerwijderd++;
}

template<class T>
bool Lijstknoop<T>::controle (int gemaakt, int verwijderd){
    if (aantalGemaakt==gemaakt && aantalVerwijderd==verwijderd)
        return true;
    else{
        std::cerr<<"Fout bij controle:\n";
        std::cerr<<"Aantal gemaakte knopen   : "<<aantalGemaakt<<" (moet zijn: "<<gemaakt<<")\n";
        std::cerr<<"Aantal verwijderde knopen: "<<aantalVerwijderd<<" (moet zijn: "<<verwijderd<<")\n";
//ook naar cout schrijven: sommige ontwikkelingsomgevingen dumpen cerr.
        std::cout<<"Fout bij controle:\n";
        std::cout<<"Aantal gemaakte knopen   : "<<aantalGemaakt<<" (moet zijn: "<<gemaakt<<")\n";
        std::cout<<"Aantal verwijderde knopen: "<<aantalVerwijderd<<" (moet zijn: "<<verwijderd<<")\n";
        throw "Mislukte controle";
    };
};
#endif

template<class T>
ostream& operator<<(ostream& os,const Lijst<T>& l){
#ifdef ITERATOR
    for (auto&& sleutel: l)
        os<<sleutel<<", ";
#else
    if (l.get()){
        os<<l.get()->sleutel<<", ";
        os<<l.get()->volgend;
    }
#endif
    return os;
}

template<class T>
void Lijst<T>::schrijf(ostream & os) const{
#ifdef ITERATOR
    if (this->get()!=0){
        os<<this->get()->sleutel;
        std::for_each (++begin(),end(),[&](const T& sleutel){ os<<" . "<<sleutel;} );
    }
#else
	{
        Lijstknoop<T> * kn=this->get();
        if (kn!=0){
            os<<kn->sleutel;
            kn=kn->volgend.get();
        };
        while (kn != 0){
            os<<" . "<<kn->sleutel;
            kn=kn->volgend.get();
        };
    }
#endif
}

template<class T>
bool Lijst<T>::isClone(const Lijst<T>& ander) const{
    const Lijst<T>* l1=this, *l2=&ander;//twee lopers
    while (*l1 && *l2 && (*l1)->sleutel == (*l2)->sleutel){
        l1=&((*l1)->volgend);
        l2=&((*l2)->volgend);
    };
    return(!(*l1) && !(*l2));
};


template<class T>
const Lijst<T>* Lijst<T>::zoek(const T& sleutel) const{
    const Lijst<T>* pl=this;
    while (*pl && pl->get()->sleutel !=sleutel)
        pl=&(pl->get()->volgend);
    return pl;
}

template<class T>
int Lijst<T>::geefAantal(const T& sleutel) const{
    int aantal=0;
    const Lijst<T>* pl=this;
    while (*pl){
        sleutel = (*pl)->sleutel;
        if (sleutel)
            ++aantal;
        pl=&(pl->get()->volgend);
    };
    return aantal;
};

template<class T>
int Lijst<T>::geefAantal() const{
    int aantal=0;
    const Lijst<T>* pl=this;
    while (*pl){
        ++aantal;
        pl=&(pl->get()->volgend);
    };
    return aantal;
};

template<class T>
Lijst<T>* Lijst<T>::zoek(const T& sleutel){
    Lijst* pl=this;
    while (*pl && pl->get()->sleutel != sleutel)
        pl=&(pl->get()->volgend);
    return pl;
}

template<class T>
void Lijst<T>::voegToe(const T& sleutel){
    Lijstknoopptr<T> nieuw=std::make_unique<Lijstknoop<T>>(sleutel);
    Lijstknoopptr<T>::swap(nieuw->volgend);
    *this=std::move(nieuw);
}

template<class T>
void Lijst<T>::verwijderEerste(){
    if (this->get()!=0){
        Lijstknoopptr<T> staart(std::move(this->get()->volgend));
        this->reset();
        Lijstknoopptr<T>::swap(staart);
    }
}

template<class T>
void Lijst<T>::verwijder(const T& sleutel){
    zoek(sleutel)->verwijderEerste();
}

template<class T>
Lijst<T>* Lijst<T>::zoekGesorteerd(const T& sleutel){
    Lijst* plaats=this;
    while (*plaats && plaats->get()->sleutel < sleutel)
        plaats=&plaats->get()->volgend;
    return plaats;
};

template<class T>
void Lijst<T>::insertionsort(){
    Lijstknoopptr<T> ongesorteerd=std::move(*this);
    while (ongesorteerd){
        Lijst *plaats=zoekGesorteerd(ongesorteerd.get()->sleutel);
        Lijstknoopptr<T> dummy=std::move(ongesorteerd);
        //vermits ongesorteerd een nullpointer is, is het equivalent van volgende lijnen ongeveer
        //ongesorteerd=std::move(dummy.get()->volgend);
        //std::swap(*plaats,dummy.get()->volgend);
        std::swap(ongesorteerd,dummy.get()->volgend);
        dummy.get()->volgend=std::move(*plaats);
        *plaats=std::move(dummy);

    };
};

template<class T>
void Lijst<T>::teken(const char * bestandsnaam) const{
    ofstream uit(bestandsnaam);
    assert(uit);
    uit<<"digraph {\nrankdir=\"LR\";\n\"0\"[label=\"\",shape=diamond];\n\"0\" -> \"1\";\n";
    int knoopteller=1;//knopen moeten een eigen nummer krijgen.
    const Lijst<T>* loper=this;
    while (*loper){
        uit<<"subgraph cluster_"<<knoopteller<<" {\nrankdir=\"LR\";\n";
        uit<<"\""<<knoopteller<<"\" [label=\""<<(*loper)->sleutel<<"\",color=white];\n";
        uit<<"\""<<knoopteller<<"v\" [shape=diamond,label=\"\"];\n";
        uit<<"\""<<knoopteller<<"\" -> \""<<knoopteller<<"v\" [color=white];\n";
        uit<<"}\n";
        uit<<"\""<<knoopteller<<"v\" -> \""<<knoopteller+1
           <<"\" [lhead=cluster_"<<knoopteller<<" ltail=cluster_"<<knoopteller+1<<"];\n";
        loper=&((*loper)->volgend);
        knoopteller++;
    };
    uit<<"\""<<knoopteller<<"\" [shape=point];\n";
    uit<<"}";
}

#endif
