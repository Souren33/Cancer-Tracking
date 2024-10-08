"""
File Cancer API
Description: API for interacting with the dataset of focus
"""

import pandas as pd
import altair as alt
import seaborn as sns

filename = r"C:\Users\Souren Prakash\OneDrive\Desktop\Cancer Tracking project\CTDC_Participants_download 2024-10-04 12-59-58.csv"

class CANAPI:

    can = None

    def load_can(self, filename):
        self.can= pd.read_csv(filename, )
       #print(self.can)
        return self.can

    def get_diagnosis(self):

        can = self.can
        can.Diagnosis = can.Diagnosis.str.lower()
        diagnosis = can.Diagnosis.unique()
        return diagnosis






def main():

    canapi = CANAPI()

    canapi.load_can(filename)

    print(canapi.get_diagnosis())


if __name__ == '__main__':
    main()