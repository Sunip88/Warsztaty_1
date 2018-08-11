import random


def lotto(random_num=False, r_num=1):
    lotto_num = random.sample(range(1, 50), 6)
    chosen_num = []
    z = 0

    def correct_num(n):
        if type(n) == int:
            if n in chosen_num:
                return 1
            if n not in range(1, 50):
                return 2
            return 0

    for i in range(1, 7):
        inp = input(f"Podaj {i} liczbę")
        while inp == "":
            inp = input(f"Podaj {i} liczbę")
        input_int = int(inp)
        while correct_num(input_int) > 0:
            if correct_num(input_int) == 1:
                print(f'Wybrane liczby to: {chosen_num} \nLiczba została już wybrana proszę wybrać inną liczbę.')
            elif correct_num(input_int) == 2:
                print('Podaj liczbę z zakresu 1 - 49')
            input_int = int(input(f"Podaj {i} liczbę"))
        chosen_num.append(input_int)
    chosen_num_sort = sorted(chosen_num)
    print(chosen_num_sort)
    print(lotto_num)
    for i in chosen_num:
        if i in lotto_num:
            z += 1
    if z > 3:
        return(f"Gratulacje trafiłeś {z}")
    else:
        return("Graj dalej")


print(lotto())