from flask import Flask, request, jsonify

app = Flask(__name__)


CAMINHO_VIDEO = "all_resort.mp4"

# Endpoint 1: Sugestão de Produto
@app.route('/sugestao-produto', methods=['POST'])
def sugestao_produto():
    """
    Recebe a necessidade do cliente e retorna um vídeo e texto explicativo.
    """

    dados_recebidos = request.get_json()
    necessidade_cliente = dados_recebidos.get('necessidade', 'Nenhuma necessidade informada')
    print(f"Necessidade recebida do cliente: {necessidade_cliente}")

    # Garante que o vídeo existe
    if not os.path.exists(CAMINHO_VIDEO):
        return jsonify({"erro": "Vídeo não encontrado"}), 404

    # Enviar vídeo como arquivo
    return send_file(CAMINHO_VIDEO, mimetype='video/mp4')


# Endpoint 2: Encaminhar para Atendimento Humano
@app.route('/encaminhar-atendimento', methods=['POST'])
def encaminhar_atendimento():
    """
    Simula o encaminhamento do chat para um humano.
    Apenas recebe os dados e confirma o sucesso.
    """
    dados_cliente = request.get_json()

    print("--- DADOS PARA ENCAMINHAMENTO HUMANO ---")
    print(f"Nome: {dados_cliente.get('nome')}")
    print(f"Região: {dados_cliente.get('regiao')}")
    print(f"Necessidade: {dados_cliente.get('necessidade')}")
    print("-----------------------------------------")

    resposta = {
        "status": "Sucesso",
        "mensagem": "Atendimento encaminhado para um especialista."
    }
    return jsonify(resposta)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
