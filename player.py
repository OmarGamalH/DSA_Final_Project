class Player:
    def __init__(self, number, name, color):

        self.number = number
        self.name = name
        self.color = color

    def __str__(self):
        return f"Player {self.number}: {self.name} ({self.color})"
