import pandas as pd
import ipywidgets as widgets
from ipywidgets import interact, interact_manual
import numpy as np
import matplotlib.pyplot as plt
import requests
import folium
import json


def clean_data(df, week,):
    new_df = df.loc[df['veckonummer'] == week]
    new_df = new_df[['KnKod','nya_fall_vecka']]
    new_df['nya_fall_vecka'] = new_df['nya_fall_vecka'].str.replace('Okänd','0')
    new_df['nya_fall_vecka'] = new_df['nya_fall_vecka'].str.replace('<','')
    new_df['nya_fall_vecka'] = new_df['nya_fall_vecka'].astype(int)
    try:
        new_df = new_df.drop(new_df.loc[new_df['KnKod'] == 'Okänd'].index)
    except:
        pass
    return new_df
