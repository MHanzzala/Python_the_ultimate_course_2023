import pandas as pd
from IPython.display import display
import numpy as np


class netflixTopRecommenderSystem:
    # Constructor to initialize instance variables
    def __init__(self, datasetPath, genre, VotesThrs, TopN):
        self._datasetPath = datasetPath
        self._genre = genre
        self._voteThrs = VotesThrs
        self._topN = TopN
        self.df = None
        self._minVotes = None

        self.colDrop = ['year', 'certificate',
                        'duration', 'description', 'stars']
        self.colTitle = {"votes": "votes", "genre": "genre",
                         "title": "title", "rating": "rating"}

    # Method to read the csv file
    def readFile(self):
        self.df = pd.read_csv(self._datasetPath)

    # Method to clean the dataset
    def cleanDataset(self):

        # Dropping the unnecessary columns from the dataset
        for items in self.colDrop:
            self.df = self.df.drop([items], axis=1)

        # Dropping the duplicate rows based on the title column
        self.df = self.df.drop_duplicates(subset=[self.colTitle['title']])

        # Converting the votes column to float data type
        if type(self.df['votes'][0]) == str:
            self.df[self.colTitle['votes']] = self.df[self.colTitle['votes']].str.replace(
                ',', '').astype(float)

        # Filling the missing values with 0
        self.df = self.df.fillna(0)

    # Method to filter the dataset based on genre
    def filterGenre(self):
        self.df = self.df[self.df[self.colTitle['genre']].str.contains(
            self._genre, case=False).fillna(False)]

    # Method to filter the dataset based on the minimum number of votes threshold
    def threshVotes(self):
        self._minVotes = np.quantile(
            self.df[self.colTitle[self.colTitle['votes']]], self._voteThrs)
        self.df = self.df.drop(self.df[self.df.votes < self._minVotes].index)

    # Method to calculate the weighted average score for each title
    def weightedAvgScore(self):
        weightedAvg = []
        mean = self.df[self.colTitle['rating']].mean()
        self.df = self.df.reset_index(drop=True)

        for i in range(0, len(self.df[self.colTitle['rating']])):
            res = (self.df[self.colTitle['votes']][i]/(self.df[self.colTitle['votes']][i] + self._minVotes) *
                   self.df[self.colTitle['rating']][i]) + (self._minVotes/(self.df[self.colTitle['votes']][i]+self._minVotes))*mean
            weightedAvg.append(res)
        self.df["WeightedAvg"] = weightedAvg

    # Method to sort the titles based on the weighted average score and display top N titles
    def sortNscores(self):
        sort = self.df.sort_values(
            "WeightedAvg", ascending=False).head(self._topN)
        display(sort)

    # Method to execute all the steps of the recommender system
    def run(self):
        self.readFile()
        self.cleanDataset()
        self.filterGenre()
        self.threshVotes()
        self.weightedAvgScore()
        self.sortNscores()


path = "/home/hanzala/Development/Python_the_ultimate_course_2023/26. Portfolio Project Netflix Recommender Systems Introduction/NetflixDatasetMovies.csv"
best5Comedy = netflixTopRecommenderSystem(path, "Comedy", 0.8, 5)
best5Comedy.colDrop = ['year', 'certificate',
                       'duration', 'description', 'stars']
best5Comedy.colTitle = {"votes": "votes", "genre": "genre",
                        "title": "title", "rating": "rating"}
best5Comedy.run()
