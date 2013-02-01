import random
from pympler import summary, muppy, asizeof
from time import time

hs = set()
q = 1000000
def rand_string(l):
    return ''.join(chr(random.randint(97,122)) for i in range(l))
x = 1
ti = time()
for i in range(q):
    fields = (rand_string(8) for i in range(12))
    h = hash(tuple(fields))
    hs.add(h)
    if x % 100000 == 0:
        print x
        print time() - ti
        ti = time()
    x +=1
all_objects = muppy.get_objects()
suml = summary.summarize(all_objects)
summary.print_(suml)
len(hs)
