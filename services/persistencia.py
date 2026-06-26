import json
from pathlib import Path
from .imobiliaria import Imobiliaria


class Persistencia:
    CAMINHO_PADRAO = Path("data/banco.json")

    @staticmethod
    def carregar_dados(caminho=None):
        caminho = Path(caminho or Persistencia.CAMINHO_PADRAO)
        if not caminho.exists():
            return Imobiliaria()
        try:
            with caminho.open("r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
            return Imobiliaria.from_dict(dados)
        except (json.JSONDecodeError, OSError):
            return Imobiliaria()

    @staticmethod
    def salvar_dados(imobiliaria, caminho=None):
        caminho = Path(caminho or Persistencia.CAMINHO_PADRAO)
        caminho.parent.mkdir(parents=True, exist_ok=True)
        with caminho.open("w", encoding="utf-8") as arquivo:
            json.dump(imobiliaria.to_dict(), arquivo, ensure_ascii=False, indent=4)
