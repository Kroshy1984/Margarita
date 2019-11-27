#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys,random
from dic2 import * #словари и списки
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtWidgets, QtCore
class MainPicture(QWidget):#первая форма
    def __init__(self):
        super().__init__()
        self.initUI() #создать фоорму

    def initUI(self):
        lbl1 = QLabel('Здравствуйте, я игра-тест по географии', self)#первая надпись
        lbl1.move(85, 10) #размещение надписи

        lbl2 = QLabel('Для продолжения игры нажмите ДАЛЕЕ', self)# вторая надпись
        lbl2.move(75, 40)#размещение надписи

        lbl3 = QLabel('Для выхода игры нажмите НЕ ХОЧУ', self)#третья надпись
        lbl3.move(95, 70)

        qbtn = QPushButton('Не хочу', self)#заводим кнопку
        qbtn.clicked.connect(self.close)#по нажатию накнопку происходит закрытие
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(100, 300)#устанавливаем положение кнопки
        qbtn.setStyleSheet("background-color: Red")

        qbtn2 = QPushButton('Далее', self)#заводим кнопку
        qbtn2.clicked.connect(self.forward)#по нажатию накнопку происходит переход на следующую форму
        qbtn2.resize(qbtn.sizeHint())
        qbtn2.move(250, 300)#устанавливаем положение кнопки
        qbtn2.setStyleSheet("background-color: Green")
        self.setGeometry(300, 300, 450, 350)#устанавливаем размеры окна
        self.setWindowTitle('Тест по географии. Основное окно')
        self.show()
    def closeEvent(self, event):#метод закрытие окна
        reply = QMessageBox.question(self, 'Внимание!', "Действительно хотите закончить тест??", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)#окно сообщения с вопросом
        if reply == QMessageBox.Yes: #если нажимаем Yes, то выходим из окна
            event.accept()#если нажимаем NO то остаемся в окне
        else:
            event.ignore()#закрываем форму
    def forward(self,event):# переход на следующую форму
        self.x3=Picture2()
        self.hide()
    def close(self,event):# переход на следующую форму
        self.hide()

