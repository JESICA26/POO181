#importacion del framework

from flask import Flask

from flask_mysqldb import MySQL

 #Inicializacion del APP
app=Flask(__name__)

#Configuracion de la conexion 

app.config ['MYSQL_HOST']='localhost'
app.config ['MYSQL_USER']='root'
app.config ['MYSQL_PASSWORD']=''
app.config ['MYSQL_DB']='dbflask'
mysql=MySQL(app)



 #Declaracion de la ruta http://localhost:5000
@app.route('/')
def index():
    return "Hola mundo FLASK"


@app.route('/guardar')
def guardar():
    return "Se guardo en la base de datos"



@app.route('/eliminar')
def eliminar():
    return "Se elimino en la BD"






 #ejecucion del servidor en el puerto 5000
if __name__ =='__main__':
    app.run(port=5000)


