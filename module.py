# using created module ---- mymodule.py

 # importing mymodule.py file
import mymodule 

# calling say_hello function from mymodule.py file

mymodule.say_hello(' sakk') 

# calling say_bye function from mymodule.py file

mymodule.say_bye(' sakshi')

# importing specific part of code from mymodule.py file
from mymodule import person1

# printing person1 dictionary from mymodule.py file

print(person1['age'])
# this will print the age of person1 from the mymodule.py file

