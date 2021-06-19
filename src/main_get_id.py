from tmdbv3api import TMDb
from tmdbv3api import Movie, Discover
import pandas as pd
import numpy as np
import json
import csv
from tqdm import tqdm  # 進度條
import configparser

config = configparser.ConfigParser()
config.read('.config')
api_key = config['TMDb']['key']

tmdb = TMDb()
tmdb.api_key = api_key
tmdb.language = 'en'
tmdb.debug = True

discover = Discover()
vote_bound = 400  # 只抓 400 票觀眾投票以上的
movie = []
for year in tqdm(range(2000, 2022)):
    page = 1
    try:
        while True and page <= 1000:  # 1000 是頁數上限
            new_movie = discover.discover_movies({
                'primary_release_year': year,
                'vote_count.gte': vote_bound,
                'sort_by': 'primary_release_date.desc',
                'page': page
            })
            if len(new_movie) > 0:
                movie += new_movie
                page += 1
            else:
                break
    except:
        # 萬一不小心超出該年的 page 上限
        continue


movie_id = [m.id for m in movie]
len(movie_id)


with open('data/movie_id.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(movie_id)
