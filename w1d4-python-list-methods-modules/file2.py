# importing modules and methods 
import file1

file1.say_hello()

# ---------------------------------#

import file1 as greetings

greetings.say_goodbye()

# ---------------------------------#

from file1 import say_hello as hello, say_goodbye as bye

hello()
bye()

