"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

# Configurações da API
app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_all_members():
    """Retorna todos os membros da família"""
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:id>', methods=['GET'])
def get_single_member(id):
    """Retorna um único membro com o ID especificado"""
    member = jackson_family.get_member(id)
    if member:
        return jsonify(member), 200
    return jsonify({"error": "Membro não encontrado"}), 404

@app.route('/member', methods=['POST'])
def create_member():
    """Adiciona um novo membro"""
    try:
        member = request.get_json()

        # Validação de campos obrigatórios
        if "first_name" not in member or "age" not in member or "lucky_numbers" not in member:
            return jsonify({"error": "Os campos 'first_name', 'age' e 'lucky_numbers' são obrigatórios."}), 400
        
        new_member = jackson_family.add_member(member)
        return jsonify(new_member), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/member/<int:id>', methods=['DELETE'])
def delete_single_member(id):
    """Remove um membro pelo ID"""
    deleted = jackson_family.delete_member(id)
    if deleted:
        return jsonify({"done": True}), 200
    return jsonify({"error": "Membro não encontrado"}), 404

# Este código só roda com o comando: python src/app.py
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
