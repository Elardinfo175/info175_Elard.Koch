#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

con=sqlite3.connect("pos_empresa.db")
cursor=con.cursor()
cursor.execute("select entity.names,entity.company_name, sum(sale.gross_total) from entity join sale on sale.entity_id=entity.id group by entity.id") #3) total de ventas por cliente
for i in cursor:
	if(len(i[0])==0):
		print "nombre cliente compañia: "+str(i[1])
	else:
		print "nombre de cliente: "+str(i[0])
	print "total de ventas: "+str(i[2]) 
