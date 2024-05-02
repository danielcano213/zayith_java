from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
# Crear objeto de la aplicación Flask
app = Flask(__name__)

# Configurar la aplicación Flask
app.config.from_object(Config)

# Crear objeto SQLAlchemy
db = SQLAlchemy(app)

# Objeto para las migraciones
migrate = Migrate(app, db)

# Importar las rutas
from . import routes

# Importar los modelos
from .models import Camiseta, Pantalon, Chaqueta, Cliente, Pedido, Tienda, InventarioTienda, Envio, Pago, Proveedor

# Ejecutar la aplicación si se llama directamente
if __name__ == "__main__":
    app.run()

