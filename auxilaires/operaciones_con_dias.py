import datetime

import sys
ahora = datetime.datetime.utcnow()
print(ahora)
NoDias=31
ayer = ahora + datetime.timedelta(days=NoDias)
print(ayer)
#FechaInicial = datetime.strptime(ahora, '%Y-%m-%d')
# print(FechaInicial)
 for i in