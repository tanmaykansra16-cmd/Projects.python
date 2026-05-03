import art



def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 -n2

def multiply(n1 ,n2):
    return n1* n2

def divide(n1,n2):
    return n1/n2

operations= {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,

}
def calculator():
    print(art.logo)
    should_continue = True
    num1 = float(input("what is your first number? "))
    while should_continue:

        for symbol in operations:
            print(symbol)
        symbols =input("pick an operations to perform: ")

        num2= float(input("what is the next number?"))
        ans = operations[symbols](num1,num2)
        print(f"{num1} {symbols} {num2} = {ans}")

        choice = input(f"type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation: ").lower()
        if choice =="y":
            num1 = ans
        else:
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()



