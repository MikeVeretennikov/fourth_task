import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QTableView, QApplication, QTableWidgetItem, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('main.ui', self)
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('coffee.sqlite')
        self.db.open()

        self.view = QTableView(self)

        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('coffee')
        self.model.select()

        self.view.setModel(self.model)
        self.view.move(150, 100)
        self.view.resize(700, 500)

        self.view.show()
        self.add_edit.clicked.connect(self.addedit)
        self.connection = sqlite3.connect('coffee.sqlite')


    def addedit(self):
        self.form = AddEdit()
        self.form.show()




class AddEdit(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.connection = sqlite3.connect('coffee.sqlite')
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.submit.clicked.connect(self.add)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('coffee.sqlite')
        self.db.open()

        self.view = QTableView(self)

        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('coffee')
        self.model.select()

        self.view.setModel(self.model)
        self.view.move(50, 100)
        self.view.resize(550, 200)

        self.view.show()




    def add(self):
        name = self.name.text()
        degree = self.degree.text()
        condition = self.condition.text()
        desc = self.description.text()
        price = self.price.text()
        volume = self.volume.text()
        query = '''INSERT INTO coffee(name,degree,condition,description,price,volume) VALUES (?,?,?,?,?,?)'''

        self.connection.cursor().execute(query, (name,degree,condition,desc,price,volume,))
        self.connection.commit()
        self.statusBar().showMessage('Успешно добавлено')
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('coffee')
        self.model.select()

        self.view.setModel(self.model)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())