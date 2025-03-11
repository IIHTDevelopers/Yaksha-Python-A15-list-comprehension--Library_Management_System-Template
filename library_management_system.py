"""
Library Book Management System (Simplified)
This program demonstrates list comprehension techniques through a library management system.
"""

def initialize_data():
    """Initialize the library data with predefined books and new arrivals."""
    books = [
        {"id": "B001", "title": "Python Fundamentals", "author": "John Smith", "genre": "reference", "publication_year": 2019, "available": True, "popularity_score": 4.5},
        {"id": "B002", "title": "Mystery at Midnight", "author": "Jane Doe", "genre": "fiction", "publication_year": 2018, "available": False, "popularity_score": 4.2},
        {"id": "B003", "title": "History of Computing", "author": "Alan Turing", "genre": "non-fiction", "publication_year": 2015, "available": True, "popularity_score": 3.8},
        {"id": "B004", "title": "The Dragon's Quest", "author": "Emily Johnson", "genre": "children", "publication_year": 2020, "available": True, "popularity_score": 4.7},
        {"id": "B005", "title": "Life of Einstein", "author": "Robert Brown", "genre": "biography", "publication_year": 2017, "available": False, "popularity_score": 4.1}
    ]
    
    new_arrivals = [
        {"id": "N001", "title": "Data Science Handbook", "author": "Sarah Miller", "genre": "reference", "publication_year": 2023, "available": True, "popularity_score": 4.9},
        {"id": "N002", "title": "Quantum Physics Simplified", "author": "Richard Feynman", "genre": "non-fiction", "publication_year": 2022, "available": True, "popularity_score": 4.3}
    ]
    
    return books, new_arrivals

def filter_by_genre(books, genre):
    """Filter books by genre using list comprehension."""
    if books is None:
        raise ValueError("Books cannot be None")
    if not isinstance(books, list):
        raise TypeError("Books must be a list")
    if genre is None:
        raise ValueError("Genre cannot be None")
    if not isinstance(genre, str):
        raise TypeError("Genre must be a string")
    
    return [book for book in books if book["genre"] == genre]

def filter_by_availability(books, available=True):
    """Filter books by availability using list comprehension."""
    if books is None:
        raise ValueError("Books cannot be None")
    if not isinstance(books, list):
        raise TypeError("Books must be a list")
    if not isinstance(available, bool):
        raise TypeError("Available must be a boolean")
    
    return [book for book in books if book["available"] == available]

