
from .jira_hook import JiraHookCommand

import requests

class JiraAddComment(JiraHookCommand):
    def __init__(self, issue, comment):
        self.issue    = issue
        self.comment  = comment
        self.endpoint = '/rest/api/2/issue/{}/comment'.format(self.issue)

    def __call__(self, url, session):
        result = session.post(url + self.endpoint, json={'body': self.comment})
