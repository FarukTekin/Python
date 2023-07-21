import pandas as pd

column_names = ["user_id", "item_id", "rating", "timestamp"]
df = pd.read_csv("users.data", sep="\t", names=column_names)

movie_titles = pd.read_csv("movie_id_titles.csv")

df = pd.merge(df, movie_titles, on="item_id")

moviemat = df.pivot_table(index="user_id", columns="title", values="rating")

starwars_user_ratings = moviemat["Star Wars (1977)"]

similar_to_starwars = moviemat.corrwith(starwars_user_ratings)

corr_starwars = pd.DataFrame(similar_to_starwars, columns=["Correlation"])
corr_starwars.dropna(inplace=True)

df.drop(["timestamp"], axis=1)

ratings = pd.DataFrame(df.groupby("title")["rating"].mean())
ratings["rating_oy_sayisi"] = pd.DataFrame(df.groupby("title")["rating"].count())

corr_starwars = corr_starwars.join(ratings["rating_oy_sayisi"])

print(corr_starwars[corr_starwars["rating_oy_sayisi"] > 100].sort_values("Correlation", ascending=False).head())
