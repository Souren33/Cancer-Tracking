"""
File Cancer API
Description: API for interacting with the dataset of focus
"""

import pandas as pd
import altair as alt
import seaborn as sns
import numpy as np

filename = r"C:\Users\Souren Prakash\OneDrive\Desktop\Cancer Tracking project\CTDC_Participants_download 2024-10-04 12-59-58.csv"

class CANAPI:

    can = None

    def load_can(self, filename):
        self.can= pd.read_csv(filename)
       #print(self.can)
        return self.can



    def get_diagnosis(self):
        """
        Getting unique diagnosis for sliders or focus
        :return:
        """

        can = self.can
        can.Diagnosis = can.Diagnosis.str.lower()
        diagnosis = can.Diagnosis.unique()
        return diagnosis




    def get_age(self):
        """
        This method objective is to find the unique values for the age
        This will be used later to create new age brackets, which in turn will be added to the data set
        This new column will have a range in which the values fall so we can create a better, more complex sankey
        :return:
        """

        can = self.can
        can.Age = can.Age.astype(int)
        unique_ages = can.Age.unique()
        return unique_ages


    def format_ages(self, age_column):

        self.can[age_column]= self.can[age_column].astype(int)
        return self



    def create_age_ranges(self):
        data = self.can

        # Calculate age quantiles based on the 'Age' column
        youngest_marker = data["Age"].quantile(0.25)
        oldest_marker = data["Age"].quantile(0.75)
        middle_marker = data["Age"].median()

        # Function to classify the age into different age ranges
        def classify_age(age):
            if age <= youngest_marker:
                return "youngest age range"
            elif youngest_marker < age <= middle_marker:
                return "middle age range"
            elif age > middle_marker and age <= oldest_marker:
                return "older middle age range"
            else:
                return 'oldest age range'

        # Apply the classification function to create a new column 'age cat'
        data['age cat'] = data['Age'].apply(classify_age)

        # Return the modified DataFrame
        return data


def main():

    #age column


    canapi = CANAPI()


    #getting dataset
    can = canapi.load_can(filename)


    #formating ages
    canapi.format_ages("Age")

    data = canapi.create_age_ranges()

    print(data)




   #print(canapi.create_age_ranges())
if __name__ == '__main__':
    main()