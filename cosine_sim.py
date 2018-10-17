
import pandas as pd
import numpy as np

from sklearn.neighbors import NearestNeighbors

class PlayerCompSystem(object):
    """Python class for creation, training, and comparison of data using cosine
    similarity. The algorithm will filter and return indices of the data, so
    these indices should be in a format that the user will understand.

    Arguments:

    comparison_matrix -- a pandas DataFrame consisting entirely of numerical
    values, and indices that are useful to the viewer
    """

    def __init__(self, comparison_matrix):
        self.matrix = comparison_matrix

    def near_neighbors(self, age):
        """Use our input matrix to generate and train a cosine similarity model
        to judge similarity between each row in our data. Returns trained model

        Arguments:

        age -- the age of players we are comparing
        """
        model = NearestNeighbors(metric='cosine', algorithm='brute')
        self.age_matrix = self.matrix.loc[self.matrix['Age']==age]
        model.fit(self.age_matrix)
        return model

    def rec_by_users(self, name, age=24, neighbors=11):
        """Use our matrix to create a model, train it, and return the n-most
        similar indices from our data.

        Arguments:

        name -- The index position of the player we want to compare
        age -- the age of the player we are comparing, to filter for only
            historical data at that age
        neighbors -- number of similar players to return. This model returns 
            our query player as its first result, so this must be equal to
            (number of comparables + 1) (default is 11)
        """
        model = self.near_neighbors(age)
        if len(self.age_matrix) < neighbors:
            neighbors = len(self.age_matrix)
        distances, indices = model.kneighbors(
            name.values.reshape(1, -1), n_neighbors=neighbors)
        
        #print(distances[:4], indices[:4])
        
        for i in range(0, len(distances.flatten())):
            if i == 0:
                print('Recommendations for {0} ({1}):\n'.format(
                            name.index[0], distances.flatten()[0]))
            else:
                print('{0}: {1}, {2}'.format(
                    i, self.matrix.index[indices.flatten()[i]], 
                                        distances.flatten()[i]))



