import pandas as pd
from pprint import pprint


def main():
    # read data
    users = pd.read_table(
        "users.dat", sep='::', names=['user_id', 'gender', 'age', 'occupation', 'zip'], engine='python'
    )
    ratings = pd.read_table(
        "ratings.dat.txt", sep='::', names=['user_id', 'movie_id', 'rating', 'timestamp'], engine='python'
    )
    movies = pd.read_table("moovies.dat", sep='::', names=['movie_id', 'title', 'genres'], engine='python')

    # merge
    df = users.merge(ratings, on='user_id')
    df = df.merge(movies, on='movie_id')

    # Gender ratings
    gender_ratings = df.pivot_table(
        values='rating',
        index='title',
        columns='gender',
        aggfunc='mean'
    )
    pprint(gender_ratings)

    ratings_by_title = df.groupby('title').size()
    top_ratings_movies = ratings_by_title[ratings_by_title >= 250]
    top_gender_ratings = gender_ratings.loc[top_ratings_movies.index]
    top_female_ratings = top_gender_ratings.sort_values(by='F', ascending=False)
    top_gender_ratings['diff'] = top_gender_ratings.F - top_gender_ratings.M
    top_diff_movies = top_gender_ratings.sort_values(by='diff')

    pprint(top_female_ratings)
    pprint(top_diff_movies)

    rating_std_by_title = df.groupby('title')['rating'].std()
    rating_std_by_title = rating_std_by_title.loc[top_ratings_movies.index]
    rating_std_by_title.sort_values(ascending=False)
    pprint(rating_std_by_title)


if __name__ == "__main__":
    main()
