"""
File Cancer API
Description: API for interacting with the dataset of focus
"""

import pandas as pd
import altair as alt
import seaborn as sns


class CANAPI:

    CAN = None

    def load_CAN(self, filename):
        self.CAN = pd.read_excel(filename)
        print(self.pal)


    def get_age(self):

        CAN_areas = self.CAN.age

    class G


    #def get_locations(self):


