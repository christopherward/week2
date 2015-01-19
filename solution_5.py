#Christopher Ward
#MPCS 50101, Winter 2015
#Homework 2, Solution 5

import math

def main():
    try:
        n = .1
        #determines whether a given number, n, is prime
        #accept only a positive whole number as input
        while n < 1 or int(n) != n:
            n = eval(input("Enter a whole number: "))
            if int(n) != n or n < 0:
                print("The number you entered is not a positive integer. Please enter a new number.")

        rootn = math.ceil(math.sqrt(n))

        prime = 1
        #for loop iterates through all possible divisors for n
        for i in range(2,rootn+1):
            if n / i == int(n / i):
                prime = 0
                divisor = i

        #print result
        if prime == 1:
            print(n, "is prime.")
        else:
            print(n, "is not prime. For example, it is divisible by", divisor)

    except NameError:
        print("Please enter numeric data.")
    except:
        print("There was an unexpected error. Please try again.")

main()
