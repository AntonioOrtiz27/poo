from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@localhost/logipack'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Sucursal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    provincia = db.Column(db.String(50))
    localidad = db.Column(db.String(50))
    direccion = db.Column(db.String(100))

class Reparador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    dni = db.Column(db.String(10))
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))

class Transporte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numerotransporte = db.Column(db.String(20), unique=True, nullable=False)
    fechahorasalida = db.Column(db.DateTime)
    fechahorallegada = db.Column(db.DateTime)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))

class Paquete(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numeroenvio = db.Column(db.String(20), unique=True, nullable=False)
    peso = db.Column(db.Numeric(5, 2))
    nomdestino = db.Column(db.String(50))
    dirdestino = db.Column(db.String(100))
    entregado = db.Column(db.Boolean, default=False)
    observaciones = db.Column(db.Text)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    idtransporte = db.Column(db.Integer, db.ForeignKey('transporte.id'))
    idreparador = db.Column(db.Integer, db.ForeignKey('reparador.id'))

db.create_all()

@app.route('/registrar_paquete', methods=['POST'])
def registrar_paquete():
    data = request.json
    nuevo_paquete = Paquete(
        numeroenvio=data['numeroenvio'],
        peso=data['peso'],
        nomdestino=data['nomdestino'],
        dirdestino=data['dirdestino'],
        idsucursal=data['idsucursal']
    )
    db.session.add(nuevo_paquete)
    db.session.commit()
    return jsonify({'message': 'Paquete registrado exitosamente'})

@app.route('/registrar_salida_transporte', methods=['POST'])
def registrar_salida_transporte():
    data = request.json
    nuevo_transporte = Transporte(
        numerotransporte=data['numerotransporte'],
        fechahorasalida=datetime.now(),
        idsucursal=data['idsucursal']
    )
    db.session.add(nuevo_transporte)
    db.session.commit()
    paquetes_ids = data['paquetes_ids']
    for paquete_id in paquetes_ids:
        paquete = Paquete.query.get(paquete_id)
        paquete.idtransporte = nuevo_transporte.id
        db.session.commit()
    return jsonify({'message': 'Salida de transporte registrada exitosamente'})

@app.route('/registrar_llegada_transporte', methods=['POST'])
def registrar_llegada_transporte():
    data = request.json
    transporte = Transporte.query.filter_by(numerotransporte=data['numerotransporte']).first()
    if transporte:
        transporte.fechahorallegada = datetime.now()
        db.session.commit()
        return jsonify({'message': 'Llegada de transporte registrada exitosamente'})
    else:
        return jsonify({'message': 'Transporte no encontrado'}), 404

@app.route('/asignar_paquetes_reparador', methods=['POST'])
def asignar_paquetes_reparador():
    data = request.json
    reparador_id = data['reparador_id']
    paquetes_ids = data['paquetes_ids']
    for paquete_id in paquetes_ids:
        paquete = Paquete.query.get(paquete_id)
        paquete.idreparador = reparador_id
        db.session.commit()
    return jsonify({'message': 'Paquetes asignados exitosamente'})

@app.route('/registrar_entrega_paquete', methods=['POST'])
def registrar_entrega_paquete():
    data = request.json
    paquete = Paquete.query.filter_by(numeroenvio=data['numeroenvio']).first()
    if paquete:
        paquete.entregado = data['entregado']
        paquete.observaciones = data.get('observaciones', '')
        db.session.commit()
        return jsonify({'message': 'Entrega registrada exitosamente'})
    else:
        return jsonify({'message': 'Paquete no encontrado'}), 404

@app.route('/despachante/acceso', methods=['POST'])
def acceso_despachante():
    data = request.json
    sucursal_id = data['sucursal_id']
    sucursal = Sucursal.query.get(sucursal_id)
    if sucursal:
        return jsonify({'message': 'Acceso concedido', 'sucursal': sucursal.localidad})
    else:
        return jsonify({'message': 'Sucursal no encontrada'}), 404

@app.route('/repartidor/acceso', methods=['POST'])
def acceso_repartidor():
    data = request.json
    reparador = Reparador.query.filter_by(id=data['reparador_id'], dni=data['dni']).first()
    if reparador:
        return jsonify({'message': 'Acceso concedido'})
    else:
        return jsonify({'message': 'Reparador no encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
