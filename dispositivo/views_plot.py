from django.shortcuts import render

import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import numpy as np
import plotly.express as px
from .covid19_data_clean import clean_data




# Create your views here.
    
def plot(request):
    
    # clean_data()
    
    # read_csv
    confirmed_df = pd.read_csv('datasets/covid19/time_series_covid19_confirmed_global.csv')
    actives_df = pd.read_csv('datasets/covid19/time_series_covid19_actives_global.csv')
    recovered_df = pd.read_csv('datasets/covid19/time_series_covid19_recovered_global.csv')
    death_df = pd.read_csv('datasets/covid19/time_series_covid19_deaths_global.csv')
    country_df = pd.read_csv('datasets/covid19/cases_country.csv')
    
    context = {"plot_cases_of_a_country":plot_cases_of_a_country('Paraguay', confirmed_df, actives_df, recovered_df, death_df),
               "example_Plot":examplePlot()
               }
    return render(request, "plots/index.html", context)

def plot_cases_of_a_country(country, confirmed_df, active_df, recovered_df, death_df):

    labels = ['deaths', 'recovered', 'actives', 'confirmed']
    colors = ['red', 'green', 'orange', 'blue']
    #mode_size = [6, 8]
    line_size = [1, 1, 1, 1]
    
    df_list = [death_df, recovered_df, active_df, confirmed_df]
    
    fig = go.Figure()
    
    for i, df in enumerate(df_list):
        if country == 'World' or country == 'world':
            x_data = np.array(list(df.iloc[:, 4:].columns))
            y_data = np.sum(np.asarray(df.iloc[:,4:]),axis = 0)
            
        else:    
            x_data = np.array(list(df.iloc[:, 49:].columns))
            y_data = np.sum(np.asarray(df[df['country'] == country].iloc[:,49:]),axis = 0)
            
        fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='lines+markers',
                                 name=labels[i],
                                 line=dict(color=colors[i], width=line_size[i]),
                                 connectgaps=True,
                                 text = "Total " + str(labels[i]) +": "+ str(y_data[-1])
                                 ))
    
    fig.update_layout(
        title="COVID 19 cases of " + country,
        xaxis_title='Date',
        yaxis_title='No. of Confirmed Cases',
        margin=dict(l=20, r=20, t=40, b=20),
        #width = 800,
        #paper_bgcolor="lightgrey",
        
    )
    
    fig.update_yaxes(type="linear")
    plot_div = py.plot(fig, include_plotlyjs=False, output_type='div')

    return plot_div

def examplePlot():
    # Makes a simple plotly plot, and returns html to be included in template.
    x = np.linspace(0, 12.56, 41)
    y = np.sin(x)
    y2 = np.sin(1.2*x)

    data = [
        go.Scatter(
            name = 'Sin(x)',
            x=x,
            y=y,
        ),

        go.Scatter(
            name = 'Sin(1.2x)',
            x=x,
            y=y2,
        ),
    ]

    layout = go.Layout(
        xaxis=dict(
            title='x'
        ),

        yaxis=dict(
            title='Value',
            hoverformat = '.2f'
        ),
    )

    fig = go.Figure(data=data, layout=layout)
    plot_div = py.plot(fig, include_plotlyjs=False, output_type='div')

    return plot_div