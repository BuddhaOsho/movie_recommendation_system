import streamlit as st
import pandas as pd
import nltk
import sklearn
import joblib

st.title("Movie Recommendation System")


@st.cache_resource
def load_data():
    movies = joblib.load("artifacts/processed_data.joblib")
    similarity = joblib.load("artifacts/similarity.joblib")
    return movies, similarity

movies, similarity = load_data()

movies_names = movies["title"].values
name_movie= st.selectbox("Enter the Movie Name", movies_names)

def recommend(name_movie):
    try:
        movie_index = movies[movies["title"] == name_movie].index[0]

        recommendations = similarity[movie_index]

        movie_list = sorted(
            enumerate(recommendations),
            reverse=True,
            key=lambda x: x[1]
        )[1:6]

        recommended_movies = []

        for i in movie_list:
            recommended_movies.append(
                movies.iloc[i[0]].title
            )

        return recommended_movies

    except Exception as e:
        st.error(f"Error: {e}")
        return []



if st.button("Reccomend"):
    r= recommend(name_movie)
    st.write(f"The Reccomended movies are : ")
    for i in r:
        st.write(i)





