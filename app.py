import os
import mysql.connector
import hvac

# Get the Vault token and DB config from environment variables
token = os.getenv('VAULT_TOKEN')
db_user = os.getenv('DB_USER')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

# Create a Vault client
client = hvac.Client(
    url='http://127.0.0.1:8200',
    token=token,
)
read_response = client.secrets.kv.read_secret_version(path='my-secret-password')
password = read_response['data']['data']['password']


config = {
  'user': db_user,
  'password': password,
  'host': db_host,
  'database': db_name,
  'raise_on_warnings': True
}


cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

query = ("SELECT * FROM patients")
cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
cnx.close()
