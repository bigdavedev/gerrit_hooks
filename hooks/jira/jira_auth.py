from .jira_hook import JiraHookCommand

import requests

class JiraLogin(JiraHookCommand):
    """
    Handles logging in to Jira.

    Requires username and password for user that
    has permission to perform required operations
    for hook.

    Ideally, this is not a real person, but rather
    a user specifically for this hook or for gerrit
    """
    def __init__(self, username, password):
        self.credentials = {
            'username': username,
            'password': password
        }
        self.endpoint = '/rest/auth/1/session'

    def __call__(self, url, session):
        """
        Attempt to log in to Jira via REST API
        """
        result = session.post(url + self.endpoint, json=self.credentials)
        print(result.status_code)

class JiraLogout(JiraHookCommand):
    """
    Must be called to not leave the user logged in
    when the hook operation is finished!
    """
    def __init__(self):
        self.endpoint = '/rest/auth/1/session'

    def __call__(self, url, session):
        result = session.delete(url + self.endpoint)
        print(result.status_code)
