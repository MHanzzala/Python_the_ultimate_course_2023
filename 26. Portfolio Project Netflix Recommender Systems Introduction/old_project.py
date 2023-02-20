import pandas as pd
from IPython.display import display
import numpy as np


pd.set_option('display.max_rows', None)

df = None
minVotes = None


def readFile(path):
    global df
    df = pd.read_csv(path)


def cleanDataset():
    global df
    df = df.drop(['year'], axis=1)
    df = df.drop(['certificate'], axis=1)
    df = df.drop(['duration'], axis=1)
    df = df.drop(['description'], axis=1)
    df = df.drop(['stars'], axis=1)
    df = df.drop_duplicates(subset=['title'])
    df['votes'] = df['votes'].str.replace(',', '').astype(float)
    # 9842
    df = df.fillna(0)


def filterGenre(genre):
    global df
    df = df[df['genre'].str.contains(genre, case=False).fillna(False)]


def threshVotes(thrs):
    global df
    global minVotes
    minVotes = np.quantile(df['votes'], thrs)
    df = df.drop(df[df.votes < minVotes].index)


def weightedAvgScore():
    global df
    weightedAvg = []
    mean = df['rating'].mean()
    df = df.reset_index(drop=True)

    for i in range(0, len(df["rating"])):
        res = (df['votes'][i]/(df["votes"][i] + minVotes)*df['rating']
               [i]) + (minVotes/(df["votes"][i]+minVotes))*mean
        weightedAvg.append(res)
    df["WeightedAvg"] = weightedAvg


def sortNscores(n):
    sort = df.sort_values("WeightedAvg", ascending=False).head(n)
    display(sort)


def runRecommenderSystem(genre, votesThrs, numberofReturnedData):
    readFile(
        "/home/hanzala/Development/Python_the_ultimate_course_2023/26. Portfolio Project Netflix Recommender Systems Introduction/NetflixDatasetMovies.csv")
    cleanDataset()
    filterGenre(genre)
    threshVotes(votesThrs)
    weightedAvgScore()
    sortNscores(numberofReturnedData)


runRecommenderSystem("Drama", 0.8, 10)
