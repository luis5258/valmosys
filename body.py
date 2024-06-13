
from reportlab.platypus import Table
from reportlab.lib   import colors
from reportlab.lib.units import mm

def genBodyTable(width,height,No,TituloRep,EncabeDat,DataToTable,DataToTable2,DataToTable3):

    widthList= [
        width * 3 /100,
        width * 90 /100,
        width * 3 /100,
     ]
    heightList= [
        height * 3 / 100,
        height * 6  / 100,
        height * 91 / 100,
    ]

    if No ==1 :
        FormTabDat=[GenTablaDatos1(width,heightList[2],DataToTable)]
    elif No ==2 :
        FormTabDat=[GenTablaDatos2(width,heightList[2],DataToTable,DataToTable2,DataToTable3)]
    elif No == 3:
        FormTabDat=[GenTablaDatos3(width,heightList[2],DataToTable)]

    res = Table([
        [TituloRep],
        [GenDatosRep(width,heightList[1],EncabeDat)],
        [FormTabDat],
        
    ],
    width,        #  Cambiar por lista si requieren mas columnas
    heightList
    )
    
    res.setStyle([
        #( 'GRID', (0,0), (-1,-1), 1 , 'red' ),
        ( 'LEFTPADDING', (0,0), (0,0), 0),
        ( 'BOTTOMPADDING', (0,0),  (0,0), 10),
        ( 'ALIGN', (0,0), (0,0), 'CENTER'),
        ( 'VALIGN', (0,0), (0,0), 'MIDDLE'),
        ( 'FONTSIZE', (0,0), (0,0), 14),
        ( 'ALIGN', (0,0), (1,1), 'CENTER'),
        ( 'VALIGN', (0,0), (1,1), 'MIDDLE'),
        ( 'LINEBELOW', (0,0), (0,0), 1, 'grey'),
        ( 'LINEBELOW', (0,1), (-1,1), 1, 'grey'),
        # ( 'ALIGN', (0,2), (0,2), 'CENTER'),
        ( 'VALIGN',(0,2), (0,2), 'TOP'),
        
    
    ])
    return res

def GenDatosRep(width,height,EnCabeDat):
    widthList= [
        width * 15 /100,
        width * 35 /100,
        width * 15 /100,
        width * 35 /100,
     ]
    heightList= [
        height * 50 / 100,
        height * 50  / 100,
        
    ]

    TabToRep= Table([
        [EnCabeDat[0], EnCabeDat[1], EnCabeDat[2], EnCabeDat[3]],
        [EnCabeDat[4],EnCabeDat[5],EnCabeDat[6],EnCabeDat[7]],
        
    ],
    widthList,       
    heightList,
    )

    TabToRep.setStyle([
        #( 'GRID', (0,0), (-1,-1), 1 , 'black' ),
        # ( 'ALIGN', (0,0), (-1,0), 'CENTER'),
        # ( 'VALIGN', (0,0), (-1,0), 'MIDDLE'),
                
    
    ])
    return TabToRep


def GenTablaDatos1(width,height,DataTableList):
    widthList= [
        width * 20/100,
        width * 20 /100,
        width * 15 /100,
        width * 15 /100,
        width * 15 /100,
        width * 15 /100,
     ]
    TablaToRep= Table(
        DataTableList
    ,
    widthList,
    height/30
    )
    color= colors.beige
    TablaToRep.setStyle([
        #( 'GRID', (0,0), (-1,-1), 1 , 'gray' ),
        ( 'ALIGN', (0,0), (-1,0), 'CENTER'),
        ( 'VALIGN', (0,0), (-1,0), 'MIDDLE'),
        ( 'INNERGRID', (0,0), (-1,-1), 0.5 , 'gray' ),
        ( 'BACKGROUND', (0,0), (-1,0), color ),
        ( 'ALIGN', (1,1), (4,-1), 'RIGHT'),
                
    
    ])
    return TablaToRep

#  Formato de Tablas de Liquidacion de cliente**********************************************************************

def GenTablaDatos2(width,height,DataTableList,DataToTable2,DataToTable3):
    widthList= [ width * 50 /100, width * 50 /100, ]
   
    TabToRep= Table([
        [TabProdEnCorr(widthList[0],height,DataTableList),GenTab2yTab3(widthList[1],height,DataToTable2,DataToTable3)],
        #[TabProdEnCorr(widthList[0],height,DataTableList),'Espacios Tablas 2 y 3'],
    ],widthList, height,  )

    TabToRep.setStyle([
        ( 'GRID', (0,0), (-1,-1), 1 , 'black' ),
        ( 'ALIGN', (0,0), (-1,-1), 'CENTER'),
        ( 'VALIGN',(0,0), (-1,-1), 'TOP'),
    ])
    return TabToRep



