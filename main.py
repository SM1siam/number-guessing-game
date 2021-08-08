import random

n = random.randint(1, 3)
a = input('I have a number in my mint. Can you guess it?. It is in between 1 and 3 :')
run = True
count = 0
if int(n) == int(a):
    print('You got it right in 1 try')
    run = False
else:
    print('You are wrong')

while run:
    count += 1
    a = input('Type the number : ')
    if int(n) == int(a):
        print(f'you got it right in {count} tires')
        run = False
    else:
        print('wrong, try again.')
