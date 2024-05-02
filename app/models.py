from . import db
from datetime import datetime

class Camiseta(db.Model):
    __tablename__ = 'camisetas'
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    talla = db.Column(db.String(10), nullable=False)
    material = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    pedidos = db.relationship("Pedido", backref="camiseta")

class Pantalon(db.Model):
    __tablename__ = 'pantalones'
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    talla = db.Column(db.String(10), nullable=False)
    material = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    pedidos = db.relationship("Pedido", backref="pantalon")

class Chaqueta(db.Model):
    __tablename__ = 'chaquetas'
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    talla = db.Column(db.String(10), nullable=False)
    material = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    pedidos = db.relationship("Pedido", backref="chaqueta")

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False, unique=True)
    telefono = db.Column(db.String(20), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    pedidos = db.relationship("Pedido", backref="cliente")

class Pedido(db.Model):
    __tablename__ = 'pedidos'
    id = db.Column(db.Integer, primary_key=True)
    fecha_pedido = db.Column(db.DateTime, default=datetime.utcnow)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    camiseta_id = db.Column(db.Integer, db.ForeignKey('camisetas.id'))
    pantalon_id = db.Column(db.Integer, db.ForeignKey('pantalones.id'))
    chaqueta_id = db.Column(db.Integer, db.ForeignKey('chaquetas.id'))
    cantidad = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Float, nullable=False)

class Tienda(db.Model):
    __tablename__ = 'tiendas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)

class InventarioTienda(db.Model):
    __tablename__ = 'inventario_tienda'
    id = db.Column(db.Integer, primary_key=True)
    tienda_id = db.Column(db.Integer, db.ForeignKey('tiendas.id'))
    camiseta_id = db.Column(db.Integer, db.ForeignKey('camisetas.id'))
    pantalon_id = db.Column(db.Integer, db.ForeignKey('pantalones.id'))
    chaqueta_id = db.Column(db.Integer, db.ForeignKey('chaquetas.id'))
    cantidad_camiseta = db.Column(db.Integer, default=0)
    cantidad_pantalon = db.Column(db.Integer, default=0)
    cantidad_chaqueta = db.Column(db.Integer, default=0)

class Envio(db.Model):
    __tablename__ = 'envios'
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id'))
    fecha_envio = db.Column(db.DateTime, default=datetime.utcnow)
    direccion_destino = db.Column(db.String(255), nullable=False)

class Pago(db.Model):
    __tablename__ = 'pagos'
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id'))
    monto = db.Column(db.Float, nullable=False)
    fecha_pago = db.Column(db.DateTime, default=datetime.utcnow)
    metodo_pago = db.Column(db.String(100), nullable=False)

class Proveedor(db.Model):
    __tablename__ = 'proveedores'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)

