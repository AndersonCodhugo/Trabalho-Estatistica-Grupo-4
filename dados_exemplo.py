DATASETS_EXEMPLO = {
    "Preferência de Cores": (
        "Azul, Vermelho, Verde, Azul, Amarelo, Vermelho, Azul, Verde, "
        "Roxo, Azul, Vermelho, Amarelo, Verde, Azul, Vermelho"
    ),
    "Nível de Escolaridade": (
        "Ensino Médio, Superior, Superior, Fundamental, Pós-graduação, "
        "Superior, Ensino Médio, Superior, Fundamental, Superior, "
        "Pós-graduação, Ensino Médio"
    ),
    "Avaliação de Atendimento": (
        "Ótimo, Bom, Ótimo, Regular, Ótimo, Ruim, Bom, Ótimo, Bom, "
        "Regular, Ótimo, Bom, Ruim, Ótimo"
    ),
    "Meio de Transporte": (
        "Carro, Ônibus, Bicicleta, Carro, A pé, Carro, Ônibus, "
        "Bicicleta, Carro, A pé, Ônibus, Carro, Bicicleta"
    ),
}


def listar_datasets():
    return list(DATASETS_EXEMPLO.keys())

def obter_dataset(nome):
    return DATASETS_EXEMPLO.get(nome, "")
