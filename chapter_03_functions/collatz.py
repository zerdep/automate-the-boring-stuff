def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

num = 5

try:
    print("Enter number:")
    num = int(input())
    while num != 1:
        num = collatz(num)
        print(num)
except ValueError:
    print("you must enter an integer number")