#include <iostream>
#include <string>


int main()
{
    std::string answer = "nour"; //Change This if you want the user to guess your name
    int age_answer  = 20; //Change This if you want the user to guess your age
    std::string guess;
    std::cout << "Guess my name: ";
    std::cin >> guess;
    int age_guess;
    std::cout << "Guess my age: ";
    std::cin >> age_guess;

    if (guess == answer && age_guess == age_answer)
    {
        std::cout << "You got it right yaaaay.\n";
    }
    else if (guess != answer && age_guess != age_answer)
    {
        std::cout << "You got it  wrong :(\n";
    }
    return 0;
}
