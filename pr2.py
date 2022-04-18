import statistics as s

l1=[10,50,80,70,49,23,11,4]

mn = min(l1)
mx = max(l1)
men = s.mean(l1)
sd = s.stdev(l1)
vr = s.variance(l1)

print(round(mx,2))
print(round(men,2))
print(round(sd,2))
print(round(vr,2))