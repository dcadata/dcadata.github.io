# IMPORT NECESSARY MODULES
import pandas as pd 
import numpy as np
# import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# IMPORT DATASET
df = pd.read_csv('dataset.csv', sep='\t', names=['user_id','item_id','rating','timestamp']).drop(columns='timestamp')

# IMPORT ARTIST NAMES DATASET AND MERGE WITH DATASET
df_names = pd.read_csv('artist_names.csv')
df = df.merge(df_names, on='item_id', how='left')

# Create df with avg rating for each
ratings = pd.DataFrame(df.groupby('name').rating.mean())

# Number of ratings
ratings = ratings.assign(num_ratings = df.groupby('name').rating.count())

# Visualize the distribution of the ratings
# ratings.rating.hist(bins=50)
# ratings.num_ratings.hist(bins=50)

# Create the matrix
mx = df.pivot_table(index='user_id', columns='name', values='rating')

# Let's imagine that user A's most-listened artists are Metallica and Mozart
art1 = mx['Metallica']
art2 = mx['Mozart']

# Now we want to find artists that are similar to both of these artists
# Compute the correlation b/w two dataframes using corrwith functionality - pairwise correlation of rows or columns
similar_art1 = mx.corrwith(art1)
similar_art2 = mx.corrwith(art2)

# Get artists that are in both lists
similar = similar_art1.merge(similar_art2, on='name', how='inner')
similar = similar.sort_values(by='Correlation', ascending=False)