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

if __name__ == "__main__":
    df1 = pd.read_excel('data/update_movie_data_set.xlsx', index_col=0)
    df2 = pd.read_excel('data/covid_movie_data_set.xlsx', index_col=0)

    combined_df = pd.concat([df1, df2], ignore_index=True)

    combined_df.to_excel('data/all_movie.xlsx')
