
from reportlab.pdfgen  import canvas
from reportlab.lib.pagesizes import A4,LETTER
from reportlab.lib.units import mm
from reportlab.platypus import Table,SimpleDocTemplate,PageBreak,Paragraph
from reportlab.lib   import colors
from header import genHeaderTable
from body import *
from footer import genFooterTable
import os,sys
import subprocess
from subprocess import Popen,PIPE
from Utilis import run_query2


def GeneraReporte(self,No,TituloRep,EncabeDat,DataToTable,DataToTable2,DataToTable3):
    path=os.getcwdb()
    path=os.path.join(str(path,'utf-8'),'Reportes','reporte.pdf')
    pdf=canvas.Canvas(path,pagesize= A4)
    pdf.setTitle('ValmoRep01')
    width,height = A4
    widthList= [
        width * 2 /100,
        width * 93 /100,
        width * 2 /100,
    ]
    heightList= [
    height *6 /100,
    height *86 /100,
    height *3 /100,
    ]

    mainTable=Table ([
    ['',genHeaderTable(widthList[1],heightList[0]),''],
    ['',genBodyTable(widthList[1],heightList[1],No,TituloRep,EncabeDat,DataToTable,DataToTable2,DataToTable3),''],
    ['',genFooterTable(widthList[1],heightList[2]),''],
    ],
    colWidths=widthList,
    rowHeights=heightList
    )
    mainTable.setStyle ([
    #( 'GRID', (0,0), (-1,-1), 1 , 'red' ),
    ( 'LEFTPADDING', (0,0), (0,2), 0),
    ( 'BOTTOMPADDING', (0,0), (-1,-1), 0)

    ])
    mainTable.wrapOn(pdf,0,0)
    mainTable.drawOn(pdf,0,0)
    pdf.showPage
    try :
        pdf.save()
    except PermissionError:
        return 1
    query="SELECT  *  FROM  tblConfigs  WHERE ID > 1 AND ID < 4 "
    ruta=run_query2(self,query)
    RutaAcro=ruta[1][2]
    order_name='AcroRd32.exe ' + path
    path=RutaAcro
    P = subprocess.Popen (order_name, shell = True, stdout = subprocess.PIPE, cwd = path) # Bloqueo del programa

