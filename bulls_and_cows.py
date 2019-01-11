from random import randint

numbers = []
guess = []
j = 0
strike = 0

while len(numbers) < 3:
    new_number = randint(0, 9)
    while new_number in numbers:
        new_number = randint(0, 9)
    numbers.append(new_number)



while strike < 3:
    print('Three random numbers between 0 and 9 \n\n'
      'type three numbers below.')

    while len(guess) < 3:
        new_guess = int(input("%d st number : " % (len(guess)+1)))
        if new_guess in guess:
           print('number you already typed. try again.')
           continue
        elif new_guess > 9 or new_guess < 0:
           print('this number is not in your range. try again')
           continue
        else:
            guess.append(new_guess)
    i = 0
    strike = 0
    ball = 0

    while i <=2:
        if guess[i] == numbers[i]:
            strike = strike + 1
        elif guess[i] in numbers:
            ball = ball + 1
        i = i + 1
    j = j + 1

    print('%d S %d B' % (strike, ball))
    guess = []

print('congrats. you got  the number in %d trial' % (j))