from . import app,db
from .models import Medico
from .models import Paciente
from .models import Cita
from .models import Consultorio
from flask import render_template, request, flash, redirect
from datetime import datetime

#crear medicos
@app.route("/medicos")
def get_all_medicos():
    medicos = Medico.query.all()
    return render_template("medicos.html" , medicos=medicos)
@app.route("/medicos/<int:id>")
def get_medico_by_id(id):
    medico = Medico.query.get(id)
    return render_template("medico.html",
                            med = medico )
@app.route("/medicos/create" , methods = [ "GET" , "POST"] )
def create_medico():
    if( request.method == "GET" ):
        especialidades = [
            "Cardiologia",
            "Dermatologia",
            "Pediatria",
            "Odontologia",
            "Oncologia",
            "Medico General"
        ]
        return render_template("medico_form.html",
                            especialidades = especialidades)
     
    elif(request.method == "POST"):
        new_medico = Medico(nombre = request.form["nombre"],
                            apellido = request.form["apellidos"],
                            tipo_identificacion = request.form["ti"],
                            numero_identificacion = request.form["ni"],
                            registro_medico = request.form["rm"],
                            especialidad = request.form["es"]
                            )
        db.session.add(new_medico)
        db.session.commit()
        flash("Medico registrado correctamente")
        return redirect("/medicos")


@app.route("/pacientes")
def get_all_pacientes():
    pacientes = Paciente.query.all()
    return render_template("pacientes.html" , pacientes=pacientes)
@app.route("/pacientes/<int:id>")
def get_paciente_by_id(id):
    paciente = Paciente.query.get(id)
    return render_template("paciente.html",
                           pac = paciente )

@app.route("/consultorios")
def get_all_consultorios():
    consultorios = Consultorio.query.all()
    return render_template("consultorios.html" , consultorios=consultorios)
@app.route("/consultorios/<int:id>")
def get_consultorio_by_id(id):
    consultorio = Consultorio.query.get(id)
    return render_template("consultorio.html",
                           con = consultorio)

@app.route("/citas")
def get_all_citas():
    citas = Cita.query.all()
    return render_template("citas.html" , citas=citas)
@app.route("/citas/<int:id>")
def get_cita_by_id(id):
    cita = Cita.query.get(id)
    return render_template("cita.html",
                           cit = cita)

@app.route("/pacientes/create" , methods = [ "GET" , "POST"] )
def create_paciente():
    if( request.method == "GET" ):
        tipo_de_sangre = [
            "A+",
            "O+",
            "A-",
            "O-",
            "AB+",
            "AB-"
        ]
        return render_template("paciente_form.html",
                            tipo_de_sangre = tipo_de_sangre)
    
    
    elif(request.method == "POST"):
        new_paciente = Paciente(nombre = request.form["nombre"],
                            apellido = request.form["apellidos"],
                            tipo_identificacion = request.form["ti"],
                            numero_identificacion = request.form["ni"],
                            altura = request.form["al"],
                            tipo_sangre = request.form["rh"]
                            )
        db.session.add(new_paciente)
        db.session.commit()
        flash("paciente registrado correctamente")
        return redirect("/pacientes")
@app.route("/consultorios/create" , methods = [ "GET" , "POST"] )
def create_consultorio():
    if( request.method == "GET" ):
        numero = [
            "101",
            "102",
            "103",
            "104",
            "105",
            "201",
            "202",
            "203",
            "204",
            "205"   
        ]
        return render_template("consultorio_form.html",
                            numero = numero)
    
    
    elif(request.method == "POST"):
        new_consultorio = Consultorio( numero = request.form["nu"]
                            )
        db.session.add(new_consultorio)
        db.session.commit()
        flash('Consultorio creado')
        return redirect('/consultorios')
@app.route("/citas/create", methods = ['GET', 'POST'])
def create_cita():
    
    if(request.method == 'GET'):
        valores = [
            4500,
            7000,
            20000]
        fecha = datetime.now()
        pacientes = Paciente.query.all()
        medicos= Medico.query.all()
        consultorios = Consultorio.query.all()
        return render_template("cita_form.html", pacientes = pacientes, medicos = medicos, consultorios = consultorios, valores = valores, fecha = fecha)
    
    elif(request.method == 'POST'):
        fecha = datetime.strptime(request.form['fecha'], "%Y-%m-%dT%H:%M")
        new_cita = Cita(
            fecha=fecha,
            paciente_id = request.form['pa'],
            medico_id = request.form['med'],
            consultorio_id = request.form['con'],
            valor = request.form['val']
        )
        db.session.add(new_cita)
        db.session.commit()
        flash('cita creada')
        return redirect('/citas')
    
