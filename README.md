# Atividade — OpenRouter

Comparação de dois modelos gratuitos com o mesmo prompt em português.

**Concluído:** notebook executado com respostas reais de `liquid/lfm-2.5-2.6b:free` e `nvidia/nemotron-3.5-lightning:free`, ambos confirmados gratuitos no catálogo. Na amostra final, Liquid obteve 5/5 e NVIDIA 0/5; o segundo retornou texto ininteligível. Custo informado: US$ 0 em ambas as respostas finais. Falhas 429 e truncamentos anteriores estão documentados.

Rodada analisada: `evidencias/20260923T011523536232Z/`. O notebook contém a avaliação fundamentada, as respostas integrais, latência, uso de tokens e limitações. Análise produzida com assistência de IA, para revisão da dupla.

- `atividade.ipynb`: procedimento, catálogo, prompt, execução, evidências e análise.
- `evidencias/`: registros datados do catálogo, protocolo, ambiente e chamadas.
- `executar.py`: execução automatizada do notebook.
- `requirements.txt`: dependências; versões efetivas em `evidencias/*/ambiente.json`.

## Reproduzir

Com Python 3.10 ou superior:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
read -rsp 'Chave OpenRouter: ' OPENROUTER_API_KEY
export OPENROUTER_API_KEY
python executar.py
unset OPENROUTER_API_KEY
```

A entrada da chave fica oculta e não é salva no código ou histórico. Também é possível usar um gerenciador de segredos do ambiente. Execute todas as células em ordem; cada execução gera novas evidências. Ao reexecutar, atualize a seção 6 com as novas respostas e evidências: a análise atual identifica a rodada avaliada. Revise todos os arquivos antes do envio.

Uma chamada por modelo não comprova superioridade geral. Catálogo gratuito não garante disponibilidade. Os erros são registrados sem credenciais. Identificação da equipe deve ser feita no campo de entrega da plataforma acadêmica, preservando a orientação de não incluir dados pessoais no material.
