import random
import os
from sounds import Sounds
from playsound import playsound

class Game():

    # Initiate the game
    def __init__(self):
      self.score = 0
      self.latestScore = "-"
      self.highscore = self.read_highscore()
      self.pointsScored = 0
      self.amountExercises = 20
      self.exerciseNumber = 0

      
      self.notes = [\
      "fa#4", "fa4", "mi4", "re#4", "re4", "do#4", "do4", \
      "si3", "la#3", "la3", "sol#3", "sol3", "fa#3", "fa3", "mi3", "re#3", "re3", "do#3", "do3", \
      "si2", "la#2", "la2", "sol#2", "sol2", "fa#2", "fa2", "mi2", "re#2", "re2", "do#2", "do2", \
      "si1", "la#1"]
      self.sounds = []


    # Start game with given notes
    def start(self, notesIndex):
      print(f"Starting game {notesIndex} {self.amountExercises}")
      for i in notesIndex:
        self.sounds.append(Sounds.soundFileNames[i])
      self.current_sound = self.get_random_sound()
      

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
    
    def next_round(self, value):
      self.exerciseNumber += 1
      self.update_score(value)
      if self.exerciseNumber < self.amountExercises:
        self.current_sound = self.get_random_sound()
        self.play_sound(self.current_sound)


    def get_random_sound(self):
      sound = random.choice(self.sounds)
      sound = os.path.join(Sounds.pianoSoundDir,sound)
      return sound

    # Play random sound from sounds
    def play_sound(self, sound):
      playsound(sound, False)
      print(f"Play sound: {sound}")


