import json
from pathlib import Path
from .imobiliaria import Imobiliaria
class Persistencia:
    CAMINHO_PADRAO = Path("data/banco.json")

    @staticmethod
    def carregar_dados(caminho=None):
        # Carrega os dados do arquivo JSON
        caminho = Path(caminho or Persistencia.CAMINHO_PADRAO)
        if not caminho.exists():
            return Imobiliaria()
        arquivo = None
        try:
            arquivo = caminho.open("r", encoding="utf-8")
            dados = json.load(arquivo)
        except json.JSONDecodeError:
            print("Aviso: arquivo corrompido. Iniciando sistema vazio.")
            return Imobiliaria()
        except OSError as erro:
            print(f"Aviso: erro ao abrir arquivo ({erro}). Iniciando sistema vazio.")
            return Imobiliaria()
        else:
            return Imobiliaria.from_dict(dados)
        finally:
            if arquivo and not arquivo.closed:
                arquivo.close()

    @staticmethod
    def salvar_dados(imobiliaria, caminho=None):
        # Salva os dados no arquivo JSON
        caminho = Path(caminho or Persistencia.CAMINHO_PADRAO)
        caminho.parent.mkdir(parents=True, exist_ok=True)
        arquivo = None
        try:
            arquivo = caminho.open("w", encoding="utf-8")
            json.dump(imobiliaria.to_dict(), arquivo, ensure_ascii=False, indent=4)
        except OSError as erro:
            raise OSError(f"Não foi possível salvar os dados: {erro}") from erro
        else:
            pass  # gravação concluída sem erros
        finally:
            if arquivo and not arquivo.closed:
                arquivo.close()
