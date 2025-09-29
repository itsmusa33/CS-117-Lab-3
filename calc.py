
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
    
def even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

def percentage(part, whole):
        return (part / whole) * 100
   
while True:
    print("\n--- Simple Calculator ---")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Check Even/Odd")
    print("6. Calculate Percentage")
    print("7. Exit")

    choice = input("Choose an option (1-7): ")

    if choice == '1':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", add(a, b))

    elif choice == '2':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", subtract(a, b))

    elif choice == '3':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", multiply(a, b))

    elif choice == '4':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", divide(a, b))

    elif choice == '5':
        num = int(input("Enter a number: "))
        print("The number is", is_even(num))

    elif choice == '6':
        part = float(input("Enter the part value: "))
        whole = float(input("Enter the whole value: "))
        print("Percentage:", percentage(part, whole), "%")

    elif choice == '7':
        break

    else:
        print("Invalid option. Please try again.")