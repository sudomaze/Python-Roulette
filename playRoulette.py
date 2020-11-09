# let's play roulette
import PythonRoulette
from importlib import reload
reload(PythonRoulette)
from PythonRoulette import *

play = roulette(rouletteStyle='French', bankAccount=8, betType='Color')
play.betType = 'Straight'
red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

index = 0
betting_stages = [1,1,2,4]
end_trial = 1000
current_step = 0
while current_step < end_trial and index < len(betting_stages):
    value = random.randint(1,36)
    # get
    rollHistory = play.rollHistory[-3:]
    patternHistory = play.rollHistory[-3:]
    colorHistory = play.colorHistory[-3:]

    # pre-process
    # small and large
    if(len(rollHistory) == 3):
        for i in range(3):
            if(rollHistory[i] > 18): # large
                rollHistory[i] = 1
            else: # small
                rollHistory[i] = 0
        # odd or even
        for i in range(3):
            if((patternHistory[i] % 2) == 0): # even
                patternHistory[i] = 2
            else: # odd
                patternHistory[i] = 1

        # print
        print(f'rollHistory: {rollHistory}')
        print(f'patternHistory: {patternHistory}')
        print(f'colorHistory: {colorHistory}')

        # check condition
        if len(set(rollHistory)) <= 1:
            if (rollHistory[0] == 1): # large, bet small
                print('rollHistory: LARGE -> SMALL')
                value = random.randint(1,18)
            else: # small, bet large
                print('rollHistory: SMALL -> LARGE')
                value = random.randint(19,36)
            print(f'value: {value}')
            play.roll(betting_stages[i], value)
            index = index + 1
        elif len(set(patternHistory)) <= 1:
            if (patternHistory[0] == 2): # even, bet odd
                print('rollHistory: EVEN -> ODD')
                value = random.randrange(1, 35, 2)
            else: # odd, bet even
                print('rollHistory: ODD -> EVEN')
                value = random.randrange(2, 36, 2)
            print(f'value: {value}')
            play.roll(betting_stages[index], value)
            index = index + 1
        elif len(set(colorHistory)) <= 1:
            if (colorHistory[0] == 'Red'): # Red, bet Black
                print('rollHistory: Red -> Black')
                value = black_numbers[random.randint(0,len(black_numbers)-1)]
            else: # Black, bet Red
                print('rollHistory: Black -> Red')
                value = red_numbers[random.randint(0,len(red_numbers)-1)]
            print(f'value: {value}')
            play.roll(betting_stages[index], value)
            index = index + 1
        else:
            print(f'value: {value}')
            play.roll(0, value)
    else:
        print(f'value: {value}')
        play.roll(0, value)
    current_step = current_step + 1
print(f'play.bankAccount = {play.bankAccount}, current_step = {current_step}')
