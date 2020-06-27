from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5 import QtGui
import sys
from click import getAnswer, getQuestion

title = "Trivia"

def frameWelcome():
    app = QApplication(sys.argv)  # Giving cong setup info

    # Creating the window
    win = QMainWindow()
    win.setGeometry(300, 300, 0, 0)
    win.setFixedSize(250, 150)
    win.setWindowTitle(title)

    # Creating / Adding a label
    label = QtWidgets.QLabel(win)
    label.setFont(QtGui.QFont("Sanserif", 20))
    label.setText("Welcome")
    label.setFixedWidth(200)
    label.move(60, 40)

    # Creating / Adding a button
    button = QtWidgets.QPushButton(win)
    button.setText("Click Me")
    button.setFont(QtGui.QFont("Sanserif", 20))
    button.setFixedWidth(200)
    button.move(28, 100)
    button.clicked.connect(frameQ)
    # Showing the GUI
    win.show()
    sys.exit(app.exec_()) # Tells the program to end once the GUI is closed by the user


# Calling the frame method
def frameQ():
    app = QApplication(sys.argv)  # Giving cong setup info

    question = getQuestion() # Getting the question from the API
    answer = getAnswer() # Getting the answer to the question
    
    # Creating the window
    winQ = QMainWindow()
    winQ.setGeometry(300, 300, 0, 0)
    winQ.setFixedSize(400, 300)
    winQ.setWindowTitle(title)
    
    # Creating / Adding a label
    labelQ = QtWidgets.QLabel(winQ)
    labelQ.setText(question)
    labelQ.setFixedWidth(300)
    labelQ.move(50, 40)
    winQ.show()
    sys.exit(app.exec_()) # Tells the program to end once the GUI is closed by the user


frameWelcome()
