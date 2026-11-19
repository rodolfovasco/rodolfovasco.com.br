# Rotina semanal de artigos (rodolfovasco.com.br)

Objetivo: toda segunda-feira, preparar e **publicar** UM artigo novo (PT, EN e ES) sobre um tema em alta nas buscas. O fluxo é: branch, Pull Request e, se todas as verificações passarem, merge do próprio PR na `main` (o GitHub Pages publica). Não é preciso pedir permissão ao Rodolfo para o merge (autorizado por ele em 19/11/2026).

## Regras que nunca mudam
- **Nunca** dar push direto na `main`. O artigo vai sempre em uma branch `artigo/AAAA-MM-DD-<slug-curto>`, com Pull Request, e entra na `main` pelo merge do PR (ver seção 5).
- **Só publicar (merge) se todas as portas de qualidade da seção 5 passarem.** Se qualquer uma falhar, deixar o PR aberto, não fazer o merge e avisar o Rodolfo com o motivo.
- Alterar apenas: `_src/articles/<id>/` (3 arquivos .md) e os arquivos gerados pelo build (páginas, sitemap, feeds, llms.txt, og/). Não editar templates, i18n.py nem textos da home.
- **Não inventar** números, estudos, casos de clientes, citações ou fatos pessoais do Rodolfo. Só afirmar o que uma fonte verificável confirma. Sem estatística sem fonte.
- Citar produtos, recursos e nomes só se confirmados em fonte oficial ou confiável consultada nesta execução.
- Nada de conteúdo copiado: reescrever com palavras próprias.
- Tom: direto, profissional, claro, sem exagero de marketing. Português do Brasil; EN e ES são adaptações (não tradução literal), com exemplos e termos naturais de cada língua.

## 1. Escolher o tema
0. **Área obrigatória:** o tema precisa ser de marketing digital, martech, IA aplicada a marketing, analytics, performance/mídia paga ou SEO/AEO/GEO. Nada fora dessas áreas, por mais que esteja em alta. E **precisa estar em alta nas buscas**: registrar no PR a evidência consultada nesta execução (resultados do WebSearch, páginas recentes sobre o tema, datas), sem inventar volume de busca.
1. **Garantir que o conteúdo não existe no blog (porta anti-duplicidade).** Fazer `git pull` da `main` e listar TODOS os artigos já publicados e também os que estão em PRs abertos (`_src/articles/*/pt.md`: `title`, `slug`, `category`, `summary`; e `list_pull_requests` abertos com prefixo `artigo/`). Reprovar o tema se ele coincidir em palavra-chave principal, pergunta central ou ângulo com qualquer artigo existente (mesmo que o título seja diferente); nesse caso escolher outro tema. Um tema só passa se responder a uma pergunta que nenhum artigo atual responde como foco principal. Alternar categorias (`ia`, `martech`, `performance`, `analytics`, `seo`), priorizando as menos recentes.
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

## 5. Entregar e publicar
1. `git checkout -b artigo/AAAA-MM-DD-<slug>`; commit com a mensagem "Artigo: <título PT>" mais os trailers de coautoria exigidos pela sessão; `git push origin artigo/AAAA-MM-DD-<slug>` (nunca push direto na `main`).
2. Abrir o Pull Request (`--base main`; título "Artigo: <título PT>", corpo com tema, evidência de que está em alta, fontes e o que revisar).
3. **Portas de qualidade para o merge automático** (todas precisam ser verdadeiras; registrar o resultado no corpo do PR):
   - tema na área permitida e com evidência de busca em alta (seção 1);
   - anti-duplicidade aprovada (seção 1), inclusive contra PRs abertos;
   - build e validações da seção 4 passaram (3 idiomas gerados, JSON-LD válido, links internos existentes, title/description nos limites, imagens og criadas);
   - todo dado, nome de produto e afirmação factual tem fonte consultada nesta execução e listada em "Fontes"; nada inventado;
   - sem conflito com a `main` (se houver, fazer merge da `main` na branch, aceitar a versão da `main` nos arquivos gerados e rodar o build de novo);
   - CI do repositório verde, se existir.
4. Se todas passarem: fazer o merge do PR (`merge_pull_request`, método merge), confirmar que o PR consta como merged e informar a URL pública do artigo (`https://rodolfovasco.com.br/artigos/<slug>/`; o site atualiza em 1 a 2 minutos).
5. Se alguma falhar (ou houver dúvida factual relevante): NÃO fazer o merge, deixar o PR aberto e explicar na mensagem final o que falhou e o que o Rodolfo precisa revisar. Se não for possível criar o PR, informar o link de comparação `https://github.com/rodolfovasco/rodolfovasco.com.br/compare/main...artigo/AAAA-MM-DD-<slug>`.
6. Mensagem final curta (ela vira a notificação): título do artigo em PT, tema em uma linha, status (publicado via merge, ou PR aberto aguardando revisão e por quê), link do PR e do artigo. Mencionar qualquer ponto que mereça olhar humano depois (fonte secundária, nome de produto que pode mudar).

## Publicação
O merge na `main` publica o site em 1 a 2 minutos. Depois, se quiser acelerar a indexação: Search Console, inspeção de URL. Não commitar `_src/__pycache__/` (cache do Python): adicionar ao `.gitignore` não é necessário, basta não incluir na hora do `git add`.
