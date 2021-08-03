#WORKSHOP

'''
#4
'''
import random
from faker import Faker

random.random()
random.random()

random.seed(7777)
print(random.random())

random.seed(7777)
print(random.random())


fake = Faker('ko_KR')
# fake.seed_instance(4321) 
Faker.seed(4321) 

print(fake.name()) #1

fake2 = Faker('ko_KR')
print(fake2.name()) #2