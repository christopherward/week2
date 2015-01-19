#Christopher Ward
#MPCS 50101, Winter 2015
#Homework 2, Solution 1

def main():
    Fib = [1,1]
    n = -1
    try:
        #accept only a positive integer as input
        while n < 1 or int(n) != n:
            n = eval(input("Which nth number in the Fibonacci sequence do you need? "))
            if int(n) != n or n < 0:
                print("Please enter a positive integer.")

        #compute the Fibonacci sequence until the nth number
        for i in range(2,n):
            Fib.append(Fib[i-1] + Fib[i-2])

        print(Fib)

        #print the nth number in the sequence
        print("Item number", n, "in the Fibonacci sequence is:", Fib[n-1])

    except NameError:
        print("Please enter a number. No letters or special characters allowed.")

    except:
        print("There was an error. Please try again.")
main()
