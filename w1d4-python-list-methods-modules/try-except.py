try:
    a = 1
    b = 3
    c= 'cat'

    v = a + c
    d = a+b
    print(d)

    v = a + c
except: # will run on failure of try block
    print('oh no we got an error')

    try:
        c = 'n'+ 4

    except:
        print('no')

else: # will run on seccess of try block
    print('yay success')

finally:     # will always run 
    print('try except tested' )


