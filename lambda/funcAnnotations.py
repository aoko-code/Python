#mainly used as documentation
def random_func(name: str, age: int, weight: float) -> str:
    print("Name: ", name)
    print("age: ", age)
    print("weight: ", weight)
    return "{} is {} years old and weighs {} ".format(name, age, weight)
print(random_func("harrison", 40, 100))
print(random_func.__annotations__)