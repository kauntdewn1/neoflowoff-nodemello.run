# GitHub Token Authentication

Script para autenticação com GitHub usando Personal Access Token (PAT) clássico.

## Configuração

### 1. Criar um Personal Access Token

1. Acesse: https://github.com/settings/tokens
2. Clique em "Generate new token (classic)"
3. Selecione as permissões necessárias:
   - `repo` - para acessar repositórios
   - `workflow` - para gerenciar workflows (opcional)
4. Copie o token gerado

### 2. Configurar a variável de ambiente

**Opção 1: Variável de ambiente (temporária)**
```bash
export GITHUB_TOKEN="seu_token_aqui"
```

**Opção 2: Arquivo .env (recomendado)**
```bash
echo 'GITHUB_TOKEN=seu_token_aqui' > .env
```

⚠️ **Importante:** O arquivo `.env` está no `.gitignore` e não será commitado.

## Instalação

```bash
pip install -r requirements_github_token.txt
```

## Uso

```python
import os
from github_token_auth import GitHubTokenAuth

# O token será lido da variável de ambiente GITHUB_TOKEN
token = os.getenv('GITHUB_TOKEN')
github = GitHubTokenAuth(token)

# Testar conexão
github.test_connection()

# Obter informações do repositório
repo_info = github.get_repo_info('neomello', 'neoflowoff-nodemello.run')

# Listar issues
issues = github.list_issues('neomello', 'neoflowoff-nodemello.run')
```

## Executar exemplo

```bash
export GITHUB_TOKEN="seu_token_aqui"
python3 github_token_auth.py
```

