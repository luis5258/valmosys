# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RepMovAnimalesResPorCorr.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RepAnimaCorrClien(object):
    def setupUi(self, RepAnimaCorrClien):
        RepAnimaCorrClien.setObjectName("RepAnimaCorrClien")
        RepAnimaCorrClien.resize(755, 708)
        self.ClienteLbl = QtWidgets.QLabel(RepAnimaCorrClien)
        self.ClienteLbl.setGeometry(QtCore.QRect(14, 21, 54, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ClienteLbl.setFont(font)
        self.ClienteLbl.setObjectName("ClienteLbl")
        self.ClienteCBox = QtWidgets.QComboBox(RepAnimaCorrClien)
        self.ClienteCBox.setGeometry(QtCore.QRect(90, 20, 361, 20))
        self.ClienteCBox.setObjectName("ClienteCBox")
        self.FechaFinSel = QtWidgets.QDateEdit(RepAnimaCorrClien)
        self.FechaFinSel.setGeometry(QtCore.QRect(340, 50, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.FechaFinSel.setFont(font)
        self.FechaFinSel.setMaximumDate(QtCore.QDate(2050, 12, 31))
        self.FechaFinSel.setCalendarPopup(True)
        self.FechaFinSel.setDate(QtCore.QDate(2021, 1, 1))
        self.FechaFinSel.setObjectName("FechaFinSel")
        self.FechaFinalLbl = QtWidgets.QLabel(RepAnimaCorrClien)
        self.FechaFinalLbl.setGeometry(QtCore.QRect(240, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FechaFinalLbl.setFont(font)
        self.FechaFinalLbl.setObjectName("FechaFinalLbl")
        self.PBHacer = QtWidgets.QPushButton(RepAnimaCorrClien)
        self.PBHacer.setGeometry(QtCore.QRect(50, 650, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PBHacer.setFont(font)
        self.PBHacer.setObjectName("PBHacer")
        self.PBExcel = QtWidgets.QPushButton(RepAnimaCorrClien)
        self.PBExcel.setGeometry(QtCore.QRect(170, 650, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PBExcel.setFont(font)
        self.PBExcel.setObjectName("PBExcel")
        self.PBCerrar = QtWidgets.QPushButton(RepAnimaCorrClien)
        self.PBCerrar.setGeometry(QtCore.QRect(320, 650, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PBCerrar.setFont(font)
        self.PBCerrar.setObjectName("PBCerrar")
        self.Tabla = QtWidgets.QTableWidget(RepAnimaCorrClien)
        self.Tabla.setGeometry(QtCore.QRect(30, 140, 671, 491))
        self.Tabla.setObjectName("Tabla")
        self.Tabla.setColumnCount(7)
        self.Tabla.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.Tabla.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.Tabla.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.Tabla.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.Tabla.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.Tabla.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.Tabla.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla.setHorizontalHeaderItem(6, item)
        self.BanLbl_2 = QtWidgets.QLabel(RepAnimaCorrClien)
        self.BanLbl_2.setGeometry(QtCore.QRect(100, 90, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.BanLbl_2.setFont(font)
        self.BanLbl_2.setAlignment(QtCore.Qt.AlignCenter)
        self.BanLbl_2.setObjectName("BanLbl_2")
        self.FechaInicSel = QtWidgets.QDateEdit(RepAnimaCorrClien)
        self.FechaInicSel.setGeometry(QtCore.QRect(110, 51, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.FechaInicSel.setFont(font)
        self.FechaInicSel.setMaximumDate(QtCore.QDate(2050, 12, 31))
        self.FechaInicSel.setCalendarPopup(True)
        self.FechaInicSel.setDate(QtCore.QDate(2021, 1, 1))
        self.FechaInicSel.setObjectName("FechaInicSel")
        self.FechaIniLbl = QtWidgets.QLabel(RepAnimaCorrClien)
        self.FechaIniLbl.setGeometry(QtCore.QRect(10, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FechaIniLbl.setFont(font)
        self.FechaIniLbl.setObjectName("FechaIniLbl")
        self.groupBox_2 = QtWidgets.QGroupBox(RepAnimaCorrClien)
        self.groupBox_2.setGeometry(QtCore.QRect(500, 20, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.RBotTodos = QtWidgets.QRadioButton(self.groupBox_2)
        self.RBotTodos.setGeometry(QtCore.QRect(20, 30, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.RBotTodos.setFont(font)
        self.RBotTodos.setChecked(False)
        self.RBotTodos.setObjectName("RBotTodos")
        self.RBotPorCliente = QtWidgets.QRadioButton(self.groupBox_2)
        self.RBotPorCliente.setGeometry(QtCore.QRect(100, 30, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.RBotPorCliente.setFont(font)
        self.RBotPorCliente.setChecked(True)
        self.RBotPorCliente.setObjectName("RBotPorCliente")

        self.retranslateUi(RepAnimaCorrClien)
        QtCore.QMetaObject.connectSlotsByName(RepAnimaCorrClien)

    def retranslateUi(self, RepAnimaCorrClien):
        _translate = QtCore.QCoreApplication.translate
        RepAnimaCorrClien.setWindowTitle(_translate("RepAnimaCorrClien", "Reporte   Animales en Corral por Cliente"))
        self.ClienteLbl.setText(_translate("RepAnimaCorrClien", "Cliente:"))
        self.FechaFinalLbl.setText(_translate("RepAnimaCorrClien", "Fecha Final:"))
        self.PBHacer.setText(_translate("RepAnimaCorrClien", "Hacer"))
        self.PBExcel.setText(_translate("RepAnimaCorrClien", "Bajar a Excel"))
        self.PBCerrar.setText(_translate("RepAnimaCorrClien", "Cerrar"))
        item = self.Tabla.horizontalHeaderItem(0)
        item.setText(_translate("RepAnimaCorrClien", "Cliente"))
        item = self.Tabla.horizontalHeaderItem(1)
        item.setText(_translate("RepAnimaCorrClien", "Corral"))
        item = self.Tabla.horizontalHeaderItem(2)
        item.setText(_translate("RepAnimaCorrClien", "Cant. Inical"))
        item = self.Tabla.horizontalHeaderItem(3)
        item.setText(_translate("RepAnimaCorrClien", "Tot Entradas"))
        item = self.Tabla.horizontalHeaderItem(4)
        item.setText(_translate("RepAnimaCorrClien", "TotSalidas"))
        item = self.Tabla.horizontalHeaderItem(5)
        item.setText(_translate("RepAnimaCorrClien", "Cant.Actual"))
        self.BanLbl_2.setText(_translate("RepAnimaCorrClien", "Reporte Resumen  Corral por Cliente"))
        self.FechaIniLbl.setText(_translate("RepAnimaCorrClien", "Fecha Inicial:"))
        self.groupBox_2.setTitle(_translate("RepAnimaCorrClien", "Filtro:"))
        self.RBotTodos.setText(_translate("RepAnimaCorrClien", "Todos"))
        self.RBotPorCliente.setText(_translate("RepAnimaCorrClien", "Por Cliente"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RepAnimaCorrClien = QtWidgets.QDialog()
    ui = Ui_RepAnimaCorrClien()
    ui.setupUi(RepAnimaCorrClien)
    RepAnimaCorrClien.show()
    sys.exit(app.exec_())