def GeneraRepLiquidaLargo(self,No,TituloRep,EncabeDat,DataToTable,DataToTable2,DataToTable3):
    path=os.getcwdb()
    path=os.path.join(str(path,'utf-8'),'Reportes','reporte.pdf')
    #print(path)
    pdf=canvas.Canvas(path,pagesize= A4)
    pdf.setTitle('ValmoRep01')
    width,height = A4
    widthList= [
        width * 2 /100,
        width * 94 /100,
        width * 2 /100,
    ]
    heightList= [
    height *8 /100,
    height *5 /100,
    #height *5 /100,
    ]
    color= colors.beige
    mainTable=Table ([
    ['',genHeaderTable(widthList[1],heightList[0]),''],
    ['', [GenDatosRep(width,heightList[1],EncabeDat)],''],
    ],
    colWidths=widthList,
    rowHeights=heightList
    )
    mainTable.setStyle ([
    #( 'GRID', (0,0), (-1,-1), 1 , 'red' ),
    ( 'LEFTPADDING', (0,0), (0,2), 0),
    ( 'BOTTOMPADDING', (0,0), (-1,-1), 0)

    ])
    #  Acomoda datos de Tablas 1 y Tabla 2  en una lista para llenar reporte
    ListaAux=[]
    LenDataT2=len(DataToTable2)
    ListaT=[]
    for ren,Ren in enumerate(DataToTable):
        for col,Data in enumerate(Ren):
            ListaAux.append(Data)
        ListaAux.append('')
        if ren < LenDataT2:
            for col2,Data2 in enumerate(DataToTable2[ren]):
                ListaAux.append(Data2)
        else:
            for i in range(0,4):
                ListaAux.append('')
        ListaT.append(ListaAux)
        ListaAux=[]
    # ------------------------------------------------------------------------------------
    
    
    # Tablas  y Tabla 2
    TextoNombreT1T2="_____________Servido  Por Corral_______________________Total Alimento Por Corral__"
    Titulos1_2=Paragraph(TextoNombreT1T2)
    EncabT1=['Corral','Producto','UdeM','Cantidad','','Corral','TotalServ','DiasAnim','PromDia']
    ListaT.insert(0,EncabT1)
    t1=Table(ListaT,colWidths=[60,120,40,50,30,60,50,50,60] )
    t1.setStyle([
        #( 'GRID', (0,0), (-1,-1), 1 , 'red' ),
        ( 'ALIGN', (0,0), (0,0), 'RIGHT'),
        ( 'ALIGN', (1,0), (1,0), 'LEFT'),
        ( 'VALIGN', (0,1), (-1,-1), 'MIDDLE'),
        ( 'LINEBELOW', (0,0), (-1,0), 1, 'grey'),
        ( 'INNERGRID', (0,1), (-1,-1), 0.5 , 'gray' ),
        ( 'BACKGROUND', (0,0), (-1,0), color ),
        ( 'ALIGN', (0,0), (-1,0), 'CENTER' ),
        # ( 'FONTSIZE', (0,1), (-1,1), 8),
        # ( 'FONTSIZE', (0,2), (-1,-1), 6),
        ( 'ALIGN', (1,1), (-1,-1), 'RIGHT'),
        ])
    # -------------------------------------------------------------------------- 
    TextoNombreT3= "-------------------------------------------  Totales    Alimento Servido------------------------------------"
    Titulo3=Paragraph(TextoNombreT3)
    EncabT3=['Producto','UdeM','TotalServido','PUnitario','Importe']
    DataToTable3.insert(0,EncabT3)
    t3=Table(DataToTable3,colWidths=[120,40,60,40,40] )
    t3.setStyle([
        #( 'GRID', (0,0), (-1,-1), 1 , 'red' ),
        ( 'ALIGN', (0,0), (0,0), 'RIGHT'),
        ( 'ALIGN', (1,0), (1,0), 'LEFT'),
        ( 'VALIGN', (0,1), (-1,-1), 'MIDDLE'),
        ( 'LINEBELOW', (0,0), (-1,0), 1, 'grey'),
        ( 'INNERGRID', (0,1), (-1,-1), 0.5 , 'gray' ),
        ( 'BACKGROUND', (0,0), (-1,0), color ),
        ( 'ALIGN', (0,0), (-1,0), 'CENTER' ),
        # ( 'FONTSIZE', (0,1), (-1,1), 8),
        # ( 'FONTSIZE', (0,2), (-1,-1), 6),
        ( 'ALIGN', (1,1), (-1,-1), 'RIGHT'),
        ])      
    #pdf=SimpleDocTemplate("C:\\Users\\Mariano\\Documents\\PROYECTOS\\VALMO\\valmosys\\Reportes\\reporte.pdf")
    pdf=SimpleDocTemplate(path)
    flowAble=[]
    flowAble.append(mainTable)
    flowAble.append(Titulos1_2)
    flowAble.append(t1)
    flowAble.append(Titulo3)
    flowAble.append(t3)
    try :
        pdf.build(flowAble)
    except PermissionError:
        return 1
    
    query="SELECT  *  FROM  tblConfigs  WHERE ID > 1 AND ID < 4 "
    ruta=run_query2(self,query)
    RutaAcro=ruta[1][2]
    order_name='AcroRd32.exe ' + path
    path=RutaAcro
    P = subprocess.Popen (order_name, shell = True, stdout = subprocess.PIPE, cwd = path) # Bloqueo del programa


def GeneraRepDiarioLargo(self,No,TituloRep,EncabeDat,DataToTable):
    path=os.getcwdb()
    path=os.path.join(str(path,'utf-8'),'Reportes','reporte.pdf')
    pdf=canvas.Canvas(path,pagesize= A4)
    pdf.setTitle('ValmoRep01')
    width,height = A4
    widthList= [
        width * 2 /100,
        width * 94 /100,
        width * 2 /100,
    ]
    heightList= [
    height *8 /100,
    height *5 /100,
    #height *5 /100,
    ]
    color= colors.beige
    mainTable=Table ([
    ['',genHeaderTable(widthList[1],heightList[0]),''],
    ['', [GenDatosRep(width,heightList[1],EncabeDat)],''],
     ],
    colWidths=widthList,
    rowHeights=heightList
    )
    mainTable.setStyle ([
    #( 'GRID', (0,0), (-1,-1), 1 , 'red' ),
    ( 'LEFTPADDING', (0,0), (0,2), 0),
    ( 'BOTTOMPADDING', (0,0), (-1,-1), 0)

    ])

    # Tabla
    # t1=Table(DataToTable,colWidths=[60,65,65,65,65,65,65,65,65] )
    t1=Table(DataToTable,colWidths=[60,55,50,50,50,50,53,53,53,53] )
    t1.setStyle([
        #( 'GRID', (0,0), (-1,-1), 1 , 'red' ),
        ( 'ALIGN', (0,0), (0,0), 'RIGHT'),
        ( 'ALIGN', (1,0), (1,0), 'LEFT'),
        ( 'VALIGN', (0,1), (-1,-1), 'MIDDLE'),
        ( 'LINEBELOW', (0,0), (-1,0), 1, 'grey'),
        ( 'INNERGRID', (0,1), (-1,-1), 0.5 , 'gray' ),
        ( 'BACKGROUND', (0,0), (-1,0), color ),
        ( 'ALIGN', (0,0), (-1,0), 'CENTER' ),
        # ( 'FONTSIZE', (0,1), (-1,1), 8),
        # ( 'FONTSIZE', (0,2), (-1,-1), 6),
        ( 'ALIGN', (1,1), (-1,-1), 'RIGHT'),
        ])
    pdf=SimpleDocTemplate(path)
    flowAble=[]
    flowAble.append(mainTable)
    flowAble.append(t1)
    try :
        pdf.build(flowAble)
    except PermissionError:
        return 1
    query="SELECT  *  FROM  tblConfigs  WHERE ID > 1 AND ID < 4 "
    ruta=run_query2(self,query)
    RutaAcro=ruta[1][2]
    order_name='AcroRd32.exe ' + path
    #order_name='Acrobat.exe ' + path
    path=RutaAcro
    P = subprocess.Popen (order_name, shell = True, stdout = subprocess.PIPE, cwd = path) # Bloqueo del programa

