def multiply_numbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    print("Multiplication of all numbers:", result)

def main():
    # Example list of numbers
    numbers = [2, 3, 4, 5]
    multiply_numbers(numbers)

if __name__ == "__main__":
    main()
