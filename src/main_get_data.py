import csv
from datetime import datetime
from tmdbv3api import TMDb
from tmdbv3api import Movie, Discover
import pandas as pd
import numpy as np
import json
from rt_scraper import MovieScraper
from tqdm import tqdm

import configparser

config = configparser.ConfigParser()
config.read('.config')
api_key = config['TMDb']['key']

tmdb = TMDb()
tmdb.api_key = api_key
tmdb.language = 'en'
tmdb.debug = True

col_names = ['id',
             'title',
             'budget',
             'genres',
             'original_language',
             'production_companies',
             'release_date',
             'TW_release_date',
             'revenue',
             'runtime',
             'cast',
             'cast_cnt',
             'crew_cnt',
             'female_cast_cnt',
             'male_cast_cnt',
             'cast_popularity_ave',
             'director',
             'direcotr_gender',
             'TMDB_score',
             'TMDB_vote_count',
             'profit',
             'ROI',
             'rotten_score',
             'rating',
             'rotten_aud_score',
             'zh_title']

with open('data/movie_id.csv', newline='') as f:
    reader = csv.reader(f)
    movie_id = list(reader)[0]

if __name__ == '__main__':

    movie_df = pd.DataFrame(columns=col_names)

    for ID in tqdm(movie_id):
        movie_obj = Movie()
        m = movie_obj.details(ID)
        data_row = dict()
        data_row['id'] = m.id
        data_row['title'] = m.title
        data_row['budget'] = m.budget

        gen = [g['name'] for g in m.genres]
        data_row['genres'] = gen

        data_row['original_language'] = m.original_language

        pcs = [pc['name'] for pc in m.production_companies]
        data_row['production_companies'] = pcs

        data_row['release_date'] = m.release_date

        if m['homepage'] != "":
            data_row['has_homepage'] = 1
        else:
            data_row['has_homepage'] = 0

        TW_release_date_flag = False
        for loc in m.release_dates['results']:
            for key, value in loc.items():
                if value == 'TW':
                    TW_release_date_flag = True
                    data_row['TW_release_date'] = loc['release_dates'][0]['release_date']
                else:
                    continue
        if not TW_release_date_flag:
            data_row['TW_release_date'] = np.nan

        try:
            belongs_to_collection = m['belongs_to_collection']['name']
            data_row['belongs_to_collection'] = belongs_to_collection
        except:
            data_row['belongs_to_collection'] = np.nan

        data_row['revenue'] = m.revenue
        data_row['runtime'] = m.runtime

        pop_bound = 2
        cn = [c['name']
              for c in m.casts['cast'] if c['popularity'] >= pop_bound]
        data_row['cast'] = cn
        data_row['cast_cnt'], data_row['crew_cnt'] = len([c for c in movie_obj.credits(ID)[
            'cast'] if c['popularity'] >= pop_bound and c['gender'] != 0 and c['gender'] != 3]), len(movie_obj.credits(ID)['crew'])
        data_row['female_cast_cnt'] = len(
            [c['gender'] for c in m.casts['cast'] if c['gender'] == 1 and c['popularity'] >= pop_bound])
        data_row['male_cast_cnt'] = len(
            [c['gender'] for c in m.casts['cast'] if c['gender'] == 2 and c['popularity'] >= pop_bound])
        data_row['cast_popularity_ave'] = np.mean(
            [c['popularity'] for c in m.casts['cast'] if c['popularity'] >= pop_bound])
        try:
            data_row['director'] = [c['name']
                                    for c in movie_obj.credits(ID)['crew'] if c['job'] == 'Director'][0]
            data_row['direcotr_gender'] = [c['gender']
                                           for c in movie_obj.credits(ID)['crew'] if c['job'] == 'Director'][0]
        except:
            data_row['director'] = np.nan
            data_row['direcotr_gender'] = np.nan

        data_row['TMDB_score'] = m.vote_average
        data_row['TMDB_vote_count'] = m.vote_count

        data_row['profit'] = data_row['revenue'] - data_row['budget']

        try:
            data_row['ROI'] = data_row['profit'] / data_row['budget']
        except:
            continue

        try:
            # 爛番茄爬蟲
            year = datetime.strptime(data_row['release_date'], '%Y-%m-%d').year
            movie_scraper = MovieScraper(movie_title=m.title, year=year)
            movie_scraper.extract_metadata()
            data_row['rotten_score'] = float(
                movie_scraper.metadata['Score_Rotten'])
            data_row['rotten_aud_score'] = float(
                movie_scraper.metadata['Score_Audience'])
            data_row['rating'] = movie_scraper.metadata['Rating']
        except:
            data_row['rotten_score'] = np.nan
            data_row['rating'] = np.nan
            data_row['rotten_aud_score'] = np.nan

        # zh_title
        zh_title_flag = False
        for loc in m.translations['translations']:
            for key, value in loc.items():
                if value == 'TW':
                    data_row['zh_title'] = loc['data']['title']
                    zh_title_flag = True
                    break
                else:
                    continue
        if not zh_title_flag:
            data_row['zh_title'] = np.nan

        movie_df = movie_df.append(data_row, ignore_index=True)

    movie_df.to_excel('data/movie_data_set.xlsx')
