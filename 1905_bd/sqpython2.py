#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

con=sqlite3.connect("pos_empresa.db")
cursor=con.cursor()
cursor.execute("select product.name, avg(sale_product.net_unit_price) from product join sale_product on sale_product.product_id=product.id group by product.name") # 2) promedio de venta por producto

for i in cursor:
	print "nombre de producto: "+i[0]
	print "promedio de ventas: "+str(i[1])