def GeneraRepAnimales(self,No,TituloRep,EncabeDat,DataToTable):
    path=os.getcwdb()
    path=os.path.join(str(path,'utf-8'),'Reportes','reporte.pdf')
    pdf=canvas.Canvas(path,pagesize= A4)
    pdf.setTitle('ValmoRep01')
    width,height = A4
    widthList= [
        width * 2 /100,
        width * 94 /100,
        width * 2 /100,
    ]
    heightList= [
    height *8 /100,
    height *5 /100,
    #height *5 /100,
    ]
    color= colors.beige
    mainTable=Table ([
    ['',genHeaderTable(widthList[1],heightList[0]),''],
    ['', [GenDatosRep(width,heightList[1],EncabeDat)],''],
     ],
    colWidths=widthList,
    rowHeights=heightList
    )
    mainTable.setStyle ([
    #( 'GRID', (0,0), (-1,-1), 1 , 'red' ),
    ( 'LEFTPADDING', (0,0), (0,2), 0),
    ( 'BOTTOMPADDING', (0,0), (-1,-1), 0)

    ])

    # Tabla
    t1=Table(DataToTable,colWidths=[60,65,65,65,65,65,65,65,65] )
    t1.setStyle([
        #( 'GRID', (0,0), (-1,-1), 1 , 'red' ),
        ( 'ALIGN', (0,0), (0,0), 'RIGHT'),
        ( 'ALIGN', (1,0), (1,0), 'LEFT'),
        ( 'VALIGN', (0,1), (-1,-1), 'MIDDLE'),
        ( 'LINEBELOW', (0,0), (-1,0), 1, 'grey'),
        ( 'INNERGRID', (0,1), (-1,-1), 0.5 , 'gray' ),
        ( 'BACKGROUND', (0,0), (-1,0), color ),
        ( 'ALIGN', (0,0), (-1,0), 'CENTER' ),
        # ( 'FONTSIZE', (0,1), (-1,1), 8),
        # ( 'FONTSIZE', (0,2), (-1,-1), 6),
        ( 'ALIGN', (1,1), (-1,-1), 'RIGHT'),
        ])
    pdf=SimpleDocTemplate(path)
    flowAble=[]
    flowAble.append(mainTable)
    flowAble.append(t1)
    try :
        pdf.build(flowAble)
    except PermissionError:
        return 1
    query="SELECT  *  FROM  tblConfigs  WHERE ID > 1 AND ID < 4 "
    ruta=run_query2(self,query)
    RutaAcro=ruta[1][2]
    order_name='AcroRd32.exe ' + path
    path=RutaAcro
    P = subprocess.Popen (order_name, shell = True, stdout = subprocess.PIPE, cwd = path) # Bloqueo del programa

