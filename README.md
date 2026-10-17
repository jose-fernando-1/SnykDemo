# Snyk Demo — FastAPI AppSec

Mini projeto didático para demonstrar:
- SAST: análise do código com `snyk code test`
- SCA: análise de dependências com `snyk test`
- Correção: comparar `app_vulnerable.py` e `app_secure.py`

> Use apenas em ambiente local e com dados fictícios. O arquivo vulnerável existe para demonstração; não o publique como serviço.

## 1. Pré-requisitos
- Python 3.10+
- Node.js/npm (para instalar o Snyk CLI)
- Conta Snyk

## 2. Instale e autentique o Snyk CLI
```bash
npm install -g snyk
snyk --version
snyk auth
```

## 3. Prepare o ambiente Python
Crie e ative um ambiente virtual.

Windows PowerShell:
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 4. Rode a versão vulnerável (opcional)
```bash
uvicorn app_vulnerable:app --reload
```
Abra `http://127.0.0.1:8000/docs`. Use somente dados fictícios. Pare com Ctrl+C.

## 5. Rode a versão corrigida
```bash
uvicorn app_secure:app --reload
```
Abra `http://127.0.0.1:8000/docs`.

## 6. Execute as análises Snyk
Na raiz do projeto:

```bash
# SAST: análise estática do código
snyk code test

# SCA: análise de dependências
snyk test

# Opcional: registrar snapshot para monitoramento no painel
snyk monitor
```

Dependendo da conta, do plano e da configuração, `snyk code test` pode exigir que o recurso Snyk Code esteja habilitado. O conjunto de achados varia com a base de vulnerabilidades atualizada e com a versão do CLI.

## 7. Demonstração sugerida
1. Execute `snyk code test` e guarde o resultado.
2. Analise `app_vulnerable.py`: a consulta SQL é montada por interpolação de string.
3. Execute `snyk code test` novamente após selecionar a versão corrigida ou analisar o arquivo corrigido.
4. Compare com `app_secure.py`, que usa consulta parametrizada.
5. Execute `snyk test` para revisar vulnerabilidades conhecidas nas dependências.
6. Documente os achados, severidade, recomendação e evidência da correção.

## 8. Limpeza
Para remover o ambiente virtual:
- Windows: `Remove-Item -Recurse -Force .venv`
- Linux/macOS: `rm -rf .venv`

## Limitações
Este é um exemplo pequeno para aprendizado, não uma auditoria de segurança completa. Um resultado sem achados não prova que a aplicação está segura.
