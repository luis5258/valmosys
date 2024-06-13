SELECT tblContenedoresMateriaPrima.Cliente, DESCRIP, II, ENTRADAS, SALIDAS,  II+ENTRADAS-SALIDAS AS TOTAL
FROM(
	SELECT ALMACEN AS ALMA, MP.MP_DES AS DESCRIP , MP.Cantidad +
			SUM (CASE WHEN tblMovimientosMP.TipoMov = 0 AND tblMovimientosMP.FechaMov BETWEEN  MP.FECHA_INV  AND DATE(?,'-1 day')  
					AND  tblMovimientosMP.IDAlmacen = MP.ALMACEN	THEN tblMovimientosMP.Cantidad ELSE 0 END) - 
			SUM (CASE WHEN tblMovimientosMP.TipoMov = 1 AND tblMovimientosMP.FechaMov BETWEEN  MP.FECHA_INV  AND DATE(?,'-1 day') 
					AND  tblMovimientosMP.IDAlmacen =  MP.ALMACEN 	THEN tblMovimientosMP.Cantidad ELSE 0 END) AS II,
			SUM (CASE WHEN tblMovimientosMP.TipoMov = 0 AND tblMovimientosMP.FechaMov BETWEEN  ?  AND  ? 
					AND  tblMovimientosMP.IDAlmacen =  MP.ALMACEN	THEN tblMovimientosMP.Cantidad ELSE 0 END) AS ENTRADAS,
			SUM (CASE WHEN tblMovimientosMP.TipoMov = 1 AND tblMovimientosMP.FechaMov BETWEEN  ? AND ?    
					AND  tblMovimientosMP.IDAlmacen =  MP.ALMACEN  THEN tblMovimientosMP.Cantidad ELSE 0 END) AS SALIDAS
					
	FROM (  SELECT IDMP AS IDMP  , tblMateriaPrima.Descripcion  AS MP_DES, MAX(tblInventarioInicialesMP.Fecha) AS FECHA_INV, Cantidad, ? AS ALMACEN
			FROM tblInventarioInicialesMP
			INNER JOIN tblMateriaPrima ON tblMateriaPrima.ID = tblInventarioInicialesMP.IDMP
			WHERE tblInventarioInicialesMP.IDContenedor = ALMACEN 
			GROUP BY IDMP ) AS MP
	LEFT JOIN tblMovimientosMP  ON   tblMovimientosMP.IDMP = MP.IDMP
	GROUP BY MP.IDMP

	) AS PPAL 
INNER JOIN tblContenedoresMateriaPrima ON tblContenedoresMateriaPrima.ID =ALMA
UNION
SELECT tblContenedoresMateriaPrima.Cliente, DESCRIP, II, ENTRADAS, SALIDAS,  II+ENTRADAS-SALIDAS AS TOTAL
FROM(
	SELECT ALMACEN AS ALMA, MP.MP_DES AS DESCRIP , MP.Cantidad +
			SUM (CASE WHEN tblMovimientosMP.TipoMov = 0 AND tblMovimientosMP.FechaMov BETWEEN  MP.FECHA_INV  AND DATE(?,'-1 day')  
					AND  tblMovimientosMP.IDAlmacen = MP.ALMACEN	THEN tblMovimientosMP.Cantidad ELSE 0 END) - 
			SUM (CASE WHEN tblMovimientosMP.TipoMov = 1 AND tblMovimientosMP.FechaMov BETWEEN  MP.FECHA_INV  AND DATE(?,'-1 day') 
					AND  tblMovimientosMP.IDAlmacen =  MP.ALMACEN 	THEN tblMovimientosMP.Cantidad ELSE 0 END) AS II,
			SUM (CASE WHEN tblMovimientosMP.TipoMov = 0 AND tblMovimientosMP.FechaMov BETWEEN  ?  AND  ? 
					AND  tblMovimientosMP.IDAlmacen =  MP.ALMACEN	THEN tblMovimientosMP.Cantidad ELSE 0 END) AS ENTRADAS,
			SUM (CASE WHEN tblMovimientosMP.TipoMov = 1 AND tblMovimientosMP.FechaMov BETWEEN  ? AND ?    
					AND  tblMovimientosMP.IDAlmacen =  MP.ALMACEN  THEN tblMovimientosMP.Cantidad ELSE 0 END) AS SALIDAS
					
	FROM (  SELECT IDMP AS IDMP  , tblMateriaPrima.Descripcion  AS MP_DES, MAX(tblInventarioInicialesMP.Fecha) AS FECHA_INV, Cantidad, ? AS ALMACEN
			FROM tblInventarioInicialesMP
			INNER JOIN tblMateriaPrima ON tblMateriaPrima.ID = tblInventarioInicialesMP.IDMP
			WHERE tblInventarioInicialesMP.IDContenedor = ALMACEN 
			GROUP BY IDMP ) AS MP
	LEFT JOIN tblMovimientosMP  ON   tblMovimientosMP.IDMP = MP.IDMP
	GROUP BY MP.IDMP

	) AS PPAL 
