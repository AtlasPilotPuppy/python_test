"""Complete this program to find the greatest produdct of five consecutive
digits in the list"""
import re
in_file = open('array.txt')


stnum = re.sub(r"\n","", in_file.read())
print stnum
s = 0
e = 5
largeval = 0
while e <= len(stnum):
    subset = stnum[s:e]
    prod = reduce(lambda x,y : x*y, [int(x) for x in subset])
    if prod > largeval:
        largeval = prod
    s += 1
    e += 1
    
print largeval
