from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'richwan'
app.config['MYSQL_DATABASE_PASSWORD'] = 'r_ichwan'
app.config['MYSQL_DATABASE_DB'] = 'basic_coding_kulina'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)