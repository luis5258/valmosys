# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RepAlmaxProdActual.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RepAlmaxProdActual(object):
    def setupUi(self, RepAlmaxProdActual):
        RepAlmaxProdActual.setObjectName("RepAlmaxProdActual")
        RepAlmaxProdActual.resize(715, 638)
        self.FechaFinSel = QtWidgets.QDateEdit(RepAlmaxProdActual)
        self.FechaFinSel.setGeometry(QtCore.QRect(480, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.FechaFinSel.setFont(font)
        self.FechaFinSel.setMaximumDate(QtCore.QDate(2050, 12, 31))
        self.FechaFinSel.setCalendarPopup(True)
        self.FechaFinSel.setDate(QtCore.QDate(2021, 1, 1))
        self.FechaFinSel.setObjectName("FechaFinSel")
        self.FechaFinalLbl = QtWidgets.QLabel(RepAlmaxProdActual)
        self.FechaFinalLbl.setGeometry(QtCore.QRect(400, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FechaFinalLbl.setFont(font)
        self.FechaFinalLbl.setObjectName("FechaFinalLbl")
        self.PBHacer = QtWidgets.QPushButton(RepAlmaxProdActual)
        self.PBHacer.setGeometry(QtCore.QRect(10, 600, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PBHacer.setFont(font)
        self.PBHacer.setObjectName("PBHacer")
        self.PBExcel = QtWidgets.QPushButton(RepAlmaxProdActual)
        self.PBExcel.setGeometry(QtCore.QRect(130, 600, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PBExcel.setFont(font)
        self.PBExcel.setObjectName("PBExcel")
        self.PBCerrar = QtWidgets.QPushButton(RepAlmaxProdActual)
        self.PBCerrar.setGeometry(QtCore.QRect(280, 600, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PBCerrar.setFont(font)
        self.PBCerrar.setObjectName("PBCerrar")
        self.Tabla = QtWidgets.QTableWidget(RepAlmaxProdActual)
        self.Tabla.setGeometry(QtCore.QRect(10, 60, 691, 531))
        self.Tabla.setObjectName("Tabla")
        self.Tabla.setColumnCount(7)
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
        self.ProductoCBox = QtWidgets.QComboBox(RepAlmaxProdActual)
        self.ProductoCBox.setGeometry(QtCore.QRect(90, 20, 301, 20))
        self.ProductoCBox.setObjectName("ProductoCBox")
        self.ProdLbl = QtWidgets.QLabel(RepAlmaxProdActual)
        self.ProdLbl.setGeometry(QtCore.QRect(10, 20, 91, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ProdLbl.setFont(font)
        self.ProdLbl.setObjectName("ProdLbl")
        self.TotalLbl = QtWidgets.QLabel(RepAlmaxProdActual)
        self.TotalLbl.setGeometry(QtCore.QRect(430, 600, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TotalLbl.setFont(font)
        self.TotalLbl.setObjectName("TotalLbl")
        self.TotalLblVal = QtWidgets.QLabel(RepAlmaxProdActual)
        self.TotalLblVal.setGeometry(QtCore.QRect(570, 600, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.TotalLblVal.setFont(font)
        self.TotalLblVal.setObjectName("TotalLblVal")

        self.retranslateUi(RepAlmaxProdActual)
        QtCore.QMetaObject.connectSlotsByName(RepAlmaxProdActual)

    def retranslateUi(self, RepAlmaxProdActual):
        _translate = QtCore.QCoreApplication.translate
        RepAlmaxProdActual.setWindowTitle(_translate("RepAlmaxProdActual", "Reporte de Almacenes por Productos"))
        self.FechaFinalLbl.setText(_translate("RepAlmaxProdActual", "  Fecha :"))
        self.PBHacer.setText(_translate("RepAlmaxProdActual", "Hacer"))
        self.PBExcel.setText(_translate("RepAlmaxProdActual", "Bajar a Excel"))
        self.PBCerrar.setText(_translate("RepAlmaxProdActual", "Cerrar"))
        item = self.Tabla.horizontalHeaderItem(0)
        item.setText(_translate("RepAlmaxProdActual", "Almacen"))
        item = self.Tabla.horizontalHeaderItem(1)
        item.setText(_translate("RepAlmaxProdActual", "Producto"))
        item = self.Tabla.horizontalHeaderItem(2)
        item.setText(_translate("RepAlmaxProdActual", "InvInic"))
        item = self.Tabla.horizontalHeaderItem(3)
        item.setText(_translate("RepAlmaxProdActual", "Entrada"))
        item = self.Tabla.horizontalHeaderItem(4)
        item.setText(_translate("RepAlmaxProdActual", "Salida"))
        item = self.Tabla.horizontalHeaderItem(5)
        item.setText(_translate("RepAlmaxProdActual", "Total"))
        self.ProdLbl.setText(_translate("RepAlmaxProdActual", "Producto:"))
        self.TotalLbl.setText(_translate("RepAlmaxProdActual", "Total Producto :"))
        self.TotalLblVal.setText(_translate("RepAlmaxProdActual", "xxxxxxxxx"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RepAlmaxProdActual = QtWidgets.QDialog()
    ui = Ui_RepAlmaxProdActual()
    ui.setupUi(RepAlmaxProdActual)
    RepAlmaxProdActual.show()
    sys.exit(app.exec_())
