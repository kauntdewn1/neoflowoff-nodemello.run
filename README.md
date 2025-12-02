# NΞØ FLOWOFF · NodeMello RUN

### Deploy Visual Contínuo — Full-Time Observer Node

Este repositório contém o sistema que transforma qualquer input do MELLØ em:

- post de feed

- story

- capsule para X

- cast para Farcaster

- artigo

- asset on-chain (IPFS)

Componentes:

- MCP Core

- MCP-Visual

- Render Engine

- IPFS Uploader

- Multi-distributor (Meta, Twitter/X, LinkedIn, Farcaster)

- Blog autopublisher

- Endpoint /post

Deploys:

- Fly.io (core)

- Vercel (painel + blog)

- IPFS (asset layer)

Modo: **FULL-TIME**

---

## 📋 Status de Implementação

### ✅ Estrutura Base
- [x] Estrutura completa de diretórios criada (38 arquivos)
- [x] `package.json` configurado com dependências
- [x] `.env.example` criado
- [x] `fly.toml` criado para deploy

### ✅ Core do Sistema
- [x] `src/server.js` - Servidor Express configurado
  - Rotas: `/input`, `/render`, `/upload`, `/post`
  - Middleware JSON com limite de 30mb
  - Endpoint raiz com status do sistema

### ✅ MCP Core
- [x] `src/mcp/core/classify.js` - Classificador de inputs
  - Categorias: BUILD, INSIGHT, CASE, STRATEGY, CRISE, GERAL
  - Análise de texto para categorização automática

### ✅ MCP Visual
- [x] `src/mcp/visual/generators/thesis.gen.js` - Gerador de teses
  - Gera teses contextuais baseadas na categoria do evento
  - Mensagens alinhadas com a identidade NΞØ FlowOFF

### ✅ Engine de Renderização
- [x] `src/engine/render.js` - Orquestrador de renderização
  - Integração com `buildImage.js` para geração de assets visuais

### ✅ Upload IPFS
- [x] `src/upload/ipfsUpload.js` - Upload para Web3 Storage
  - Suporte a múltiplos provedores (configurável via env)
  - Retorna CID e URL IPFS

### ✅ Distribuidor
- [x] `src/distributor/router.js` - Roteador multi-canal
  - Instagram, Twitter/X, LinkedIn, Farcaster, Blog
  - Distribuição condicional baseada em perfis

### ✅ Rotas
- [x] `src/routes/post.js` - Endpoint de publicação
  - POST `/post` para distribuição em todos os canais
  - Tratamento de erros e resposta padronizada

### ✅ Documentação
- [x] `docs/configuracaoinicial.md` - Guia de configuração
  - Variáveis de ambiente necessárias
  - Configuração de provedores IPFS
  - Estrutura de administração
  - Endpoints admin documentados

### 🚧 Pendente
- [ ] Implementação dos distribuidores individuais (instagram.js, twitter.js, linkedin.js, farcaster.js, blog.js)
- [ ] Implementação do buildImage.js e buildVideo.js
- [ ] Implementação das rotas restantes (input.js, render.js, upload.js)
- [ ] Implementação dos generators restantes (visual.gen.js, feed.gen.js, story.gen.js, log.gen.js)
- [ ] Implementação dos reducers (visual.reduce.js, reduce.js, route.js)
- [ ] Implementação do observer.js
- [ ] Configuração dos arquivos de config (meta.config.js, twitter.config.js, etc.)
- [ ] Implementação dos utilitários (logger.js, date.js, sanitize.js)
- [ ] Implementação do pinataUpload.js

---

## 🚀 Como Usar

1. **Instalar dependências:**
   ```bash
   npm install
   ```

2. **Configurar variáveis de ambiente:**
   ```bash
   cp .env.example .env
   # Editar .env com suas credenciais
   ```

3. **Executar em desenvolvimento:**
   ```bash
   npm run dev
   ```

4. **Executar em produção:**
   ```bash
   npm start
   ```

---

## 📚 Documentação Adicional

- [Configuração Inicial](./docs/configuracaoinicial.md) - Guia completo de setup
- [Estrutura do Projeto](./.cursor/estrutura.md) - Mapa de arquivos e diretórios
