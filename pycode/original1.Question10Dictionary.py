# Q 10: Take dictionary d1 as below:
# d1 = {"one":1, "two":2, "three":3, "four":4}. Create two tuples (t1 and t2) from the dictionary d1, such that t1 contains keys and t2 contains values.

d1 = {"one":1, "two":2, "three":3, "four":4}
t1 = []
t2 = []
for i in d1:
    print(i)
    t1.append(i)
    t2.append(d1.get(i))
       
print(t1)
print(t2)

