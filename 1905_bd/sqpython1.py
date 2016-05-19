#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

con=sqlite3.connect("pos_empresa.db")
cursor=con.cursor()
cursor.execute("select sum(gross_total) as suma_total_de_ventas from sale where date like '2013%'") # 1) suma total de ventas en el año 2013
for i in cursor:
	print "total de ventas en 2013 fue: "+str(i)
