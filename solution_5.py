#Christopher Ward
#MPCS 50101, Winter 2015
#Homework 2, Solution 5

import math

def main():
    n = .1

    try:
        n = input("\nEnter a positive integer. (<Enter> to quit): ")
        #determines whether a given number, n, is prime
        #accept only a positive whole number as input
        while n != "":
            n = eval(n)
            while n < 1 or int(n) != n:
                print("\nThe number you entered is not a positive integer. Please enter a new number.")
                n = eval(input("\nEnter a positive integer. "))

            rootn = math.ceil(math.sqrt(n))

            prime = 1
            divisors = []
            #for loop iterates through all possible divisors for n
            for i in range(2,rootn+1):
                if n / i == int(n / i):
                    prime = 0
                    divisors.append(i)

            #print result
            if prime == 1:
                print(n, "is prime.")
            else:
                print(n, "is not prime. For example, it is divisible by", divisors[0])

            n = input("\nEnter a positive integer. (<Enter> to quit): ")

    except NameError:
        print("Please enter numeric data. No letters allowed.")
    except:
        print("There was an unexpected error. Please try again.")

main()
