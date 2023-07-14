from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

#Inicializacion del Servidor
app=Flask(__name__)

#Configuracion de la conexion
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='db_floreria'
app.secret_key='mysecretkey'
mysql=MySQL(app)

#Declaracion de la ruta http://localhost:5000
@app.route('/')
def index():
    return render_template('IndexV.html')

#Ruta http://localhost:5000/guardar tipo POST para insert

#Declaracion de la ruta http://localhost:5000


@app.route('/guardarFlores', methods=['POST'])
def guardarFlores():
    if request.method == 'POST':

        #pasamos a variables el contenido de los input 
        vnombre= request.form['txtNombre']
        vcantidad= request.form['txtCantidad']
        vprecio= request.form['txtPrecio']
        
        #print(nombre,cantidad,precio) 
        
        #Conectar y ejecutar el insert
        cs = mysql.connection.cursor()
        cs.execute('insert into tb_floreria(nombre,cantidad,precio) values (%s,%s,%s)', (vnombre,vcantidad,vprecio))
        mysql.connection.commit()
        
    
    flash('La flor fue agregado correctamente')
    return redirect(url_for('index'))

@app.route('/eliminar_editar')
def eliminar_editar():
    consulta= mysql.connect.cursor()
    consulta.execute('select * from tb_flores')
    conFlores= consulta.fetchall()
    #print(conAlbums)
    return render_template('Eliminar_editar.html', flores = conFlores)



@app.route('/editarFlor/<id>')
def editar(id):
    cursorId=mysql.connection.cursor()
    cursorId.execute('select * from tb_flores where id=%s',(id,))
    consId = cursorId.fetchone()
    return render_template('editar_Flores.html', frutas=consId)

@app.route('/actualizarFlores/<id>',methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        vnombre= request.form['txtNombre']
        vcantidad= request.form['txtCantidad']
        vprecio= request.form['txtPrecio']
    

        curAct = mysql.connection.cursor()
        curAct.execute('update tb_flores set nombre= %s, cantidad=%s, precio=%s, where id=%s',(vnombre,vcantidad,vprecio,id))
        mysql.connection.commit()
    flash('Se actualizó la flor'+vnombre)
    return redirect(url_for('Eliminar_editar'))

@app.route('/eliminar/<id>')
def eliminar(id):
    cursorId=mysql.connection.cursor()
    cursorId.execute('select * from tb_flores where id=%s',(id,))
    consId = cursorId.fetchone()
    return render_template('borrarFlores.html', flores= consId)

@app.route('/delete/<id>',methods=['POST'])
def delete(id):
    if request.method == 'POST':
        varNombre = request.form['txtNombre']

        curAct = mysql.connection.cursor()
        curAct.execute('delete from tb_frutas where id=%s',(id))
        mysql.connection.commit()
    flash('Se borró el Album '+varNombre)
    return redirect(url_for('Eliminar_editar'))

@app.route('/Consult')
def Consult():
    return render_template('buscaFruta.html')

@app.route('/Consultanombre', methods=['POST'])
def consultanombre():
    Varbuscar= request.form['txtbuscar']
    print(Varbuscar)
    CC= mysql.connection.cursor()
    CC.execute('select * from tb_frutas where nombre LIKE %s', (f'%{Varbuscar}%',))
    conflor= CC.fetchall()
    print(conflor)
    return render_template('buscaFlor.html', listafruta = conflor)

if __name__ == '__main__':
    app.run(port=5000, debug=True)