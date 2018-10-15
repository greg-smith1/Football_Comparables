import os
import pandas as pd


from cosine_sim import PlayerRecommendationSystem as prs

df = pd.read_csv('football_comps.csv', index_col='Player')
lookup = pd.read_csv('fb_lookup.csv')
lookup = test_df.set_index('Player')

while True:
    os.system('clear')
    lookup_name = input('/n/nPlayer Name: ')
    subset = 