import random
from genetics import rndInt

rng = random.Random()


x = [random.randint(0, 10) for i in range(10)]
y = [rndInt(rng, 0, 10) for i in range(10)]
print(x)
print(y)