INNER JOIN tblContenedoresMateriaPrima ON tblContenedoresMateriaPrima.ID =ALMA
UNION
SELECT tblContenedoresMateriaPrima.Cliente, DESCRIP, II, ENTRADAS, SALIDAS,  II+ENTRADAS-SALIDAS AS TOTAL
FROM(
	SELECT ALMACEN AS ALMA, MP.MP_DES AS DESCRIP , MP.Cantidad +
			SUM (CASE WHEN tblMovimientosMP.TipoMov = 0 AND tblMovimientosMP.FechaMov BETWEEN  MP.FECHA_INV  AND DATE(?,'-1 day')  
					AND  tblMovimientosMP.IDAlmacen = MP.ALMACEN	THEN tblMovimientosMP.Cantidad ELSE 0 END) - 
			SUM (CASE WHEN tblMovimientosMP.TipoMov = 1 AND tblMovimientosMP.FechaMov BETWEEN  MP.FECHA_INV  AND DATE(?,'-1 day') 
					AND  tblMovimientosMP.IDAlmacen =  MP.ALMACEN 	THEN tblMovimientosMP.Cantidad ELSE 0 END) AS II,
			SUM (CASE WHEN tblMovimientosMP.TipoMov = 0 AND tblMovimientosMP.FechaMov BETWEEN  ?  AND  ? 
					AND  tblMovimientosMP.IDAlmacen =  MP.ALMACEN	THEN tblMovimientosMP.Cantidad ELSE 0 END) AS ENTRADAS,
			SUM (CASE WHEN tblMovimientosMP.TipoMov = 1 AND tblMovimientosMP.FechaMov BETWEEN  ? AND ?    
					AND  tblMovimientosMP.IDAlmacen =  MP.ALMACEN  THEN tblMovimientosMP.Cantidad ELSE 0 END) AS SALIDAS
					
	FROM (  SELECT IDMP AS IDMP  , tblMateriaPrima.Descripcion  AS MP_DES, MAX(tblInventarioInicialesMP.Fecha) AS FECHA_INV, Cantidad, ? AS ALMACEN
			FROM tblInventarioInicialesMP
			INNER JOIN tblMateriaPrima ON tblMateriaPrima.ID = tblInventarioInicialesMP.IDMP
			WHERE tblInventarioInicialesMP.IDContenedor = ALMACEN 
			GROUP BY IDMP ) AS MP
	LEFT JOIN tblMovimientosMP  ON   tblMovimientosMP.IDMP = MP.IDMP
	GROUP BY MP.IDMP

	) AS PPAL 
INNER JOIN tblContenedoresMateriaPrima ON tblContenedoresMateriaPrima.ID =ALMA

