import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors


class PlayerRecommendationSystem(object):

    def __init__(self, matrix):
        self.matrix = matrix

    def near_neighbors(self):
        model = NearestNeighbors(metric='cosine', algorithm='brute')
        model.fit(self.matrix)

        return model

    def rec_by_users(self, model, index, neighbors):
        matrix = self.matrix
        query_index = index
        distances, indices = model.kneighbors(
            matrix.iloc[query_index].values
            .reshape(1, -1), n_neighbors = neighbors)

        for i in range(0, len(distances.flatten())):
            if i == 0:
                print('Recommendations for {0}:\n'.format(matrix.index[query_index]))
            else:
                print('{0}: {1}'.format(i, matrix.index[indices.flatten()[i]]))