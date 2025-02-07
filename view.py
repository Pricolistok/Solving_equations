import sys
from PyQt5.Qt import *
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from PyQt5 import QtWidgets
from main import find_mas_x, createSchedule, value_func


class Error(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window_about_creator = QWidget()
        self.window_about_creator.setWindowTitle('Error')
        self.window_about_creator.resize(300, 150)
        textbox_about_creator = QLabel(self.window_about_creator)
        textbox_about_creator.setText("  Ошибка ввода")
        textbox_about_creator.move(50, 60)
        textbox_about_creator.setFont(QFont('Comfortaa', 18))
        self.window_about_creator.show()


class Creator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window_about_creator = QWidget()
        self.window_about_creator.setWindowTitle('About creator')
        self.window_about_creator.resize(400, 200)
        textbox_about_creator = QLabel(self.window_about_creator)
        textbox_about_creator.setText("Доколин Георгий ИУ7-22Б")
        textbox_about_creator.move(50, 60)
        textbox_about_creator.setFont(QFont('Comfortaa', 18))
        self.window_about_creator.show()


class Calc(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window_about_prog = QWidget()
        self.window_about_prog.setWindowTitle('About programm')
        self.window_about_prog.resize(500, 200)
        textbox_about_creator = QLabel(self.window_about_prog)
        textbox_about_creator.setText("Приложение считает корни, \nвыводит таблицу значений, "
                                      "\nстроит графики.")
        textbox_about_creator.move(2, 40)
        textbox_about_creator.setFont(QFont('Comfortaa', 18))
        self.window_about_prog.show()


class App(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.err = None
        self.prog_inf = None
        self.creator_inform = None
        self.vtable = None
        self.window_table = None
        self.answer = ''
        self.window = QWidget()
        self.window.setWindowTitle('Calculator')
        type_font = 'Comfortaa'
        font_size = 18

        self.grid = QGridLayout(self.window)

        self.menubar = QMenuBar()
        inform = self.menubar.addMenu('INFO')
        inform.addAction('About creator').triggered.connect(self.about_creator_func)
        inform.addAction('About programm').triggered.connect(self.about_prog_func)
        self.grid.addWidget(self.menubar, 0, 8)

        self.txtMathFunc = QLabel()
        self.txtMathFunc.setText('Function')
        self.grid.addWidget(self.txtMathFunc, 0, 0)

        self.inpMathFunc = QLineEdit()
        self.inpMathFunc.setFixedSize(265, 40)
        self.inpMathFunc.setFont(QFont(type_font, font_size))
        self.grid.addWidget(self.inpMathFunc, 1, 0, 1, 4)

        self.txtStart = QLabel()
        self.txtStart.setText('Start num')
        self.grid.addWidget(self.txtStart, 2, 0)

        self.inpNumStart = QLineEdit()
        self.inpNumStart.setFixedSize(130, 40)
        self.inpNumStart.setFont(QFont(type_font, font_size))
        self.grid.addWidget(self.inpNumStart, 3, 0, 3, 2)

        self.txtFinish = QLabel()
        self.txtFinish.setText('Finish num')
        self.grid.addWidget(self.txtFinish, 2, 2)

        self.inpNumFinish = QLineEdit()
        self.inpNumFinish.setFixedSize(130, 40)
        self.inpNumFinish.setFont(QFont(type_font, font_size))
        self.grid.addWidget(self.inpNumFinish, 3, 2, 3, 4)

        self.txtNumStepH = QLabel()
        self.txtNumStepH.setText('Step')
        self.grid.addWidget(self.txtNumStepH, 0, 5)

        self.inpStepH = QLineEdit()
        self.inpStepH.setFixedSize(265, 40)
        self.inpStepH.setFont(QFont(type_font, font_size))
        self.grid.addWidget(self.inpStepH, 1, 5, 1, 9)

        self.txtMaxIter = QLabel()
        self.txtMaxIter.setText('Maximum iterations')
        self.grid.addWidget(self.txtMaxIter, 2, 5)

        self.inpMaxIter = QLineEdit()
        self.inpMaxIter.setFixedSize(265, 40)
        self.inpMaxIter.setFont(QFont(type_font, font_size))
        self.grid.addWidget(self.inpMaxIter, 3, 5, 3, 9)

        self.txtEpsilon = QLabel()
        self.txtEpsilon.setText('Epsilon')
        self.grid.addWidget(self.txtEpsilon, 6, 0)

        self.inpEpsilon = QLineEdit()
        self.inpEpsilon.setFixedSize(265, 40)
        self.inpEpsilon.setFont(QFont(type_font, font_size))
        self.grid.addWidget(self.inpEpsilon, 7, 0, 7, 4)

        self.btnEnter = QPushButton('Enter')
        self.btnEnter.setFixedSize(265, 40)
        self.btnEnter.setFont(QFont(type_font, font_size))
        self.grid.addWidget(self.btnEnter, 7, 5, 7, 9)
        self.btnEnter.clicked.connect(self.funcEnter)
        self.window.show()

    def funcEnter(self):
        try:
            value_func(self.inpMathFunc.text(), int(self.inpNumStart.text()))
            res_arr = find_mas_x(math_func=self.inpMathFunc.text(),
                                 start=float(self.inpNumStart.text()),
                                 finish=float(self.inpNumFinish.text()),
                                 step=float(self.inpStepH.text()),
                                 epsilon=float(self.inpEpsilon.text()),
                                 maximum_iter=int(self.inpMaxIter.text()))
            if res_arr == 'Error':
                self.err = Error()
            else:
                self.new_window(res_arr)
            res = createSchedule(math_func=self.inpMathFunc.text(),
                           start=float(self.inpNumStart.text()),
                           finish=float(self.inpNumFinish.text()),
                           step=float(self.inpStepH.text()),
                           res_arr=res_arr)
            if res == 'Error':
                self.err = Error()
        except ValueError:
            self.err = Error()

    def new_window(self, res_arr):
        self.window_table = QWidget()
        self.window_table.setWindowTitle('Calculator')
        self.vtable = QtWidgets.QTableWidget(self.window_table)
        self.vtable.setFixedSize(1400, 600)
        self.vtable.setColumnCount(4)
        self.vtable.setColumnWidth(0, 500)
        self.vtable.setColumnWidth(1, 300)
        self.vtable.setColumnWidth(2, 300)
        self.vtable.setColumnWidth(3, 300)
        self.vtable.setHorizontalHeaderLabels(['X(i) : X(i+1)', 'X', 'f(x)', 'Iterations', 'Code error'])
        self.vtable.setRowCount(len(res_arr))
        for i in range(len(res_arr)):
            for j in range(4):
                item = str(res_arr[i][0][j])
                self.vtable.setItem(i, j, QTableWidgetItem(item))
        self.window_table.show()

    def about_creator_func(self):
        self.creator_inform = Creator()

    def about_prog_func(self):
        self.prog_inf = Calc()


def main():
    # Create app and window
    app = QApplication([])
    ex = App()
    ex.setStyle(QStyleFactory.create('CDEstyle'))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
