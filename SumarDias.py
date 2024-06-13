from datetime import datetime
from datetime import timedelta
import sys
from Utilis import *
# fi=sys.argv[1]
# ff=sys.argv[2]

fi='2023-01-25'
ff='2023-01-29'

cnt=0
IDCorral=207

def CantidadActualAnimales(self,IDCorral,fecha):
    query=  """ SELECT  SUM(case WHEN  tblMovimientoAnimales.IDMovimiento = 0  THEN  tblMovimientoAnimales.Cantidad ELSE 0 END) -
                       SUM(case WHEN  tblMovimientoAnimales.IDMovimiento = 1  THEN  tblMovimientoAnimales.Cantidad  ELSE 0 END) AS SUMA
                FROM tblMovimientoAnimales 
                WHERE tblMovimientoAnimales.IDCorral= ?  AND tblMovimientoAnimales.Fecha BETWEEN 
                (SELECT FechaAsigna FROM tblCorrales WHERE ID=? ) AND ?
            """
    Cantidad=run_query2(self,query,(IDCorral,IDCorral,fecha))
    if Cantidad[0][0] is None :
        return -1
    else:
        return Cantidad[0][0]

def DiasAnimal(self,IDCorral,fi,ff):
    FechaInicial = datetime.strptime(fi, '%Y-%m-%d')
    FechaFinal = datetime.strptime(ff, '%Y-%m-%d')
    Fecha=FechaInicial
    ListaFechas=[datetime.strftime(Fecha, '%Y-%m-%d'),]
    Dias=0
    AnimalesActual=CantidadActualAnimales(self,IDCorral,Fecha)
    while Fecha != FechaFinal:
        Fecha=Fecha + timedelta(days=1)
        ListaFechas.append(datetime.strftime(Fecha, '%Y-%m-%d'))
    query=  """     SELECT ifnull(  
                        SUM(case WHEN  tblMovimientoAnimales.IDMovimiento = 0  THEN  tblMovimientoAnimales.Cantidad ELSE 0 END) -
                        SUM(case WHEN  tblMovimientoAnimales.IDMovimiento = 1  THEN  tblMovimientoAnimales.Cantidad  ELSE 0 END)  , 0)
                        
                    FROM  tblMovimientoAnimales 
                    WHERE    IDCorral= ?  AND Fecha = ?
            """
    for i in ListaFechas:
        data=(IDCorral,i)
        CantMov=run_query2(self,query,data)[0]
        AnimalesActual+=CantMov[0]
        Dias+=AnimalesActual
        print(i,CantMov)
    print("Dias Animal= ",Dias)

def MySqlConect(connData):
    conn = mysql.connector.connect(host =connData[0], 
    port=connData[1], 
    user = connData[2],
    password= connData[3],
    database= connData[4] )
    return conn

def run_queryMy( MsgSoN,query, parameters = ()):
        result=[]
        try:            
            conn=MySqlConect(CONNDATA)
            cursor = conn.cursor()
            cursor.execute(query, parameters)
            result=cursor.fetchall()
            conn.commit()
            if MsgSoN == 1 :
                MesageBox(1)
            return result 
        except  mysql.connector.Error as e:
            if MsgSoN == 1 :
                print ("Error code:", e.errno)        # error number
                print ("SQLSTATE value:", e.sqlstate) # SQLSTATE value
                print ("Error message:", e.msg)       # error message
                print ("Error:", e)                   # errno, sqlstate, msg values
            return
    
d=DiasAnimal(5,407,'2022-12-01','2023-01-24')

