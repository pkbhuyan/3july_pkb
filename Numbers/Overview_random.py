

import random

print(random.choice([123, 789, "three_hundred", 345, 901, [5.6, 7.8]]))      # A Non Empty sequence is provided

# print(random.randrange(100, 110, 5))   # Starting point ,ending Point and step should be provided

#random.seed(50) # Every random number has a seed value ,if you know their seed value ,
# then everytime you mention these seeds within function seed() you will get the desied random value.
print(random.random( )) # Displays a random number in between the 0 & 1

#random.seed(50)
print(random.random())

#random.seed(30)
# print(random.randint(10.6, 14)) # will give Error
print(random.randint(10, 14))

print("Generation of float Numbers", random.uniform(1, 2)) # random.uniform() can be used for generating
# floating point numbers in between desired values.


# seed() applies to choice(),randrange(),randint()

list1 =[123, 789, 345, 901]
print(random.shuffle(list1)) # will give the result as none as random.shuffle returns none by default
print(list1) # will display the shuffled list









