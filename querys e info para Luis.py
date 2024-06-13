
# Lista Los movimientos de Materias primas  en un rango de fechas el primero todas y el segundo fecha y almacen


if self.ui.RBotTodos.isChecked() :
           
            query=  """     SELECT  tblMovimientosMP.Folio, tblMovimientosMP.FechaMov, tblTipoMov.Descripcion, tblMateriaPrima.Descripcion,
                                    tblMovimientosMP.Cantidad, tblContenedoresMateriaPrima.Cliente, tblMovimientosMP.Notas
                            FROM tblMovimientosMP
                            INNER JOIN tblTipoMov ON tblTipoMov.ID = tblMovimientosMP.TipoMov
                            INNER JOIN tblMateriaPrima ON tblMateriaPrima.ID = tblMovimientosMP.IDMP
                            INNER JOIN tblContenedoresMateriaPrima ON tblContenedoresMateriaPrima.ID = tblMovimientosMP.IDAlmacen 
                            WHERE (tblMovimientosMP.FechaMov  BETWEEN ? AND ? )
                            ORDER BY FechaMov
                    """
            Datos=run_query2(self,query,(FechaInicial,FechaFinal)) 
            
        elif self.ui.RBotAlmacen.isChecked():
            query=  """     SELECT  tblMovimientosMP.Folio, tblMovimientosMP.FechaMov, tblTipoMov.Descripcion, tblMateriaPrima.Descripcion,
                                    tblMovimientosMP.Cantidad, tblContenedoresMateriaPrima.Cliente, tblMovimientosMP.Notas
                            FROM tblMovimientosMP
                            INNER JOIN tblTipoMov ON tblTipoMov.ID = tblMovimientosMP.TipoMov
                            INNER JOIN tblMateriaPrima ON tblMateriaPrima.ID = tblMovimientosMP.IDMP
                            INNER JOIN tblContenedoresMateriaPrima ON tblContenedoresMateriaPrima.ID = tblMovimientosMP.IDAlmacen 
                            WHERE (tblMovimientosMP.FechaMov  BETWEEN ? AND ? ) AND  tblMovimientosMP.IDAlmacen= ?
                            ORDER BY FechaMov
                   """
            Datos=run_query2(self,query,(FechaInicial,FechaFinal,Almacen))
        self.LlenaTabla(Datos)

# Saca lista de las materias primas en el almacen seleccionado.
        query=  """ SELECT  DESCRIP, II, ENTRADAS, SALIDAS,  II+ENTRADAS-SALIDAS AS TOTAL
                    FROM(
                        SELECT  MP.MP_DES AS DESCRIP , MP.Cantidad +
                                SUM (CASE WHEN tblMovimientosMP.TipoMov = 0 AND tblMovimientosMP.FechaMov BETWEEN  MP.FECHA_INV  AND DATE(?,'-1 day')  
	                                    AND  tblMovimientosMP.IDAlmacen = MP.ALMACEN	THEN tblMovimientosMP.Cantidad ELSE 0 END) - 
                                SUM (CASE WHEN tblMovimientosMP.TipoMov = 1 AND tblMovimientosMP.FechaMov BETWEEN  MP.FECHA_INV  AND DATE(?,'-1 day') 
	                                    AND  tblMovimientosMP.IDAlmacen =  MP.ALMACEN 	THEN tblMovimientosMP.Cantidad ELSE 0 END) AS II,
                                SUM (CASE WHEN tblMovimientosMP.TipoMov = 0 AND tblMovimientosMP.FechaMov BETWEEN  ?  AND  ?  
	                                    AND  tblMovimientosMP.IDAlmacen =  MP.ALMACEN	THEN tblMovimientosMP.Cantidad ELSE 0 END) AS ENTRADAS,
		                        SUM (CASE WHEN tblMovimientosMP.TipoMov = 1 AND tblMovimientosMP.FechaMov BETWEEN  ?  AND ?   
		                                AND  tblMovimientosMP.IDAlmacen =  MP.ALMACEN  THEN tblMovimientosMP.Cantidad ELSE 0 END) AS SALIDAS
		                FROM (  SELECT IDMP AS IDMP  , tblMateriaPrima.Descripcion  AS MP_DES, MAX(tblInventarioInicialesMP.Fecha) AS FECHA_INV, Cantidad, ? AS ALMACEN
                                FROM tblInventarioInicialesMP
                                INNER JOIN tblMateriaPrima ON tblMateriaPrima.ID = tblInventarioInicialesMP.IDMP
                                WHERE tblInventarioInicialesMP.IDContenedor = ALMACEN 
                                GROUP BY IDMP ) AS MP
                        LEFT JOIN tblMovimientosMP  ON   tblMovimientosMP.IDMP = MP.IDMP
                        GROUP BY MP.IDMP
                        ) AS PPAL
                """
        DaQu=(FechaInicial,FechaInicial,FechaInicial, FechaFinal,FechaInicial, FechaFinal,Almacen)
        ListaToTable=run_query2(self,query,DaQu)