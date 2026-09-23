"""Executa todas as células; a chave deve existir no ambiente, nunca no código."""
from pathlib import Path
import nbformat
from nbclient import NotebookClient
p = Path(__file__).resolve().parent
nb = nbformat.read(p / "atividade.ipynb", as_version=4)
NotebookClient(nb, timeout=600, kernel_name="python3", resources={"metadata": {"path": str(p)}}).execute()
nbformat.write(nb, p / "atividade.ipynb")
print("Notebook executado. Confira as evidências e a seção de análise crítica.")
