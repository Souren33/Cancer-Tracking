"""
File title: sankey
Author: Souren Prakash, Kuan Chun Chiu, Atharva
Description: The sankey library containing the make_sankey function and multi_layer_sankey function
Date: 2024/10/10
"""

# This file is only to construct the make_sankey() and multi_layer_sankey() functions,
# so no main() function is constructed or called at the end. This file only serves as
# a library so that files from future work can import this library and call the two functions within.

import pandas as pd
import plotly.graph_objects as go
def make_sankey(artist_df, source, target):
    """
      Purpose: Create a normal 2 layers sankey diagram, given the source and target column names
      Parameter 1: artist_df, the grouped df with artist count
      Parameter 2: source, the source column name
      Parameter 3: target, the target column name
      Return: N/A since there's no return() at the end of the function. Yet the sankey diagram is displayed.
    """
    label = list(pd.concat([artist_df[source], artist_df[target]]).unique())
    source = artist_df[source].apply(lambda x: label.index(x))
    target = artist_df[target].apply(lambda x: label.index(x))
    link = {"source": source, "target": target, "value": artist_df["Artist_count"]}
    node = {"pad": 50, "thickness": 50, "label": label}
    sk = go.Sankey(link=link, node=node)
    fig = go.Figure(sk)
    return fig

def multi_layer_sankey(can_df, source, inter_1, inter_2, target, **kwargs):
    """
      Purpose: Create a 3 layers sankey diagram, given the source, intermediate, and target column names
      Parameter 1: artist_df, the grouped df with artist count
      Parameter 2: source, the source column name
      Parameter 3: target, the target column name
      Parameter 4: intermediate, the intermediate column name
      Return: N/A since there's no return() at the end of the function. Yet the sankey diagram is displayed.
    """
    label = pd.concat([source, inter_1, inter_2, target])
    source = source.apply(lambda x: label.index(x))
    inter_1 = inter_1.apply(lambda x: label.index(x))
    inter_2 = inter_2.apply(lambda x: label.index(x))
    target = target.apply(lambda x: label.index(x))
    value = 1 * len(can_df)
    link = {"source": pd.concat([source, inter_1]),
            "intermediate": pd.concat([inter_1, inter_2])
            "target": pd.concat([inter_2, target]),
            "value": value}
    node = {"pad": 50, "thickness": 50, "label": label}
    sk = go.Sankey(link = link, node = node)
    fig = go.Figure(sk)
    height = kwargs.get("height", 800)
    width = kwargs.get("width", 1500)
    fig.update_layout(autosize=False, width=width, height=height)
    return fig