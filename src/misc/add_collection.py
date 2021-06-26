from collections import defaultdict
import difflib
from urllib.request import urlopen
import requests
import re
from bs4 import BeautifulSoup
import csv
from tmdbv3api import TMDb
from tmdbv3api import Movie, Discover
import pandas as pd
import numpy as np
import json
from tqdm import tqdm
from datetime import datetime
import csv
from datetime import datetime
from tmdbv3api import TMDb
from tmdbv3api import Movie, Discover
import pandas as pd
import numpy as np
import json
# from rotten_tomatoes_scraper.rt_scraper import MovieScraper
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


if __name__ == '__main__':

    # movie_df = pd.read_excel('data/movie_data_set.xlsx', index_col=0)
    # u_movie_df = pd.read_excel('data/update_movie_data_set.xlsx', index_col=0)
    # start_id = u_movie_df.shape[0]
    movie_df = pd.read_excel('data/all_movie.xlsx',
                             index_col=0).drop(columns=['Unnamed: 0.1'])

    def get_collection_info(data_row):
        ID = data_row['id']
        movie_obj = Movie()
        m = movie_obj.details(ID)
        try:
            belongs_to_collection = m['belongs_to_collection']['name']
            data_row['belongs_to_collection'] = belongs_to_collection
        except:
            data_row['belongs_to_collection'] = np.nan

        return data_row

    # u_movie_df = movie_df.iloc[:6, :].apply(get_rt_info, axis=1)
    tqdm.pandas()
    movie_df = movie_df.progress_apply(get_collection_info, axis=1)

    movie_df.to_excel('data/all_movie.xlsx')
    # print(movie_df.columns)