def filter_by_decade(books, decade):
    """Filter books by publication decade using list comprehension."""
    if books is None:
        raise ValueError("Books cannot be None")
    if not isinstance(books, list):
        raise TypeError("Books must be a list")
    if decade is None:
        raise ValueError("Decade cannot be None")
    if not isinstance(decade, int):
        raise TypeError("Decade must be an integer")
    
    return [book for book in books if book["publication_year"] // 10 * 10 == decade]

def filter_by_keyword(books, keyword):
    """Filter books by keyword in title or author using list comprehension."""
    if books is None:
        raise ValueError("Books cannot be None")
    if not isinstance(books, list):
        raise TypeError("Books must be a list")
    if keyword is None:
        raise ValueError("Keyword cannot be None")
    if not isinstance(keyword, str):
        raise TypeError("Keyword must be a string")
    
    keyword_lower = keyword.lower()
    return [book for book in books if keyword_lower in book["title"].lower() or keyword_lower in book["author"].lower()]

def transform_titles(books, case="upper"):
    """Transform book titles to the specified case using list comprehension."""
    if books is None:
        raise ValueError("Books cannot be None")
    if not isinstance(books, list):
        raise TypeError("Books must be a list")
    if case is None:
        raise ValueError("Case cannot be None")
    if not isinstance(case, str):
        raise TypeError("Case must be a string")
    
    if case == "upper":
        return [book["title"].upper() for book in books]
    elif case == "lower":
        return [book["title"].lower() for book in books]
    elif case == "title":
        return [book["title"].title() for book in books]
    return [book["title"] for book in books]

def generate_citations(books):
    """Generate formatted citations for books using list comprehension."""
    if books is None:
        raise ValueError("Books cannot be None")
    if not isinstance(books, list):
        raise TypeError("Books must be a list")
    
    return [f"{book['author']} ({book['publication_year']}). {book['title']}." for book in books]

def get_book_availability(books):
    """Create a list of book titles with availability indicators using list comprehension with conditionals."""
    if books is None:
        raise ValueError("Books cannot be None")
    if not isinstance(books, list):
        raise TypeError("Books must be a list")
    
    return [f"{book['title']} - {'Available' if book['available'] else 'On Loan'}" for book in books]

def calculate_genre_counts(books):
    """Count books in each genre using list comprehension."""
    if books is None:
        raise ValueError("Books cannot be None")
    if not isinstance(books, list):
        raise TypeError("Books must be a list")
    
    genres = ["fiction", "non-fiction", "reference", "children", "biography"]
    return {genre: len([book for book in books if book["genre"] == genre]) for genre in genres}

def calculate_average_popularity(books):
    """Calculate the average popularity score using list comprehension."""
    if books is None:
        raise ValueError("Books cannot be None")
    if not isinstance(books, list):
        raise TypeError("Books must be a list")
    
    if not books:
        return 0.0
    return round(sum([book["popularity_score"] for book in books]) / len(books), 2)

def integrate_new_arrivals(books, new_arrivals):
    """Integrate new arrivals into the main collection with section field added using list comprehension."""
    if books is None:
        raise ValueError("Books cannot be None")
    if new_arrivals is None:
        raise ValueError("New arrivals cannot be None")
    if not isinstance(books, list):
        raise TypeError("Books must be a list")
    if not isinstance(new_arrivals, list):
        raise TypeError("New arrivals must be a list")
    
    tagged_new_arrivals = [{**book, "section": "New"} for book in new_arrivals]
    combined_books = books + tagged_new_arrivals
    
    # Remove the duplicate section field from the original books
    return [{key: value for key, value in book.items() if key != "section"} if "section" not in book else book for book in combined_books]

def get_formatted_book(book):
    """Format a book for display."""
    if book is None:
        raise ValueError("Book cannot be None")
    if not isinstance(book, dict):
        raise TypeError("Book must be a dictionary")
    
    # Check required fields
    required_fields = ["id", "title", "author", "genre", "publication_year", "available", "popularity_score"]
    for field in required_fields:
        if field not in book:
            raise ValueError(f"Book is missing required field: {field}")
    
    availability = "Available" if book["available"] else "On Loan"
    stars = "★" * int(book["popularity_score"]) + "☆" * (5 - int(book["popularity_score"]))
    section = f" [{book['section']}]" if "section" in book else ""
    
    return f"{book['id']} | {book['title']}{section} | {book['author']} | {book['genre']} | {book['publication_year']} | {availability} | Rating: {stars}"

def display_data(data, data_type="books"):
    """Display formatted books or other data."""
    if data is None:
        raise ValueError("Data cannot be None")
    
    if data_type == "books":
        print("\nCurrent Book Collection:")
        for book in data:
            print(get_formatted_book(book))
    elif data_type == "results":
        print("\nFiltered Results:")
        if data:
            for book in data:
                print(get_formatted_book(book))
        else:
            print("No books match the criteria.")
    elif data_type == "titles" or data_type == "citations" or data_type == "availability":
        print(f"\n{data_type.title()}:")
        for i, item in enumerate(data):
            print(f"{i+1}. {item}")
    elif data_type == "statistics":
        print("\nLibrary Statistics:")
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print(f"\nUnknown data type: {data_type}")
        print(data)

def main():
    """Main program function."""
    books, new_arrivals = initialize_data()
    integrated = False
    
    while True:
        total_books = len(books)
        available_books = len([book for book in books if book["available"]])
        
        print(f"\n===== LIBRARY BOOK MANAGEMENT SYSTEM =====")
        print(f"Total Books: {total_books}")
        print(f"Available Books: {available_books}")
        
        print("\n1. View Books")
        print("2. Filter Books")
        print("3. Transform Data")
        print("4. Generate Statistics")
        print("5. Integrate New Arrivals")
        print("0. Exit")
        
        choice = input("Enter your choice (0-5): ")
        
        if choice == "0":
            print("Thank you for using the Library Book Management System!")
            break
            
        elif choice == "1":
            display_data(books, "books")
        
        elif choice == "2":
            print("\n1. Filter by Genre")
            print("2. Filter by Availability")
            print("3. Filter by Decade")
            print("4. Filter by Keyword")
            filter_option = input("Select filter option (1-4): ")
            
            if filter_option == "1":
                genre = input("Enter genre to filter by (fiction/non-fiction/reference/children/biography): ")
                filtered = filter_by_genre(books, genre)
                display_data(filtered, "results")
            
            elif filter_option == "2":
                availability = input("Filter by available or on loan? (available/on_loan): ")
                is_available = availability == "available"
                filtered = filter_by_availability(books, is_available)
                display_data(filtered, "results")
            
            elif filter_option == "3":
                try:
                    decade = int(input("Enter decade to filter by (e.g., 2010 for 2010s): "))
                    filtered = filter_by_decade(books, decade)
                    display_data(filtered, "results")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            
            elif filter_option == "4":
                keyword = input("Enter keyword to search for: ")
                filtered = filter_by_keyword(books, keyword)
                display_data(filtered, "results")
        
        elif choice == "3":
            print("\n1. Transform Titles")
            print("2. Generate Citations")
            print("3. Display Availability")
            transform_option = input("Select transformation option (1-3): ")
            
            if transform_option == "1":
                print("\n1. Uppercase")
                print("2. Lowercase")
                print("3. Title Case")
                case_option = input("Select case option (1-3): ")
                
                if case_option == "1":
                    transformed = transform_titles(books, "upper")
                elif case_option == "2":
                    transformed = transform_titles(books, "lower")
                elif case_option == "3":
                    transformed = transform_titles(books, "title")
                else:
                    transformed = transform_titles(books)
                
                display_data(transformed, "titles")
            
            elif transform_option == "2":
                citations = generate_citations(books)
                display_data(citations, "citations")
            
            elif transform_option == "3":
                availability_list = get_book_availability(books)
                display_data(availability_list, "availability")
        
        elif choice == "4":
            genre_counts = calculate_genre_counts(books)
            avg_popularity = calculate_average_popularity(books)
            
            statistics = {
                "Total books": len(books),
                "Available books": len([book for book in books if book["available"]]),
                "Average popularity": f"{avg_popularity}/5.0"
            }
            
            for genre, count in genre_counts.items():
                statistics[f"{genre.capitalize()} books"] = count
            
            display_data(statistics, "statistics")
            
            # Most popular books (top 3)
            popular_books = sorted(books, key=lambda book: book["popularity_score"], reverse=True)[:3]
            print("\nMost Popular Books:")
            for i, book in enumerate(popular_books):
                print(f"{i+1}. {book['title']} ({book['popularity_score']}/5.0)")
        
        elif choice == "5":
            if not integrated:
                books = integrate_new_arrivals(books, new_arrivals)
                integrated = True
                print("New arrivals added to the collection.")
            else:
                print("New arrivals already integrated.")
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()