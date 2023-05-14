#include <iostream>
using namespace std;
class Base {
public:
};
Base() { cout << "Base" << endl; }
class Derived public Base {
public:
};
Derived(int i) { cout << i << endl; }
int main() {
Derived d2(10);
return 0;
}