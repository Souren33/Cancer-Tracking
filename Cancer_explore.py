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
width = pn.widgets.IntSlider(name="Diagram width", start=250, end=2000, step=125, value=1500)
height = pn.widgets.IntSlider(name="Diagram height", start=200, end=2500, step=100, value=800)

# Callback functions:
def get_plot(can_df, width, height):
    diagnosis = can_df["Diagnosis"]
    gender = can_df["Gender"]
    therapy = can_df["Therapy"]
    can_api.format_ages("Age")
    can_df = can_api.create_age_ranges()
    age = can_df["age_cat"]
    fig = sk.multi_layer_sankey(diagnosis, age, gender, therapy, width=width, height=height)
    return fig

print (get_plot(can_df, width, height))

"""
def get_catalog():
    pass



# Callback bindings
plot = get_plot(can_df)
catalog = get_catalog()


# Dashboard widgets card
card_width = 320

search_card = pn.Card(
    pn.Column(
        search_widget,
        search_widget,
        search_widget
    ),
    title="Search", width=card_width, collapsed=True
)

plot_card = pn.Card(
    pn.Column(
        width,
        height
    ),
    title="Plot", width=card_width, collapsed=True
)

# Dashboard layout
layout = pn.template.FastListTemplate(
    title="The Diagnosis & Therapy Linkage Dashboard",
    sidebar=[
        search_card,
        plot_card,
    ],
    theme_toggle=False,
    main=[
        pn.Tabs(
            ("Network", plot),  # Replace None with callback binding
            ("Associations", catalog),  # Replace None with callback binding
            active=0   # Which tab is active by default?
        )
    ],
    header_background='#a93226'
).servable()

layout.show()


"""













