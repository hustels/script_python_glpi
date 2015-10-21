# -*- coding: utf-8 -*-
import xlrd
import mysql.connector
file = 'files/activos.xlsx'

workbook = xlrd.open_workbook(file , encoding_override="utf-8") # Abrir el archivo excel
sheet = workbook.sheet_by_index(0)# Eliger la hoja con el que vamos a trabajar
sheet.cell_value(2,2) # index del valor fila e index del valor columna
#print sheet.nrows #numero de filas
#print sheet.ncols #numero de columnas



		
#Database connection
conn = mysql.connector.connect(user='root', password='root' , host='localhost' , database='compras')
# Crear el cursor
myCursor = conn.cursor()


data = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]#List Comprehensions
f =sheet.cell_value(2,6)
fc = xlrd.xldate_as_tuple(f , 0)
import datetime
datetime.date(fc[0] , fc[1],fc[2])


def insertData():
	for row in range(sheet.nrows):

		try:
			id = row
			peticionario= sheet.cell_value(row , 2)
			num_serie = sheet.cell_value(row  , 4)
			#fecha_compra= sheet.cell_value(row ,6 )
		   	date = sheet.cell_value(row ,6)
			datetuple = xlrd.xldate_as_tuple(date , 0)
			dtime = datetime.date(datetuple[0] , datetuple[1], datetuple[2])
			myCursor.execute("""  INSERT INTO ordenadores VALUES ('%s' ,'%s' ,'%s' , '%s') """ % (id , peticionario , num_serie,dtime)) 
			conn.commit()
			print num_serie
		except ValueError:
		   pass 
		
	print 'Insertados los datos '		


def deleteData():
	for row in range(sheet.nrows):
		myCursor.execute("DELETE FROM ordenadores WHERE id=%s " % row) 
		conn.commit()


	print 'Borrados los datos'
		
def updateData():
		for row in range(sheet.nrows):

			try:
				id = row
				peticionario= sheet.cell_value(row , 2)
				num_serie = sheet.cell_value(row  , 4)
				#fecha_compra= sheet.cell_value(row ,6 )
			   	date = sheet.cell_value(row ,6)
				datetuple = xlrd.xldate_as_tuple(date , 0)
				dtime = datetime.date(datetuple[0] , datetuple[1], datetuple[2])
				query =("""  UPDATE ordenadores SET fecha_compra='%s'  WHERE num_serie='%s' """ % ( dtime,num_serie))
				myCursor.execute(query)
				#print ("affected rows = {}".format(myCursor.rowcount))
				conn.commit()

			except ValueError:
			   pass 
		print 'Actualizados';
updateData()