def TabProdEnCorr(width,height,DataTableList):
    ToTableData=DataTableList
    TitulosCols=['Corral','Producto','UdeM',"Cantidad"]
    ToTableData.insert(0,TitulosCols)
    ToTableData.insert(0,['','Producto','en Corral',''])
    widthList= [
        width * 22 /100,
        width * 34 /100,
        width * 22 /100,
        width * 22 /100,
        
     ]
    #TabToRep= Table(ToTableData ,widthList,height/60,  )
    TabToRep= Table(ToTableData ,widthList,4.5*mm,  )
    color= colors.beige
    TabToRep.setStyle([
        #( 'GRID', (0,0), (-1,-1), 1 , 'red' ),
        ( 'ALIGN', (0,0), (0,0), 'RIGHT'),
        ( 'ALIGN', (1,0), (1,0), 'LEFT'),
        # ( 'FONTSIZE', (0,1), (-1,1), 8),
        # ( 'FONTSIZE', (0,2), (-1,-1), 6),
        ( 'VALIGN', (0,1), (-1,-1), 'MIDDLE'),
        ( 'TOPPADDING', (0,1), (-1,-1), 1),
        ( 'LINEBELOW', (0,0), (-1,0), 1, 'grey'),
        ( 'INNERGRID', (0,1), (-1,-1), 0.5 , 'gray' ),
        ( 'BACKGROUND', (0,1), (-1,1), color ),
        ( 'ALIGN', (3,2), (3,-1), 'RIGHT'),
    
    ])
    return TabToRep

def GenTab2yTab3(width,height,DataToTable2,DataToTable3):
    heightList= [
        height * 75 / 100,
        height * 25  / 100,
    ]
    #TabToRep= Table([TabPromedio(width,heightList[0],DataToTable2), 'Tabla3'] ,width,heightList  )
    TabToRep= Table([
                   [TabPromedio(width,heightList[0],DataToTable2)],[TabTotales(width,heightList[1],DataToTable3),],
     ] , 
     width,
     heightList )
    color= colors.beige
    TabToRep.setStyle([
        ( 'GRID', (0,0), (-1,0), 1 , 'black' ),
        ( 'ALIGN', (0,0), (-1,-1), 'CENTER'),
        ( 'VALIGN', (0,0), (-1,-1), 'TOP' ),
                             
    ])
    return TabToRep

def TabPromedio(width,height,DataToTable2):
    ToTableData=DataToTable2
    TitulosCols=['Corral','TotalServ','DiasAnimal','PromDiario']
    ToTableData.insert(0,TitulosCols)
    ToTableData.insert(0,['','Promedio','Diario',''])
    widthList= [
        width * 34 /100,
        width * 22 /100,
        width * 22 /100,
        width * 22 /100,
    ]
    #TabToRep= Table(ToTableData ,widthList,height/32,  )
    TabToRep= Table(ToTableData ,widthList,4.5*mm,  )
    color= colors.beige
    TabToRep.setStyle([
        #( 'GRID', (0,0), (-1,-1), 1 , 'red' ),
        ( 'ALIGN', (0,0), (0,0), 'RIGHT'),
        ( 'ALIGN', (1,0), (1,0), 'LEFT'),
        ( 'VALIGN', (0,1), (-1,-1), 'MIDDLE'),
        ( 'LINEBELOW', (0,0), (-1,0), 1, 'grey'),
        ( 'INNERGRID', (0,1), (-1,-1), 0.5 , 'gray' ),
        ( 'BACKGROUND', (0,1), (-1,1), color ),
        # ( 'FONTSIZE', (0,1), (-1,1), 8),
        # ( 'FONTSIZE', (0,2), (-1,-1), 6),
        ( 'ALIGN', (1,2), (-1,-1), 'RIGHT'),
    
    ])
    return TabToRep

def TabTotales(width,height,DataToTable3):
    ToTableData=DataToTable3
    TitulosCols=['Producto','UdeM','TotServ','P.Unitario','Importe']
    ToTableData.insert(0,TitulosCols)
    ToTableData.insert(0,['','Totales','',''])
    widthList= [
        width * 34 /100,
        width * 12 /100,
        width * 18 /100,
        width * 18 /100,
        width * 18 /100,
     ]
    TabToRep= Table(ToTableData ,widthList,height/10,  )
    color= colors.beige
    TabToRep.setStyle([
        #( 'GRID', (0,0), (-1,-1), 1 , 'red' ),
        ( 'ALIGN', (0,0), (0,0), 'RIGHT'),
        ( 'ALIGN', (1,0), (1,0), 'LEFT'),
        ( 'LINEBELOW', (0,0), (-1,0), 1, 'grey'),
        ( 'INNERGRID', (0,1), (-1,-1), 0.5 , 'gray' ),
        ( 'BACKGROUND', (0,1), (-1,1), color ),
    
    ])
    return TabToRep

#  Genera Body Reporte Servido y promedio diario
def GenTablaDatos3(width,height,DataToTable):
    ToTableData=DataToTable
    TitulosCols=['Corral','Alfalfa ','Fase 1', 'Fase 2','Fase 3','Tot Servido','No Anim Act','DiasAnimal','PromDiario']
    #ToTableData.insert(0,TitulosCols)
    widthList= [
        width * 14 /100,
        width * 10 /100,
        width * 10/100,
        width * 10 /100,
        width * 10 /100,
        width * 12 /100,
        width * 12 /100,
        width * 11 /100,
        width * 11 /100,
     ]
    TabToRep= Table(ToTableData ,widthList,height/45,  )
    color= colors.beige
    TabToRep.setStyle([
        #( 'GRID', (0,0), (-1,-1), 1 , 'red' ),
        ( 'ALIGN', (0,0), (0,0), 'RIGHT'),
        ( 'ALIGN', (1,0), (1,0), 'LEFT'),
        ( 'LINEBELOW', (0,0), (-1,0), 1, 'grey'),
        ( 'INNERGRID', (0,0), (-1,-1), 0.5 , 'gray' ),
        ( 'BACKGROUND', (0,0), (-1,1), color ),
    
    ])
    return TabToRep







