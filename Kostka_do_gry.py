import re
from random import randint

"""
Application returns 'False' or result of Dice equation (xDy+z as string np.: '2D10+10' or 'D12-1' where:
        x - is number of Dice, 
        y - is Dice type np. D6, D10, 
        z - is value that application should add or remove).
    'False' is returned when argument 'dice_code' differs from equation.
"""


def dice(dice_code):
    if type(dice_code) == str:
        pattern = re.compile(r'^([1-9][0-9]*)?[D](100|20|12|10|[3468])([+-])?([1-9][0-9]*)?$')
        match = pattern.fullmatch(dice_code)
        if match is not None:
            num_dices = match.group(1)
            dice_type = int(match.group(2))
            dice_mode_sign = match.group(3)
            dice_mode = match.group(4)
            sum_dice = 0
            if num_dices is not None:
                num_dices = int(num_dices)
            else:
                num_dices = 1
            i = 1
            while i <= num_dices:
                draw = randint(1, dice_type)
                sum_dice += draw
                i += 1
            if dice_mode is not None:
                dice_mode = int(dice_mode)
                if dice_mode_sign == '+':
                    sum_dice += dice_mode
                elif dice_mode_sign == '-':
                    sum_dice -= dice_mode
            return sum_dice
        else:
            return False
    else:
        return False


print(dice('19D100+1000'))
print(dice("2D10+10"))
print(dice("D6"))
print(dice("2D3"))
print(dice("D12-100"))
print(dice("019D100+1000"))
print(dice("15D200+1000"))
print(dice("15D100+0100"))
print(dice("lambada"))
print(dice(185))
print(dice("2D6-3"))