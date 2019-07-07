# -*- coding: utf-8 -*-
"""Simple functions to get information about github repos using the api."""

from github import Github
import pandas as pd


class GH(object):
    """Github object."""
    def __init__(self, user='sdhutchins', password='Ilovesam2'):
        """Create a Github instance."""
        self.github_login = Github(user, password)

    def getrepos(self):
        """Get a list of the repositories."""
        repolist = []
        # Print a list of all of your repos
        for repo in self.github_login.get_user().get_repos():
            repolist.append(str(repo.name))
        return repolist

    def repolist2csv(self, filename):
        repodf = pd.DataFrame(self.getrepos())
        repodf.to_csv(filename, header=None, index=False)

    def deleterepo(self, reponame):
        repo = self.github_login.get_repo(reponame)
        answer = input('Delete %s repository [Y/N]? ' % reponame)
        acceptable = ['Y', 'y']
        if answer not in acceptable:
            raise Exception('You do not want to delete this repository.')
        else:
            repo.delete()
            print('%s repository deleted.' % reponame)
