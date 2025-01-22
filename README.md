# Movie Recommendation App

This is a **Movie Recommendation System** built using **Python** and **Streamlit**. The app recommends movies based on a content-based filtering approach using **Cosine Similarity**.

## Features

- **Movie Recommendation**: Recommends similar movies based on the movie you search for.
- **Cosine Similarity**: Measures similarity between movies using their tags (genres, keywords, cast, crew, overview).

## Tech Stack

- **Python**
- **Streamlit**
- **pandas**
- **scikit-learn**
- **pickle**

## File Structure

- **tmdb_5000_movies.csv**: Movie data.
- **tmdb_5000_credits.csv**: Movie credits data.
- **similarity.pkl**: Similarity matrix for recommending movies (download separately).
- **movies.pkl**: Processed movie data.
- **app.py**: Streamlit app.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Zafyy/Movie-recommender-app.git
   cd Movie-recommender-app 
   ```
   

2. **Install dependencies**:
   ```bash
   pip install pandas numpy scikit-learn streamlit
   ```

3. **Download the similarity.pkl file from "https://drive.google.com/file/d/1JRuT4nSij3cgXa3OCClOGmxQEB8LoOmP/view?usp=sharing".**

4. **Place the downloaded similarity.pkl in the project folder.**

## DEMO

![image copy 2](https://github.com/user-attachments/assets/51abd779-8dfe-4eed-96e3-fcf3f4239076)

![image copy](https://github.com/user-attachments/assets/4b9b5b30-634b-4c3d-908d-7c7cb77f6c4c)

![image](https://github.com/user-attachments/assets/7c49fe19-50a1-4d32-b7c6-1b669961091c)




