"""There were several moments over the last few weeks when I heard people discuss differences between Python lists
and dicts and one of the first ones mentioned was that lists are ordered and dicts are not. Well, not anymore.
Quoting the docs referenced above: Changed in version 3.7: Dictionary order is guaranteed to be insertion order. This
behavior was an implementation detail of CPython from 3.6. So if you want to discuss fundamental differences you can
pretty much only point out that dict values are accessible by keys, which could be of any immutable type, while list
values are indexed with integers. That's it :-) """
from collections import Counter, defaultdict, OrderedDict
li = [1,2,3,4,4,5,5,5,6,7,8]
sentence = "blah blah blah thinking about python"
print(Counter(li))
print(Counter(sentence)) # create hash map \ dictionary - duplicate emails or duplicate words etc.
dictionary = {'a': 1, 'b': 2}
dictionary1 = {'b': 2, 'a': 1}
print("validate if values of both dict are same in order = ", dictionary == dictionary)
# if we try to access a key which already exist then we can get the value. but what if we try to access a key which
# does not exist then we will get an error ... so how to easily overcome that? lets try ..
print("value = ", dictionary['a'])
#print(dictionary['c']) # we are getting KeyError
dictionary = defaultdict(lambda: 'Does not exist', {'a': 1, 'b': 2}) # it will require a first argument a function even lambda function
print("value = ", dictionary['a'])
print("value = ", dictionary['b'])
print("value = ", dictionary['c']) # this is due to lambda function.. we are not getting an error.

# now let us understand Ordereddict() - This gives guarantee of dictionary created will be in order although may
# have some performance issues.
d1 = OrderedDict({'a': 1, 'b': 2})
print(d1['a'])
d2 = OrderedDict({'a': 1, 'b': 2})
d3 = OrderedDict({'b': 2, 'a': 1})
print('validate if values of both dict are same in order = ', d1 == d2)
print('validate if values of both dict are same in order = ', d1 == d3)
