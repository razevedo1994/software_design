from book import Book
from catalogue import Catalogue


def fill(catalogue: Catalogue):
    catalogue.add("Life of Pi", "Martel", "Yann")
    catalogue.add("The Call of the Wilde", "London", "Jack")

    catalogue.add("To Kill a Monckinbird", "Lee", "Harper")
    catalogue.add("Little Woman", "Alcott", "Louisa")

    catalogue.add("The Adventures of Sherlock Homles", "Doyle", "Arthur")
    catalogue.add("And Then There Were None", "Christie", "Agatha")

    catalogue.add("Carrie", "King", "Stephen")
    catalogue.add("It: A Novel", "King", "Stephen")

    catalogue.add("Frankenstein", "Shelley", "Mary")
    catalogue.add("2001: A Space Odyssey", "Clarke", "Arthur")

    catalogue.add("Ender's Game", "Card", "Orson")

def search(catalogue: Catalogue, target: Book):
    print()
    print("Find ", end="")
    print(target)

    matches = catalogue.find(target)

    if len(matches) == 0:
        print("No matches.")
    else:
        print("Matches:")

        for book in matches:
            print(" ", end="")
            print(book)

def test(catalogue: Catalogue):
    target = Book("Life of Pi", "Martel", "Yann")
    search(catalogue, target)

    target = Book("", "King", "")
    search(catalogue, target)

    target = Book("1984", "Orwell", "George")
    search(catalogue, target)

    target = Book("", "", "")
    search(catalogue, target)

if __name__ == "__main__":
    catalogue = Catalogue()
    fill(catalogue)
    test(catalogue)