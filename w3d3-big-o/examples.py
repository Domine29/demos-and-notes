def example_1(my_list):
    total = 0
    for x in my_list:
        value = x ** 2
        if value > 20:
            for y in my_list:
                if y > 0:
                    total += y + value
    return total



def example_2(my_list):
    for item in my_list:
        counter = my_list.count(item)
        if counter > 2:
            return True

    return False




def example_3(my_list):
    yummy_list = ["donut", "cake", "pie", "muffin"]

    food_list = []
    for item in my_list:
        if isinstance(item, str):
            food_list.append(item)

    yummy_count = 0
    for food in food_list:
        for yummy in yummy_list:
            if food == yummy:
                yummy_count += 1

    return yummy_count