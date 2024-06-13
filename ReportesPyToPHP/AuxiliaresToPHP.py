import sys,sqlite3
import mysql.connector


def RepsLiquidacion(NoRep,cliente,FechaInicial,FechaFinal):
    query=""
    if NoRep == '1':
        query= """
            SELECT tblCorrales.Descripcion, tblProductos.Descripcion, tblProductos.UdeM, SUM(tblDetalleOrdenSurtido.CantSurtida)
            FROM tblDetalleOrdenSurtido
            INNER JOIN tblOrdenesSurtido ON tblDetalleOrdenSurtido.IDOrden=tblOrdenesSurtido.ID
            INNER JOIN tblProductos ON  tblOrdenesSurtido.IDProducto= tblProductos.ID
            INNER JOIN tblCorrales ON tblDetalleOrdenSurtido.IDCorral = tblCorrales.ID          
            WHERE  tblDetalleOrdenSurtido.IDCliente = ?  AND  (tblDetalleOrdenSurtido.Fecha BETWEEN ? AND ? )
            GROUP BY  tblProductos.Descripcion,tblDetalleOrdenSurtido.IDCorral 
            ORDER BY tblCorrales.Descripcion
            """
    elif NoRep ==  '3':
        query= """
                SELECT tblProductos.Descripcion,tblProductos.UdeM, SUM(tblDetalleOrdenSurtido.CantSurtida),tblProductos.PU
                FROM tblDetalleOrdenSurtido
                INNER JOIN tblOrdenesSurtido ON tblDetalleOrdenSurtido.IDOrden=tblOrdenesSurtido.ID
                INNER JOIN tblProductos ON  tblOrdenesSurtido.IDProducto= tblProductos.ID
                WHERE  tblDetalleOrdenSurtido.IDCliente = ?  AND  (tblDetalleOrdenSurtido.Fecha BETWEEN ? AND ? )
                GROUP BY  tblProductos.ID
                ORDER BY  tblProductos.Descripcion
               """
    else :
        return -1
    #Datos=run_query2(query,(cliente,FechaInicial,FechaFinal))
    Datos=runMySqlQuery(query,(cliente,FechaInicial,FechaFinal))
    DatosToRep=[]
    ListaTem=[]
    for ren in range(0,len(Datos)):
        for col in range(0,len(Datos[0])):
            DaToTabla=str(Datos[ren][col])
            if col == 6 or col == 7:
                DaToTabla='{:.2f}'.format(Datos[ren][col])
            ListaTem.append(DaToTabla)
        DatosToRep.append(ListaTem)
        ListaTem=[]
    for i in DatosToRep:
        print(i)
    return DatosToRep

def Reporte2(cliente,FechaInicial,FechaFinal):
        query= """
                SELECT  tblCorrales.Descripcion, SUM(tblDetalleOrdenSurtido.CantSurtida),tblCorrales.ID
                FROM tblDetalleOrdenSurtido
                INNER JOIN 	tblCorrales ON  tblDetalleOrdenSurtido.IDCorral = tblCorrales.ID
                WHERE  tblDetalleOrdenSurtido.IDCliente = ?  AND  (tblDetalleOrdenSurtido.Fecha BETWEEN ? AND ? )
                GROUP BY  tblDetalleOrdenSurtido.IDCorral
                ORDER BY  tblCorrales.Descripcion
                """
        #Data=run_query2(query,(cliente,FechaInicial,FechaFinal))
        Data=runMySqlQuery(query,(cliente,FechaInicial,FechaFinal))
        ListaTem=[]
        Datos=[]
        
        
        for i in range(0,len(Data)):
            ListaTem.append(Data[i][0])
            ListaTem.append(Data[i][1])
            DiasAnimal=CalculaDiasAnimal(cliente,Data[i][2],FechaInicial,FechaFinal)
            DiasAnimFomated="{:.0f}".format(DiasAnimal)
            if DiasAnimal < 1 :
                DiasAnimal=1
                ToTab="ND"
            else :
                ToTab=DiasAnimFomated
            
            ListaTem.append(ToTab)
            PromDia=int(Data[i][1])/int(DiasAnimal)
            PromDia="{:.4f}".format(PromDia)
            ListaTem.append(PromDia)
            Datos.append(ListaTem)
            ListaTem=[]
        
        ListaTem=[]
        DataToRep=[]
        for ren in range(0,len(Datos)):
            for col in range(0,len(Datos[0])):
                DaToTabla=str(Datos[ren][col])
                ListaTem.append(DaToTabla)
            DataToRep.append(ListaTem)
            ListaTem=[]
        for i in DataToRep:
            print(i)
        return DataToRep


