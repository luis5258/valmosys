
from AuxiliaresToPHP import *
import sys
NoRep=sys.argv[1]
cliente=sys.argv[2]
FechaInicial=sys.argv[3]
FechaFinal=sys.argv[4]

if NoRep == '1' or NoRep == '3':
    RepsLiquidacion(NoRep,cliente,FechaInicial,FechaFinal)
elif NoRep == '2' :
    Reporte2(cliente,FechaInicial,FechaFinal)
elif NoRep == '4' :
    ReporteDiario(cliente,FechaInicial,FechaFinal)

