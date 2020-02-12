import sys

number = int(sys.argv[1])

def isPrime():
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is not a prime number")
                break
        else:
            print(number, "is a prime number")

    # if the entered number is less than or equal to 1
    # then it is not prime number
    else:
        print(number, "is not a prime number")

isPrime()
