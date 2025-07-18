import random
secret_number = random.randint(1, 10)
print("I'm thinking of a number between 30 and 100. Can you guess it?")
guess = int(input("gues what is the number: "))
match guess:
    case n if guess < secret_number:
        print("Nope, your guess is a bit low. Give it another shot!")
    case n if guess > secret_number:
        print("Nope, your guess is a bit low. Give it another shot!")
    case secret_number:
        print("Congratulations, you guessed it!")
play_again = input("yes / no  : ").lower()
while play_again == "yes":
    continue