# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RepMovAnimaResumen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RepMovAnimaResumen(object):
    def setupUi(self, RepMovAnimaResumen):
        RepMovAnimaResumen.setObjectName("RepMovAnimaResumen")
        RepMovAnimaResumen.resize(843, 709)
        self.ClienteLbl = QtWidgets.QLabel(RepMovAnimaResumen)
        self.ClienteLbl.setGeometry(QtCore.QRect(14, 21, 91, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ClienteLbl.setFont(font)
        self.ClienteLbl.setObjectName("ClienteLbl")
        self.ClienteCBox = QtWidgets.QComboBox(RepMovAnimaResumen)
        self.ClienteCBox.setGeometry(QtCore.QRect(120, 20, 361, 20))
        self.ClienteCBox.setObjectName("ClienteCBox")
        self.FechaFinSel = QtWidgets.QDateEdit(RepMovAnimaResumen)
        self.FechaFinSel.setGeometry(QtCore.QRect(130, 60, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.FechaFinSel.setFont(font)
        self.FechaFinSel.setMaximumDate(QtCore.QDate(2050, 12, 31))
        self.FechaFinSel.setCalendarPopup(True)
        self.FechaFinSel.setDate(QtCore.QDate(2021, 1, 1))
        self.FechaFinSel.setObjectName("FechaFinSel")
        self.FechaFinalLbl = QtWidgets.QLabel(RepMovAnimaResumen)
        self.FechaFinalLbl.setGeometry(QtCore.QRect(30, 60, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FechaFinalLbl.setFont(font)
        self.FechaFinalLbl.setObjectName("FechaFinalLbl")
        self.PBHacer = QtWidgets.QPushButton(RepMovAnimaResumen)
        self.PBHacer.setGeometry(QtCore.QRect(40, 670, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PBHacer.setFont(font)
        self.PBHacer.setObjectName("PBHacer")
        self.PBExcel = QtWidgets.QPushButton(RepMovAnimaResumen)
        self.PBExcel.setGeometry(QtCore.QRect(160, 670, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PBExcel.setFont(font)
        self.PBExcel.setObjectName("PBExcel")
        self.PBCerrar = QtWidgets.QPushButton(RepMovAnimaResumen)
        self.PBCerrar.setGeometry(QtCore.QRect(310, 670, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PBCerrar.setFont(font)
        self.PBCerrar.setObjectName("PBCerrar")
        self.BanLbl_3 = QtWidgets.QLabel(RepMovAnimaResumen)
        self.BanLbl_3.setGeometry(QtCore.QRect(10, 100, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.BanLbl_3.setFont(font)
        self.BanLbl_3.setAlignment(QtCore.Qt.AlignCenter)
        self.BanLbl_3.setObjectName("BanLbl_3")
        self.Tabla = QtWidgets.QTableWidget(RepMovAnimaResumen)
        self.Tabla.setGeometry(QtCore.QRect(20, 140, 711, 521))
        self.Tabla.setObjectName("Tabla")
        self.Tabla.setColumnCount(6)
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
        self.groupBox = QtWidgets.QGroupBox(RepMovAnimaResumen)
        self.groupBox.setGeometry(QtCore.QRect(500, 60, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.RBotTodos = QtWidgets.QRadioButton(self.groupBox)
        self.RBotTodos.setGeometry(QtCore.QRect(20, 30, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.RBotTodos.setFont(font)
        self.RBotTodos.setChecked(True)
        self.RBotTodos.setObjectName("RBotTodos")
        self.RBotCliente = QtWidgets.QRadioButton(self.groupBox)
        self.RBotCliente.setGeometry(QtCore.QRect(100, 30, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.RBotCliente.setFont(font)
        self.RBotCliente.setObjectName("RBotCliente")
        self.TotalLbl = QtWidgets.QLabel(RepMovAnimaResumen)
        self.TotalLbl.setGeometry(QtCore.QRect(490, 670, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TotalLbl.setFont(font)
        self.TotalLbl.setObjectName("TotalLbl")
        self.TotalLblVal = QtWidgets.QLabel(RepMovAnimaResumen)
        self.TotalLblVal.setGeometry(QtCore.QRect(620, 670, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TotalLblVal.setFont(font)
        self.TotalLblVal.setObjectName("TotalLblVal")

        self.retranslateUi(RepMovAnimaResumen)
        QtCore.QMetaObject.connectSlotsByName(RepMovAnimaResumen)

    def retranslateUi(self, RepMovAnimaResumen):
        _translate = QtCore.QCoreApplication.translate
        RepMovAnimaResumen.setWindowTitle(_translate("RepMovAnimaResumen", "Reporte Movimiento Animales por Cliente"))
        self.ClienteLbl.setText(_translate("RepMovAnimaResumen", "Cliente:"))
        self.FechaFinalLbl.setText(_translate("RepMovAnimaResumen", "Fecha :"))
        self.PBHacer.setText(_translate("RepMovAnimaResumen", "Hacer"))
        self.PBExcel.setText(_translate("RepMovAnimaResumen", "Bajar a Excel"))
        self.PBCerrar.setText(_translate("RepMovAnimaResumen", "Cerrar"))
        self.BanLbl_3.setText(_translate("RepMovAnimaResumen", "Totales Animales Por Corral "))
        item = self.Tabla.horizontalHeaderItem(0)
        item.setText(_translate("RepMovAnimaResumen", "Corral/Cliente"))
        item = self.Tabla.horizontalHeaderItem(1)
        item.setText(_translate("RepMovAnimaResumen", "Fecha Asigna"))
        item = self.Tabla.horizontalHeaderItem(2)
        item.setText(_translate("RepMovAnimaResumen", "Entradas"))
        item = self.Tabla.horizontalHeaderItem(3)
        item.setText(_translate("RepMovAnimaResumen", "Salidas"))
        item = self.Tabla.horizontalHeaderItem(4)
        item.setText(_translate("RepMovAnimaResumen", "Cant Actual"))
        self.groupBox.setTitle(_translate("RepMovAnimaResumen", "Filtro:"))
        self.RBotTodos.setText(_translate("RepMovAnimaResumen", "Todos"))
        self.RBotCliente.setText(_translate("RepMovAnimaResumen", "Detalle Cliente"))
        self.TotalLbl.setText(_translate("RepMovAnimaResumen", "Total Reporte:"))
        self.TotalLblVal.setText(_translate("RepMovAnimaResumen", "0000"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RepMovAnimaResumen = QtWidgets.QDialog()
    ui = Ui_RepMovAnimaResumen()
    ui.setupUi(RepMovAnimaResumen)
    RepMovAnimaResumen.show()
    sys.exit(app.exec_())
