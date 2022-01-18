from PyQt5 import QtCore, QtGui, QtWidgets
from src.GUI.ui_child import UI

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
