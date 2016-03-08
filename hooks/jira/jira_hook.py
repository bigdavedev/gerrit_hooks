class JiraHook:
    def __init__(self, url):
        self.commands = []
        self.url = url

    def execute(self):
        for command in self.commands:
            command(self.url)

    def appendJiraCommand(self, command):
        self.commands.append(command)

class JiraHookCommand:
    def __call__(self, url): pass
