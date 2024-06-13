
from reportlab.platypus import Table
from reportlab.lib import colors

def genFooterTable(width,height):
    text= " Corrales Valmo SA de CV Perifierico Oriente No.23  Col. El Faro "
    res= Table([[text]], width,height)
    
    color=colors.beige
    res.setStyle([
        #( 'GRID', (0,0), (-1,-1), 1 , 'red' ),
        ( 'LEFTPADDING', (0,0), (-1,-1), 0),
        ( 'BOTTOMPADDING', (0,0), (-1,-1), 0),
        ( 'BACKGROUND', (0,0), (-1,-1), color),
        ( 'TEXTCOLOR', (0,0), (-1,-1), 'black'),
        ( 'ALIGN', (0,0), (-1,-1), 'CENTER'),
        ( 'VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ( 'FONTSIZE', (0,0), (-1,-1), 12),
    
    ])

    return res