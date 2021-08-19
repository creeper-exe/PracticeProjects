//Area Of Triangle

#include <string>
#include <iostream>

int main()
{
    int base;
    int height; 
    int result;
    std::cout << "What is the base of the triangle: ";
    std::cin >> base;
    std::cout << "What is the height of the triangle: ";
    std::cin >> height;
    result = {base * height / 2};
    std::cout << result;

}

