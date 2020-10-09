from django.shortcuts import render, get_object_or_404

# import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np
import plotly.express as px
from .covid19_data_clean import clean_data
from .models import Sensor, PublicacionSensor


# Create your views here.

def plot(request, id_sensor):
    id_sensor_list = [id_sensor,]

    context = {"plot_sensor": plot_sensor(id_sensor_list)}
    return render(request, "plots/index.html", context)


def plot_sensor(id_sensor_list):

    colors = ['red', ]
    #mode_size = [6, 8]

    #fig = go.Figure()
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    for i, id_sensor in enumerate(id_sensor_list):
        sensor = get_object_or_404(Sensor, id=id_sensor)
        qs = PublicacionSensor.objects.filter(id_sensor_fk=sensor)
        x_data = np.array(list(qs.values_list('fecha', flat=True)))
        y_data = np.array(list(qs.values_list('valor', flat=True)))

        fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='lines+markers',
                                 name=sensor.tipo.descripcion,
                                 line=dict(
                                     # color=colors[i],
                                     width=1),
                                 connectgaps=True,
                                 text=sensor.tipo.descripcion + \
                                 " Actual: " + str(y_data[-1])
                                 ),
                      secondary_y=bool(i),)
        max_val = 100
        min_val = 0
        fig.update_yaxes(type="linear", range=[
                         min_val, max_val], secondary_y=bool(i))

    fig.update_layout(
        #title='Diagrama de Tiempo',
        xaxis_title=None,
        yaxis_title=None,
        margin=dict(l=10, r=10, t=10, b=10),
        #width = 800,
        # paper_bgcolor="lightgrey",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    # fig.update_yaxes(type="linear", range=[0, 9], , secondary_y=False)
    plot_div = py.plot(fig, include_plotlyjs=False, output_type='div')

    return plot_div
