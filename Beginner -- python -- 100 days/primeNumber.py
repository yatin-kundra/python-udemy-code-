def prime_checker(number):
    isPrime = True

    for i in range(2,number):
        if number%i == 0:
            isPrime = False
    if isPrime:
        print(f"the number {number} is prime ")
    else:
        print(f"the number {number} is not prime")




number = input("enter a number to check if its a prime number: ")
number = int(number)


prime_checker(number)
