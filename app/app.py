from flask import Flask, render_template_string

app = Flask(__name__)
HTML = """
<!DOCTYPE html>
<html>
<head><title>Buku Tamu Digital</title></head>
<body style="font-family: Arial; text-align:center; margin-top:50px;">
<h1>Buku Tamu Digital - UTS Platform</h1>
<p>Aplikasi Berjalan di Docker Compose!</p>
<p><b>Nama: Utari Rohiriwu</b></p>
<p>Status: OK - Port 5000</p>
</body>
</html>
"""
@app.route('/')
def index():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