def GeneraRepMPLargo(self,No,TituloRep,EncabeDat,DataToTable):
    path=os.getcwdb()
    path=os.path.join(str(path,'utf-8'),'Reportes','reporte.pdf')
    pdf=canvas.Canvas(path,pagesize= A4)
    pdf.setTitle('ValmoRep01')
    width,height = A4
    widthList= [
        width * 2 /100,
        width * 94 /100,
        width * 2 /100,
    ]
    heightList= [
    height *8 /100,
    height *5 /100,
    #height *5 /100,
    ]
    color= colors.beige
    mainTable=Table ([
    ['',genHeaderTable(widthList[1],heightList[0]),''],
    ['', [GenDatosRep(width,heightList[1],EncabeDat)],''],
     ],
    colWidths=widthList,
    rowHeights=heightList
    )
    mainTable.setStyle ([
    #( 'GRID', (0,0), (-1,-1), 1 , 'red' ),
    ( 'LEFTPADDING', (0,0), (0,2), 0),
    ( 'BOTTOMPADDING', (0,0), (-1,-1), 0)

    ])

    # Tabla
    t1=Table(DataToTable,colWidths=[130,80,75,75,75,75] )
    t1.setStyle([
        #( 'GRID', (0,0), (-1,-1), 1 , 'red' ),
        ( 'ALIGN', (0,0), (0,0), 'RIGHT'),
        ( 'ALIGN', (1,0), (1,0), 'LEFT'),
        ( 'VALIGN', (0,1), (-1,-1), 'MIDDLE'),
        ( 'LINEBELOW', (0,0), (-1,0), 1, 'grey'),
        ( 'INNERGRID', (0,1), (-1,-1), 0.5 , 'gray' ),
        ( 'BACKGROUND', (0,0), (-1,0), color ),
        ( 'ALIGN', (0,0), (-1,0), 'CENTER' ),
        # ( 'FONTSIZE', (0,1), (-1,1), 8),
        # ( 'FONTSIZE', (0,2), (-1,-1), 6),
        ( 'ALIGN', (1,1), (-1,-1), 'RIGHT'),
        ])
    pdf=SimpleDocTemplate(path)
    flowAble=[]
    flowAble.append(mainTable)
    flowAble.append(t1)
    try :
        pdf.build(flowAble)
    except PermissionError:
        return 1
    query="SELECT  *  FROM  tblConfigs  WHERE ID > 1 AND ID < 4 "
    ruta=run_query2(self,query)
    RutaAcro=ruta[1][2]
    order_name='AcroRd32.exe ' + path
    path=RutaAcro
    P = subprocess.Popen (order_name, shell = True, stdout = subprocess.PIPE, cwd = path) # Bloqueo del programa


def GeneraRepAnimalClienteCorral(self,No,TituloRep,EncabeDat,DataToTable):
    path=os.getcwdb()
    path=os.path.join(str(path,'utf-8'),'Reportes','reporte.pdf')
    pdf=canvas.Canvas(path,pagesize= A4)
    pdf.setTitle('ValmoRep01')
    width,height = A4
    widthList= [
        width * 2 /100,
        width * 94 /100,
        width * 2 /100,
    ]
    heightList= [
    height *8 /100,
    height *5 /100,
    #height *5 /100,
    ]
    color= colors.beige
    mainTable=Table ([
    ['',genHeaderTable(widthList[1],heightList[0]),''],
    ['', [GenDatosRep(width,heightList[1],EncabeDat)],''],
     ],
    colWidths=widthList,
    rowHeights=heightList
    )
    mainTable.setStyle ([
    #( 'GRID', (0,0), (-1,-1), 1 , 'red' ),
    ( 'LEFTPADDING', (0,0), (0,2), 0),
    ( 'BOTTOMPADDING', (0,0), (-1,-1), 0)

    ])

    # Tabla
    t1=Table(DataToTable,colWidths=[200,100,100] )
    t1.setStyle([
        #( 'GRID', (0,0), (-1,-1), 1 , 'red' ),
        ( 'ALIGN', (0,0), (0,0), 'RIGHT'),
        ( 'ALIGN', (1,0), (1,0), 'LEFT'),
        ( 'VALIGN', (0,1), (-1,-1), 'MIDDLE'),
        ( 'LINEBELOW', (0,0), (-1,0), 1, 'grey'),
        ( 'INNERGRID', (0,1), (-1,-1), 0.5 , 'gray' ),
        ( 'BACKGROUND', (0,0), (-1,0), color ),
        ( 'ALIGN', (0,0), (-1,0), 'CENTER' ),
        # ( 'FONTSIZE', (0,1), (-1,1), 8),
        # ( 'FONTSIZE', (0,2), (-1,-1), 6),
        ( 'ALIGN', (1,1), (-1,-1), 'RIGHT'),
        ])
    pdf=SimpleDocTemplate(path)
    flowAble=[]
    flowAble.append(mainTable)
    flowAble.append(t1)
    try :
        pdf.build(flowAble)
    except PermissionError:
        return 1
    query="SELECT  *  FROM  tblConfigs  WHERE ID > 1 AND ID < 4 "
    ruta=run_query2(self,query)
    RutaAcro=ruta[1][2]
    order_name='AcroRd32.exe ' + path
    path=RutaAcro
    P = subprocess.Popen (order_name, shell = True, stdout = subprocess.PIPE, cwd = path) # Bloqueo del programa