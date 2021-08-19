//Factorial Calculator

#include <string>
#include <iostream>

int main()
{
    int factorial;
    std::cout << "Insert a Number: ";
    std::cin >> factorial;
    for (int i = factorial - 1; i > 1; i--)
    {
        factorial = factorial * i;
        
    }
    std::cout << "Factorial = " << factorial << std::endl;
    return 0;
}
