class Book():
    favorites = []
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    def is_long(self):
        if self.pages > 100:
            return True
        return False
    def __str__(self):
        return f"{self.title} is {self.pages} long."
    def __eq__(self, other):
        if self.title == other.title and self.pages == other.pages:
            return True
        return False
    def __hash__(self):
        return hash(self.title) ^ hash(self.pages)

book = Book("Are you my mother?", 72)

open("input.txt", 'a') # if the file does not exist it will create it.
file = open("input.txt", 'w')
file.write("Are you my mother\t  72\n")
file.write("Another title\t      92\n")

file.close()

file = open('input.txt', 'r')
data = file.read().split('\n')
print(" data = ", data)

book1_data = data[0].split('\t')
print("book1 data = ", book1_data)
book1 = Book(book1_data[0],book1_data[1]) #instantiating another book object.
print(book1)

book2_data = data[1].split('\t')
print("book2 data = ", book1_data)
book2 = Book(book2_data[0],book2_data[1]) #instantiating another book object.
print(book2)


