import pandas as pd
from ydata_profiling import ProfileReport



links = pd.read_csv('links.csv')
# print(links)

movies_metadata = pd.read_csv('movies_metadata.csv', low_memory=False)
movies_metadata['imdbId'] = movies_metadata['imdbId'].str.replace('^tt', '', regex=True)
movies_metadata['imdbId'] = pd.to_numeric(movies_metadata['imdbId'], errors='coerce')
movies_metadata = movies_metadata.dropna(subset=['imdbId'])
movies_metadata['imdbId'] = movies_metadata['imdbId'].astype(int)

# print(movies_metadata)

ratings = pd.read_csv('ratings.csv')
# print(ratings)

df_ratings = pd.merge(links, ratings, on ='movieId', how ='inner')
df_ratings['imdbId'] = df_ratings['imdbId'].astype(int)

# df_merged = pd.merge(df_ratings, movies_metadata, on='imdbId', how='inner')


df_ratings_amostra = df_ratings.sample(n=80000, random_state=42)


df_merged_amostra = pd.merge(df_ratings_amostra, movies_metadata, on='imdbId', how='inner')

print(df_merged_amostra.head())
print(len(df_merged_amostra))
print(df_merged_amostra.describe(include='all'))
print(df_merged_amostra.info())
profile = ProfileReport(df_merged_amostra, title="Relatório", explorative=True)
profile.to_file("relatorio.html")

# print(df_merged)