import random

n = int(random.randint(1, 3))
run = True
a = int(input('I have a number in my mind, can you guess it between 1 and 3? : '))
if n == a:
    print('correct!')
    print('you guessed the number in 1 try.')
    run = False
else:
    print('wrong, try again')
count = 1
while run:
    count += 1
    a = int(input('Type the number: '))
    if n == a:
        print('correct!')
        print(f'You guessed the correct number in {count} try.')
        run = False
    else:
        print('wrong, try again ')
