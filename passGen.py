from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton
from random import shuffle

def check():
    global login, lock
    login = logLine.text()
    lock = passLine.text()
    if login in logins:
        if not logins[login].somelock == lock:
            errTitle.setText('Неправильный логин или пароль!')
        else:
            showpass()
    else:
        shuffle(shifr1)
        logins[login] = Users(lock, shifr1)

        file = open('UsersDict.txt', 'a')
        strshifr = ''
        for i in logins[login].someshifr:
            strshifr = strshifr + i + ' '
        file.write(login + '   ')
        addlist = str(logins[login].somelock) + '   ' +  strshifr + '\n'
        file.write(addlist)
        file.close()

        showpass()

def generation():
    webName = nameLine.text()
    alph = 'abcdefghijklmnopqrstuvwxyz1234567890.-'
    webName.lower()
    password = ''
    for i in webName:
        ind = alph.find(i)
        password += logins[login].someshifr[ind]
    passwLine.setText(password)

def LOGwindow():
    global logLine, passLine, errTitle

    logWin = QWidget()
    logWin.setWindowTitle('Password Generator')
    logWin.setFixedSize(400, 200)

    title = QLabel('Добро пожаловать! Введите свой логин и пароль!')
    logtitle = QLabel('Логин:')
    passtitle = QLabel('Пароль:')
    errTitle = QLabel('')

    logLine = QLineEdit('')

    passLine = QLineEdit('')

    enterButton = QPushButton('Вход')
    enterButton.clicked.connect(check)
    
    h_line1 = QHBoxLayout()
    h_line1.addWidget(logtitle, alignment = Qt.AlignRight)
    h_line1.addWidget(logLine, alignment = Qt.AlignLeft)

    h_line2 = QHBoxLayout()
    h_line2.addWidget(passtitle, alignment = Qt.AlignRight)
    h_line2.addWidget(passLine, alignment = Qt.AlignLeft)

    v_line = QVBoxLayout()
    v_line.addWidget(title, alignment = Qt.AlignCenter)
    v_line.addLayout(h_line1)
    v_line.addLayout(h_line2)
    v_line.addWidget(enterButton, alignment = Qt.AlignCenter)
    v_line.addWidget(errTitle, alignment = Qt.AlignCenter)

    logWin.setLayout(v_line)

    return logWin

def showpass():
    passLine.clear()
    errTitle.setText('')
    logWin.hide()
    passWin.show()

def showlog():
    logLine.clear()
    passwLine.clear()
    passWin.hide()
    logWin.show()
    nameLine.clear()

def PASSwindow():
    global nameLine, passwLine

    passWin = QWidget()
    passWin.setWindowTitle('Password Generator')
    passWin.setFixedSize(800, 400)

    title = QLabel('Введите имя сайта:')
    passTitle = QLabel('Пароль:')

    nameLine = QLineEdit()

    passwLine = QLineEdit()
    passwLine.setReadOnly(True)

    generButton = QPushButton('Пароль')
    generButton.clicked.connect(generation)

    exitButton = QPushButton('Выход')
    exitButton.clicked.connect(showlog)

    h_line1 = QHBoxLayout()
    h_line1.addWidget(title, alignment = Qt.AlignRight)
    h_line1.addWidget(nameLine, alignment = Qt.AlignLeft)

    h_line2 = QHBoxLayout()
    h_line2.addWidget(exitButton, alignment = Qt.AlignCenter)

    v_line = QVBoxLayout()
    v_line.addLayout(h_line1)
    v_line.addWidget(generButton, alignment = Qt.AlignCenter)
    v_line.addWidget(passTitle, alignment = Qt.AlignCenter)
    v_line.addWidget(passwLine, alignment = Qt.AlignTop)
    v_line.addLayout(h_line2)

    passWin.setLayout(v_line)

    return passWin

class Users():
    def __init__(self, lock, shifr):
        self.somelock = lock
        self.someshifr = shifr

app = QApplication([])

shifr1 = ['1q','2a', 'zxc', '4x', '5c','V8', '7b', '8n', '9m','_l', 
         '1p', '2o', 'I3', 'u_', '5y', '6t', '7r', '8e', '9w', '0s',
         '1d', '2f', '3g', '4h', '5j', '6k', '_7', '8A', 'Q_', 'G1',
         'LOL', '4F', '5j', '6z', '7p', '8I', '9t', 'QbZ']

logins = dict()
file = open(r"C:\Users\Sergio-MSI\Desktop\Password Generator\UsersDict.txt", 'r', encoding='UTF-8')
getalllines = file.readlines()
for item in getalllines:
    datalist = item.split('   ')
    datalist[2] = datalist[2].split()
    logins[datalist[0]] = Users(datalist[1], datalist[2])
file.close()

logWin = LOGwindow()
passWin = PASSwindow()
logWin.show()


app.exec_()