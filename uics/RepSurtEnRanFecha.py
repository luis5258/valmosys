# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RepSurtEnRanFecha.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MovimientosSurtido(object):
    def setupUi(self, MovimientosSurtido):
        MovimientosSurtido.setObjectName("MovimientosSurtido")
        MovimientosSurtido.resize(918, 707)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(MovimientosSurtido.sizePolicy().hasHeightForWidth())
        MovimientosSurtido.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        MovimientosSurtido.setFont(font)
        self.label = QtWidgets.QLabel(MovimientosSurtido)
        self.label.setGeometry(QtCore.QRect(861, -459, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ClienteCBox = QtWidgets.QComboBox(MovimientosSurtido)
        self.ClienteCBox.setGeometry(QtCore.QRect(90, 20, 371, 22))
        self.ClienteCBox.setObjectName("ClienteCBox")
        self.ClienteLbl = QtWidgets.QLabel(MovimientosSurtido)
        self.ClienteLbl.setGeometry(QtCore.QRect(20, 10, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ClienteLbl.setFont(font)
        self.ClienteLbl.setObjectName("ClienteLbl")
        self.PBCerrar = QtWidgets.QPushButton(MovimientosSurtido)
        self.PBCerrar.setGeometry(QtCore.QRect(300, 660, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PBCerrar.setFont(font)
        self.PBCerrar.setObjectName("PBCerrar")
        self.PBToExcel = QtWidgets.QPushButton(MovimientosSurtido)
        self.PBToExcel.setGeometry(QtCore.QRect(140, 660, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PBToExcel.setFont(font)
        self.PBToExcel.setObjectName("PBToExcel")
        self.PBHacer = QtWidgets.QPushButton(MovimientosSurtido)
        self.PBHacer.setGeometry(QtCore.QRect(10, 660, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PBHacer.setFont(font)
        self.PBHacer.setObjectName("PBHacer")
        self.Tabla = QtWidgets.QTableWidget(MovimientosSurtido)
        self.Tabla.setGeometry(QtCore.QRect(10, 150, 891, 501))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.Tabla.sizePolicy().hasHeightForWidth())
        self.Tabla.setSizePolicy(sizePolicy)
        self.Tabla.setSizeIncrement(QtCore.QSize(10, 10))
        self.Tabla.setObjectName("Tabla")
        self.Tabla.setColumnCount(10)
        self.Tabla.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla.setHorizontalHeaderItem(9, item)
        self.groupBox = QtWidgets.QGroupBox(MovimientosSurtido)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 401, 81))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.FechaFinalLbl_2 = QtWidgets.QLabel(self.groupBox)
        self.FechaFinalLbl_2.setGeometry(QtCore.QRect(20, 30, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FechaFinalLbl_2.setFont(font)
        self.FechaFinalLbl_2.setObjectName("FechaFinalLbl_2")
        self.FechaInicSel = QtWidgets.QDateEdit(self.groupBox)
        self.FechaInicSel.setGeometry(QtCore.QRect(80, 30, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.FechaInicSel.setFont(font)
        self.FechaInicSel.setMaximumDate(QtCore.QDate(2050, 12, 31))
        self.FechaInicSel.setCalendarPopup(True)
        self.FechaInicSel.setDate(QtCore.QDate(2021, 1, 1))
        self.FechaInicSel.setObjectName("FechaInicSel")
        self.FechaFinSel = QtWidgets.QDateEdit(self.groupBox)
        self.FechaFinSel.setGeometry(QtCore.QRect(270, 30, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.FechaFinSel.setFont(font)
        self.FechaFinSel.setMaximumDate(QtCore.QDate(2050, 12, 31))
        self.FechaFinSel.setCalendarPopup(True)
        self.FechaFinSel.setDate(QtCore.QDate(2021, 1, 1))
        self.FechaFinSel.setObjectName("FechaFinSel")
        self.FechaFinalLbl = QtWidgets.QLabel(self.groupBox)
        self.FechaFinalLbl.setGeometry(QtCore.QRect(210, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FechaFinalLbl.setFont(font)
        self.FechaFinalLbl.setObjectName("FechaFinalLbl")
        self.groupBox_2 = QtWidgets.QGroupBox(MovimientosSurtido)
        self.groupBox_2.setGeometry(QtCore.QRect(420, 50, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.RBotTodos = QtWidgets.QRadioButton(self.groupBox_2)
        self.RBotTodos.setGeometry(QtCore.QRect(20, 30, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.RBotTodos.setFont(font)
        self.RBotTodos.setChecked(True)
        self.RBotTodos.setObjectName("RBotTodos")
        self.RBotPorClien = QtWidgets.QRadioButton(self.groupBox_2)
        self.RBotPorClien.setGeometry(QtCore.QRect(100, 30, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.RBotPorClien.setFont(font)
        self.RBotPorClien.setObjectName("RBotPorClien")

        self.retranslateUi(MovimientosSurtido)
        QtCore.QMetaObject.connectSlotsByName(MovimientosSurtido)

    def retranslateUi(self, MovimientosSurtido):
        _translate = QtCore.QCoreApplication.translate
        MovimientosSurtido.setWindowTitle(_translate("MovimientosSurtido", "Resume de Surtidos"))
        self.label.setText(_translate("MovimientosSurtido", "Fecha Inicial:"))
        self.ClienteLbl.setText(_translate("MovimientosSurtido", "Cliente:"))
        self.PBCerrar.setText(_translate("MovimientosSurtido", "Cerrar"))
        self.PBToExcel.setText(_translate("MovimientosSurtido", "Bajar a Exel"))
        self.PBHacer.setText(_translate("MovimientosSurtido", "Hacer"))
        item = self.Tabla.horizontalHeaderItem(0)
        item.setText(_translate("MovimientosSurtido", "Folio"))
        item = self.Tabla.horizontalHeaderItem(1)
        item.setText(_translate("MovimientosSurtido", "No.Orden"))
        item = self.Tabla.horizontalHeaderItem(2)
        item.setText(_translate("MovimientosSurtido", "Cliente"))
        item = self.Tabla.horizontalHeaderItem(3)
        item.setText(_translate("MovimientosSurtido", "Producto"))
        item = self.Tabla.horizontalHeaderItem(4)
        item.setText(_translate("MovimientosSurtido", "Corral"))
        item = self.Tabla.horizontalHeaderItem(5)
        item.setText(_translate("MovimientosSurtido", "Cant Solicitada"))
        item = self.Tabla.horizontalHeaderItem(6)
        item.setText(_translate("MovimientosSurtido", "CantSurtida"))
        item = self.Tabla.horizontalHeaderItem(7)
        item.setText(_translate("MovimientosSurtido", "Fecha Sol"))
        item = self.Tabla.horizontalHeaderItem(8)
        item.setText(_translate("MovimientosSurtido", "Fecha Surtido"))
        self.groupBox.setTitle(_translate("MovimientosSurtido", "Fechas:"))
        self.FechaFinalLbl_2.setText(_translate("MovimientosSurtido", "Inicial:"))
        self.FechaFinalLbl.setText(_translate("MovimientosSurtido", " Final:"))
        self.groupBox_2.setTitle(_translate("MovimientosSurtido", "Filtro:"))
        self.RBotTodos.setText(_translate("MovimientosSurtido", "Todos"))
        self.RBotPorClien.setText(_translate("MovimientosSurtido", "Por Cliente:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MovimientosSurtido = QtWidgets.QDialog()
    ui = Ui_MovimientosSurtido()
    ui.setupUi(MovimientosSurtido)
    MovimientosSurtido.show()
    sys.exit(app.exec_())
