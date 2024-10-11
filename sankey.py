"""
File title: sankey
Author: Souren Prakash, Kuan Chun Chiu, Atharva
Description: The sankey library containing the make_sankey function and multi_layer_sankey function
Date: 2024/10/10
"""

# This file is made to only construct the two_layer_sankey(), three_layer_sankey(), and four_layer_sankey() functions,
# so no main() function is constructed or called at the end. This file only serves as a library so that files from
# future work can import this library and call the three functions within, in order to make the sankey diagrams

import pandas as pd
import plotly.graph_objects as go

def two_layer_sankey(cancer_df, source, target, **kwargs):
    """
      Purpose: Create a normal 2 layers sankey diagram, given the source and target column names
      Parameter 1: cancer_df, the grouped df with patient count
      Parameter 2: source, the source column name
      Parameter 3: target, the target column name
      Parameter 4: kwargs, a dictionary to store the height and width input
      Return: fig, the sankey figure plotted using the source and target
    """
    label = list(pd.concat([cancer_df[source], cancer_df[target]]).unique())
    source = cancer_df[source].apply(lambda x: label.index(x))
    target = cancer_df[target].apply(lambda x: label.index(x))
    link = {"source": source, "target": target, "value": cancer_df["Patient_count"]}
    node = {"pad": 50, "thickness": 50, "label": label}
    sk = go.Sankey(link=link, node=node)
    fig = go.Figure(sk)
    width, height = kwargs.get("width", 1500), kwargs.get("height", 800)
    fig.update_layout(autosize=False, width=width, height=height)
    return fig

def three_layer_sankey(cancer_df, source, intermediate, target, **kwargs):
    """
      Purpose: Create a normal 2 layers sankey diagram, given the source and target column names
      Parameter 1: cancer_df, the grouped df with patient count
      Parameter 2: source, the source column name
      Parameter 3: intermediate, the intermediate column name
      Parameter 4: target, the target column name
      Parameter 5: kwargs, a dictionary to store the height and width input
      Return: fig, the sankey figure plotted using the source and target
    """
    label = list(pd.concat([cancer_df[source], cancer_df[intermediate], cancer_df[target]]).unique())
    source = cancer_df[source].apply(lambda x: label.index(x))
    intermediate = cancer_df[intermediate].apply(lambda x: label.index(x))
    target = cancer_df[target].apply(lambda x: label.index(x))
    source = pd.concat([source, intermediate])
    target = pd.concat([intermediate, target])
    value = cancer_df["Patient_count"]
    value = pd.concat([value, value])
    link = {"source": source, "target": target, "value": value}
    node = {"pad": 50, "thickness": 50, "label": label}
    sk = go.Sankey(link=link, node=node)
    fig = go.Figure(sk)
    width, height = kwargs.get("width", 1500), kwargs.get("height", 800)
    fig.update_layout(autosize=False, width=width, height=height)
    return fig

def four_layer_sankey(cancer_df, source, inter1, inter2, target, **kwargs):
    """
      Purpose: Create a normal 2 layers sankey diagram, given the source and target column names
      Parameter 1: cancer_df, the grouped df with patient count
      Parameter 2: source, the source column name
      Parameter 3: inter1, the first intermediate column name
      Parameter 4: inter2, the second intermediate column name
      Parameter 5: target, the target column name
      Parameter 6: kwargs, a dictionary to store the height and width input
      Return: fig, the sankey figure plotted using the source and target
    """
    label = list(pd.concat([cancer_df[source], cancer_df[inter1], cancer_df[inter2], cancer_df[target]]).unique())
    source = cancer_df[source].apply(lambda x: label.index(x))
    inter1 = cancer_df[inter1].apply(lambda x: label.index(x))
    inter2 = cancer_df[inter2].apply(lambda x: label.index(x))
    target = cancer_df[target].apply(lambda x: label.index(x))
    source = pd.concat([source, inter1, inter2])
    target = pd.concat([inter1, inter2, target])
    value = cancer_df["Patient_count"]
    value = pd.concat([value, value, value])
    link = {"source": source, "target": target, "value": value}
    node = {"pad": 50, "thickness": 50, "label": label}
    sk = go.Sankey(link=link, node=node)
    fig = go.Figure(sk)
    width, height = kwargs.get("width", 1500), kwargs.get("height", 800)
    fig.update_layout(autosize=False, width=width, height=height)
    return fig