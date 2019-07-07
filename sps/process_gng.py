# -*- coding: utf-8 -*-
# This script is using pandas version '0.23.4' and python version '3.6.6'

import pandas as pd
import numpy as np


def save_to_excel(filename, df1, sheet1, df2, sheet2):
    """Save data to an excel file with multiple sheets."""
    writer = pd.ExcelWriter(filename)
    df1.to_excel(writer, sheet1, index=False, na_rep='NA')
    df2.to_excel(writer, sheet2, index=False, na_rep='NA')
    writer.save()


def eliminate_isitime(df, time=1000):
    """Eliminate the 1000 ms trials in the `ISITime` column."""
    data = df.loc[(df['ISITime'] != time)]
    return data


def recode_session(df, session, recode_to):
    """Recode a row in the `Session` column."""
    df.loc[(df['Session'] == session), 'Session'] = recode_to
    return df


# Import the excel data.
# HINT Don't use an index.
gng_data = pd.read_excel('gng_data.xlsx', index=False)

# Add an empty column for the GoRT
gng_data["GoRT"] = np.nan

# Make a list of the subjects.
subjects = list(gng_data['Subject'].unique())

# Create an empty list for subject dataframes
subject_dfs = []

for subject in subjects:
    subject_df = str(subject) + "_df"
    subject_df = gng_data.loc[gng_data['Subject'] == subject]

    # Create new columns that have shifted to the next value for each subject.
    # 1. This ensures that DesignList.Sample has shifted 1 to the last trial in
    #    each session.
    # 2. This ensures that the LeadRT is the Fixation.RT for the next trial.
    subject_df['LeadRT'] = subject_df['Fixation.RT'].shift(-1)
    subject_df['count'] = subject_df['DesignList.Sample'].shift(-1)

    for index, row in subject_df.iterrows():
        subject = row['Subject']
        # In this instance, 1 is the last trial.
        if row['count'] == 1 or pd.isnull(row['count']):
            lead_rt = pd.np.nan
        else:
            lead_rt = row['LeadRT']
        # Valid responses
        if row['Condition'] == 'Go' and row['Stimulus.RT'] > 199:
            gort = row['Stimulus.RT']
            if pd.isnull(row['Stimulus.RT']):
                gort = 0
            subject_df.at[index, 'GoRT'] = gort
        elif row['Condition'] == 'Go' and row['Stimulus.RT'] < 200 and lead_rt != pd.np.nan and lead_rt != 0:
            gort = lead_rt + 250
            subject_df.at[index, 'GoRT'] = gort
        else:
            subject_df.at[index, 'GoRT'] = pd.np.nan
            subject_df.at[index, 'LeadRT'] = pd.np.nan

    # Add the updated dataframe to a list of dataframes
    subject_dfs.append(subject_df)

# Combine the subject dataframes into one dataframe
combined_df = pd.concat(subject_dfs)

# Remove NoGo Condition
combined_df = combined_df.loc[combined_df['Condition'] == "Go"]

# Recode the session variables
combined_df = recode_session(combined_df, 11, 1)
combined_df = recode_session(combined_df, 21, 2)
combined_df = recode_session(combined_df, 22, 2)
combined_df = recode_session(combined_df, 31, 3)
combined_df = recode_session(combined_df, 32, 3)

# Remove unneeded columns
combined_df.drop('LeadRT', axis=1, inplace=True)
combined_df.drop('count', axis=1, inplace=True)
combined_df.drop('Unnamed: 30', axis=1, inplace=True)
combined_df.drop('Unnamed: 31', axis=1, inplace=True)

# Eliminate 1000ms isitime
removed_isi_df = eliminate_isitime(combined_df)

# Save to file
save_to_excel("processed_gng_data.xlsx", removed_isi_df, "Filtered ISI",
              combined_df, "All Processed Data")