--------------------------------------------------------------------------------------------
SELECT tblContenedoresMateriaPrima.Cliente, DESCRIP, II, ENTRADAS, SALIDAS,  II+ENTRADAS-SALIDAS AS TOTAL
FROM(
	SELECT ALMACEN AS ALMA, MP.MP_DES AS DESCRIP , MP.Cantidad +
			SUM (CASE WHEN tblMovimientosMP.TipoMov = 0 AND tblMovimientosMP.FechaMov BETWEEN  MP.FECHA_INV  AND DATE(FECHA_INI,'-1 day')  
					AND  tblMovimientosMP.IDAlmacen = MP.ALMACEN	THEN tblMovimientosMP.Cantidad ELSE 0 END) - 
			SUM (CASE WHEN tblMovimientosMP.TipoMov = 1 AND tblMovimientosMP.FechaMov BETWEEN  MP.FECHA_INV  AND DATE(FECHA_INI,'-1 day') 
					AND  tblMovimientosMP.IDAlmacen =  MP.ALMACEN 	THEN tblMovimientosMP.Cantidad ELSE 0 END) AS II,
			SUM (CASE WHEN tblMovimientosMP.TipoMov = 0 AND tblMovimientosMP.FechaMov BETWEEN  FECHA_INI  AND  FECHA_FIN
					AND  tblMovimientosMP.IDAlmacen =  MP.ALMACEN	THEN tblMovimientosMP.Cantidad ELSE 0 END) AS ENTRADAS,
			SUM (CASE WHEN tblMovimientosMP.TipoMov = 1 AND tblMovimientosMP.FechaMov BETWEEN  FECHA_INI AND FECHA_FIN    
					AND  tblMovimientosMP.IDAlmacen =  MP.ALMACEN  THEN tblMovimientosMP.Cantidad ELSE 0 END) AS SALIDAS
					
	FROM (  SELECT IDMP AS IDMP  , tblMateriaPrima.Descripcion  AS MP_DES, MAX(tblInventarioInicialesMP.Fecha) AS FECHA_INV, Cantidad, 3 AS ALMACEN,'2022-04-01' AS FECHA_INI,
	        '2022-06-01' AS FECHA_FIN
			FROM tblInventarioInicialesMP
			INNER JOIN tblMateriaPrima ON tblMateriaPrima.ID = tblInventarioInicialesMP.IDMP
			WHERE tblInventarioInicialesMP.IDContenedor = ALMACEN 
			GROUP BY IDMP ) AS MP
	LEFT JOIN tblMovimientosMP  ON   tblMovimientosMP.IDMP = MP.IDMP
	GROUP BY MP.IDMP

	) AS PPAL 
INNER JOIN tblContenedoresMateriaPrima ON tblContenedoresMateriaPrima.ID =ALMA
----------------------------------------------------------------------------------------------------



SELECT TT.CORRAL, TT.FECHA_ASIGNA, TT.ENTRADAS, TT.SALIDAS, TT.ENTRADAS-TT.SALIDAS AS TOTA
FROM (  SELECT  tblCorrales.Descripcion AS CORRAL ,tblCorrales.FechaAsigna AS FECHA_ASIGNA, '2022-06-01' AS FECHA, 15 AS CLIENTE,
			SUM(case WHEN  tblMovimientoAnimales.IDMovimiento = 0 AND tblMovimientoAnimales.Fecha BETWEEN tblCorrales.FechaAsigna AND FECHA THEN  tblMovimientoAnimales.Cantidad ELSE 0 END) AS ENTRADAS,
			SUM(case WHEN  tblMovimientoAnimales.IDMovimiento = 1 AND tblMovimientoAnimales.Fecha  BETWEEN tblCorrales.FechaAsigna AND FECHA THEN  tblMovimientoAnimales.Cantidad   ELSE 0 END) AS SALIDAS
			
		FROM  tblMovimientoAnimales
		INNER JOIN tblClientes ON tblClientes.ID = tblMovimientoAnimales.IDCliente 
		INNER JOIN tblCorrales ON  tblCorrales.ID = tblMovimientoAnimales.IDCorral
		WHERE  tblMovimientoAnimales.IDCorral IN   (SELECT  tblCorrales.ID   FROM tblCorrales WHERE AsignACliente = CLIENTE ) AND tblMovimientoAnimales.IDCliente = CLIENTE
		GROUP BY tblMovimientoAnimales.IDCorral
		) AS  TT
ORDER BY TT.CORRAL