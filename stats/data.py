import os
import glob

import pandas as pd

# contains list of all file names in the 'games' folder that end with '.EVE'
game_files = glob.glob(os.path.join(os.getcwd(), 'games', '*.EVE'))

# This function sorts a given list *in-place*, to return a new sorted list use `sorted(list)`
game_files.sort()

game_frames = []
for game_file in game_files:
    #print('Hi this is a file: ', filename)
    game_frame = pd.read_csv(game_file, names=['type', 'multi2', 'multi3', 'multi4', 'multi5', 'multi6', 'event'])
    game_frames.append(game_frame)

# larger DataFrame, containing all of data from event files
games = pd.concat(game_frames)

# can use indexer syntax on games dataframe to evaluate row-based conditionals
# then pass an array of cols to second arg, and combine with assignment to set all '??'s to ''
games.loc[games['multi5'] == '??', ['multi5']] = ''

# take contents of multi2 col and pull out those that match the regex
identifiers = games['multi2'].str.extract(r'(.LS(\d{4})\d{5})')
# print(identifiers)
identifiers = identifiers.fillna(method='ffill')
identifiers.columns = ['game_id', 'year']
# print(filledIds)
# combine the two frames. What is an axis?
games = pd.concat([games, identifiers], axis=1, sort=False)
# print(bigframe)

# can use these two functions to detect missing values. In Pandas 'missing' is not implemented by setting them to be None
# print(games['multi3'].notna())
# print(games['multi3'].isna())
games = games.fillna(' ')

# replcae the unstructured 'type' column with a Category-column from pandas
games.loc[:, 'type'] = pd.Categorical(games.loc[:, 'type'])

# print(games.head())