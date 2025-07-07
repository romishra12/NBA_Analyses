import polars as pl
import numpy as np
import pandas as pd
import nba_api as nba
from nba_api.stats.endpoints import commonplayerinfo, leagueleaders, playercareerstats, leaguedashteamstats
from nba_api.stats.static import players, teams
### Let's do a simple linear model- LeBron's player stats as 
### predictors on his team's season performance

## firstly, load all of LeBron's season stats from NBA_API

### first, get LeBron's player ID
nba_players = players.get_players()
nba_plyrs = pl.DataFrame(nba_players)
lebron = nba_plyrs.filter(pl.col("full_name")=='LeBron James')
lebron_id = lebron['id']

### pull his career stats
career = playercareerstats.PlayerCareerStats(player_id=lebron_id)
career_df = career.get_data_frames()[0]



nba_teams = pl.DataFrame(teams.get_teams())

lbj_teams = (nba_teams.filter(
    pl.col('full_name').is_in(
        ['Cleveland Cavaliers',
        'Miami Heat',
        'Los Angeles Lakers']))
        .select(pl.col(['id',
        'full_name','abbreviation'])))


cle_1_years = ['2003-04', '2004-05','2005-06',
            '2006-07', '2007-08','2008-09','2009-10']

mia_years = ['2010-11', '2011-12','2012-13',
            '2013-14']

cle_2_years = ['2014-15', '2015-16','2016-17',
            '2017-18']

lal_years = ['2018-19', '2019-20','2020-21',
            '2021-22','2022-23','2023-24','2024-25']


all_lbj_seasons = cle_1_years+mia_years+ cle_2_years+lal_years
all_seasons_data=[]
for season in all_lbj_seasons:
    team_stats = leaguedashteamstats.LeagueDashTeamStats(season=season)
    df = team_stats.get_data_frames()[0]
    df['SEASON'] = season  # Add season identifier
    all_seasons_data.append(df)
combined_stats = pd.concat(all_seasons_data)

