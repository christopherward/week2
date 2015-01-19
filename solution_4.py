#Christopher Ward
#MPCS 50101, Winter 2015
#Homework 2, Solution 4

def main():
    #generates the Syracuse sequence for number n
    n = .1

    try:
        #accept only a positive integer as input
        n = input("\nFor which number would you like to generate the Syracuse sequence? (<Enter> to quit): ")
        while n != "":
            n = eval(n)
            while n < 1 or int(n) != n:
                print("\nPlease enter a positive integer.")
                n = eval(input("\nFor which number would you like to generate the Syracuse sequence? "))

            print("\nSyracuse sequence: " + str(n), end="")
            
            #print the complete Syracuse sequence until the nth element equals 1
            while n != 1:
                if n % 2 == 0:
                    n = n / 2
                    print(",", str(int(n)), end="")
                else:
                    n = n * 3 + 1
                    print(",", str(int(n)), end="")

            n = input("\n\nFor which number would you like to generate the Syracuse sequence? (<Enter> to quit): ")

    #handle exceptions when user does not enter valid, numeric data
    except NameError:
        print("\nThere was an error. Please enter a number.")
    except:
        print("\nThere was an unexpected error. Please try again.")

main()
