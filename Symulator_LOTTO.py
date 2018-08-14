import random


def lotto(random_num=False, r_num=1):
    lotto_num = random.sample(range(1, 50), 6)
    won = 0

    def correct_num(n, human_num):
        if type(n) == int:
            if n in human_num:
                return 1
            if n not in range(1, 50):
                return 2
            return 0

    def human_choice():
        human_num = []
        for i in range(1, 7):
            inp = input(f"Select {i}. number: ")
            while inp == "" or not inp.isdigit():
                inp = input(f"Select {i}. number: ")
            input_int = int(inp)
            while correct_num(input_int, human_num) > 0:
                if correct_num(input_int, human_num) == 1:
                    print(f'Choosen numbers: {human_num} \nThis number is taken, select different one.')
                elif correct_num(input_int, human_num) == 2:
                    print('Select numbers from 1-49')
                input_int = int(input(f"Select {i}. number: "))
            human_num.append(input_int)
        return human_num

    def random_choice():
        rnd_num = random.sample(range(1, 50), 6)
        return rnd_num

    def normal_game(won):

        if random_num:
            chosen_num = random_choice()
        else:
            chosen_num = human_choice()

        chosen_num_sort = sorted(chosen_num)
        for i in chosen_num:
            if i in lotto_num:
                won += 1
        if r_num == 1:
            print(chosen_num_sort, "Your numbers")
            print(lotto_num, "Prize numbers")
            if won > 3:
                print(f"Congratulations you won {won}")
            else:
                print("Play again")
        return won


    if r_num == 1:
        normal_game(won)
    else:
        winner_list = []
        win3 = 0
        win4 = 0
        win5 = 0
        win6 = 0
        for i in range(r_num):
            if not random_num:
                print(f"{i + 1} game")
            winner_list.append(normal_game(won))
        for i in winner_list:
            if i == 3:
                win3 += 1
            elif i == 4:
                win4 += 1
            elif i == 5:
                win5 += 1
            elif i == 6:
                win6 += 1
        sum_win = win3 + win4 + win5 + win6
        print(f"You win {sum_win} games in {r_num} tries:\n\n{win3} times you matched 3 numbers \n{win4}"
              f" times you matched 4 numbers \n{win5} times you matched 5 numbers \n{win6} times you matched 6 numbers ")

lotto(False, 5)