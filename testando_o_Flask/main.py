from flask import Flask, jsonify;

app = Flask(__name__)
@app.route('/api/teste', methods=['GET'])
def aula():
    return jsonify({"Mensagem": "Testando API em python usando Flask"})
if __name__ == '__main__':
    app.run(debug=True)