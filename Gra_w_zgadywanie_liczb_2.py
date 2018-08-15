def guessing_2():
    """
    Another guessing game. Default range is 1-1000. User should enter '1', '2' or '3' depending on guessing number.
    It also counts tries.
    """

    input("Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach.\nJak będziesz gotowy wciśnij enter.")
    # print("Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach")
    min_num = 0
    max_num = 1000
    check = ''
    guess = 0
    n = 0
    while check != 3:
        temp_guess = guess
        guess = int((max_num - min_num) / 2) + min_num
        if temp_guess == guess:
            print("nie oszukuj")
            break
        print(f"Zgaduję: {guess}")
        n += 1
        check = input("Zgadłem ? (Wpisz numer opisujący stan: 1: za duzo, 2: za malo, 3: zgadles): ")
        while not check.isdigit():
            print("Prosze wybrać liczbę odpowiadającą za stan gry.")
            check = input("Zgadłem ? (Wpisz numer opisujący stan: 1: za duzo, 2: za malo, 3: zgadles): ")
        check = int(check)
        if check == 3:
            print(f"Wygrałem, potrzebowałem {n} prób")
        elif check == 1:
            max_num = guess
        elif check == 2:
            min_num = guess
        else:
            print("Taka odpowiedź nie istnieję.")
            break


guessing_2()
