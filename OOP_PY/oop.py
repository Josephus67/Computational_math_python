class Newspaper:
    def __init__(self, name, editor, publication_year):
        self.name = name
        self.editor = editor
        self.publication_year = publication_year


n1 = Newspaper("The Guardian", "Katharine Viner", 1821)
n2 = Newspaper("The New York Times", "A. G. Sulzberger", 1851)
n3 = Newspaper("The Washington Post", "Fred Ryan", 1877)

print(n1.name, n3.editor, n2.publication_year)

class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = float(price.strip("$"))  # Convert price to float for calculations

    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setDiscount(self, amount):
        self._discount = amount

# Creating book instances
book1 = Book("Python", "Guido van Rossum", 300, "$4")
book2 = Book("C Programming", "Kernighan & Ritchie", 250, "$3")
book3 = Book("Java", "James Gosling", 400, "$5")

# Displaying prices and applying discounts
print(book1.getPrice())
print(book3.getPrice())
print(book2.price)

book2.setDiscount(0.25)
print(book2.getPrice())
print(book1.getPrice()) #this 
#print(getPrice(book1)) # and this are in essense the same if the getprice function is a method of the book class
print(type(book1)==type(book2)) # True
print(isinstance(book1,Book)) # True
print(isinstance(book1,Newspaper)) # False
print(isinstance(n1,Newspaper)) # True
print(isinstance(n2,Newspaper)) # True
print(isinstance(book2,object)) # True


#recap of class

class athlete:
    def __init__(self,name,age,weight,record):
        self.name = name
        self.age = age
        self.weight = weight
        self.sport = record
    
ufc = athlete("Conor McGregor",32,155,"MMA")
nba = athlete("Lebron James",36,250,"Basketball")
nfl = athlete("Tom Brady",43,225,"American Football")
print(ufc.name,nba.sport,nfl.weight)


    