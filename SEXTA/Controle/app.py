from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configuração do MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port=7306,
    database="rack_management"
)

@app.route('/')
def index():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM connections")
    connections = cursor.fetchall()
    return render_template('index.html', connections=connections)

@app.route('/add', methods=['GET', 'POST'])
def add_connection():
    if request.method == 'POST':
        switch_port = request.form['switch_port']
        patch_panel_port = request.form['patch_panel_port']
        cursor = db.cursor()
        cursor.execute("INSERT INTO connections (switch_port, patch_panel_port) VALUES (%s, %s)", (switch_port, patch_panel_port))
        db.commit()
        return redirect(url_for('index'))
    return render_template('add_connection.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_connection(id):
    cursor = db.cursor(dictionary=True)
    if request.method == 'POST':
        switch_port = request.form['switch_port']
        patch_panel_port = request.form['patch_panel_port']
        cursor.execute("UPDATE connections SET switch_port = %s, patch_panel_port = %s WHERE id = %s", (switch_port, patch_panel_port, id))
        db.commit()
        return redirect(url_for('index'))
    cursor.execute("SELECT * FROM connections WHERE id = %s", (id,))
    connection = cursor.fetchone()
    return render_template('edit_connection.html', connection=connection)

@app.route('/delete/<int:id>')
def delete_connection(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM connections WHERE id = %s", (id,))
    db.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
