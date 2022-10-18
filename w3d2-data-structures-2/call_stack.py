my_list = ["a", "b", "c"]

# print(my_list)
# print(my_list.pop())
# print(my_list)

def first():
    print('PUSH first function executes ..')
    second()
    print('POP first function resolves ..')

def second():
    print('PUSH second function executes ..')
    third()
    print('POP second function resolves ..')

def third():
    print('PUSH third function executes ..')
    print('POP third function resolves ..')


first()