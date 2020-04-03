class Pot {
    private:
        static int count;
        int diameter;
        int UUID;
    public:
        explicit Pot(int x);
        int getUUID() const;
        int getDiameter() const;
};
// lazy UUID with counter; it suffices for this exercise
int Pot::count = 0;
Pot::Pot(int x) : diameter(x) {
    this->UUID = ++Pot::count;
}

int Pot::getUUID() const {
    return this->UUID;
}

int Pot::getDiameter() const {
    return this->diameter;
}
