import pickle
import streamlit as st
import numpy as np

st.header("Books Recommender System")
model = pickle.load(open('artifacts/model.pkl','rb'))
book_names = pickle.load(open('artifacts/book_names.pkl','rb'))
books = pickle.load(open('artifacts/books.pkl','rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl','rb'))


def fetch_poster(suggestion):
    book_names = book_pivot.index
    suggested_books = []
    urls = []
    for i in suggestion:
        suggested_books.append(book_names[i].tolist())
    
    for names in suggested_books:
        for name in names:
            urls.append(books.query("title == @name ")['image_url'].unique()[0])
    
    return urls

books = pickle.load(open('artifacts/books.pkl','rb'))

def recommend_book(book_name):
    books_list = []
    # book_id = books.query("title == @book_name")['ISBN'].unique()[0][0]
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6 )

    poster_url = fetch_poster(suggestion)
    
    for i in range(len(suggestion)):
            bookss = book_pivot.index[suggestion[i]]
            for j in bookss:
                books_list.append(j)
    return books_list , poster_url       



selected_books = st.selectbox("Type or select a book from the dropdown", book_names)

if st.button('Show Recommendation'):
    recommended_books,poster_url = recommend_book(selected_books)
    col1, col2, col3, col4, col5 = st.columns(5)

    cols = [col1, col2, col3, col4, col5]

    for i, col in enumerate(cols):
        with col:
            st.text(recommended_books[i+1])
            st.image(poster_url[i+1])

    