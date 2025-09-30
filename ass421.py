def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"Addition: {add(num1, num2)}")
    print(f"Subtraction: {subtract(num1, num2)}")
   

if __name__ == "__main__":
    main()
