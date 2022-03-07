from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
df = pd.read_csv('C:/Users/Krithi/Desktop/Python/final1.csv')
df = df[df["soup"].notna()]
count = CountVectorizer(stop_words = "english")
count_matrics = count.fit_transform(df["soup"])
cosineSim = cosine_similarity(count_matrics, count_matrics)
df = df.reset_index()
indeces = pd.series(df.index, index = df['title'])
def getReccomendation(title):
  idx = indeces[title]
  simScores = list(enumerate(cosineSim[idx]))
  simScores = sorted(simScores, key = lambda x:x[1], reverse = True)
  simScores = simScores[1:11]
  movieIndeces = [i[0] for i in simScores]
  return df[["title", "poster_link", "release_date", "runTime", "vote_average", "overview"]].iloc[movieIndeces].values.tolist()