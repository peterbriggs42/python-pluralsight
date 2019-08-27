import pandas as pd
import matplotlib.pyplot as plt

from data import games

# https://stackoverflow.com/questions/48409128/what-is-the-difference-between-using-loc-and-using-just-square-brackets-to-filte
# https://stackoverflow.com/questions/38886080/python-pandas-series-why-use-loc/38886211#38886211 

my_plays = games.loc[(games['type']=='play'),:]
my_strike_outs = my_plays.loc[(my_plays['event'].str.contains('K')),:]
print('using loc: plays.len={0}, strikeouts.len={1}'.format(len(my_plays.index), len(my_strike_outs.index)))

plays = games[games['type']=='play']
strike_outs = plays[plays['event'].str.contains('K')]
# print(plays)
print('using normal selecter: plays.len={0}, strikeouts.len={1}'.format(len(plays.index), len(strike_outs.index) ))
# print(len(plays.index))
# print(len(strike_outs.index))

# groupby returns a groupby object, which is not a dataframe
strike_outs.groupby(['year', 'game_id'])
# you need to call a summary function on the grouping, e.g. size(), mean()
# but even that is still a groupby obj, not dataframe
strike_outs = strike_outs.groupby(['year', 'game_id']).size()
print(strike_outs)

# now we convert back to a dataframe by establishing new index column, and naming the group summary function "strike_outs"
strike_outs = strike_outs.reset_index(name='strike_outs')
print(strike_outs)

strike_outs = strike_outs.loc[:, ['year', 'strike_outs']].apply(pd.to_numeric)

strike_outs.plot(x='year', y='strike_outs', kind='scatter').legend(['Strike Outs'])
plt.show()
