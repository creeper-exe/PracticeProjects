//Star Triangle
#include <iostream>

int main()
{
    int rows;

    std::cout << "Enter number of rows: ";
    std::cin >> rows;

    for(int i=1; i<=rows; i++)
    {
        for(int b=rows-i; b>0; b--)
            std::cout << " ";
        for(int s=1; s<=i; s++)
            std::cout << "* ";
        std::cout << std::endl;
    }
}
