import mysql.connector as mysql
import xml.etree.cElementTree as ET
from xml.dom import minidom

global config,connection

connection = None

config = {
	'host' : '127.0.0.1',
	'user' : 'root',
	'password' : '',
	'database' : 'biblia'
}


def initConnection():
	global connection,config
	try:
		connection = mysql.connect(**config)
	except mysql.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something is wrong with your user name or password")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database does not exist")
		else:
			print(err)

def prettify(elem):
	rough_string = ET.tostring(elem, 'utf-8')
	reparsed = minidom.parseString(rough_string)
	preformat = reparsed.toprettyxml(indent="	")
	preformat = preformat.replace("{\\cf6 ","")
	preformat = preformat.replace("{\\cf6","")
	preformat = preformat.replace("{\\b","")
	preformat = preformat.replace("{","")
	preformat = preformat.replace("}","")
	return preformat


def work():
	global cursor,connection
	root_attibutes = {
		'xmlns:xsi':'http://www.w3.org/2001/XMLSchema-instance',
		'biblename':'Reina Valera 1960'
	}
	root = ET.Element("XMLBIBLE",root_attibutes)
	try:
		cursor1 = connection.cursor()
		query1 = "SELECT idBook,name FROM bible_books"
		cursor1.execute(query1)
		for book in cursor1:
			child_attributes = {
				'bnumber' : str(book[0]),
				'bname': book[1]
			}
			child = ET.SubElement(root,"BIBLEBOOK",child_attributes)
			local_connection_1 = mysql.connect(**config)
			local_cursor_1 = local_connection_1.cursor()
			local_query_1 = "SELECT MAX(chapter) FROM bible_verses WHERE idBook = " + str(book[0])
			local_cursor_1.execute(local_query_1)
			AMOUNT_OF_CHAPTERS = 0
			for tmp in local_cursor_1:
				AMOUNT_OF_CHAPTERS = tmp[0]

			for i in range(1,AMOUNT_OF_CHAPTERS+1):
				subchild_attributes = {
					'cnumber' : str(i)
				}
				subchild = ET.SubElement(child,"CHAPTER",subchild_attributes)


				local_connection_2 = mysql.connect(**config)
				local_cursor_2 = local_connection_2.cursor()
				local_query_2 = "SELECT * FROM bible_verses WHERE idBible = 1 AND idBook = " + str(book[0]) + " AND chapter = " + str(i)
				local_cursor_2.execute(local_query_2)
				for verse in local_cursor_2:
					subsubchild_attribute = {
						'vnumber' : str(verse[4])
					}
					subsubchild = ET.SubElement(subchild,"VERS",subsubchild_attribute)
					subsubchild.text = verse[5]

				local_cursor_2.close()
				local_connection_2.close()		

			local_cursor_1.close()
			local_connection_1.close()
			

		cursor1.close()
		connection.close()
	
		with open('BibliaRVR1960.xml', 'w') as file:
			file.write(prettify(root))

	except mysql.Error as err:
		print(err)

def main():
	initConnection()
	work()
	print("Done!")

main()