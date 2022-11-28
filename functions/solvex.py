def solve_eqn(equation):
    x, add, num1, equal, num2 = equation.split()
    num1, num2 = int(num1), int(num2)
    return "x = "+ str(num2 - num1)

print(solve_eqn("x + 4 = 9"))