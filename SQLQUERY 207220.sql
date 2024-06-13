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

