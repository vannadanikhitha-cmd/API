from flask import Flask, request, jsonify
import pyodbc
app = Flask(__name__)
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=.\\SQLEXPRESS;"
    "DATABASE=employee;"
    "Trusted_Connection=yes;"
)
@app.route('/getage', methods=['POST'])
def get_age():

    data = request.get_json()

    name = data.get("name")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT age FROM emp WHERE name = ?",
        (name,)
    )

    row = cursor.fetchone()

    if row:
        return jsonify({
            "age": row[0]
        })

    return jsonify({
        "message": "Employee not found"
    }), 404

if __name__ == "__main__":
    app.run(debug=True)