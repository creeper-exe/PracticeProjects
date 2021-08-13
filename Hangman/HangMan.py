import random

with open("wordlist.txt", 'r') as f:
    words = f.readlines()

word = random.choice(words)[:-1]

allowed_mistakes = 6
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")    
    print("")
    
    
    guess = input(f"Allowed Mistakes Left {allowed_mistakes}, Next Guess:")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_mistakes -= 1
        if allowed_mistakes == 0:
            break

    done = True 
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"You found the word yaaaay, it was {word}!")
else:
    print(f"Game Over Loser, the word was {word}!")
