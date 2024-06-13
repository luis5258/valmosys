SELECT TT.CORRAL, TT.FECHA, TT.ENTRADAS, TT.SALIDAS, TT.ENTRADAS-TT.SALIDAS AS TOTA
FROM (  SELECT  tblCorrales.Descripcion AS CORRAL ,tblCorrales.FechaAsigna AS FECHA,
			SUM(case WHEN  tblMovimientoAnimales.IDMovimiento = 0 AND tblMovimientoAnimales.Fecha BETWEEN tblCorrales.FechaAsigna AND '2022-07-05' THEN  tblMovimientoAnimales.Cantidad ELSE 0 END) AS ENTRADAS,
			SUM(case WHEN  tblMovimientoAnimales.IDMovimiento = 1 AND tblMovimientoAnimales.Fecha  BETWEEN tblCorrales.FechaAsigna AND '2022-07-05' THEN  tblMovimientoAnimales.Cantidad   ELSE 0 END) AS SALIDAS
			
		FROM  tblMovimientoAnimales
		INNER JOIN tblClientes ON tblClientes.ID = tblMovimientoAnimales.IDCliente 
		INNER JOIN tblCorrales ON  tblCorrales.ID = tblMovimientoAnimales.IDCorral
		WHERE  tblMovimientoAnimales.IDCorral IN   (SELECT  tblCorrales.ID   FROM tblCorrales WHERE AsignACliente = 3 ) AND tblMovimientoAnimales.IDCliente = 3
		GROUP BY tblMovimientoAnimales.IDCorral
		) AS  TT
ORDER BY TT.CORRAL

SELECT TT.CLIENTE.TT, CORRAL,  TT.ENTRADAS-TT.SALIDAS AS TOTA
FROM (  SELECT  tblCorrales.Descripcion AS CORRAL ,tblCorrales.FechaAsigna AS FECHA, tblClientes.Nombre AS CLIENTE,
			SUM(case WHEN  tblMovimientoAnimales.IDMovimiento = 0 AND tblMovimientoAnimales.Fecha BETWEEN tblCorrales.FechaAsigna AND '2022-07-05' THEN  tblMovimientoAnimales.Cantidad ELSE 0 END) AS ENTRADAS,
			SUM(case WHEN  tblMovimientoAnimales.IDMovimiento = 1 AND tblMovimientoAnimales.Fecha  BETWEEN tblCorrales.FechaAsigna AND '2022-07-05' THEN  tblMovimientoAnimales.Cantidad   ELSE 0 END) AS SALIDAS
			
		FROM  tblMovimientoAnimales
		INNER JOIN tblClientes ON tblClientes.ID = tblMovimientoAnimales.IDCliente 
		INNER JOIN tblCorrales ON  tblCorrales.ID = tblMovimientoAnimales.IDCorral
		WHERE  tblMovimientoAnimales.IDCorral IN   (SELECT  tblCorrales.ID   FROM tblCorrales WHERE AsignACliente = 3 ) AND tblMovimientoAnimales.IDCliente = 3
		GROUP BY tblMovimientoAnimales.IDCorral
		) AS  TT
		
ORDER BY TT.CORRAL

SELECT ID  FROM  tblClientes WHERE tblClientes.ID 
IN ( SELECT tblCorrales.AsignACliente FROM tblCorrales WHERE tblCorrales.AsignACliente > 0 )
ORDER BY Nombre
-------------------------------------------------------------


SELECT  tblClientes.Nombre AS CLIENTE, tblCorrales.Descripcion AS CORRAL,
        SUM(case WHEN  tblMovimientoAnimales.IDMovimiento = 0 AND tblMovimientoAnimales.Fecha BETWEEN tblCorrales.FechaAsigna AND '2022-07-05' THEN  tblMovimientoAnimales.Cantidad ELSE 0 END) -
		SUM(case WHEN  tblMovimientoAnimales.IDMovimiento = 1 AND tblMovimientoAnimales.Fecha  BETWEEN tblCorrales.FechaAsigna AND '2022-07-05' THEN  tblMovimientoAnimales.Cantidad   ELSE 0 END) AS SUBTOTAL
FROM  tblMovimientoAnimales
INNER JOIN tblClientes ON tblClientes.ID = tblMovimientoAnimales.IDCliente 
INNER JOIN tblCorrales ON  tblCorrales.ID = tblMovimientoAnimales.IDCorral
WHERE  tblMovimientoAnimales.IDCorral IN   (SELECT  tblCorrales.ID   FROM tblCorrales WHERE AsignACliente >  0 ) 
GROUP BY tblMovimientoAnimales.IDCorral,CLIENTE 
order by CLIENTE
;


INNER JOIN tblClientes ON tblClientes.ID = IDCORRAL 