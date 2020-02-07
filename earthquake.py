import pandas as pd
def clean():
    
    df = pd.read_csv('earthquake.csv')
    #extract new feature:region from existing:place
    df['region']=[ i[-1] for i in df['place'].str.split(', ')]
    df_clean = df[['time','latitude','longitude','depth','mpg','region']]
    #remove duplicates and nan
    df_clean = df_clean.drop_duplicates().drop_na()
    
    return df_clean
    
def mag_region():
    
    df_clean = clean()
    #data discretization using pd.cut to convert mag into a set of intervals
    df_clean['mag']=pd.cut(df_clean['mag'],bins=[0,2,5,7,9,12], right=False, labels=['micro','light','strong','major','great'])
    #group by mag and region and count number of values in each group, remove na values from results
    df_grouped = df_clean.groupby(by=['mag','region']).count().dropna()
    #reset index, sort by count and mag, then keep only the regions with the biggest count for each mag level
    df_new = df_grouped.reset_index().sort_values(by=['time','mag'], ascending = False).drop_duplicates(['mag'])
    #rename columns
    df_new.rename(columns ={'time':'times'}, inplace = True)
    #convert data types
    df_new['times'] = df_new['times'].astype('int')
    #output final dataset, set index
    df_final = df_new[['mag','region','times']].set_index(['mag'])
    
    return df_final



