# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RepMovTodosMP.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RepMovTodosMP(object):
    def setupUi(self, RepMovTodosMP):
        RepMovTodosMP.setObjectName("RepMovTodosMP")
        RepMovTodosMP.resize(987, 707)
        self.FechaInicSel = QtWidgets.QDateEdit(RepMovTodosMP)
        self.FechaInicSel.setGeometry(QtCore.QRect(110, 51, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.FechaInicSel.setFont(font)
        self.FechaInicSel.setMaximumDate(QtCore.QDate(2050, 12, 31))
        self.FechaInicSel.setCalendarPopup(True)
        self.FechaInicSel.setDate(QtCore.QDate(2021, 1, 1))
        self.FechaInicSel.setObjectName("FechaInicSel")
        self.FechaFinSel = QtWidgets.QDateEdit(RepMovTodosMP)
        self.FechaFinSel.setGeometry(QtCore.QRect(340, 50, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.FechaFinSel.setFont(font)
        self.FechaFinSel.setMaximumDate(QtCore.QDate(2050, 12, 31))
        self.FechaFinSel.setCalendarPopup(True)
        self.FechaFinSel.setDate(QtCore.QDate(2021, 1, 1))
        self.FechaFinSel.setObjectName("FechaFinSel")
        self.FechaFinalLbl = QtWidgets.QLabel(RepMovTodosMP)
        self.FechaFinalLbl.setGeometry(QtCore.QRect(240, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FechaFinalLbl.setFont(font)
        self.FechaFinalLbl.setObjectName("FechaFinalLbl")
        self.FechaIniLbl = QtWidgets.QLabel(RepMovTodosMP)
        self.FechaIniLbl.setGeometry(QtCore.QRect(10, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FechaIniLbl.setFont(font)
        self.FechaIniLbl.setObjectName("FechaIniLbl")
        self.PBHacer = QtWidgets.QPushButton(RepMovTodosMP)
        self.PBHacer.setGeometry(QtCore.QRect(10, 660, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PBHacer.setFont(font)
        self.PBHacer.setObjectName("PBHacer")
        self.PBExcel = QtWidgets.QPushButton(RepMovTodosMP)
        self.PBExcel.setGeometry(QtCore.QRect(130, 660, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PBExcel.setFont(font)
        self.PBExcel.setObjectName("PBExcel")
        self.PBCerrar = QtWidgets.QPushButton(RepMovTodosMP)
        self.PBCerrar.setGeometry(QtCore.QRect(610, 660, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PBCerrar.setFont(font)
        self.PBCerrar.setObjectName("PBCerrar")
        self.Tabla = QtWidgets.QTableWidget(RepMovTodosMP)
        self.Tabla.setGeometry(QtCore.QRect(10, 130, 1131, 521))
        self.Tabla.setObjectName("Tabla")
        self.Tabla.setColumnCount(16)
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
        item = QtWidgets.QTableWidgetItem()
        self.Tabla.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla.setHorizontalHeaderItem(15, item)
        self.BanLbl_2 = QtWidgets.QLabel(RepMovTodosMP)
        self.BanLbl_2.setGeometry(QtCore.QRect(100, 90, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.BanLbl_2.setFont(font)
        self.BanLbl_2.setAlignment(QtCore.Qt.AlignCenter)
        self.BanLbl_2.setObjectName("BanLbl_2")
        self.AlmacenCBox = QtWidgets.QComboBox(RepMovTodosMP)
        self.AlmacenCBox.setGeometry(QtCore.QRect(116, 19, 361, 20))
        self.AlmacenCBox.setObjectName("AlmacenCBox")
        self.ClienteLbl = QtWidgets.QLabel(RepMovTodosMP)
        self.ClienteLbl.setGeometry(QtCore.QRect(10, 20, 91, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ClienteLbl.setFont(font)
        self.ClienteLbl.setObjectName("ClienteLbl")
        self.groupBox = QtWidgets.QGroupBox(RepMovTodosMP)
        self.groupBox.setGeometry(QtCore.QRect(500, 40, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.RBotTodos = QtWidgets.QRadioButton(self.groupBox)
        self.RBotTodos.setGeometry(QtCore.QRect(20, 20, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.RBotTodos.setFont(font)
        self.RBotTodos.setChecked(True)
        self.RBotTodos.setObjectName("RBotTodos")
        self.RBotAlmacen = QtWidgets.QRadioButton(self.groupBox)
        self.RBotAlmacen.setGeometry(QtCore.QRect(100, 20, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.RBotAlmacen.setFont(font)
        self.RBotAlmacen.setObjectName("RBotAlmacen")
        self.PBBorrar = QtWidgets.QPushButton(RepMovTodosMP)
        self.PBBorrar.setGeometry(QtCore.QRect(300, 660, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PBBorrar.setFont(font)
        self.PBBorrar.setObjectName("PBBorrar")
        self.groupBox.raise_()
        self.FechaInicSel.raise_()
        self.FechaFinSel.raise_()
        self.FechaFinalLbl.raise_()
        self.FechaIniLbl.raise_()
        self.PBHacer.raise_()
        self.PBExcel.raise_()
        self.PBCerrar.raise_()
        self.Tabla.raise_()
        self.BanLbl_2.raise_()
        self.AlmacenCBox.raise_()
        self.ClienteLbl.raise_()
        self.PBBorrar.raise_()

        self.retranslateUi(RepMovTodosMP)
        QtCore.QMetaObject.connectSlotsByName(RepMovTodosMP)

    def retranslateUi(self, RepMovTodosMP):
        _translate = QtCore.QCoreApplication.translate
        RepMovTodosMP.setWindowTitle(_translate("RepMovTodosMP", "Reporte Movimiento de Materia Prima"))
        self.FechaFinalLbl.setText(_translate("RepMovTodosMP", "Fecha Final:"))
        self.FechaIniLbl.setText(_translate("RepMovTodosMP", "Fecha Inicial:"))
        self.PBHacer.setText(_translate("RepMovTodosMP", "Hacer"))
        self.PBExcel.setText(_translate("RepMovTodosMP", "Bajar a Excel"))
        self.PBCerrar.setText(_translate("RepMovTodosMP", "Cerrar"))
        item = self.Tabla.horizontalHeaderItem(0)
        item.setText(_translate("RepMovTodosMP", "Folio"))
        item = self.Tabla.horizontalHeaderItem(1)
        item.setText(_translate("RepMovTodosMP", "Fecha"))
        item = self.Tabla.horizontalHeaderItem(2)
        item.setText(_translate("RepMovTodosMP", "TipoMov"))
        item = self.Tabla.horizontalHeaderItem(3)
        item.setText(_translate("RepMovTodosMP", "MateriaPrima"))
        item = self.Tabla.horizontalHeaderItem(4)
        item.setText(_translate("RepMovTodosMP", "Cantidad"))
        item = self.Tabla.horizontalHeaderItem(5)
        item.setText(_translate("RepMovTodosMP", "Almacen"))
        item = self.Tabla.horizontalHeaderItem(6)
        item.setText(_translate("RepMovTodosMP", "Costo"))
        item = self.Tabla.horizontalHeaderItem(7)
        item.setText(_translate("RepMovTodosMP", "Flete"))
        item = self.Tabla.horizontalHeaderItem(8)
        item.setText(_translate("RepMovTodosMP", "Maniobra"))
        item = self.Tabla.horizontalHeaderItem(9)
        item.setText(_translate("RepMovTodosMP", "Provedor"))
        item = self.Tabla.horizontalHeaderItem(10)
        item.setText(_translate("RepMovTodosMP", "Pesador"))
        item = self.Tabla.horizontalHeaderItem(11)
        item.setText(_translate("RepMovTodosMP", "Camion"))
        item = self.Tabla.horizontalHeaderItem(12)
        item.setText(_translate("RepMovTodosMP", "Placas"))
        item = self.Tabla.horizontalHeaderItem(13)
        item.setText(_translate("RepMovTodosMP", "Chofer"))
        item = self.Tabla.horizontalHeaderItem(14)
        item.setText(_translate("RepMovTodosMP", "Notas"))
        self.BanLbl_2.setText(_translate("RepMovTodosMP", "Movimientos  Todos en Rango de Fechas"))
        self.ClienteLbl.setText(_translate("RepMovTodosMP", "Alamacen:"))
        self.groupBox.setTitle(_translate("RepMovTodosMP", "Filtro Origen:"))
        self.RBotTodos.setText(_translate("RepMovTodosMP", "Todos"))
        self.RBotAlmacen.setText(_translate("RepMovTodosMP", "Almacen:"))
        self.PBBorrar.setText(_translate("RepMovTodosMP", "Borrar Movimiento"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RepMovTodosMP = QtWidgets.QDialog()
    ui = Ui_RepMovTodosMP()
    ui.setupUi(RepMovTodosMP)
    RepMovTodosMP.show()
    sys.exit(app.exec_())