class Picture2(QWidget):#вторая форма
    def __init__(self):#вызов формы
        super().__init__()

        self.initUI()


    def initUI(self):# расположение элементов на форме
        self.setGeometry(300, 300, 450, 350)#устанавливаем размеры окна
        self.setWindowTitle('Тест по географии. Выбор уровня')
        lbl1 = QLabel('Выберете желаемый уровень', self)#первая надпись
        lbl1.move(85, 10)
        self.lbl2= QLabel('Выбор уровня')#название слоя
        self.level1=QRadioButton('1й уровень')#1-й переключатель
        self.level1.toggled.connect(self.click_on_button1)
        self.level2=QRadioButton('2й уровень')#2-й переключатель
        self.level2.toggled.connect(self.click_on_button1)
        self.level3=QRadioButton('3й уровень')#3-й переключатель
        self.level3.toggled.connect(self.click_on_button3)
        layout=QVBoxLayout()#контейнер для переключателя
        #укладываем переключатель в контейнер
        layout.addWidget(self.lbl2)#укладываем название
        layout.addWidget(self.level1)#укладываем 1й переключатель
        layout.addWidget(self.level2)#укладываем 2й переклчатель
        layout.addWidget(self.level3)#укладываем 3й переключатель
        self.setLayout(layout)# устанавливаем на форму

        qbtn3 = QPushButton('Не хочу', self)#заводим кнопку
        qbtn3.clicked.connect(self.back)#по нажатию накнопку происходит переход на предыдущую форму
        qbtn3.resize(qbtn3.sizeHint())
        qbtn3.move(100, 300)#устанавливаем положение кнопки
        qbtn3.setStyleSheet("background-color: Red")

        self.qbtn4 = QPushButton('Далее',self)#заводим кнопку
        self.qbtn4.resize(self.qbtn4.sizeHint())
        self.qbtn4.move(250, 300)#устанавливаем положение кнопки
        self.qbtn4.setStyleSheet("background-color: Green")
        self.qbtn4.setEnabled(False)#Кнопка изначально неактивна

        #if self.level1.isChecked(): qbtn4.setEnabled(True)

        self.show()
    def closeEvent(self, event):#окно закрытия 2й формы
        reply = QMessageBox.question(self, 'Внимание', "Форма закроется. Вы правда этого хотите?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes: #если нажимаем Yes, то выходим из окна
             event.accept()#если нажимаем NO то остаемся в окне
        else:
             event.ignore()
    def back(self,event):# возвращение назад
             self.x3=MainPicture()
    def forward (self,event):# продвиждение вперед
             self.x3=Picture3()
             self.hide()
    def click_on_button1(self):
        self.qbtn4.setEnabled(True)
        self.qbtn4.clicked.connect(self.forward)#по нажатию накнопку происходит переход на следующую форму
    def click_on_button3(self):
        self.qbtn4.setEnabled(True)
class Picture3(QWidget): #вызов третьей формы

    def __init__(self):# инициация третьей формы
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(300, 300, 450, 350)#устанавливаем размеры окна
        self.setWindowTitle('Тестрование')#название окна
        n=random.randint(0,199)#случайный выбор страны из списка стран от 0 до 199
        question= countries[n]+' какую имеет столицу?'#формируем вопрос
        lbl1 = QLabel(question, self)#первая надпись
        lbl1.move(85, 50)
        qbtn4 = QPushButton('Далее',self)#заводим кнопку
        #qbtn4.clicked.connect(self.forward)#по нажатию накнопку происходит переход на следующую форму
        qbtn4.resize(qbtn4.sizeHint())
        qbtn4.move(250, 300)#устанавливаем положение кнопки
        qbtn4.setStyleSheet("background-color: Green")
        qbtn4.setEnabled(True)#Делаем кнопку не активной
        self.answer=CorrectDir[countries[n]]#это правильный ответ из словаря
        lbl2 = QLabel(self.answer, self)#первая надпись
        lbl2.move(95, 60)
        nint2=random.randint(0,3)
        key={}#заводим пустой словарь для того чтобы разместить в нем варианты ответов
        key[nint2]=CorrectDir[countries[n]]#присваиваем случайному элементу правильное значение
        k=0#счетчик для цикла
        #формируем ответы на кнопках. Формируем словарь с вариантами ответов, один из которых правильный
        while k<4:
            k+=1
            if k!=nint2:
                while True:
                    nint=random.randint(0,9)
                    if CorrectDir[countries[nint]] not in key.values():
                        key[k]=CorrectDir[countries[nint]]
                        break
        qbtn5=QPushButton(key[1],self) #первая кнопка
        self.y1=key[1]
        qbtn5.move(100, 150)#устанавливаем положение кнопки
        qbtn5.clicked.connect(self.On_Click1)#говорим, что при нажатии кнопки будет вызываться метод On_Click
        qbtn5.setStyleSheet("background-color: Blue")
        qbtn6=QPushButton(key[2],self) #вторая кнопка
        qbtn6.move(250, 150)#устанавливаем положение кнопки
        qbtn6.setStyleSheet("background-color: Blue")
        qbtn4.clicked.connect(self.On_Click1)
        qbtn7=QPushButton(key[3],self)#третья кнопка
        qbtn7.move(100, 200)#устанавливаем положение кнопки
        qbtn7.setStyleSheet("background-color: Blue")
        qbtn4.clicked.connect(self.On_Click1)
        qbtn8=QPushButton(key[4],self)#четвертая кнопка
        qbtn8.move(250, 200)#устанавливаем положение кнопки
        qbtn8.setStyleSheet("background-color: Blue")
        qbtn4.clicked.connect(self.On_Click1)
        qbtn3 = QPushButton('Не хочу', self)#заводим кнопку
        qbtn3.clicked.connect(self.back)#по нажатию накнопку происходит переход на предыдущую форму
        qbtn3.resize(qbtn3.sizeHint())
        qbtn3.move(100, 300)#устанавливаем положение кнопки
        qbtn3.setStyleSheet("background-color: Red")
        lbl4 = QLabel(str(self.q), self)
        lbl4.move(115, 70)


        self.show()
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Внимание', "Форма закроется. Вы правда этого хотите?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes: #если нажимаем Yes, то выходим из окна
            event.accept()#если нажимаем NO то остаемся в окне
        else:
            event.ignore()
    def back(self,event):
        self.x3=Picture2()
    def forward (self,event):
        self.x3=Picture3()
        self.hide()
    def On_Click1(self):
        lbl3 = QLabel(self.y1, self)
        lbl3.move(105, 70)
        if self.answer == self.y1:
            self.x3=Picture4()
            self.q+=1
        else:
            self.x3=Picture5()
class Picture4(QWidget):
    def __init__(self):# инициация третьей формы
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(300, 300, 450, 350)#устанавливаем размеры окна
        self.setWindowTitle('yes')#название окна
        self.show()
class Picture5(QWidget):
    def __init__(self):# инициация третьей формы
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(300, 300, 450, 350)#устанавливаем размеры окна
        self.setWindowTitle('no')#название окна
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainPicture()
    sys.exit(app.exec_())
