# 🎲 Number Guessing Game 🎯
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100...")

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    guess = int(input("\n🤔 Your guess (1-100): "))
    attempts += 1

    if guess < secret_number:
        print("🔺 Go higher!")
    elif guess > secret_number:
        print("🔻 Go lower!")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} tries!")
        break

    remaining = max_attempts - attempts
    print(f"Attempts left: {remaining}")

if attempts == max_attempts:
    print(f"\n💥 Game Over! The number was {secret_number}")

# Bonus: Calculate score based on performance
score = max(0, 100 - (attempts * 10))
print(f"\n🏆 Your final score: {score}/100")
