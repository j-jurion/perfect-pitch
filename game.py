import random

class Game():

    # Initiate the game
    def __init__(self):
      self.score = 0
      self.latestScore = "-"
      self.highscore = self.read_highscore()
      self.pointsScored = 0
      self.amountExercises = 20
      self.exerciseNumber = 0

      self.notes = ["fa#4", "fa4", "mi4", "re#4", "re4", "do#4", "do4", "si3", "la#3", "la3", "sol#3", \
      "sol3", "fa#3", "fa3", "mi3", "re#3", "re3", "do#3", "do3", "si2", "la#2", "la2", "sol#2", "sol2", \
      "fa#2", "fa2", "mi2", "re#2", "re2", "do#2", "do2", "si1", "la#1"]
      self.sounds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

      self.exerciseNotes = []

    # Start game with given notes
    def start(self, notes):
      self.exerciseNotes = notes
      print(f"Starting game {self.exerciseNotes} {self.amountExercises}")

    # Update the current score with given feedback value
    def update_score(self, value):
      if value == 1:
        self.pointsScored = 5
      elif value == 2:
        self.pointsScored = 2
      elif value == 3:
        self.pointsScored = 1
      elif value == 0:
        self.pointsScored = 0
      self.score += self.pointsScored

    # Reset score and exercise number to zero
    def reset(self):
      self.score = 0
      self.pointsScored = 0
      self.exerciseNumber = 0

    # End the game, update highscore and latest score
    def finalize(self):
      self.latestScore = self.score
      if self.score > self.highscore:
        self.highscore = self.score
        self.write_highscore()
      self.reset()

    # Write highscore file
    def write_highscore(self):
      file = open("highscore.txt","w")
      file.write(str(self.highscore))

    # Read highscore file
    def read_highscore(self):
      file = open("highscore.txt","r")
      return int(file.read())

    # Play random sound from sounds
    def play_sound(self):
      sound = random.choice(self.sounds)
      print(f"Play sound: {sound}")

