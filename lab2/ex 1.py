def greet(user_name: str):
    print(f"Привет, {user_name}")
    
def square(number: int):
    print(number ** 2)

def max_of_two(x: int, y: int):
    if x > y: print(x)
    elif y > x: print(y)
    else: print("Числа равны.") 


greet(input())
square(int(input()))
max_of_two(int(input()), int(input()))