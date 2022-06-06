from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

from game import Game
from customwidgets import CheckableComboBox


class GUI(QMainWindow):

    # Initiate game and GUI
    def __init__(self):
      self.game = Game()
      self.initWindow(self.game.notes)


    # Initiate GUI window
    def initWindow(self, notes):
      app = QApplication([])

      window = QWidget()
      window.setWindowTitle('Perfect Pitch')
      window.setMinimumSize(600,300)

      # Layout
      # - combo Widget
      # - startLayout
      #    * startButton
      #    * stopButton
      # - frame widget --> gameLayout
      #    * playLayout
      #    * feedbackLayout
      #    * scoreLayout
      # - bottomLayout
      #    * latestScore
      #    * highscore
      layout = QVBoxLayout()
        
      # Select Notes
      self.combo = CheckableComboBox()
      layout.addWidget(self.combo)
      for i in range(len(notes)-1):
        self.combo.addItem(notes[i])
        self.combo.setItemChecked(i, True)
    
      # Start and Stop Buttons
      startLayout = QHBoxLayout()
      self.startButton = QPushButton('Start')
      self.startButton.clicked.connect(lambda: self.start_clicked(notes))
      startLayout.addWidget(self.startButton)
      self.stopButton = QPushButton('Stop')
      self.stopButton.clicked.connect(lambda: self.stop_clicked())
      self.stopButton.setEnabled(False)
      startLayout.addWidget(self.stopButton)
      layout.addLayout(startLayout)

      # Horizontal Line
      horLine = QFrame()
      horLine.setLineWidth(1)
      horLine.setFrameShape(QFrame.HLine)
      layout.addWidget(horLine)

      # Frame: Game Layout
      self.frame = QFrame()
      gameLayout = QVBoxLayout()
      self.frame.setLayout(gameLayout)
      layout.addWidget(self.frame)

      # Play Layout
      playLayout = QHBoxLayout()
      self.playLabel = QLabel("Exercise " + str(self.game.exerciseNumber))
      playLayout.addWidget(self.playLabel)
      playButton = QPushButton('Play')
      playLayout.addWidget(playButton)
      playButton.clicked.connect(lambda: self.play_clicked())

      gameLayout.addLayout(playLayout)

      # Feedback Layout
      feedbackLayout = QHBoxLayout()
      first = QPushButton('First attempt')
      second = QPushButton('Second attempt')
      third = QPushButton('Third attempt')
      incorrect = QPushButton('Incorrect')
      feedbackLayout.addWidget(first)
      feedbackLayout.addWidget(second)
      feedbackLayout.addWidget(third)
      feedbackLayout.addWidget(incorrect)
      first.clicked.connect(lambda: self.feedback_clicked(1))
      second.clicked.connect(lambda: self.feedback_clicked(2))
      third.clicked.connect(lambda: self.feedback_clicked(3))
      incorrect.clicked.connect(lambda: self.feedback_clicked(0))
      gameLayout.addLayout(feedbackLayout)

      # Score Layout
      scoreLayout = QVBoxLayout()
      self.points = QLabel('Points scored: +' + str(self.game.pointsScored))
      self.tot_points = QLabel('Total points: ' + str(self.game.score))
      self.latestScore = QLabel('Latest Score: ' + str(self.game.latestScore))
      self.highscore = QLabel('High Score: ' + str(self.game.highscore))
      scoreLayout.addWidget(self.points)
      scoreLayout.addWidget(self.tot_points)
      gameLayout.addLayout(scoreLayout)

      self.frame.hide()
      
      # Latest and High Scores
      bottomLayout = QHBoxLayout()
      bottomLayout.addWidget(self.latestScore, alignment=Qt.AlignBottom)
      bottomLayout.addWidget(self.highscore, alignment=Qt.AlignBottom)
      layout.addLayout(bottomLayout)

      window.setLayout(layout)
      window.show()
      app.exec_()


    # Click start
    def start_clicked(self, notes):
      self.update_numbers()
      notesUsed = []
      for i in range(len(self.combo)-1):
        if self.combo.itemChecked(i):
          notesUsed.append(notes[i])
      self.game.start(notesUsed)

      self.combo.setEnabled(False)
      self.stopButton.setEnabled(True)
      self.startButton.setEnabled(False)
      self.frame.show()

    # Click stop
    def stop_clicked(self):
      self.game.reset()
      self.combo.setEnabled(True)
      self.stopButton.setEnabled(False)
      self.startButton.setEnabled(True)
      self.frame.hide()
    
    # Click play
    def play_clicked(self):
      self.game.play_sound()
      print("Play")

    # Click on feedback buttons
    def feedback_clicked(self, value):
      self.game.exerciseNumber += 1
      self.game.update_score(value)
      if self.game.exerciseNumber >= self.game.amountExercises:
        self.game.finalize()
        self.stop_clicked()
      self.update_numbers()
      
    # Update exercise number, current points, total points, latest score and highscore 
    # with latest numbers from Game 
    def update_numbers(self):
      self.playLabel.setText("Exercise " + str(self.game.exerciseNumber))
      self.points.setText('Points scored: +' + str(self.game.pointsScored))
      self.tot_points.setText('Total points: ' + str(self.game.score))
      self.latestScore.setText('Latest Score: ' + str(self.game.latestScore))
      self.highscore.setText('High Score: ' + str(self.game.highscore))
