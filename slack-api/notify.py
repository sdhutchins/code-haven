# -*- coding: utf-8 -*-
import argparse
import textwrap
import logging as log
from datetime import datetime as d

from slacker import Slacker

#------------------------------------------------------------------------------
# Set up the logger
format1 = '%a %b %d at %I:%M:%S %p %Y'  # Used to add as a date
format2 = '%m-%d-%Y@%I:%M:%S-%p'  # Used to append to archives

# Set up the blastn logger & log file
LOGFORMAT = '%(name)s - [%(levelname)-2s]: %(message)s'
log.basicConfig(level=log.DEBUG,
                format=LOGFORMAT,
                filename="logs/slack_notify.log")
slack_log = log.getLogger('Slack Message')

#------------------------------------------------------------------------------
class Slack(object):
    def init():
        config = configparser.ConfigParser()
        config.read('config.cfg')
        apikey = config['APIKEYS']['slack']
        self.slack = Slacker(apikey)

    def upload_img(self, channel, imgfile):
        """ Definition for uploading images. """
        self.slack.files.upload(imgfile, channel=channel)

    def upload_file(self, channel, file):
        """Definition for uploading file. """
        self.slack.files.upload(file, channel=channel)

    def message_slack(self, channel, message, username):
        """Definition for posting messages. """
        self.slack.chat.post_message(channel, message, username, as_user = True)

__author__ = 'SDH'

parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
                                    This is a command line wrapper for the Vallender Lab's Slack channel.

                                    Channels = #hall-project, #drd4-project, #karg-project,
                                               #l' '''))
parser.add_argument("-c", "--channel", help="Input a channel name", required=True)
parser.add_argument("-m", "--message", help="Write a message here", required=True)
parser.add_argument("-u", "--username", help="Input a username", required=True)
args = parser.parse_args()



Slack().message_slack(args.channel, args.message, args.username)
print('Your message was posted to Slack.')
slack_log.info('You posted to the %s channel with the user, %s.' % (args.channel, args.username))
log.shutdown()
