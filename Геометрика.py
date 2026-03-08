from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QHBoxLayout, QVBoxLayout, QLineEdit
from PyQt5.QtGui import QFont, QPixmap
from random import randint





'''Дефы'''
def next_bnt_cliced():
    global next_question
    global last_questions
    global question
    global text1
    global all_questions
    global g
    global question_p1

    for j in all_questions:
        if j in last_questions:
            g += 1

    if g != len(question_p1):
        next_btn.hide()
        answer_plase.show()
        answer_btn.show()

        answer_plase.clear()

        next_question = randint(0, len(question_p1) - 1)

        if not(next_question in last_questions):
            question = next_question

            show_image()

            last_questions.append(next_question)

        else:
            next_bnt_cliced()

        text1.setText(question_p1[question])

    else:
        next_btn.hide()
        answer_plase.hide()
        answer_btn.hide()

        text1.setText(f"Правильных ответов: {len(right_answer)} из {len(last_questions)},\nНеправильных ответов: {len(wrong_answer)} из {len(last_questions)}")

def answer_btn_cliced():
    global question
    global right_answer
    global wrong_answer
    global answer_p1
    global question_p1

    if answer_plase.text() != '':
        if answer_plase.text() == answer_p1[question]:
            answer_btn.hide()
            answer_plase.hide()
            next_btn.show()

            text1.setText("Правильно!")

            right_answer.append(question)

        else:
            answer_btn.hide()
            answer_plase.hide()
            next_btn.show()

            text1.setText("Неправильно!")

            wrong_answer.append(question)


    else:
        window_error("Поле не может быть пустым")

def window_error(text_error):
    win = QMessageBox()
    win.setText(text_error)
    win.setWindowTitle("Alarm sistem")
    win.exec_()

def show_image():
    global question

    filename = "Задача" + str(question) + ".png"

    pixmapimage = QPixmap(filename)
    label_width, label_hight = lb_image.width(), lb_image.height()
    scaled_pixmap = pixmapimage.scaled(label_width, label_hight, Qt.KeepAspectRatio)
    lb_image.setPixmap(scaled_pixmap)
    lb_image.setVisible(True)





'''Окно_часть1'''
app = QApplication([])

window = QWidget()
window.setWindowTitle("Геометрика")

next_question = None

question = None
last_questions = []

right_answer = []
wrong_answer = []





'''Задачи'''
q1 = open("Задачи§1.txt", "r", encoding='UTF-8')
question_p1 = q1.read().split("(*)")

a1 = open("Ответы§1.txt", "r", encoding='UTF-8')
answer_p1 = a1.read().split("\n")

lb_image = QLabel("Картинка")





'''Настройи'''
all_questions = []
q = 0
g = -1

for i in question_p1:
    all_questions.append(q)
    q += 1





'''Тексты'''
text1 = QLabel("")
text1.setStyleSheet("color:'green'")
font = QFont("Intro", 12)
text1.setFont(font)

# lb_image = QLabel("Картинка")





'''Лаяуты'''
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col3 = QVBoxLayout()

# row1 = QHBoxLayout()
# row2 = QHBoxLayout()
# row3 = QHBoxLayout()

Hlayout1 = QHBoxLayout()





'''Поле для ответа'''
answer_plase = QLineEdit(' ')
answer_plase.setPlaceholderText('Ответ в градусах...')
answer_plase.setFont(font)
answer_plase.setStyleSheet("color:'red'")





'''Кнопки'''
next_btn = QPushButton("Дальше")
next_btn.setFont(font)
next_btn.setStyleSheet("color:'blue'")
answer_btn = QPushButton("Ответить")
answer_btn.setFont(font)
answer_btn.setStyleSheet("color:'blue'")





'''Привязка к лаяутам'''
Hlayout1.addLayout(col1)
Hlayout1.addLayout(col2)
Hlayout1.addLayout(col3)

# col2.addLayout(row1)
# col2.addLayout(row2)
# col2.addLayout(row3)

col2.addWidget(text1, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

col2.addWidget(lb_image, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

# col2.addWidget(lb_image, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

col2.addWidget(answer_plase)
col2.addWidget(answer_btn)

col2.addWidget(next_btn)





'''Подключение кнопок'''
next_btn.clicked.connect(next_bnt_cliced)
answer_btn.clicked.connect(answer_btn_cliced)





'''Окно_часть2'''
next_btn.hide()

next_bnt_cliced()

window.setLayout(Hlayout1)
window.resize(800, 600)
window.show()
app.exec_()
