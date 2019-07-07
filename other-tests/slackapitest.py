# -*- coding: utf-8 -*-

""" I think one cool way to use this is within scripts on the MCSR when they
complete. In addition to email, you can use this in your script."""

from slacker import Slacker

# First, generate an api token
apikey = ''
slack = Slacker(apikey)

# Definition for uploading images
def upload_img(channel, imgfile):
    slack.files.upload(imgfile, channel=channel)

# Definition for uploading files
def upload_file(channel, file):
    slack.files.upload(file, channel=channel)

# Definition for posting messages
def post_message(channel, message, username):
    slack.chat.post_message(channel, message, username, as_user = True)

#------------------------------------------------------------------------------

post_message(channel='#general', message='YAS!', username='alert')


