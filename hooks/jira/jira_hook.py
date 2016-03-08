import requests

class JiraHook:
    """
    Composable hook for manipulating Jira instances.

    Can be customised with JiraHookCommand classes.
    """
    def __init__(self, url, session=requests.Session()):
        self.commands = []
        self.url = url
        self.session = session

    def execute(self):
        for command in self.commands:
            command(self.url, self.session)

    def appendJiraCommand(self, command):
        self.commands.append(command)

class JiraHookCommand:
    """
    Base class for any commands that should be run against
    the Jira instance.
    """
    def __call__(self, url, session): pass
