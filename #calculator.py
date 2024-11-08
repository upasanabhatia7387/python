# calculator
class solution:
    def add(self, a1, a2) -> float:
        return a1+a2

    def sub(self, s1, s2) -> float:
        return s1-s2

    def div(self, d1, d2) -> float:
        if d2 == 0:
            return "division by zero error. please enter a non zero integer"
        else:
            return d1/d2

    def mul(self, m1, m2) -> float:
        return m1*m2


obj = solution()
while True:
    print("what do you want to calculate today?")
    print("choose one: add, sub, mul, div or type end to exit")
    option = input("Enter your choice:").strip().lower()

    if option == "end":
        print("Existing the calcultor. Byeee")
        break

    match option:
        case "add":
            print("You have choosen Add. Please enter two numbers:")
            a1 = float(input("Enter your first number:"))
            a2 = float(input("Enter your second number:"))
            print(obj.add(a1, a2))
        case "sub":
            s1 = float(input("Enter your first number:"))
            s2 = float(input("Enter your second number:"))
            print(obj.sub(s1, s2))
        case "mul":
            m1 = float(input("Enter your first number:"))
            m2 = float(input("Enter your second number:"))
            print(obj.mul(m1, m2))
        case "div":
            d1 = float(input("Enter your first number:"))
            d2 = float(input("Enter your second number:"))
            print(obj.div(d1, d2))
        case _:
            print(
                "invalid option. Please choose correct option i.e add,sub,mul,div or end to exit")
