def hello():
    print("hello world")
    hello()

# hello()

def space_x_countdown(num):
    # fancy way of counting down
    for i in range(num, 0, -1):
        print(i)
    
    return "liftoff"

# print(space_x_countdown(10))

def space_x_countdown_recursive(num):
    # Base case
    if num == 0:
        return "Liftoff!"

    print(num)
    num_minus_one = num - 1
    return space_x_countdown_recursive(num_minus_one)

space_x_countdown_recursive(10)