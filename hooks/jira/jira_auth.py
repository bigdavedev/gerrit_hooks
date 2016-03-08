
from .jira_hook import JiraHookCommand

import requests

class JiraLogin(JiraHookCommand):
    def __init__(self, username, password):
        self.credentials = {
            'username': username,
            'password': password
        }
        self.endpoint = '/rest/auth/1/session'

    def __call__(self, url, session):
        result = session.post(url + self.endpoint, json=self.credentials)
        print(result.status_code)

class JiraLogout(JiraHookCommand):
    def __init__(self):
        self.endpoint = '/rest/auth/1/session'

    def __call__(self, url, session):
        result = session.delete(url + self.endpoint)
        print(result.status_code)
