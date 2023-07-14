#Importacion del framework
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

#Inicializacion del Servidor
app=Flask(__name__)

#Configuracion de la conexion
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='dbFruteria'
app.secret_key='mysecretkey'
mysql=MySQL(app)

#Declaracion de la ruta http://localhost:5000
@app.route('/')
def index():
    consulta= mysql.connect.cursor()
    consulta.execute('select * from tbfrutas')
    contbfrutas= consulta.fetchall()
    #print(contbfrutas)
    return render_template('index1.html', tbfrutas = contbfrutas)

#Ruta http://localhost:5000/guardar tipo POST para insert
@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        
        #pasamos a variables el contenido de los input 
        vfruta= request.form['txtFruta']
        vtemporada= request.form['txtTemporada']
        vprecio= request.form['txtprecio']
        vstock= request.form['txtstock']
        #print(fruta,temporada,precio,stock)
        
        #Conectar y ejecutar el insert
        cs = mysql.connection.cursor()
        cs.execute('insert into tbfrutas(fruta,temporada,precio,stock) values (%s,%s,%s,%s)', (vfruta,vtemporada,vprecio,vstock))
        mysql.connection.commit()
        
    flash('La fruta fue agregada correctamente')
    return redirect(url_for('index'))

@app.route('/editar/<string:id>')
def editar(id):
    cursoId=mysql.connection.cursor()
    cursoId.execute('select * from tbfrutas where id= %s',(id))
    consulId= cursoId.fetchone()
    print(consulId)
    flash('fue actualizado correctamente')
    return render_template('editarAlbum1.html',album=consulId)
    
@app.route('/update/<id>', methods=['POST'])
def update(id):
   if request.method == 'POST':
    varfruta= request.form['txtFruta']
    vartemporada= request.form['txtTemporada']
    varprecio= request.form['txtprecio']
    varstock= request.form['txtstock']
    
    curAct= mysql.connection.cursor()
    curAct.execute('update tbfrutas set titulo= %s,fruta= %s, temporada= %s, precio= %s, stock= %s where id= %s',(varfruta,vartemporada,varprecio,varstock,id))
    mysql.connection.commit()
    
    
    flash('Se  ah actualizo '+varfruta)    
    return redirect(url_for('index'))

@app.route('/eliminar/<id>')
def eliminar(id):
    cursorId=mysql.connection.cursor()
    cursorId.execute('select * from tbfrutas where id=%s',(id,))
    consId = cursorId.fetchone()
    return render_template('borrarAlbum1.html', album= consId)

@app.route('/delete/<id>',methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        varfruta = request.form['txtfruta']
        
        curAct = mysql.connection.cursor()
        curAct.execute('delete from tbfrutas where id=%s',(id))
        mysql.connection.commit()
    flash('Se borró la fruta  '+varfruta)
    return redirect(url_for('index'))




    
#Ejecucion de nuestro programa
if __name__ == '__main__':
    app.run(port=5000, debug=True)
    