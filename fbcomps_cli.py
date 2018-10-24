import os
import pandas as pd

from cosine_sim import PlayerCompSystem as pcs


df = pd.read_csv('football_total.csv', index_col='Unnamed: 1')
recs = pcs(df)
while True:
    os.system('clear')
    player = input('\nWho would you like to compare?\n')
    recs.rec_by_users(player)
    input()
