
import pandas as pd
import numpy as np

from sklearn.neighbors import NearestNeighbors

class PlayerRecommendationSystem(object):

    def __init__(self, comparison_matrix):
        self.matrix = comparison_matrix
        self.age_matrix = None

    def near_neighbors(self, age):
        model = NearestNeighbors(metric='cosine', algorithm='brute')
        self.age_matrix = self.matrix.loc[self.matrix['Age']==age]
        model.fit(self.age_matrix)
        return model

    def rec_by_users(self, model, name, age, neighbors=6):
        model = self.near_neighbors(age)
        if len(self.age_matrix) < neighbors:
            neighbors = len(self.age_matrix)
        distances, indices = model.kneighbors(
            name.values.reshape(1, -1), n_neighbors=neighbors)

        for i in range(0, len(distances.flatten())):
            if i == 0:
                print('Recommendations for {0}:\n'.format(name.index[0]))
            else:
                print('{0}: {1}, {2}'.format(i, self.age_matrix.index[indices.flatten()[i]], distances.flatten()[i]))


