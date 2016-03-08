import requests

class JiraHook:
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
    def __call__(self, url): pass
