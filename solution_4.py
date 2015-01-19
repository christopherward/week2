#Christopher Ward
#MPCS 50101, Winter 2015
#Homework 2, Solution 4

def main():
    #Generates the Syracuse sequence for number n
    Syr = [0]
    n = .1

    try:
        while n < 1 or int(n) != n:
            n = eval(input("For which number would you like to generate the Syracuse sequence? "))
            if int(n) != n or n < 0:
                print("Please enter a positive integer.")

        print("Syracuse sequence: " + str(n), end="")
        
        while n != 1:
            if n % 2 == 0:
                n = n / 2
                print(",", str(int(n)), end="")
            else:
                n = n * 3 + 1
                print(",", str(int(n)), end="")

    except NameError:
        print("Please enter a number.")
    except:
        print("There was an unexpected error. Please try again.")

main()
