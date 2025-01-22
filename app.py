import streamlit as st
import pickle
import requests

# Fetch movie poster from API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data.get('poster_path')
    if poster_path:
        return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    else:
        return "https://via.placeholder.com/150"  # Default image if poster not found

# Recommend movies
def recommend_movie(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    recommended_movie_names = []
    recommended_movie_posters = []

    for i in movies_list_indices:  
        # Fetch poster from API
        movie_id = movies_list.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies_list.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters

# Load data
movies_list = pickle.load(open('movies.pkl', "rb"))
movies = movies_list['title'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit UI
st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    "Discover movies you'll love! Select a movie to get recommendations:",
    movies,
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend_movie(selected_movie_name)
    
    # Layout for 2 rows and 5 columns
    for row in range(2):  # Two rows
        cols = st.columns(5)  # Create 5 columns per row
        for idx in range(5):  # Loop through each column
            movie_idx = row * 5 + idx  # Calculate the movie index
            if movie_idx < len(recommended_movie_names):  # Check if the index is within bounds
                with cols[idx]:  # Use the specific column
                    st.image(recommended_movie_posters[movie_idx], use_container_width=True)  # Display poster
                    st.text(recommended_movie_names[movie_idx])  # Display movie title
