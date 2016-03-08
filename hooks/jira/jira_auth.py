
from .jira_hook import JiraHookCommand

import requests

class JiraLogin(JiraHookCommand):
    def __init__(self, session, username, password):
        self.session  = session
        self.credentials = {
            'username': username,
            'password': password
        }
        self.endpoint = '/rest/auth/1/session'

    def __call__(self, url):
        result = self.session.post(url + self.endpoint, json=self.credentials)
        print(result.status_code)

class JiraLogout(JiraHookCommand):
    def __init__(self, session):
        self.session  = session
        self.endpoint = '/rest/auth/1/session'

    def __call__(self, url):
        result = self.session.delete(url + self.endpoint)
        print(result.status_code)
