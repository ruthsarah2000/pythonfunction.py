'''
9. The Personal Library Organizer
Objective:
The aim of this assignment is to create a system that organizes a personal library of books.

Task 1: Write a function to add books with title, author, and genre.
Task 2: Code a search function to find books by title or author.
Task 3: Implement a way to display books sorted by genre or author.
'''

def books():
    titles = [('Dating the Grump', "The Billionaire's Secret"), ('Flying High with Boogies', 'Finding the Flies'), ('Finding the Fools', 'Laughing Too Hard')]
    author = ['Amber Rose', 'Summer Ambrose', 'Kay Bella']
    genre = ['Romance', 'Action', 'Comedy']
    catalog = list(zip(titles, author, genre))
   
    print(catalog)

books()

def search_feature():
    
    author = ['Amber Rose', 'Summer Ambrose', 'Kay Bella']
    search_string = input("Type the name of the author you are searching for in the catalog - (Amber Rose, Summer Ambrose, Kay Bella): ")

    for name in author:
        if name == search_string:
            print(f"{search_string} found in the catalog!")
            break  
        
    else:
        print(f"{search_string} not found in the catalog.")

search_feature()

def catalog_display():
    
    author = ['Amber Rose', 'Summer Ambrose', 'Kay Bella']
    genre = ['Romance', 'Action', 'Comedy']

    sorted_list = sorted(zip(genre, author))

    sorted_list1, sorted_list2 = zip(*sorted_list)

    print(f"Genre:", sorted_list1)
    print(f"Author:", sorted_list2)

catalog_display()
