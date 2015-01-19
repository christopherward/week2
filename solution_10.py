#Christopher Ward
#MPCS 50101, Winter 2015
#Homework 2, Solution 10

def main():
    #ask user for location of mileage data
    try:
        filename = input("Where are the travel data located? ")
        infile = open(filename,'r')
 
        #initialize variables to hold MPG data
        miles = []
        gas = [0]
        legs = 0
        line = infile.readline()

    except FileNotFoundError:
        print("\nPlease enter a valid file name.")

    #read file
    try:
        while line != "":
            #read only odometer from first line
            if legs == 0:
                miles.append(eval(line))
                
            #for all subsequent lines, read both odometer and gas estimate
            elif legs > 0:
                miles.append(eval(line.split(" ")[0]))
                gas.append(eval(line.split(" ")[1]))
            legs = legs + 1
            line = infile.readline()

        #print MPG for each leg, followed by overall MPG for total journey
        for i in range(1,legs):
            print("\nThe MPG for leg", i ,"is: ", (miles[i] - miles[i-1]) / (gas[i]))
        print("\nThe MPG for all legs is: ", (miles[legs-1] - miles[0]) / sum(gas))
    except NameError:
        print("\nPlease use a file with numeric data only. Restart the program and try again.")
    except:
        print("\nThere was an unexpected error. Please restart the program and try again.")
main()
