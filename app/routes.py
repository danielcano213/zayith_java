from . import app, db, Flask
from .models import Camiseta, Pantalon, Chaqueta, Cliente, Pedido, Tienda, InventarioTienda, Envio, Pago, Proveedor
from flask import render_template, request, flash, redirect
from datetime import datetime

# Rutas para las camisetas
@app.route("/camisetas")
def get_all_camisetas():
    camisetas = Camiseta.query.all()
    return render_template("camisetas.html", camisetas=camisetas)

@app.route("/camisetas/<int:id>")
def get_camiseta_by_id(id):
    camiseta = Camiseta.query.get(id)
    return render_template("camiseta.html", cam=camiseta)

# Rutas para los pantalones
@app.route("/pantalones")
def get_all_pantalones():
    pantalones = Pantalon.query.all()
    return render_template("pantalones.html", pantalones=pantalones)

@app.route("/pantalones/<int:id>")
def get_pantalon_by_id(id):
    pantalon = Pantalon.query.get(id)
    return render_template("pantalon.html", pant=pantalon)

# Rutas para las chaquetas
@app.route("/chaquetas")
def get_all_chaquetas():
    chaquetas = Chaqueta.query.all()
    return render_template("chaquetas.html", chaquetas=chaquetas)

@app.route("/chaquetas/<int:id>")
def get_chaqueta_by_id(id):
    chaqueta = Chaqueta.query.get(id)
    return render_template("chaqueta.html", cha=chaqueta)

# Rutas para los clientes
@app.route("/clientes")
def get_all_clientes():
    clientes = Cliente.query.all()
    return render_template("clientes.html", clientes=clientes)

@app.route("/clientes/<int:id>")
def get_cliente_by_id(id):
    cliente = Cliente.query.get(id)
    return render_template("cliente.html", cli=cliente)

# Rutas para los pedidos
@app.route("/pedidos")
def get_all_pedidos():
    pedidos = Pedido.query.all()
    return render_template("pedidos.html", pedidos=pedidos)

@app.route("/pedidos/<int:id>")
def get_pedido_by_id(id):
    pedido = Pedido.query.get(id)
    return render_template("pedido.html", ped=pedido)

# Rutas para las tiendas
@app.route("/tiendas")
def get_all_tiendas():
    tiendas = Tienda.query.all()
    return render_template("tiendas.html", tiendas=tiendas)

@app.route("/tiendas/<int:id>")
def get_tienda_by_id(id):
    tienda = Tienda.query.get(id)
    return render_template("tienda.html", tie=tienda)

# Rutas para el inventario de tiendas
@app.route("/inventario_tienda")
def get_all_inventario_tienda():
    inventario = InventarioTienda.query.all()
    return render_template("inventario_tienda.html", inventario=inventario)

@app.route("/inventario_tienda/<int:id>")
def get_inventario_tienda_by_id(id):
    inventario = InventarioTienda.query.get(id)
    return render_template("inventario_tiendas.html", inv=inventario)

# Rutas para los envíos
@app.route("/envios")
def get_all_envios():
    envios = Envio.query.all()
    return render_template("envios.html", envios=envios)

@app.route("/envios/<int:id>")
def get_envio_by_id(id):
    envio = Envio.query.get(id)
    return render_template("envio.html", env=envio)

# Rutas para los pagos
@app.route("/pagos")
def get_all_pagos():
    pagos = Pago.query.all()
    return render_template("pagos.html", pagos=pagos)

@app.route("/pagos/<int:id>")
def get_pago_by_id(id):
    pago = Pago.query.get(id)
    return render_template("pago.html", pag=pago)

# Rutas para los proveedores
@app.route("/proveedores")
def get_all_proveedores():
    proveedores = Proveedor.query.all()
    return render_template("proveedores.html", proveedores=proveedores)

@app.route("/proveedores/<int:id>")
def get_proveedor_by_id(id):
    proveedor = Proveedor.query.get(id)
    return render_template("proveedor.html", prov=proveedor)

        
        
                            



