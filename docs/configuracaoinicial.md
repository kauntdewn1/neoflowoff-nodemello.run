NΞØ FlowOFF · NodeMello RUN

Configuração Inicial do Sistema de Deploy Visual Contínuo



Versão: 1.0

Última Atualização: AUTO-GERADA PELO NODE



1. Introdução



Este documento define a configuração obrigatória para ativar e operar o NodeMello RUN, o sistema full-time que transforma qualquer input do MELLØ em ativos visuais, narrativos e distribuídos em múltiplos canais (Meta, X, LinkedIn, Farcaster, Blog, IPFS, etc).



O objetivo deste documento é:



alinhar variáveis ambientais



definir provedores de storage



padronizar distribuidores



criar base para expansão



manter coerência entre múltiplos nodes MELLØ



servir como referência formal para novos desenvolvedores



2. Variáveis de Ambiente Necessárias



As variáveis abaixo são essenciais para o funcionamento do Node:



# Meta (Instagram/Facebook)

META_APP_ID=

META_APP_SECRET=

META_ACCESS_TOKEN=

META_IG_USER_ID=



# Twitter / X

TWITTER_API_KEY=

TWITTER_API_SECRET=

TWITTER_ACCESS_TOKEN=

TWITTER_ACCESS_SECRET=



# LinkedIn

LINKEDIN_CLIENT_ID=

LINKEDIN_CLIENT_SECRET=

LINKEDIN_ACCESS_TOKEN=



# Farcaster

FARCASTER_FID=

FARCASTER_MNEMONIC=

FARCASTER_HUB_URL=https://hub.pinata.cloud



# IPFS (definir provedor)

IPFS_PROVIDER=pinata | web3storage | infura | lighthouse

WEB3_STORAGE_TOKEN=

PINATA_JWT=

PINATA_API_KEY=

PINATA_SECRET_KEY=

INFURA_IPFS_PROJECT_ID=

INFURA_IPFS_PROJECT_SECRET=

LIGHTHOUSE_API_KEY=



# Blog / FlowOFF.xyz

BLOG_TOKEN=

BLOG_API_URL=



# Segurança interna

NODEMELLO_ADMIN_KEY=

NODEMELLO_ENV=production | development



Observação



O sistema foi projetado para funcionar com mais de um provider IPFS ativo ao mesmo tempo.

Isso reduz risco de downtime e garante redundância.



4. Estrutura de Administração



O NodeMello RUN precisa de um mecanismo de administração simples e direto.



4.1 Admin Key



O acesso administrativo usa a variável:



NODEMELLO_ADMIN_KEY=





Recomendações:



mínimo 48 caracteres



nunca commitar em repositório



invalidar e rotacionar a cada 30 dias



expor em headers somente via HTTPS



4.2 Funções Admin



O sistema aceita:



POST /admin/add-distributor



Registra novo distribuidor na estrutura:



{

   "name": "threads",

   "enabled": true,

   "module": "src/distributor/threads.js"

}



POST /admin/revoke-distributor



Desativa ou remove por completo.



POST /admin/rotate-tokens



Atualiza chaves de conexão externas.



POST /admin/set-providers



Seleciona provedores IPFS ativos.

