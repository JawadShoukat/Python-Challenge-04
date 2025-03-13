# personal_library_manager_streamlit.py

import streamlit as st
import json
import os

# File path to store data
FILE_PATH = 'library.json'

# Load library from file
def load_library():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return []

# Save library to file
def save_library(library):
    with open(FILE_PATH, 'w') as file:
        json.dump(library, file, indent=4)

# App Title
st.title("📚 Personal Library Manager")

# Initialize library
library = load_library()

# Sidebar Navigation
menu = st.sidebar.radio("Navigate", ["Add Book", "Delete Book", "Search Books", "List All Books"])

# Add Book Section
if menu == "Add Book":
    st.subheader("Add a New Book")
    title = st.text_input("Book Title:")
    author = st.text_input("Author:")
    category = st.text_input("Category:")
    
    if st.button("Add Book"):
        if title and author and category:
            library.append({"title": title, "author": author, "category": category})
            save_library(library)
            st.success(f"'{title}' by {author} added successfully!")
        else:
            st.warning("Please fill all fields!")

# Delete Book Section
elif menu == "Delete Book":
    st.subheader("Delete a Book")
    book_titles = [book['title'] for book in library]
    book_to_delete = st.selectbox("Select a book to delete:", ["Select..."] + book_titles)
    
    if st.button("Delete Book"):
        if book_to_delete != "Select...":
            library = [book for book in library if book['title'] != book_to_delete]
            save_library(library)
            st.success(f"'{book_to_delete}' removed successfully!")
        else:
            st.warning("Please select a book!")

# Search Books Section
elif menu == "Search Books":
    st.subheader("Search Books")
    query = st.text_input("Enter search query (Title/Author):")
    
    if st.button("Search"):
        results = [book for book in library if query.lower() in book['title'].lower() or query.lower() in book['author'].lower()]
        if results:
            st.write("### Search Results:")
            for idx, book in enumerate(results, start=1):
                st.write(f"{idx}. {book['title']}** by {book['author']} ({book['category']})")
        else:
            st.warning("No matching books found!")

# List All Books Section
elif menu == "List All Books":
    st.subheader("All Books in Library")
    
    if library:
        for idx, book in enumerate(library, start=1):
            st.write(f"{idx}. {book['title']}** by {book['author']} ({book['category']})")
    else:
        st.info("Your library is empty.")