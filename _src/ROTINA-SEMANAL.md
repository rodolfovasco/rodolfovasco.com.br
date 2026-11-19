# Rotina semanal de artigos (rodolfovasco.com.br)

Objetivo: toda segunda-feira, preparar UM artigo novo (PT, EN e ES) sobre um tema em alta nas buscas, numa **branch**, sem publicar. O Rodolfo aprova (merge) e o GitHub Pages publica.

## Regras que nunca mudam
- **Nunca** dar push na `main`. Só em uma branch `artigo/AAAA-MM-DD-<slug-curto>`.
- Alterar apenas: `_src/articles/<id>/` (3 arquivos .md) e os arquivos gerados pelo build (páginas, sitemap, feeds, llms.txt, og/). Não editar templates, i18n.py nem textos da home.
- **Não inventar** números, estudos, casos de clientes, citações ou fatos pessoais do Rodolfo. Só afirmar o que uma fonte verificável confirma. Sem estatística sem fonte.
- Citar produtos, recursos e nomes só se confirmados em fonte oficial ou confiável consultada nesta execução.
- Nada de conteúdo copiado: reescrever com palavras próprias.
- Tom: direto, profissional, claro, sem exagero de marketing. Português do Brasil; EN e ES são adaptações (não tradução literal), com exemplos e termos naturais de cada língua.

## 1. Escolher o tema
1. Listar os artigos já publicados (`_src/articles/*/pt.md`, campo `title`/`category`) para não repetir tema e alternar categorias (`ia`, `martech`, `performance`, `analytics`, `seo`).
2. Usar WebSearch (modo "extended") para achar temas em alta nas últimas semanas sobre IA aplicada a marketing, marketing digital, martech, analytics, performance, SEO/AEO/GEO e tecnologia. Priorizar: pergunta que as pessoas pesquisam, intenção clara ("o que é", "como", "diferença", "guia"), relevância para um Head de Marketing & Martech, e espaço para um texto útil e original.
3. Escolher UM tema. Anotar: por que está em alta, a palavra-chave principal em PT/EN/ES e a intenção de busca.

## 2. Pesquisar
Ler fontes oficiais/confiáveis (documentação das plataformas, anúncios oficiais, pesquisas com metodologia). Anotar as URLs. Se uma informação não for confirmada, deixar de fora.

## 3. Escrever (3 arquivos)
Criar `_src/articles/<id>/pt.md`, `en.md`, `es.md` (`<id>` = slug curto em PT sem acento). Formato exato, igual aos existentes:

```
---
title: <até ~60 caracteres, palavra-chave no início>
description: <120 a 155 caracteres, com a palavra-chave e o benefício>
slug: <slug da língua, minúsculo, hifens, sem acento>
date: <data de hoje AAAA-MM-DD>
updated: <igual a date>
category: <ia|martech|performance|analytics|seo>
summary: <2 a 3 frases que respondem a pergunta principal>
---
```
Corpo (markdown):
- 1º parágrafo: **definição/resposta direta em negrito** (1–2 frases) — formato bom para snippets e para IAs.
- `##` seções com títulos em forma de pergunta ou de intenção de busca; tabela comparativa quando fizer sentido; listas curtas; passo a passo numerado; "Erros comuns"; "Como saber se está funcionando".
- Bloco de FAQ com 3 a 5 perguntas reais:
```
:::faq
Q: pergunta?
A: resposta curta e completa.
:::
```
- Seção `## Fontes` com links em markdown para as fontes consultadas (cada idioma pode usar a mesma lista).
- Link interno para 1 ou 2 artigos já publicados (mesma língua; caminhos `/artigos/<slug>/`, `/en/articles/<slug>/`, `/es/articulos/<slug>/`) e fechamento com `[fale comigo](#contato)` (EN: `[get in touch](#contato)`, ES: `[habla conmigo](#contato)`).
- Entre 900 e 1.400 palavras. Sem emojis.

## 4. Gerar e validar
```
python3 _src/build.py .
NODE_PATH=$(npm root -g) node _src/og.js .
```
(Se faltar playwright: `npm i -g playwright` não é necessário, o Chromium/Playwright já vem instalado no ambiente.) Verificar:
- os 3 artigos foram gerados e aparecem em `sitemap.xml`, `llms.txt`, nos `feed.xml` e na lista de artigos;
- todo `<script type="application/ld+json">` é JSON válido e os links internos (`href="/..."`) apontam para arquivos existentes;
- `<title>` até ~60 caracteres e description até ~160;
- as imagens `og/<id>-pt|en|es.png` foram criadas (abrir uma para conferir que o título cabe).

## 5. Entregar para aprovação
1. `git checkout -b artigo/AAAA-MM-DD-<slug>`; commit com a mensagem "Artigo: <título PT>" mais os trailers de coautoria exigidos pela sessão; `git push origin artigo/AAAA-MM-DD-<slug>`.
2. Tentar `gh pr create --base main` (título "Artigo: <título PT>", corpo com tema, por que está em alta, fontes e o que revisar). Se o `gh` não funcionar, não insistir: informar o link de comparação `https://github.com/rodolfovasco/rodolfovasco.com.br/compare/main...artigo/AAAA-MM-DD-<slug>` (lá ele abre o PR e dá merge).
3. Mensagem final curta (ela vira a notificação): título do artigo em PT, tema em uma linha, link do PR/comparação e "Para publicar: faça o merge". Mencionar qualquer ponto que precise de olhar humano (dado sem fonte forte, nome de produto que pode ter mudado).

## Publicação
O merge na `main` publica o site em 1 a 2 minutos. Depois, se quiser acelerar a indexação: Search Console, inspeção de URL.
