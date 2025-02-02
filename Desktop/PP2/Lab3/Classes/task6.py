def check_for_prime(num):
    if(num < 2):
        return False
    for i in range(2, num):
        if num%i == 0:
            return False
    return True
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
prime_numbers = list(filter(lambda num: check_for_prime(num), numbers))
print("Prime numbers: ", prime_numbers)
