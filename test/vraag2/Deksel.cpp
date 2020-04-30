class Deksel{
    private:
        static int count;
        int diameter;
        int UUID;
    public:
        explicit Deksel(int x);
        int getUUID() const;
        int getDiameter() const;
};
// lazy UUID with counter; it suffices for this exercise
int Deksel::count = 0;
Deksel::Deksel(int x) : diameter(x) {
    this->UUID = ++Deksel::count;
}

int Deksel::getUUID() const {
    return this->UUID;
}
int Deksel::getDiameter() const {
    return this->diameter;
}
