from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/saque', methods=['POST'])
def saque():
    try:
        data = request.get_json()
    except Exception:
        return jsonify({'Erro': 'Insira somente números'}), 400

    if data is None or 'valor' not in data:
        return jsonify({'Erro': 'Quantia inválida'}), 400

    try:
        valor = float(data.get('valor'))
    except (TypeError, ValueError):
        return jsonify({'Erro': 'Quantia inválida'}), 400
    
    if valor <= 0:
        return jsonify({'Erro': 'Quantia inválida'}), 400
    
    notas = [100, 50, 20, 10, 5, 2]
    result = {}

    for nota in notas:
        result[nota] = int(valor // nota)
        valor = valor % nota

    if valor != 0:
        return jsonify({'Erro': 'Não possuímos notas para tal valor'}), 400

    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)