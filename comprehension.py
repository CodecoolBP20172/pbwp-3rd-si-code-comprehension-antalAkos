import random  # import the random module

guessesTaken = 0  # create the guessesTaken variable with the 0 initial value

print('Hello! What is your name?')  # print the text inside brackets
myName = input()  # prompt the user to input a name

number = random.randint(1, 20)  # create the number variable with a random value between 1 and 20 using the randint function
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # print a message with the user input name included

while guessesTaken < 6:  # initialize a while loop which runs repeatedly while the value of guessesTaken is below 6
    print('Take a guess.')  # prints the message
    guess = input()  # create the guess variable which gets a value from a user input
    guess = int(guess)  # converts the guess variable to integer

    guessesTaken += 1  # the value of guessesTaken variable is increased by one

    if guess < number:  # create a condition for the case when the guess is smaller than the number
        print('Your guess is too low.')  # print message if the case is true

    if guess > number:  # create a condition for the case when the guess is greater than the number
        print('Your guess is too high.')   # print message if the case is true

    if guess == number:  # check if the guess given by the user equals the randomly generated number
        break  # exit the while loop

if guess == number:  # if the two variables are equal
    guessesTaken = str(guessesTaken)  # convert the guessesTaken variable to a string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # print a message

if guess != number:  # in the case that the guess is not equal to the number
    number = str(number)  # transform the number to string
    print('Nope. The number I was thinking of was ' + number)  # print message revealing the value of number to the user
