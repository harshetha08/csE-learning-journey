import random

# Guessing Game
print("=" * 40)
print("Welcome to Number Guessing Game! 🎮")
print("=" * 40)
print("I'm thinking of a number between 1-100")
print("Can you guess it?")
print()

# Generate random number
number = random.randint(1, 100)
attempts = 0
guessed = False

# Game loop
while not guessed:
    try:
        # Take user input
        guess = int(input("Enter your guess (1-100): "))
        
        # Validate input
        if guess < 1 or guess > 100:
            print("⚠️ Please enter a number between 1-100!")
            continue
        
        attempts += 1
        
        # Check if guess is correct
        if guess == number:
            print()
            print("=" * 40)
            print(f"🎉 Correct! The number was {number}!")
            print(f"✨ You took {attempts} attempts!")
            print("=" * 40)
            guessed = True
        elif guess < number:
            remaining = number - guess
            print(f"📈 Too low! Try a higher number.")
            print(f"   (Attempts: {attempts})")
        else:
            remaining = guess - number
            print(f"📉 Too high! Try a lower number.")
            print(f"   (Attempts: {attempts})")
        
        # Hint after 5 attempts
        if attempts == 5:
            print("💡 Hint: You're getting closer!")
    
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")

print()
print("Thanks for playing! 👋")