def run_query2( query, parameters = ()):
        conn=sqlite3.connect("valmodb") 
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        result=cursor.fetchall()
        conn.commit()
        return result

def runMySqlQuery(query, parameters = () ):
        mydb = mysql.connector.connect(host="root",#user="yourusername",#password="yourpassword",
        database="sistemas" )
        cursor=mydb.cursor()
        cursor.execute(query, parameters)
        result=cursor.fetchall()
        mydb.commit()
        return result



#  Calcula los dias animal en rango de fecha de un solo corral
def CalculaDiasAnimal(IDCliente,IDCorral,FechaInicial,FechaFinal):
    ListaTem=[]
    ListaForRet=[]
    FechasOcupa=RangoFechasOcupaCorral(IDCorral,IDCliente)
    if FechasOcupa[0][1] == 0:
        pass
    else :
        if FechasOcupa[0][1] < FechaFinal :
            FechaFinal=FechasOcupa[0][1]
    # -----------------------------------------------------------------------
    ListaFechas=GeneraListaFechas(FechaInicial,FechaFinal)
    AcuDiasAnimal=0
    for i, fecha in enumerate(ListaFechas):
            ListaTem.append(fecha)
            ListaTem.append(CantidadActualAnimales(IDCorral,fecha))
            ListaForRet.append(ListaTem)
            ListaTem=[]
    for d, item in enumerate(ListaForRet):
        if int(item[1]) > -1 :
           AcuDiasAnimal=AcuDiasAnimal+int(item[1])
    return AcuDiasAnimal

#  Saca el rango de fechas de cuando se asigno y libero un corral con un cliente, si el segundo dato es 0 significa que sigue asignado
#  al cliente. si es diferente de 0 es la ultima fecha cuando se libero a este cliente
def RangoFechasOcupaCorral(IDCorral,IDCliente):
    query= """  SELECT FECHAS.FECHA_ASIGNA, 
                    (SELECT (CASE WHEN FECHAS.FECHA_LIBERA > FECHAS.FECHA_ASIGNA THEN FECHAS.FECHA_LIBERA ELSE 0 END)) AS FECHA_LIBERA
                FROM (
                        SELECT 
                        MAX ( CASE WHEN tblAsignaCorrales.IDCorral = ? AND tblAsignaCorrales.IDCliente= ?  AND tblAsignaCorrales.TipoMov = 1  
                        THEN tblAsignaCorrales.Fecha ELSE 0 END) AS FECHA_ASIGNA,
	                    MAX ( CASE WHEN tblAsignaCorrales.IDCorral = ? AND tblAsignaCorrales.IDCliente= ?  AND tblAsignaCorrales.TipoMov = 0  
                        THEN tblAsignaCorrales.Fecha ELSE 0 END) AS FECHA_LIBERA
                        FROM tblAsignaCorrales 
                     ) AS FECHAS
            """
    Datos=run_query2(query,(IDCorral,IDCliente,IDCorral,IDCliente))
    return Datos

#  Genera una lista de fechas a partir de una inicial y final
def GeneraListaFechas(fi,ff):
    from datetime import datetime
    from datetime import timedelta
    import sys
    FechaInicial = datetime.strptime(fi, '%Y-%m-%d')
    FechaFinal = datetime.strptime(ff, '%Y-%m-%d')
    Fecha=FechaInicial
    ListaFechas=[datetime.strftime(Fecha, '%Y-%m-%d'),]
    cnt=0
    while Fecha != FechaFinal:
        cnt+=1
        if cnt > 30 :
            break
        Fecha=Fecha + timedelta(days=1)
        ListaFechas.append(datetime.strftime(Fecha, '%Y-%m-%d'))
    return ListaFechas    

#   Obtiene  la cantidad de animales en el corral desde la fecha de asignacion hasta la fecha proporcionada

def CantidadActualAnimales(IDCorral,fecha):
    query=  """ SELECT  SUM(case WHEN  tblMovimientoAnimales.IDMovimiento = 0  THEN  tblMovimientoAnimales.Cantidad ELSE 0 END) -
                       SUM(case WHEN  tblMovimientoAnimales.IDMovimiento = 1  THEN  tblMovimientoAnimales.Cantidad  ELSE 0 END) AS SUMA
                FROM tblMovimientoAnimales 
                WHERE tblMovimientoAnimales.IDCorral= ?  AND tblMovimientoAnimales.Fecha BETWEEN 
                (SELECT FechaAsigna FROM tblCorrales WHERE ID=? ) AND ?
            """
    Cantidad=run_query2(query,(IDCorral,IDCorral,fecha))
    if Cantidad[0][0] is None :
        return -1
    else:
        return Cantidad[0][0]
