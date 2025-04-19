import streamlit as st
import pickle


# Load data
movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

# Streamlit UI
st.header("Movies Recommender System")
selectvalue = st.selectbox("Select a movie from the dropdown", movies_list)
  

# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie = []
    for i in distances[1:0]:  # Skip the first element (itself)
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie

# Display recommended movies when the button is clicked
if st.button("Show Recommend"):
    movie_name = recommend(selectvalue)
    
    # Create columns for displaying the recommended movie names
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(movie_name[0])
    with col2:
        st.text(movie_name[1])
    with col3:
        st.text(movie_name[2])
    with col4:
        st.text(movie_name[3])
    with col5:
        st.text(movie_name[4])
