import pandas as pd


def clean_data():
    
    # loading data right from the source:
    print("Loading global deaths")
    death_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    print("Loading global confirmed")
    confirmed_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    print("Loading global recovered")
    recovered_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
    print("Loading cases country")
    country_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv')

    # data cleaning
    
    # renaming the df column names to lowercase
    country_df.columns = map(str.lower, country_df.columns)
    confirmed_df.columns = map(str.lower, confirmed_df.columns)
    death_df.columns = map(str.lower, death_df.columns)
    recovered_df.columns = map(str.lower, recovered_df.columns)
    
    # changing province/state to state and country/region to country
    confirmed_df = confirmed_df.rename(columns={'province/state': 'state', 'country/region': 'country'})
    recovered_df = recovered_df.rename(columns={'province/state': 'state', 'country/region': 'country'})
    death_df = death_df.rename(columns={'province/state': 'state', 'country/region': 'country'})
    country_df = country_df.rename(columns={'country_region': 'country'})
    # country_df.head()
    
    # save
    print("Save confirmed cases")
    confirmed_df.to_csv('datasets/covid19/time_series_covid19_confirmed_global.csv', index=False)
    print("Save recovered cases")
    recovered_df.to_csv('datasets/covid19/time_series_covid19_recovered_global.csv', index=False)
    print("Save death cases")
    death_df.to_csv('datasets/covid19/time_series_covid19_deaths_global.csv', index=False)
    print("Save country cases")
    country_df.to_csv('datasets/covid19/cases_country.csv', index=False)

    # total number of confirmed, death and recovered cases
    confirmed_total = int(country_df['confirmed'].sum())
    deaths_total = int(country_df['deaths'].sum())
    recovered_total = int(country_df['recovered'].sum())
    active_total = int(country_df['active'].sum())
    
    # create active actives dataframe
    active_df = pd.DataFrame(columns=confirmed_df.columns)
    count = len(confirmed_df.index)
    for i, row in confirmed_df.iterrows():
        country = row['country']
        state = row['state']
        
        column, value = '', ''
        if isinstance(state, str):
            column = 'state'
            value = state
        else:
            column = 'country'
            value = country
            
        if (value in recovered_df[column].values) and (value in death_df[column].values):
            recovered_list = recovered_df.loc[recovered_df[column] == value].iloc[:,4:].values.tolist()[0]
            deaths_list = death_df.loc[death_df[column] == value].iloc[:,4:].values.tolist()[0]
                
            active_df = active_df.append(confirmed_df.loc[i])            
            active_df.iloc[-1:, 4:] = active_df.iloc[-1:, 4:].sub(recovered_list, axis='columns')
            active_df.iloc[-1:, 4:] = active_df.iloc[-1:, 4:].sub(deaths_list, axis='columns')
            print(i, " de ", count, ".. creating active dataframe")

    # save actives dataframe as csv file
    print("Save active cases")
    active_df.to_csv('datasets/covid19/time_series_covid19_actives_global.csv', index=False)
    
    
    
    
    
    