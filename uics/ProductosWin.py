# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProductosWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Productos(object):
    def setupUi(self, Productos):
        Productos.setObjectName("Productos")
        Productos.resize(739, 667)
        Productos.setStyleSheet("DialogAltaAnimales{\n"
"\n"
"}\n"
"\n"
"lineEdit{  font-size: 16px;\n"
"\n"
"}")
        self.Tabla = QtWidgets.QTableWidget(Productos)
        self.Tabla.setGeometry(QtCore.QRect(10, 230, 701, 391))
        self.Tabla.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Tabla.setAlternatingRowColors(True)
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
        self.layoutWidget = QtWidgets.QWidget(Productos)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 630, 561, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PBAgregaModIng = QtWidgets.QPushButton(self.layoutWidget)
        self.PBAgregaModIng.setObjectName("PBAgregaModIng")
        self.horizontalLayout.addWidget(self.PBAgregaModIng)
        self.PBCerrar = QtWidgets.QPushButton(self.layoutWidget)
        self.PBCerrar.setObjectName("PBCerrar")
        self.horizontalLayout.addWidget(self.PBCerrar)
        self.groupBox_2 = QtWidgets.QGroupBox(Productos)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 20, 401, 171))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.PUnitarioLbl = QtWidgets.QLabel(self.groupBox_2)
        self.PUnitarioLbl.setGeometry(QtCore.QRect(12, 90, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PUnitarioLbl.setFont(font)
        self.PUnitarioLbl.setObjectName("PUnitarioLbl")
        self.PUCampo = QtWidgets.QLineEdit(self.groupBox_2)
        self.PUCampo.setGeometry(QtCore.QRect(120, 90, 133, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.PUCampo.setFont(font)
        self.PUCampo.setText("")
        self.PUCampo.setObjectName("PUCampo")
        self.DescripcionCampo = QtWidgets.QLineEdit(self.groupBox_2)
        self.DescripcionCampo.setGeometry(QtCore.QRect(100, 60, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.DescripcionCampo.setFont(font)
        self.DescripcionCampo.setText("")
        self.DescripcionCampo.setObjectName("DescripcionCampo")
        self.ClaveCampo = QtWidgets.QLineEdit(self.groupBox_2)
        self.ClaveCampo.setGeometry(QtCore.QRect(53, 29, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ClaveCampo.setFont(font)
        self.ClaveCampo.setText("")
        self.ClaveCampo.setObjectName("ClaveCampo")
        self.ClaveLbl = QtWidgets.QLabel(self.groupBox_2)
        self.ClaveLbl.setGeometry(QtCore.QRect(10, 29, 38, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ClaveLbl.setFont(font)
        self.ClaveLbl.setObjectName("ClaveLbl")
        self.NombreLbl = QtWidgets.QLabel(self.groupBox_2)
        self.NombreLbl.setGeometry(QtCore.QRect(10, 60, 75, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.NombreLbl.setFont(font)
        self.NombreLbl.setObjectName("NombreLbl")
        self.UdeMLbl_1 = QtWidgets.QLabel(self.groupBox_2)
        self.UdeMLbl_1.setGeometry(QtCore.QRect(270, 90, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.UdeMLbl_1.setFont(font)
        self.UdeMLbl_1.setObjectName("UdeMLbl_1")
        self.UdeMLblVal = QtWidgets.QLabel(self.groupBox_2)
        self.UdeMLblVal.setGeometry(QtCore.QRect(330, 90, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.UdeMLblVal.setFont(font)
        self.UdeMLblVal.setObjectName("UdeMLblVal")
        self.EstatusLbl = QtWidgets.QLabel(self.groupBox_2)
        self.EstatusLbl.setGeometry(QtCore.QRect(180, 30, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.EstatusLbl.setFont(font)
        self.EstatusLbl.setObjectName("EstatusLbl")
        self.EstatusLblVal = QtWidgets.QLabel(self.groupBox_2)
        self.EstatusLblVal.setGeometry(QtCore.QRect(240, 30, 71, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.EstatusLblVal.setFont(font)
        self.EstatusLblVal.setObjectName("EstatusLblVal")
        self.groupBox_4 = QtWidgets.QGroupBox(Productos)
        self.groupBox_4.setGeometry(QtCore.QRect(430, 30, 261, 161))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.UdeMComBox = QtWidgets.QComboBox(self.groupBox_4)
        self.UdeMComBox.setGeometry(QtCore.QRect(70, 140, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.UdeMComBox.setFont(font)
        self.UdeMComBox.setObjectName("UdeMComBox")
        self.UdeMLbl_2 = QtWidgets.QLabel(self.groupBox_4)
        self.UdeMLbl_2.setGeometry(QtCore.QRect(7, 140, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.UdeMLbl_2.setFont(font)
        self.UdeMLbl_2.setObjectName("UdeMLbl_2")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 151, 51))
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.RBotAlta = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RBotAlta.setFont(font)
        self.RBotAlta.setAcceptDrops(False)
        self.RBotAlta.setChecked(True)
        self.RBotAlta.setObjectName("RBotAlta")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.RBotAlta)
        self.RBotBaja = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RBotBaja.setFont(font)
        self.RBotBaja.setObjectName("RBotBaja")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.RBotBaja)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 70, 151, 51))
        self.groupBox_5.setObjectName("groupBox_5")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_5)
        self.formLayout_2.setObjectName("formLayout_2")
        self.RBotNo = QtWidgets.QRadioButton(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RBotNo.setFont(font)
        self.RBotNo.setAcceptDrops(False)
        self.RBotNo.setChecked(True)
        self.RBotNo.setObjectName("RBotNo")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.RBotNo)
        self.RBotSi = QtWidgets.QRadioButton(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RBotSi.setFont(font)
        self.RBotSi.setObjectName("RBotSi")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.RBotSi)
        self.PBModificar = QtWidgets.QPushButton(Productos)
        self.PBModificar.setGeometry(QtCore.QRect(140, 200, 126, 23))
        self.PBModificar.setObjectName("PBModificar")
        self.PBAgregar = QtWidgets.QPushButton(Productos)
        self.PBAgregar.setGeometry(QtCore.QRect(8, 200, 126, 23))
        self.PBAgregar.setObjectName("PBAgregar")
        self.groupBox_2.raise_()
        self.Tabla.raise_()
        self.layoutWidget.raise_()
        self.groupBox_4.raise_()
        self.PBModificar.raise_()
        self.PBAgregar.raise_()

        self.retranslateUi(Productos)
        QtCore.QMetaObject.connectSlotsByName(Productos)
        Productos.setTabOrder(self.ClaveCampo, self.DescripcionCampo)
        Productos.setTabOrder(self.DescripcionCampo, self.PUCampo)
        Productos.setTabOrder(self.PUCampo, self.UdeMComBox)
        Productos.setTabOrder(self.UdeMComBox, self.Tabla)
        Productos.setTabOrder(self.Tabla, self.RBotAlta)
        Productos.setTabOrder(self.RBotAlta, self.PBCerrar)

    def retranslateUi(self, Productos):
        _translate = QtCore.QCoreApplication.translate
        Productos.setWindowTitle(_translate("Productos", "Productos"))
        item = self.Tabla.horizontalHeaderItem(0)
        item.setText(_translate("Productos", "ID"))
        item = self.Tabla.horizontalHeaderItem(1)
        item.setText(_translate("Productos", "Clave"))
        item = self.Tabla.horizontalHeaderItem(2)
        item.setText(_translate("Productos", "Nombre"))
        item = self.Tabla.horizontalHeaderItem(3)
        item.setText(_translate("Productos", "UdeM"))
        item = self.Tabla.horizontalHeaderItem(4)
        item.setText(_translate("Productos", "P.Unitario"))
        item = self.Tabla.horizontalHeaderItem(5)
        item.setText(_translate("Productos", "Estatus"))
        item = self.Tabla.horizontalHeaderItem(6)
        item.setText(_translate("Productos", "Se Sirve En Corral"))
        self.PBAgregaModIng.setText(_translate("Productos", "Agre-Modf  Ingredientes Receta"))
        self.PBCerrar.setText(_translate("Productos", "Cerrar"))
        self.groupBox_2.setTitle(_translate("Productos", "Agregar-Modificar Producto:"))
        self.PUnitarioLbl.setText(_translate("Productos", "Precio Unitario:"))
        self.ClaveLbl.setText(_translate("Productos", "Clave:"))
        self.NombreLbl.setText(_translate("Productos", "Descripcion:"))
        self.UdeMLbl_1.setText(_translate("Productos", "U de M:"))
        self.UdeMLblVal.setText(_translate("Productos", "0.0"))
        self.EstatusLbl.setText(_translate("Productos", "Estatus:"))
        self.EstatusLblVal.setText(_translate("Productos", "0.0"))
        self.groupBox_4.setTitle(_translate("Productos", "Ajustar Para Agregar o Modificar:"))
        self.UdeMLbl_2.setText(_translate("Productos", "U de M:"))
        self.groupBox.setTitle(_translate("Productos", "Estatus :"))
        self.RBotAlta.setText(_translate("Productos", "Activo"))
        self.RBotBaja.setText(_translate("Productos", "Baja"))
        self.groupBox_5.setTitle(_translate("Productos", "Se sirve en Corrales:"))
        self.RBotNo.setText(_translate("Productos", "No"))
        self.RBotSi.setText(_translate("Productos", "Si"))
        self.PBModificar.setText(_translate("Productos", "Modifi.Datos "))
        self.PBAgregar.setText(_translate("Productos", "Agregar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Productos = QtWidgets.QDialog()
    ui = Ui_Productos()
    ui.setupUi(Productos)
    Productos.show()
    sys.exit(app.exec_())
