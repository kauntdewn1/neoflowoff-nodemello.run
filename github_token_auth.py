"""
Script para autenticação com GitHub usando Personal Access Token (PAT) clássico
Para o repositório: git@github.com:neomello/neoflowoff-nodemello.run.git

Para criar um token:
1. Acesse: https://github.com/settings/tokens
2. Clique em "Generate new token (classic)"
3. Selecione as permissões necessárias (repo, workflow, etc.)
4. Copie o token gerado
"""

import os
import requests
from typing import Optional


class GitHubTokenAuth:
    """Classe simples para autenticação com Personal Access Token (PAT)"""
    
    def __init__(self, token: str):
        """
        Inicializa a autenticação com token clássico
        
        Args:
            token: Personal Access Token do GitHub
        """
        if not token:
            raise ValueError("Token não pode ser vazio")
        self.token = token
        self.base_url = "https://api.github.com"
    
    def _get_headers(self) -> dict:
        """Retorna headers padrão para requisições autenticadas"""
        return {
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'GitHub-Agent-Python'
        }
    
    def make_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """
        Faz uma requisição autenticada à API do GitHub
        
        Args:
            method: Método HTTP (GET, POST, PUT, DELETE, PATCH, etc.)
            endpoint: Endpoint da API (ex: '/repos/neomello/neoflowoff-nodemello.run')
            **kwargs: Argumentos adicionais para requests (json, data, params, etc.)
        
        Returns:
            Response object do requests
        """
        headers = kwargs.pop('headers', {})
        headers.update(self._get_headers())
        kwargs['headers'] = headers
        
        url = f'{self.base_url}{endpoint}'
        response = requests.request(method, url, **kwargs)
        response.raise_for_status()
        
        return response
    
    def get_repo_info(self, owner: str, repo: str) -> dict:
        """Obtém informações de um repositório"""
        response = self.make_request('GET', f'/repos/{owner}/{repo}')
        return response.json()
    
    def list_issues(self, owner: str, repo: str, state: str = 'open', per_page: int = 30) -> list:
        """Lista issues de um repositório"""
        response = self.make_request(
            'GET',
            f'/repos/{owner}/{repo}/issues',
            params={'state': state, 'per_page': per_page}
        )
        return response.json()
    
    def create_issue(self, owner: str, repo: str, title: str, body: str, labels: Optional[list] = None) -> dict:
        """Cria uma nova issue"""
        data = {'title': title, 'body': body}
        if labels:
            data['labels'] = labels
        
        response = self.make_request(
            'POST',
            f'/repos/{owner}/{repo}/issues',
            json=data
        )
        return response.json()
    
    def list_commits(self, owner: str, repo: str, branch: str = 'main', per_page: int = 30) -> list:
        """Lista commits de um repositório"""
        response = self.make_request(
            'GET',
            f'/repos/{owner}/{repo}/commits',
            params={'sha': branch, 'per_page': per_page}
        )
        return response.json()
    
    def get_file_content(self, owner: str, repo: str, path: str, branch: str = 'main') -> dict:
        """Obtém conteúdo de um arquivo do repositório"""
        response = self.make_request(
            'GET',
            f'/repos/{owner}/{repo}/contents/{path}',
            params={'ref': branch}
        )
        return response.json()
    
    def test_connection(self) -> bool:
        """Testa se o token está válido"""
        try:
            response = self.make_request('GET', '/user')
            user_data = response.json()
            print(f"[+] Token válido! Autenticado como: {user_data.get('login')}")
            return True
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                print("[ERRO] Token inválido ou expirado")
            else:
                print(f"[ERRO] Erro ao autenticar: {e}")
            return False


def exemplo_uso():
    """
    Exemplo de como usar a classe GitHubTokenAuth
    """
    # --- CONFIGURAÇÃO ---
    # Para obter um token:
    # 1. Acesse: https://github.com/settings/tokens
    # 2. Clique em "Generate new token (classic)"
    # 3. Selecione as permissões (repo, workflow, etc.)
    # 4. Configure a variável de ambiente:
    #    export GITHUB_TOKEN="seu_token_aqui"
    #    Ou crie um arquivo .env (não commitado) com: GITHUB_TOKEN=seu_token_aqui
    
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
    if not GITHUB_TOKEN:
        print("[ERRO] Variável de ambiente GITHUB_TOKEN não encontrada!")
        print("\nPara configurar:")
        print("  export GITHUB_TOKEN='seu_token_aqui'")
        print("\nOu use um arquivo .env (não commitado):")
        print("  echo 'GITHUB_TOKEN=seu_token_aqui' > .env")
        return
    
    REPO_OWNER = "neomello"
    REPO_NAME = "neoflowoff-nodemello.run"
    # --------------------
    
    try:
        # Inicializa autenticação
        github = GitHubTokenAuth(GITHUB_TOKEN)
        
        # Testa conexão
        if not github.test_connection():
            return
        
        # Obtém informações do repositório
        print(f"\n[+] Obtendo informações do repositório {REPO_OWNER}/{REPO_NAME}...")
        repo_info = github.get_repo_info(REPO_OWNER, REPO_NAME)
        print(f"    Nome: {repo_info['full_name']}")
        print(f"    Descrição: {repo_info.get('description', 'N/A')}")
        print(f"    Stars: {repo_info['stargazers_count']}")
        print(f"    Forks: {repo_info['forks_count']}")
        print(f"    Linguagem: {repo_info.get('language', 'N/A')}")
        print(f"    URL: {repo_info['html_url']}")
        
        # Lista issues abertas
        print(f"\n[+] Listando issues abertas...")
        issues = github.list_issues(REPO_OWNER, REPO_NAME, state='open', per_page=5)
        print(f"    Issues abertas encontradas: {len(issues)}")
        for issue in issues[:3]:
            print(f"    - #{issue['number']}: {issue['title']}")
            if issue.get('body'):
                body_preview = issue['body'][:50] + "..." if len(issue['body']) > 50 else issue['body']
                print(f"      {body_preview}")
        
        # Lista últimos commits
        print(f"\n[+] Listando últimos commits...")
        commits = github.list_commits(REPO_OWNER, REPO_NAME, per_page=5)
        for commit in commits[:3]:
            print(f"    - {commit['sha'][:7]}: {commit['commit']['message'][:60]}")
            print(f"      Por: {commit['commit']['author']['name']}")
        
        # Exemplo: Criar uma issue (descomente se necessário)
        # print("\n[+] Criando issue de teste...")
        # new_issue = github.create_issue(
        #     owner=REPO_OWNER,
        #     repo=REPO_NAME,
        #     title="Teste via API",
        #     body="Esta issue foi criada via GitHub API usando Personal Access Token"
        # )
        # print(f"    Issue criada: {new_issue['html_url']}")
        
    except requests.exceptions.HTTPError as e:
        print(f"\n[ERRO HTTP] {e}")
        if e.response.status_code == 401:
            print("    Token inválido ou sem permissões suficientes")
        elif e.response.status_code == 404:
            print(f"    Repositório {REPO_OWNER}/{REPO_NAME} não encontrado ou sem acesso")
        print(f"    Resposta: {e.response.text}")
    except Exception as e:
        print(f"\n[ERRO] {e}")


if __name__ == "__main__":
    exemplo_uso()

