#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

con=sqlite3.connect("pos_empresa.db")
cursor=con.cursor()
cursor.execute("select product.name, sum(sale_product.quantity),sum(sale_product.gross_total) from sale_product join product on sale_product.product_id=product.id  group by product.name order by sum(sale_product.quantity) desc;") #6) Cantidad y montos totales agrupados por producto en orden descendente según cantidad
for i in cursor:
	print "Nombre de producto :"+i[0]
	print "cantidad total del producto :"+str(i[1])
	print "monto total del producto :"+str(i[2])
