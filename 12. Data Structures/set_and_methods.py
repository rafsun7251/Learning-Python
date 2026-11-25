## Sets 

s ={3,4,6,2,5}
d = [3,56,67,467]
f = (22,4532,54,546)
print(s, type(s))  ## sets 
print(d, type(d))  ## list 
print(f, type(f))  ## Tuple 

## Sets Methods

q = {54,36,44,86,43,11,86,46,3}
q.add(22)  ## add 22 in sets
q.remove(36) ## remove 36 from sets
q.discard(533452) ## if 533452 find in set then remove otherwise do nothing 
q.pop() ## remove any set number from sets 

print(q) 

## Sets Operations 

e = {1,3,4,6,7,9}
r = {2,4,6,8,7,9}

t = e.union(r)
print(t) 
print(e.union(r))

y = e.intersection(r)
print(y)
print(e.intersection(r))
print(r.intersection(e))

u = e.difference(r)
print(u)
print(e.difference(r))
