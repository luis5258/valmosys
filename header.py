from reportlab.platypus import Table, Image
from reportlab.lib import colors

def genHeaderTable(width,height):

    widthList= [
        width * 35 /100,
        width * 60 /100,
    ]
    TextoSupDerecho=" Corrales Valmo SA de CV"
    LogoPath='valmologo.jpeg'
    LogoImagen=Image(LogoPath,widthList[0],height)
    res= Table([
        [LogoImagen, TextoSupDerecho],
     ],
    widthList,
    height  )
    
    res.setStyle([
        #( 'GRID', (0,0), (-1,-1), 1 , 'red' ),
        ( 'LEFTPADDING', (0,0), (-1,-1), 0),
        ( 'BOTTOMPADDING', (0,0), (-1,-1), 0),

        ( 'ALIGN', (1,0), (-1,-1), 'CENTER'),
        ( 'VALIGN', (1,0), (-1,-1), 'MIDDLE'),
        ( 'FONTSIZE', (1,0), (-1,-1), 20),
        
    ])
    
    return res