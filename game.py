class Game():
  def __init__(self, players):
    if players < 2:
        raise ValueError('The game must be played with at least 2 players')
    if players > 4:
        raise ValueError('The game cannot be played with more than 4 players')
    self.players = players