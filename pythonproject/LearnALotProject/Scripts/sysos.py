import os
import sys
#print(dir(os))

# print("os.name ", os.name)
# print(os.environ)
# print(os.getlogin())
# print(os.getppid())
# print(os.getcwd())
# #filefound = open("abc.txt")
# print(os.listdir())
# #os.mkdir("trial") # will through error if already exist
# #os.makedirs("This\That\why\what") # will through error if already exist
# #os.rename("abc.txt", "xyz.txt") # will through error if DOES NOT exist
# os.chdir("c:/")
# print(os.getcwd())
# print(os.environ.get('PATH'))
# # sys.exit() #This will tell python interpreter to quit the execution. It stops the execution so it will not run below lines.
# print(os.path.join("c://", "/Users")) # It takes one or more paths and join them by using current OS path separator.
# print(os.path.abspath("../randomgame/")) # It take relative path and return the absolute path.
# print(os.path.normpath("../randomgame/.")) # convert path from non standard to standardized format.
# print(os.path.exists("c:/"))
# print(os.path.isfile("c://ProgramData"))
# print(os.path.split(os.getcwd()))
# print(os.path.split("C:/Users/GIRISHPAREEK/Desktop/Amity/PythonByGirishPareek/pythonproject/randomgame/sysos.py"))
# print(os.path.splitext("C:/Users/GIRISHPAREEK/Desktop/Amity/PythonByGirishPareek/pythonproject/randomgame/sysos.py"))
# print(os.path.splitext(os.getcwd()))
for (root,dirs,files) in os.walk(os.getcwd()):
    print(root)
    print(dirs)
    print(files)
    print('--------------------------')

# #================================
# print(sys.winver)
# print(sys.flags) # it displays command lines sequence of all the flags
# print(sys.prefix) # it point to the venv directory OR A string giving the site-specific directory prefix where the
# # platform independent Python files are installed; by default, this is the string '/usr/local'.
# # This can be set at build time with the --prefix argument to the configure script.
#
#
#
#
#
