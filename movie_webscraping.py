import pandas as pd
import numpy as np
from imdb import IMDb
input_ = input('Enter file name of Movie Dataset : \n')
movies = pd.read_csv(input_)
def get_all_details_of_movie(movie_name):
    
    ia = IMDb()
    # Ccreate dictionary for all details
    dict_ = {'localized title':np.nan, 'original title':np.nan, 'imdbID':np.nan, 'original air date':np.nan, 'genres':np.nan, 'cast':np.nan,
          'plot outline':np.nan, 'rating':np.nan, 'votes':np.nan, 'age of content':np.nan, 'directors':np.nan, 'writers':np.nan,
          'producers':np.nan, 'composers':np.nan, 'cinematographers':np.nan, 'editors':np.nan, 'editorial department':np.nan,
          'production designers':np.nan, 'art directors':np.nan, 'costume designers':np.nan, 'production managers':np.nan, 'assistant directors':np.nan,
          'top 250 rank':np.nan, 'production companies':np.nan, 'distributors':np.nan, 'other companies':np.nan}
    
    
    search_ = ia.search_movie(movie_name)
    if not search_:
    return dict_
    search_movie_id = [x.movieID for x in search_]
    if not search_movie_id:
    return dict_
    movie_id = search_movie_id[0]
    # for m_id in search_movie_id:
    #   i = ia.get_movie(m_id)
    #   if movie_name == i['original title'] if 'original title' in i and 'movie' == i['kind'] else np.nan and 'movie' == i['kind']:
    #     movie_id = m_id
    #     # print(m_id)
    #     movie = ia.get_movie(movie_id)

    movie = ia.get_movie(movie_id)
    # localized title
    dict_['localized title'] = movie['localized title'] if 'localized title' in movie else np.nan
    # original title
    dict_['original title'] = movie['original title'] if 'original title' in movie else np.nan
    # imdbID
    dict_['imdbID'] = movie['imdbID'] if 'imdbID' in movie else np.nan
    # original air date
    dict_['original air date'] = movie['original air date'] if 'original air date' in movie else np.nan
    # genres
    dict_['genres'] = ''.join(f'{x}, ' for x in movie['genres']) if 'genres' in movie else np.nan
    # cast
    dict_['cast'] = ''.join(f'{y}, ' for y in [x['name'] for x in movie['cast'] if 'name' in x and 'cast' in movie]) if 'cast' in movie else np.nan
    # plot outline
    dict_['plot outline'] = movie['plot outline'] if 'plot outline' in movie else np.nan
    # rating
    dict_['rating'] = movie['rating'] if 'rating' in movie else np.nan
    # votes
    dict_['votes'] = movie['votes'] if 'votes' in movie else np.nan
    # age of content
    dict_['age of content'] = 2021 - int(movie['year']) if 'year' in movie else np.nan
    # directors
    dict_['directors'] = ''.join(f'{y}, ' for y in [x['name'] for x in movie['directors'] if 'name' in x]) if 'directors' in movie else np.nan
    # writers
    dict_['writers'] = ''.join(f'{y}, ' for y in [x['name'] for x in movie['writers'] if 'name' in x]) if 'writers' in movie else np.nan
    # producers
    dict_['producers'] = ''.join(f'{y}, ' for y in [x['name'] for x in movie['producers'] if 'name' in x])  if 'producers' in movie else np.nan
    # composers
    dict_['composers'] = ''.join(f'{y}, ' for y in [x['name'] for x in movie['composers'] if 'name' in x])  if 'composers' in movie else np.nan
    # cinematographers
    dict_['cinematographers'] = ''.join(f'{y}, ' for y in [x['name'] for x in movie['cinematographers'] if 'name' in x]) if 'cinematographers' in movie else np.nan
    # editors
    dict_['editors'] = ''.join(f'{y}, ' for y in [x['name'] for x in movie['editors'] if 'name' in x]) if 'editors' in movie else np.nan
    # editorial department
    dict_['editorial department'] = ''.join(f'{y}, ' for y in [x['name'] for x in movie['editorial department'] if 'name' in x]) if 'editorial department' in movie else np.nan
    # production designers
    dict_['production designers'] = ''.join(f'{y}, ' for y in [x['name'] for x in movie['production designers'] if 'name' in x]) if 'production designers' in movie else np.nan
    # art directors
    dict_['art directors'] = ''.join(f'{y}, ' for y in [x['name'] for x in movie['art directors'] if 'name' in x])  if 'art directors' in movie else np.nan
    # costume designers
    dict_['costume designers'] = ''.join(f'{y}, ' for y in [x['name'] for x in movie['costume designers'] if 'name' in x]) if 'costume designers' in movie else np.nan
    # production managers
    dict_['production managers'] = ''.join(f'{y}, ' for y in [x['name'] for x in movie['production managers'] if 'name' in x]) if 'production managers' in movie else np.nan
    # assistant directors
    dict_['assistant directors'] = ''.join(f'{y}, ' for y in [x['name'] for x in movie['assistant directors'] if 'name' in x])  if 'assistant directors' in movie else np.nan
    # top 250 rank
    dict_['top 250 rank'] = movie['top 250 rank'] if 'top 250 rank' in movie else np.nan
    # production companies
    dict_['production companies'] = ''.join(f'{y}, ' for y in [x['name'] for x in movie['production companies'] if 'name' in x]) if 'production companies' in movie else np.nan
    # distributors
    dict_['distributors'] = ''.join(f'{y}, ' for y in [x['name'] for x in movie['distributors'] if 'name' in x]) if 'distributors' in movie else np.nan
    # other companies
    dict_['other companies'] = ''.join(f'{y}, ' for y in [x['name'] for x in movie['other companies'] if 'name' in x]) if 'other companies' in movie else np.nan

    return dict_

from tqdm import tqdm
final_data = pd.DataFrame(columns=['localized title', 'original title', 'imdbID', 'original air date', 'genres', 'cast', 'plot outline', 'rating', 
                                   'votes', 'age of content', 'directors', 'writers', 'producers', 'composers', 'cinematographers', 'editors',
                                   'editorial department', 'production designers', 'art directors', 'costume designers', 'production managers',
                                   'assistant directors', 'top 250 rank', 'production companies', 'distributors', 'other companies'])
for index_num, row in tqdm(movies.iterrows()):
    movie_search = row['Movie Title']
    if not IMDb().search_movie(movie_search):
        index_num
    else: 
        movie_data = get_all_details_of_movie(movie_search)
        final_data = final_data.append(movie_data, True)

output = input('Enter output filename : ') + '.csv'
final_data.to_csv(output, index=False)
print('Done...')
