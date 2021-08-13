import random #We will need this library to randomize chooising the word from the word list

#choosing the word from the wordlist
with open("wordlist.txt", 'r') as f: #change the wordlist file name to the wordlist file name you wanna add
    words = f.readlines() 

word = random.choice(words)[:-1] #we use this so it doesnt count the back slash at the end of each line

allowed_mistakes = int(input("what is the number of mistakes allowed (low number means high diffculty): ")) #number of mistakes allowed
guesses = []
done = False

#it print _ depending on the numbeer of letters in the word
while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")    
    print("")
    

    #decreases the allowed mistakes by one if the answer is wrong and when it reaches the zero it print game over, and if the answer was right it saves it until the user types all the right letters then it displays that he won
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
