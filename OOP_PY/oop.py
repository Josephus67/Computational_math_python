class Book:
   def __init__(self,title,author,pages,price):
      self.title = title
      self.author = author
      self.pages = pages
      self.price = price

book1 =Book("Python","Guido van Rossum",300,4)
book2 = Book("C Programming","Kernighan & Ritchie",250,3)
book3 = Book("Java","James Gosling",400,5)

print(book1.title)
print(book2.author)
print(book3.pages)
def getPrice(self):
   return self.price
print(getPrice(book1))
print(getPrice(book3))
#print(book1.getprice())