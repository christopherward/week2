#Christopher Ward
#MPCS 50101, Winter 2015
#Homework 2, Solution 1

def main():
    n = -1
    try:
        n = input("\nWhich nth number in the Fibonacci sequence do you need? (<Enter> to quit): ")
        while str(n) != "":
            Fib = [1,1]
            n = eval(n)
            #accept only a positive integer as input
            while n < 1 or int(n) != n:
                print("\nPlease enter a positive integer.")
                n = eval(input("\nWhich nth number in the Fibonacci sequence do you need? "))

            #compute the Fibonacci sequence until the nth number
            for i in range(2,n):
                Fib.append(Fib[i-1] + Fib[i-2])

            print(Fib)

            #print the nth number in the sequence
            if n == 1:
                print("\nThe " + str(n) + "st element in the Fibonacci sequence is:", Fib[n-1])
            elif n == 2:
                print("\nThe " + str(n) + "nd element in the Fibonacci sequence is:", Fib[n-1])
            elif n == 3:
                print("\nThe " + str(n) + "rd element in the Fibonacci sequence is:", Fib[n-1])
            else:
                print("\nThe " + str(n) + "th element in the Fibonacci sequence is:", Fib[n-1])

            n = input("\nWhich nth number in the Fibonacci sequence do you need? (<Enter> to quit) ")

    #handle some exception types in case the user entered characters or did something unexpected
    except NameError:
        print("Please enter a number. No letters or special characters allowed.")

    except:
        print("There was an error. Please try again.")
main()
