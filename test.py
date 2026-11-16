import soccerdata as sd
import pandas as pd
fbref = sd.FBref(
    leagues=["ENG-Premier League", "ESP-La Liga", "ITA-Serie A", "GER-Bundesliga", "FRA-Ligue 1"], 
    seasons="2025-2026")

stats = fbref.read_player_season_stats(stat_type="standard")
df=stats.reset_index()
df.columns=[' '.join(col).strip() if isinstance(col, tuple) else col for col in df.columns]
df.to_csv("players_2526.csv", index=False)
print(len(df))
print(df.columns.tolist())