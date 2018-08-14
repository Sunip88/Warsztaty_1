from random import randint
'''
Simple guessing game. Default range is 1-100 but it takes max range argument (only integer). Returns tips about where your
guesses are located compared, to secret number. It also counts tries.
'''

def guess_game(guess_range=100):
    i = 0
    secret_num = randint(1, guess_range + 1)

    def validator(guess):
        if guess.isdigit():
            guess = int(guess)
            if 0 < guess < guess_range + 1:
                return 1
            else:
                return 2
        else:
            return 3

    while True:
        guess = input(f"Zgadnij liczbę z zakresu 1 - {guess_range}: ")
        guess_v = validator(guess)
        while guess_v > 1:
            if guess_v == 3:
                print("To nie jest liczba")
            elif guess_v == 2:
                print(f"Liczba poza zakresem (1 - {guess_range})")
            guess = input("Zgadnij liczbę: ")
            guess_v = validator(guess)
        guess = int(guess)
        i += 1
        if guess < secret_num:
            print("Za mało")
        if guess > secret_num:
            print("Za dużo")
        if guess == secret_num:
            print(f"Potrzebowałeś {i} prób")
            return("Zgadłeś")

print(guess_game())
# print(guess_game(1000))