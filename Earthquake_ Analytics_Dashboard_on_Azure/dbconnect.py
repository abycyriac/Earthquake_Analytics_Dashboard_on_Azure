import pyodbc

server = ''
database = ''
username = ''
password = ''
driver = '{ODBC Driver 17 for SQL Server}'
try:
    connect = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
except Exception as e:
	print(e)
	connect = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)