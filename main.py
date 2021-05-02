"""
Pick some positive integer and call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one.
"""

def main():
    num = int(input("Enter a number: "))
    result = 0 # variable that will be the result of the action and then the original value
    i = 0 # variable to count steps until num is equal to one
    while result != 1:
        if num % 2 == 0:
            result = num // 2
            print(num, "is even, so I take half:", result)
            num = result
            i += 1
        else:
            result = num * 3 + 1
            print(num, "is odd, so I make 3n+1:", result)
            num = result
            i += 1
    print("The process took", i, "steps to reach 1")

if __name__ == "__main__":
    main()