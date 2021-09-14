from random import randint

colors = ['red', 'blue', 'black', 'pink']
generator = randint(0,len(colors)-1)
guess = input('guess a color: ')

for color in colors[generator]:
    if guess != colors[generator]:
        print('wrong, try again')
        guess = input('guess a color: ')
    elif guess == colors[generator]:
        break


print('hey!! color was: ' + colors[generator])
