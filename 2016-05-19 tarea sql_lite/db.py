import sqlite3
conn = sqlite3.connect('pos_empresa.db')

cursor = conn.execute('SELECT SUM(gross_total) as "Suma 2013" FROM sale WHERE [date] LIKE "2013%";')
for row in cursor:
	print 'Total entre "2013-01-01" y "2014-01-01"'
	print str(row[0])

cursor = conn.execute('SELECT AVG(net_unit_price), product_id FROM sale_product GROUP BY product_id LIMIT 20;')
print '\n"Promedio de venta" ,"producto"'
for row in cursor:
	print str(row[0])+"  ,  "+str(row[1])

cursor = conn.execute('SELECT entity_id,SUM(gross_total) FROM sale GROUP BY entity_id LIMIT 20')
print '\n"Cliente" ,"precio total" (limite 20)'
for row in cursor:
	print str(row[0])+"  ,  "+str(row[1])

cursor = conn.execute('SELECT entity_id,SUM(gross_total) FROM sale WHERE [date] LIKE "2014%" GROUP BY entity_id LIMIT 20')
print '\n"Cliente" ,"precio total"   2014(limite 20)'
for row in cursor:
	print str(row[0])+"  ,  "+str(row[1])

cursor = conn.execute('SELECT COUNT(*), SUM(gross_total), [date]\
					   FROM sale\
					   WHERE [date] BETWEEN "2013-11-01" AND "2013-11-30"\
					   GROUP BY [date]\
					   ORDER BY [date];')
print '\n"Num de ventas  ,  monto total  ,  fecha (solo noviembre 2013 por dia)"'
for row in cursor:
	print str(row[0])+"  ,  "+str(row[1])+"  ,  "+str(row[2])
