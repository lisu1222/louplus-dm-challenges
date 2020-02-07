import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def clean_df():
    data = pd.read_excel('ClimateChange.xlsx', sheetname = 'Data')
    #replace .. with nan
    data.replace({'..': np.NaN}, inplace = True)
    
    #create two separate datasets
    co2 = data.loc[data['Series code'] == 'EN.ATM.CO2E.KT'].drop(labels=['Series code', 'Series name', 'Country name', 'SCALE', 'Decimals'], axis = 1).set_index('Country code')
    gdp = data.loc[data['Series code'] == 'NY.GDP.CMKTP.CD'].drop(labels = ['Series code', 'Series name', 'Country name', 'SCALE', 'Decimals'], axis = 1).set_index('Country code')
    #clean data
    co2 = co2.fillna(method ='ffill', axis=1).fillna(method='bfill',axis=1).fillna(0)
    gdp = gdp.fillna(method='ffill',axis = 1).fillna(method='bfill', axis=1).fillna(0)
    
    co2['co2 sum'] = co2.sum(axis = 1)
    gdp['gdp sum'] = gdp.sum(axis = 1)
    
    #integrate and normalize data
    combined = pd.concat([co2['co2 sum'], gdp['gdp sum']], axis = 1)
    combined = (combined - combined.min()) / (combined.max() - combined.min())
    
    return combined
    
    
def co2_gdp_plot():
    combined = clean_df()
    #specify five countries labels and xtick positions
    countries_labels = ['CHN','USA','GBR','FRA','RUS']
    countries_labels_position = []
    for i in range(len(combined)):
        if combined.index[i] in countries_labels:
            countries_labels_position.append(i)
            
    #draw the line plots
    fig,axes = plt.subplots()
    combined.plot(kind='line', title = 'GDP-CO2', ax = axes)
    plt.xlabel('Countries')
    plt.ylabel('Values')
    plt.xticks(countries_labels_position, countries_labels, rotation = 'vertical')
    plt.show()
    
    china = np.round(combined.loc['CNH'],3).tolist()
    
    return axes, china