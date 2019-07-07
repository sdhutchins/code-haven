# -*- coding: utf-8 -*-
"""
Date created: Wed Feb 22 01:08:49 2017
Author: S. Hutchins

Description: Use the redcap api to work with data.

"""
# Modules used
from redcap import Project, RedcapError
import pandas as pd
import io

#------------------------------------------------------------------------------
# Add api url and api key to communicate with the project
URL = 'https://redcap.umc.edu/redcap/api/'
API_KEY = ''
project = Project(URL, API_KEY)

#------------------------------------------------------------------------------
def get_fields():
    """Get a list of the fields from the metadata."""
    for field in project.metadata:
        print("%s (%s) ---> %s" % (field['field_name'], field['field_type'],
              field['field_label']))
#------------------------------------------------------------------------------
def upload_file(filename, record):
    """Upload a file to the project. The file size can't be > 100MB."""
    file = filename
    field = 'upload'
    fileobj = open(file, 'rb')
    try:
        # You have to issue a record number. '1' in this case.
        project.import_file(record, field=field, fname=file, fobj=fileobj)
        print("The file has uploaded.")
    except RedcapError:
        print("There is an error, and the file has not uploaded.")
    finally:
        fileobj.close()

#------------------------------------------------------------------------------
def download_file(record):
    """Download a file from my project.
    Use the record number and field to download the file."""
    file_content, headers = project.export_file(record, field='upload')
    try:
        with open(headers['name'], 'wb') as file_download:
            file_download.write(file_content)
        print("The file has successfully downloaded.")
    except RedcapError:
        print("There has been an error, and the file could not be downloaded.")

#------------------------------------------------------------------------------
def delete_file(record):
    """Delete a file. Enter the record number ('1') and the field 'upload'."""
    try:
        project.delete_file(record, field='upload')
    except ValueError:
        print("There's an error in the either the record or field value.")

#------------------------------------------------------------------------------
def create_df(record):
    """ Create a dataframe from the file content. """
    file_content, headers = project.export_file(record, field='upload', return_format='csv')
    df = pd.read_csv(io.BytesIO(file_content))
    return df;
