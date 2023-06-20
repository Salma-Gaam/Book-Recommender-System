# Book Recommender System
## Introduction
This is my end-to-end data science project involving exploratory data analysis, machine learning modeling and web app deployment. In this project, I tried to develop book recommendation system based on data from the Amazon Books. 

## Problem Description
* Problem: Book Recommendation System for Online Bookstore  
  
In today's digital age, online bookstores offer a vast selection of books, making it challenging for users to navigate through the extensive collection and discover books that align with their interests. Users often struggle to find relevant books, leading to decision paralysis and missed opportunities to explore new authors, genres, or topics.




* Solution: Recommender System for Books  
  
A book recommendation system can address this problem by leveraging user preferences, book attributes, and other relevant data to provide personalized book recommendations. 

## Data Description
This dataset comprises 3 files:
### 1. Users
Contains the users; their id, age and location

### 2. Books
Books are identified by their respective ISBN, and some content-based information is given (Book-Title, Book-Author, Year-Of-Publication, Publisher), obtained from Amazon Web Services. URLs linking to cover images are also given, appearing in three different flavors (Image-URL-S, Image-URL-M, Image-URL-L), i.e., small, medium, large. These URLs point to the Amazon website.

### 3. Ratings
Contains the book rating information; the id of the user, the ISBN and the rating.

[Dataset Link](https://www.kaggle.com/datasets/somnambwl/bookcrossing-dataset?select=Users.csv)

## Objective
The main objective of this project is to develop a book recommendation system.

## Filtering

***Collaborative Filtering*** is a recommendation technique that relies on the past behavior and preferences of users. It identifies similarities between users or items based on their interactions or ratings and uses that information to make recommendations. 
In this project, i used a pivot table to represent user-book interactions, and then feeding that data into a Nearest Neighbors model. 
Nearest Neighbors is a common algorithm used in collaborative filtering, as it finds similar users or items based on their interaction patterns. Therefore, it will recommend  books based on the preferences of similar users.

**Content-based filtering** focuses on the attributes or features of items to make recommendations. It analyzes the characteristics of items, such as book genres, authors, or other metadata, and recommends similar items based on those attributes.

## Demo

<img width="897" alt="1" src="https://github.com/Salma-Gaam/Book-Recommender-System/assets/107813298/b9a00567-e0d5-4c0e-85b4-031ed8c8902f">
<img width="902" alt="2" src="https://github.com/Salma-Gaam/Book-Recommender-System/assets/107813298/06c3aa8f-326d-48e1-9709-601388ccdc45">

## How to run
To set up the book recommender system locally, follow these steps:

* Clone the repository: git clone https://github.com/Salma-Gaam/Book-Recommender-System

* Install the required dependencies: pip install -r requirements.txt

* Run the application: python app.py

* Access the application in your web browser at http://localhost:8080 and start exploring personalized book recommendations.

