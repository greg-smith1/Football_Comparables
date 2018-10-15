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

    def rec_by_users(self, model, name, age, neighbors):
        matrix = self.matrix
        distances, indices = model.kneighbors(
            matrix.loc[(df['Name']==name)][:1]].values
            .reshape(1, -1), n_neighbors = neighbors)

        for i in range(0, len(distances.flatten())):
            if i == 0:
                print('Recommendations for {0}:\n'.format(matrix.index[query_index]))
            else:
                print('{0}: {1}'.format(i, matrix.index[indices.flatten()[i]]))

    def name_to_index(name, age):
    index = current.loc[(current['Name']==name) & current['Age']==age]
    return index

&df['Age']==age