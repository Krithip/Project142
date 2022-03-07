import pandas as pd
import numpy as np
df = pd.read_csv('C:/Users/Krithi/Desktop/Python/final1.csv')
c = df["vote_average"].mean()
m = df["vote_count"].quantile(0.9)
qmovies = df.copy().loc[df2["vote_count"]>=m]
def weightedRating(x, m = m, c = c):
  v = x["vote_count"]
  r = x["vote_average"]
  return(v/(v + m)*r) + (m/(m + v)*c)
qmovies["score"] = qmovies.apply(weightedRating, axis = 1)
qmovies = qmovies.sort_values("score", ascending = False)
qmovies[["title", "poster_link", "release_date", "runTime", "vote_average", "overview"]].head(20).values.tolist()