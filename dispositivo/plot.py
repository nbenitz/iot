from django.shortcuts import render, get_object_or_404
from django.utils import timezone
import pytz
from datetime import datetime, timedelta

import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np
import plotly.express as px
from .covid19_data_clean import clean_data
from .models import Sensor, Dispositivo, PublicacionSensor, PublicacionControlador


def plot_sensor(id_sensor_list, timezone_name, start, end):
    tz = pytz.timezone(timezone_name)
    
    start = datetime.strptime(start, "%Y-%m-%d").astimezone(pytz.timezone('UTC'))
    timezone.localtime(start, tz)

    end = datetime.strptime(end, "%Y-%m-%d").astimezone(pytz.timezone('UTC'))
    end = end + timedelta(days=1)
    timezone.localtime(end, tz)
    print(start)
    print(end)

    colors = ['red', ]
    #mode_size = [6, 8]
    #fig = go.Figure()
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    for i, id_sensor in enumerate(id_sensor_list):
        sensor = get_object_or_404(Sensor, id=id_sensor)
        qs = PublicacionSensor.objects.filter(
            id_sensor_fk=sensor,
            retain=0,
            fecha__range=[start, end]
        )

        if not qs.exists():
            return "<div class='row justify-content-center my-5 py-5'>" + \
                "No hay resultador para el rango de fechas</div>"

        x_df = pd.DataFrame(qs.values('fecha'))
        x_df['fecha'] = x_df['fecha'].map(
            lambda fecha: timezone.localtime(fecha, tz))

        x_data = np.array(list(x_df['fecha']))
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
        if sensor.tipo.descripcion == 'Temperatura':
            max_val = 60
        elif sensor.tipo.descripcion == 'Humedad':
            max_val = 100

        fig.update_yaxes(type="linear",
                         range=[min_val, max_val],
                         secondary_y=bool(i))

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


def plot_controller(id_controller_list, timezone_name, start, end):
    tz = pytz.timezone(timezone_name)

    start = datetime.strptime(start, "%Y-%m-%d").astimezone(pytz.timezone('UTC'))
    timezone.localtime(start, tz)

    end = datetime.strptime(end, "%Y-%m-%d").astimezone(pytz.timezone('UTC'))
    end = end + timedelta(days=1)
    timezone.localtime(end, tz)

    colors = ['red', ]
    #mode_size = [6, 8]

    #fig = go.Figure()
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    for i, id_controller in enumerate(id_controller_list):
        controller = get_object_or_404(Dispositivo, id=id_controller)
        qs = PublicacionControlador.objects.filter(
            controlador=controller, 
            retain=0,
            fecha__range=[start, end])
        x_df = pd.DataFrame(qs.values('fecha'))
        x_df['fecha'] = x_df['fecha'].map(
            lambda fecha: timezone.localtime(fecha, tz))
        x_data = np.array(list(x_df['fecha']))
        y_data = np.array(list(qs.values_list('valor', flat=True)))
        fig.add_trace(go.Scatter(x=x_data,
                                 y=y_data,
                                 mode='lines+markers',
                                 line_shape="hv",
                                 name=controller.nombre,
                                 line=dict(
                                     # color=colors[i],
                                     width=1),
                                 connectgaps=True,
                                 ),
                      secondary_y=bool(i),)
        max_val = 1
        min_val = 0
        fig.update_yaxes(type="linear", secondary_y=bool(i))

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
