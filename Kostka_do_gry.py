import re
from random import randint


def Dice(dice_code):
    if type(dice_code) == str:
        if re.match('^([1-9][0-9]*)?[D]([1][0][0]|[2][0]|[1][2]|[1][0]|[3468])[+-]?([1-9][0-9]*)?$', dice_code):
            num_dices_raw = re.search('^([1-9][0-9]{0,6})?[D]', dice_code) # wszystko do D
            num_dices = num_dices_raw.group(0).replace('D', '')
            dice_raw = re.search('[D]([1][0][0]|[2][0]|[1][2]|[1][0]|[3468])', dice_code)  # kostka
            dice = int(dice_raw.group(0).replace('D', ''))
            dice_mode_raw = re.search('[+-]?([1-9][0-9]*)?$', dice_code)  # modyfikator
            if dice_mode_raw.group(0) != '':
                dice_mode = dice_mode_raw.group(0)[1:]
                dice_mode_sign = dice_mode_raw.group(0)[:1]
            else:
                dice_mode = ''
            sum_dice = 0
            if num_dices != '':
                num_dices = int(num_dices)
            else:
                num_dices = 1
            i = 1
            while i <= num_dices:
                draw = randint(1, dice)
                sum_dice += draw
                i += 1
            if dice_mode != '':
                dice_mode = int(dice_mode)
                if dice_mode_sign == '+':
                    sum_dice += dice_mode
                elif dice_mode_sign == '-':
                    sum_dice -= dice_mode
            return sum_dice, dice_raw.group(0)
        else:
            return False
    else:
        return False

print(Dice('19D100+1000'))
print(Dice("2D10+10"))
print(Dice("lambada"))
print(Dice(185))
print(Dice("D6"))
print(Dice("2D3"))
print(Dice("D12-100"))
print(Dice("019D100+1000"))
print(Dice("15D200+1000"))
print(Dice("15D100+0100"))

print(Dice("2D6-3"))