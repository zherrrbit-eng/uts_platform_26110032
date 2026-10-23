from flask import Flask
import os, socket
app = Flask(__name__)
@app.route('/')
def home():
    db_host = os.getenv('DB_HOST', 'db')
    db_name = os.getenv('DB_NAME', 'bukutamu')
    try:
        import mysql.connector
        conn = mysql.connector.connect(host=db_host, user=os.getenv('DB_USER','root'), password=os.getenv('DB_PASSWORD','root'), database=db_name)
        db_status = f"✅ Terhubung ke DB {db_name} di host {db_host}"
        conn.close()
    except Exception as e:
        db_status = f"⚠️ DB belum siap: {e} (host={db_host}) - Tapi OK"
    return f"<h1>Buku Tamu Digital - UTS Platform</h1><p><b>Nama: Agrin</b></p><p><b>{db_status}</b></p><p>Network: bukutamu-net | Volume: db_data</p>"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
