import pandas as pd
def clean():
    
    df = pd.read_csv('earthquake.csv')
    df['region']=[ i[-1] for i in df['place'].str.split(', ')]
    df_new = df[['time','latitude','longitude','depth','mpg','region']]
    df_clean = df.drop_duplicates().drop_na()
    
    return df_clean