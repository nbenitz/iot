from django.shortcuts import render, get_object_or_404
from django.utils import timezone
import pytz
from datetime import datetime, timedelta

#import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np
import plotly.express as px
from .models import Sensor, Dispositivo, PublicacionSensor, PublicacionControlador


def plot_sensor(id_sensor_list, timezone_name, start, end):
    lz = pytz.timezone(timezone_name)
    utc = pytz.timezone('UTC')

    start = datetime.strptime(str(start), "%Y-%m-%d")
    start = lz.localize(start).astimezone(utc)

    end = datetime.strptime(str(end), "%Y-%m-%d")
    end = lz.localize(end).astimezone(utc)
    end = end + timedelta(days=1)

    colors = ['red', ]
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    for i, id_sensor in enumerate(id_sensor_list):
        sensor = get_object_or_404(Sensor, id=id_sensor)
        qs = PublicacionSensor.objects.filter(id_sensor_fk=sensor,
                                              fecha__range=[start, end]
                                              ).order_by('fecha')

        if not qs.exists():
            return "<div class='row justify-content-center my-5 py-5'>" + \
                "No hay resultados para el rango de fechas</div>"

        x_data = [timezone.localtime(entry.fecha, lz) for entry in qs]
        y_data = [entry.valor for entry in qs]

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
        elif sensor.tipo.descripcion == 'Ph':
            max_val = 14
        elif sensor.tipo.descripcion == 'Ec':
            max_val = 2100
        elif sensor.tipo.descripcion == 'Sensor de Puerta':
            max_val = 1.2
        elif sensor.tipo.descripcion == 'Velocidad del Viento':
            max_val = 130
        elif sensor.tipo.descripcion == 'Presión Atmosférica':
            max_val = 1015
        elif sensor.tipo.descripcion == 'Corriente':
            max_val = 500
        elif sensor.tipo.descripcion == 'Voltaje':
            max_val = 5.2

        fig.update_yaxes(type="linear",
                         range=[min_val, max_val],
                         secondary_y=bool(i))

    fig.update_layout(
        #title='Diagrama de Tiempo',
        xaxis_title=None,
        yaxis_title=None,
        margin=dict(l=10, r=10, t=10, b=10),
        #width = 800,
        height=300,
        # paper_bgcolor="lightgrey",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    # Add range slider
    fig.update_layout(
        xaxis=go.layout.XAxis(
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )

    # fig.update_yaxes(type="linear", range=[0, 9], , secondary_y=False)
    plot_div = py.plot(fig, include_plotlyjs=False, output_type='div')

    return plot_div


def plot_controller(id_controller_list, timezone_name, start, end):
    lz = pytz.timezone(timezone_name)
    utc = pytz.timezone('UTC')

    start = datetime.strptime(str(start), "%Y-%m-%d")
    start = lz.localize(start).astimezone(utc)

    end = datetime.strptime(str(end), "%Y-%m-%d")
    end = lz.localize(end).astimezone(utc)
    end = end + timedelta(days=1)

    colors = ['red', ]
    #mode_size = [6, 8]

    #fig = go.Figure()
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    for i, id_controller in enumerate(id_controller_list):
        controller = get_object_or_404(Dispositivo, id=id_controller)
        qs = PublicacionControlador.objects.filter(
            controlador=controller,
            fecha__range=[start, end]).order_by('fecha')

        if not qs.exists():
            return "<div class='row justify-content-center my-5 py-5'>" + \
                "No hay resultados para el rango de fechas</div>"

        x_data = [timezone.localtime(entry.fecha, lz) for entry in qs]
        y_data = [entry.valor for entry in qs]

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
        height=200,
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
