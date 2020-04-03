// lt and gt methods for comparing Deksels and Potten
// Could be expanded into a more generic comparator class,
// seems like an unnecessary abstraction at this point
template <class T, class G>
bool dia_lt(const T& a, const G& b)  {
    return a.getDiameter() < b.getDiameter();
}

template <class T, class G>
bool dia_gt(const T& a, const G& b)  {
    return a.getDiameter() > b.getDiameter();
}
