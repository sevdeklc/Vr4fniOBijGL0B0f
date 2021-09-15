import sys
import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
import pandas as pd

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()
        self.showMaximized()

        ## We read the csv file and transfer it to the 'data' variable as a list
        with open('./twitterdata.csv', newline='', encoding="utf8") as f:
            reader = csv.reader(f)
            data = list(reader)


        ## sort by date (Descending order)
        def sortingByDate(elem):
            return elem[3]
        data.sort(key=sortingByDate, reverse=True)


        ## sort by Id (Ascending order)
        """ def sortingById(elem):
            return elem[0]
        data.sort(key=sortingById)  """


        ## sort by retweet count (Ascending order)
        """ def sortingByRetweetCount(elem):
            return elem[16]
        data.sort(key=sortingByRetweetCount) """


        ## sort by likes count (Ascending order)
        """ def sortingByLikesCount(elem):
            return elem[17]
        data.sort(key=sortingByLikesCount) """


        ## sort by discussion count (Ascending order)
        """ def sortingByRepliesCount(elem):
            return elem[15]
        data.sort(key=sortingByRepliesCount) """


        ## We print the 'data' list in the interface
        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)

    

app=QtWidgets.QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()