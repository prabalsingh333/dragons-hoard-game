import random

total_gold = 0
def steal():
    gold = random.randint(1,10)
    return gold

wish = input('Do you want to steal gold? (Y/N) ').upper()

while wish == 'Y':
    stolen_gold = steal()
    total_gold += stolen_gold
    print(f'You grabbed {stolen_gold} gold coins. You now have {total_gold} gold coins.')
    dragon_roll = random.randint(1, 20)
    if dragon_roll == 1:
        print('ROAR! The dragon caught you!')
        print('You lose all your gold coins!')
        total_gold = 0
        break
    wish = input('Do you want to steal more gold? (Y/N) ').upper()
else:
    print(f'You stole {total_gold} gold coins from the dragon!')
