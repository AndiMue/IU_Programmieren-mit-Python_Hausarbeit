class NoMatchFoundError(Exception):
    def __init__(self):
        message = "Es konnte eine Übereinstimmung gefunden werden"
        self.message = message
        