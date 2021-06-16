from array import array
# arrays are useful in case if you don't want to use genreators but far better formance then list.
# it is a fix object unlike list which can be modified on fly.

# arr = array('i',[2,4,5,6])
# print(arr)
# print(arr[0], arr[3])

import pathlib

print(pathlib.Path.cwd())

fileobject = open('simplefile.txt')
print(fileobject.read())  # open file has a cursor so you can't read it multiple times.
fileobject.seek(0)
print(fileobject.read())
print(fileobject.read())  # These reads will not work because after above read cursor went to the end of file.
print(fileobject.read())

print('next command -- readline()')
fileobject.seek(0)
print(fileobject.readline())  # this will reach each line by line in a file based on cursor location.
print(fileobject.readline())
print(fileobject.readline())

print('next command -- readlines()')  # this will create and return a list. It includes all the new line characters etc.
fileobject.seek(0)
print(fileobject.readlines())
fileobject.close()  # you must close the file so that it can be release and used by other

# what is better way?
print("what is better way to read with file?")
with open('simplefile.txt') as myfile:  # default here is mode = 'r'
    # this is the normal way to deal with files now. It does not require you to close the file.
    print(myfile.readlines())

print("To read and write a file?")
with open('simplefile.txt', mode='a') as myfile:  # default here is mode = 'r'
    # this is the normal way to deal with files now. It does not require you to close the file.
    text = myfile.write("This is me :)")
   