@app.route('/medicos/update/<int:id>', methods=['GET','POST'])
def update_medico(id):
    especialidades = [
            "Cardiologia",
            "Dermatologia",
            "Pediatria",
            "Odontologia",
            "Oncologia",
            "Medico General"
    ]
    medico_update = Medico.query.get(id)
    
    if(request.method == 'GET'):
        return render_template('medico_update.html' , 
                                medico_update = medico_update, 
                                especialidades=especialidades)
    elif(request.method == 'POST'):
        medico_update.nombre = request.form['nombre']
        medico_update.apellido = request.form['apellidos']
        medico_update.tipo_identificacion = request.form['ti']
        medico_update.numero_identificacion = request.form['ni']
        medico_update.registro_medico = request.form['rm']
        medico_update.especialidad = request.form['es']
        db.session.commit()
        flash('Medico actualizado')
        return redirect('/medicos') 
@app.route('/medicos/delete/<int:id>', methods=['GET','POST'])
def delete_medico(id):
    medico_delete = Medico.query.get(id)
    db.session.delete(medico_delete)
    db.session.commit()
    flash("Medico eliminado correctamente")
    return redirect('/medicos')
@app.route('/pacientes/update/<int:id>', methods=['GET','POST'])
def update_paciente(id):
    tipo_de_sangre = [
            "A+",
            "O+",
            "A-",
            "O-",
            "AB+",
            "AB-"
    ]
    paciente_update = Paciente.query.get(id)
    
    if(request.method == 'GET'):
        return render_template('paciente_update.html' , 
                                paciente_update = paciente_update, 
                                tipo_de_sangre = tipo_de_sangre)
    elif(request.method == 'POST'):
        paciente_update.nombre = request.form['nombre']
        paciente_update.apellido = request.form['apellidos']
        paciente_update.tipo_identificacion = request.form['ti']
        paciente_update.numero_identificacion = request.form['ni']
        paciente_update.altura = request.form['al']
        paciente_update.tipo_de_sangre = request.form['rh']
        db.session.commit()
        flash('Paciente Actualizado')
        return redirect('/pacientes')   
@app.route('/pacientes/delete/<int:id>', methods=['GET','POST'])
def delete_paciente(id):
    paciente_delete = Paciente.query.get(id)
    db.session.delete(paciente_delete)
    db.session.commit()
    flash('Paciente Eliminado')
    return redirect('/pacientes')
@app.route('/consultorios/update/<int:id>', methods=['GET','POST'])
def update_consultorio(id):
    numero = [
            "101",
            "102",
            "103",
            "104",
            "105",
            "201",
            "202",
            "203",
            "204",
            "205"
    ]
    consultorio_update = Consultorio.query.get(id)
    
    if(request.method == 'GET'):
        return render_template('consultorio_update.html' , 
                                consultorio_update = consultorio_update, 
                                numero = numero)
    elif(request.method == 'POST'):
        consultorio_update.numero = request.form['nu']
        db.session.commit()
        flash('Consultorio Actualizado')
        return redirect('/consultorios')
@app.route('/consultorios/delete/<int:id>', methods=['GET','POST'])
def delete_consultorio(id):
    consultorio_delete = Consultorio.query.get(id)
    db.session.delete(consultorio_delete)
    db.session.commit()
    flash('Consultorio Eliminado')  
    return redirect('/consultorios')
@app.route('/citas/update/<int:id>', methods=['GET','POST'])
def update_cita(id):
    if(request.method == 'GET'):
        fecha = datetime.now()
        pacientes = Paciente.query.all()
        medicos= Medico.query.all()
        consultorios = Consultorio.query.all()
        cita_update = Cita.query.get(id)
        return render_template("cita_update.html", pacientes = pacientes, medicos = medicos, consultorios = consultorios,  fecha = fecha, cita_update = cita_update)
    elif(request.method == 'POST'):
        cita_update = Cita.query.get(id)
        cita_update.fecha = datetime.strptime (request.form['fecha'],"%Y-%m-%dT%H:%M")
        cita_update.paciente_id = request.form['pa']
        cita_update.medico_id = request.form['med']
        cita_update.consultorio_id = request.form['con']
        cita_update.valor = request.form['val']
        db.session.commit()
        flash('Cita Actualizada')
        return redirect('/citas')
@app.route('/citas/delete/<int:id>', methods=['GET','POST'])
def delete_cita(id):
    cita_delete = Cita.query.get(id)
    db.session.delete(cita_delete)
    db.session.commit()
    flash('Cita Eliminada')
    return redirect('/citas')

        
        
                            



