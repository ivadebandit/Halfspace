import pandas as pd
df=pd.read_csv("players_2526.csv")


df=df.rename(columns={
    'Playing Time Min': 'minutes',
    'Performance Gls': 'goals',
    'Performance Ast':'assists',
    'Per 90 Minutes Gls':'goals_per90',
    'Per 90 Minutes Ast':'assists_per90',
    'pos': 'position'})
df=df[df['minutes'] >1500]

df.to_csv("cleaned.csv",index=False)

print(df['position'].unique())
print(len(df))
print(df[['player','team','position','minutes','goals','assists']].head())
