import ast
"""
File title: Cancer_explore
Description: The backend program that calls the API functions and connects to the panel dashboard
Author: Souren Prakash, Kuan Chun Chiu, Atharva
Date: 2024/10/10
"""

import panel as pn
from Cancer_API import CANAPI
import sankey as sk

# Loads javascript dependencies and configure panel
pn.extension()

# Initialize the API object
file_name = "CTDC_Participants_download 2024-10-04 12-59-58.csv"
can_api = CANAPI()

# Load the cancer file
can_df = can_api.load_can(file_name)
can_df = can_api.clean_can()
print (can_df.head(15))

# Search widgets




# Plot widgets
width = pn.Widgets.IntSlider(name="Diagram width", start=250, end=2000, step=125, value=1500)
height = pn.Widgets.IntSlider(name="Diagram height", start=200, end=2500, step=100, value=800)

# Callback functions:
def get_plot():
    diagnosis = can_api.get_diagnosis()
    gender = can_api.get_gender()
    therapy = can_api.get_therapy()
    can_api.format_ages()
    can_df = can_api.create_age_ranges()
    age = can_df["age_cat"].unique()
    fig = sk.multi_layer_sankey(can_df, diagnosis, gender, age, therapy, width=width, height=height)
    return fig

def get_catalog():























