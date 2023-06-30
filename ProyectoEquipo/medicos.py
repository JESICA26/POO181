#importacion del framework
from flask import Flask, render_template, request,redirect,url_for,flash
from flask_mysqldb import MySQL

#Inicializacion del APP
app= Flask (__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='Medicos'
app.secret_key= 'mysecrety'
mysql= MySQL(app)

#Declaracion de ruta http://localhost:5000
@app.route('/')
def medicos():
  
  return render_template('Medicos.html')


#rura http:localhost:5000/guardar tipo POST para insert
@app.route('/guardar',methods=['POST'])
def guardar():
  if request.method == 'POST':

    # pasamos a variables el contenido de los input
    Vnombre=request.form['txtNombre']
    Vapellidop=request.form['textAp']
    Vapellidom=request.form['txtAm']
    Vrfc=request.form['textRFC']
    Vcorreo=request.form['txtCorreo']
    Vcontraseña=request.form['textcontrasena']
    Vrolid=request.form['txtid_rol']

    #Conectar y ejecutar el insert
    cs= mysql.connection.cursor()
    cs.execute('insert into medicos (nombre,ap,am,rfc,correo_electronico,contraseña,id_rol) values(%s,%s,%s,%s,%s,%s,%s)',(Vnombre,Vapellidop,Vapellidom,Vrfc,Vcorreo,Vcontraseña,Vrolid))
    mysql.connection.commit()

  flash('Se agrego correctamente')
  return redirect(url_for('medicos'))


@app.route('/eliminar')
def eliminar():
  
 return "Se elimino en la BD"

#Ejecucion del servidor en el puerto 5000
if __name__ == '_main_':
  app.run(port=5000,debug=True)