"""
File title: Cancer_API
Description: The API that mediates the data passing between the backend program and frontend dashboard interface
Author: Souren Prakash, Kuan Chun Chiu, Atharva
Date: 2024/10/10
"""

import pandas as pd
#import altair as alt
#import seaborn as sns
#import numpy as np

filename = r"C:\Users\Souren Prakash\OneDrive\Desktop\Cancer Tracking project\CTDC_Participants_download 2024-10-04 12-59-58.csv"

class CANAPI:

    can = None

    def load_can(self, filename):
        self.can= pd.read_csv(filename)
        return self.can

    def clean_can(self):
        self.can = self.can[["Diagnosis", "Age", "Sex", "Targeted Therapy"]]
        self.can.columns = ["Diagnosis", "Age", "Gender", "Therapy"]
        self.can["Therapy"] = self.can["Therapy"].apply(lambda x: x.replace("[", "").replace("]", "").split(",")[0])
        self.can["Therapy"] = self.can["Therapy"].apply(lambda x: "No_therapy_listed" if x == "" else x)
        return self.can

    def create_age_ranges(self):
        self.can["Age"] = self.can["Age"].astype(int)
        youngest_marker = self.can["Age"].quantile(0.25)
        middle_marker = self.can["Age"].median()
        oldest_marker = self.can["Age"].quantile(0.75)

        def classify_age(age):
            if age <= youngest_marker:
                return "youngest_age"
            elif age > youngest_marker and age <= middle_marker:
                return "middle_age"
            elif age > middle_marker and age <= oldest_marker:
                return "older_middle_age"
            else:
                return "oldest_age"
        self.can["Age"] = self.can["Age"].apply(classify_age)
        return self.can

    def group_df(self, group_list, min_patient_count):
        """
          Purpose: Group the df by two desired columns and add a artist_count column. Exclude rows where its artist_count
                   value is less than 20
          Parameter 1: artist_df, the filtered df
          Parameter 2: group_list, the list of columns to group by
          Return: artist_df, the df with artist count based on grouping the two entered columns
        """
        cancer_df = self.can
        if len(group_list) == 2:
            group_col1, group_col2 = group_list[0], group_list[1]
            cancer_df = cancer_df.groupby([group_col1, group_col2]).size().reset_index(name="Patient_count")
        elif len(group_list) == 3:
            group_col1, group_col2, group_col3 = group_list[0], group_list[1], group_list[2]
            cancer_df = cancer_df.groupby([group_col1, group_col2, group_col3]).size().reset_index(name="Patient_count")
        elif len(group_list) == 4:
            group_col1, group_col2, group_col3, group_col4 = group_list[0], group_list[1], group_list[2], group_list[3]
            cancer_df = cancer_df.groupby([group_col1, group_col2,
                                           group_col3, group_col4]).size().reset_index(name="Patient_count")
        cancer_df = cancer_df[cancer_df["Patient_count"] >= min_patient_count]
        return cancer_df

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