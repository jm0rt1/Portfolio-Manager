from pathlib import Path
from typing import Optional
from src.GUI.ui_base import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets

import src.parser as parser
import src.analyzer as analyzer


class UI(Ui_MainWindow):
    def __init__(self) -> None:
        self.model = Model()
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.pushButton.clicked.connect(self.get_file)

    def get_file(self):
        path = QFileDialog.getOpenFileName()
        path = Path(path[0])
        path_str = str(path)
        self.textBrowser.setText(path_str)
        self.model.set_csv_path(path)

        self.populate_table()

    def populate_table(self):
        p = parser.Parser(self.model.csv_path)
        a = analyzer.Analyzer(p.portfolio_data)
        result = a.analyze()
        for i, row in enumerate(result.iterrows()):
            val = str(result.iloc[i, 0])
            symbol_item = QtWidgets.QTableWidgetItem()
            symbol_item.setText(val)
            self.tableWidget.setItem(i, 0, symbol_item)
            pass

        pass


class Model():
    def __init__(self):
        self._csv_path: Optional[Path] = None

    def set_csv_path(self, csv_path: Path):
        self._csv_path = csv_path

    @property
    def csv_path(self):
        if self._csv_path is not None:
            return self._csv_path
        else:
            raise AttributeError("csv_path is not initialized")
