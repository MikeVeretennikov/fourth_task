import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QTableView, QApplication, QTableWidgetItem, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect('coffee.sqlite')

        query = 'SELECT * FROM coffee'
        res = self.connection.cursor().execute(query).fetchall()



        self.table.setColumnCount(7)
        self.table.setRowCount(0)

        for i, row in enumerate(res):
            self.table.setRowCount(
                self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table.setItem(
                    i, j, QTableWidgetItem(str(elem)))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())