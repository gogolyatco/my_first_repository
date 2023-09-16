from PyQt5.QtWidgets import  QApplication, QWidget, QPushButton, QLabel
from random import randint
app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle("Визначник переможця")
my_win.move(300, 100)
my_win.resize(400, 200)
button = QPushButton(my_win)
button.setText('Згенерувати')
button.move(140, 130)
text = QLabel(my_win)
text.setText('Й хто, ж переміг?')
text.move(70, 10)

winner = QLabel(my_win)
winner.setText('?')
winner.move(190, 70)

def show_winner():
    number = randint(1, 100)
    winner.setText9(str(number))
    text.setText('Переможець')
    text.move(190,10)

button.clicked.connect(show_winner)




my_win.show()
app.exec_()

