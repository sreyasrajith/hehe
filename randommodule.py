import random


random_variable = random.random()
random_int_variable = random.randint(1111,9999)
random_range_variable = random.randrange(100,1000,10000)
uniform_random_variable = random.uniform(3,4)

sample_list = [1,3,56,78]

choice_variable = random.choice(sample_list)
random.shuffle(sample_list)
print(sample_list)
