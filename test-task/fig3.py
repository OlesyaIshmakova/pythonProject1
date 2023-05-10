#include <iostream>
#include <string>
#include <vector>
using namespace std;
struct Figure {
virtual ~Figure() {}
virtual void draw(char ch = '#')const {}
virtual double area()const { return 0; };
virtual double perimeter()const { return 0; };
};
class Triangle : public Figure {
public:
explicit Triangle(const int h) : h(h) {}
void draw(char ch = '#')const override {
string img;
for (int i = 1, n = 1, b = 2 * h - 1; i <= h; ++i, n += 2, b -= 2) {
string dotted = string(b >> 1, '.');
img += dotted + string(n, '#') + dotted + '\n';
}
cout << img;
}
double area()const override {
return (h * (h * 2 - 1)) / 2.;
}
double perimeter()const override {
double a = h * 2 - 1;
double x = a / 2;
double b = sqrt(h * h + x * x);
return a + b + b;
}
private:
int h;
};
class Rectangle : public Figure {
public:
Rectangle(const int a, const int b) : a(a), b(b) {}
void draw(char ch = '#')const override {
string img;
for (int i = 0; i < b; ++i) {
img += string(a, '#') + '\n';
}
cout << img;
}
double area()const override {
return a * b;
}
double perimeter()const override {
return (a + b) * 2;
}
private:
int a, b;
};
class Circle : public Figure {
public:
Circle(const int r) : r(r) {}
void draw(char ch = '#')const override {
string img = ":)\n";
cout << img;
}
double area()const override {
return pi * r * r;
}
double perimeter()const override {
return 2 * pi * r;
}
private:
int r;
inline static const double pi = 3.1415926535897932;
};
void draw_array(vector<Figure*> box, const size_t size) {
for (size_t i = 0; i < size; ++i) {
box[i]->draw();
puts("");
}
}
int main() {
size_t size;
cin >> size;
vector<Figure*> box(size);
for (size_t i = 0; i < size; ++i) {
string name;
cin >> name;
if (name == "Triangle") {
int h;
cin >> h;
box[i] = new Triangle{ h };
} else if (name == "Rectangle") {
int a, b;
cin >> a >> b;
box[i] = new Rectangle{ a, b };
} else if (name == "Circle") {
int r;
cin >> r;
box[i] = new Circle{ r };
} else {
--i;
}
}
puts("");
draw_array(box, size);
}