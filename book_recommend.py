import requests

def search_books(book_title):
    url = f"http://openlibrary.org/search.json?title={book_title}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "docs" in data and data["docs"]:
            print(f"\nTop matches for '{book_title}':\n")
            for book in data["docs"][:5]:  # Top 5 results
                title = book.get("title", "Unknown Title")
                author = book.get("author_name", ["Unknown Author"])
                year = book.get("first_publish_year", "Unknown Year")
                print(f"👉 {title} by {', '.join(author)} ({year})")
        else:
            print("No results found.")
    else:
        print("Error fetching data.")

book = input("Enter a book title: ")
search_books(book)
