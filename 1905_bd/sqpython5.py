#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

con=sqlite3.connect("pos_empresa.db")
cursor=con.cursor()
cursor.execute("select sale.date,sum(sale_product.quantity),sum(sale.gross_total) from sale join sale_product on sale.id= sale_product.id where date like '2013-11%' group by date") #5) monto total de ventas por dia en noviembre del 2013
for i in cursor:
	print "Fecha :"+i[0]
	print "cantidad de ventas: "+str(i[1])
	print "Monto total de ventas: "+str(i[2])

