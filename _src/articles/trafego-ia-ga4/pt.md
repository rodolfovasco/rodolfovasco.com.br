---
title: Tráfego de IA no GA4: como medir ChatGPT e Gemini
description: Visitas vindas de ChatGPT, Gemini e Perplexity aparecem no GA4 como referral ou Direct. Veja como separar esse tráfego e o que ele não consegue mostrar.
slug: trafego-de-ia-no-ga4-como-medir
date: 2026-11-23
updated: 2026-11-23
category: analytics
summary: Para medir o tráfego de assistentes de IA no GA4, crie um grupo de canais personalizado que reúna as origens (source) desses assistentes. Uma parte das visitas chega sem referenciador e cai em Direct, então o número que você vê é um piso, não o total.
---

**Tráfego de IA no GA4 é o conjunto de sessões que chegam ao seu site depois de um clique em um link dentro de um assistente como ChatGPT, Gemini, Perplexity ou Claude.** Medir isso exige um agrupamento próprio, porque o GA4 nem sempre separa essas visitas dos demais referrals, e parte delas chega sem origem identificável.

Se você investe em conteúdo para ser citado por IAs, esta é a pergunta que vem logo depois: isso está trazendo visita? Este guia mostra como montar a medição básica e, com a mesma importância, até onde ela vai.

## Por que o tráfego de IA se perde no GA4?

O GA4 classifica cada sessão em canais (Organic Search, Referral, Direct e outros) a partir da origem e da mídia. Visitas de assistentes de IA costumam chegar como referral, com o domínio do assistente como origem, mas dois fatores atrapalham:

- **Mistura com outros referrals.** Sem uma regra própria, as visitas de IA ficam diluídas entre todos os sites que linkam para você.
- **Visitas sem referenciador.** Segundo a Terminus, aplicativos de assistentes para celular e desktop normalmente não enviam referenciador, e essas sessões caem em Direct. A Trackingplan diz o mesmo: visita sem referenciador entra como Direct e fica lá.

Há também uma divergência entre as fontes. A Terminus e a Trackingplan descrevem a existência de um canal padrão para assistentes de IA no GA4, enquanto a Seresa afirmou, em outubro de 2026, que o Google não havia anunciado um agrupamento nativo. Por isso, abra a sua propriedade e confira o que ela mostra antes de criar qualquer regra.

## Quais domínios entram na regra?

A lista abaixo vem da Terminus (atualizada em setembro de 2026). Trate como ponto de partida e revise de tempos em tempos, porque produtos e domínios mudam.

| Assistente | Origem (source) |
|---|---|
| ChatGPT | chatgpt.com (e o antigo chat.openai.com) |
| Gemini | gemini.google.com (e o antigo bard.google.com) |
| Perplexity | perplexity.ai e www.perplexity.ai |
| Claude | claude.ai |
| Copilot | copilot.microsoft.com |
| DeepSeek | chat.deepseek.com |
| Grok | grok.com |
| Outros | meta.ai, you.com, poe.com |

A mesma fonte recomenda não incluir domínios genéricos como openai.com, anthropic.com ou google.com, porque eles misturam tráfego que não vem de assistentes. Isso vale principalmente para o google.com, onde as fontes consultadas não permitem separar com segurança o que veio de recursos de IA da busca comum.

## Como criar um canal de IA no GA4?

O método descrito pelas fontes é um grupo de canais personalizado, com uma regra sobre a origem da sessão usando expressão regular. O passo a passo:

1. **Abra a configuração de grupos de canais** da sua propriedade GA4 e crie um grupo personalizado. Confira a documentação do Google para o caminho exato no seu painel, porque a interface muda.
2. **Crie um canal chamado, por exemplo, "Assistentes de IA"** com uma condição sobre a origem (source) que corresponda a uma expressão regular.
3. **Cole a expressão com os domínios.** A Terminus publica esta, ancorada para casar a origem inteira: `^(claude\.ai|perplexity\.ai|www\.perplexity\.ai|meta\.ai|you\.com|poe\.com|chatgpt\.com|chat\.openai\.com|gemini\.google\.com|bard\.google\.com|copilot\.microsoft\.com|chat\.deepseek\.com|grok\.com)$`
4. **Posicione o canal acima de Referral** na ordem das regras. A Seresa recomenda prioridade acima do grupo padrão; sem isso, a sessão pode ser classificada antes pelo canal genérico.
5. **Compare com a exploração de origem/mídia.** Se aparecer uma origem de IA que não está na lista, acrescente.

Uma observação sobre UTM: segundo a Terminus, o ChatGPT também acrescenta `utm_source=chatgpt.com` aos links de citação, então parte desse tráfego chega marcada, além de referida. Apenas uma das fontes lidas afirma isso, e não consegui confirmar na documentação da OpenAI nesta pesquisa. Não monte relatórios dependendo desse detalhe sem testar.

## O que fazer com o tráfego que cai em Direct?

Não atribua o Direct à IA por suposição. A Branddi, citando o suporte do Google Analytics, lembra que "(direct) / (none)" significa falta de origem clara, e que esse grupo não deve ser entregue à IA por palpite.

O que dá para fazer com segurança:

- **Olhar sinais indiretos.** A Trackingplan sugere observar aumentos de Direct em páginas internas profundas, que raramente são digitadas à mão.
- **Perguntar na origem.** Um campo "como nos conheceu?" em formulários captura o que o analytics não vê.
- **Registrar o piso.** Reporte o número do canal de IA como o mínimo observado e diga isso no relatório.
- **Avaliar medição no servidor.** A Seresa defende que o server-side recupera parte dessas visitas. A empresa vende uma solução desse tipo, então trate a afirmação como hipótese a testar, não como garantia.

## Erros comuns

- **Comparar o canal de IA com Organic Search como se fossem equivalentes.** O primeiro é um piso; o segundo tem muito mais cobertura.
- **Usar regex sem âncora e capturar domínios que não são assistentes.** Teste a expressão antes.
- **Comparar períodos sem checar o alcance da regra.** Confirme na documentação do Google se o agrupamento vale para dados históricos antes de comparar períodos.
- **Concluir resultado de negócio só com visitas.** Olhe conversões e qualidade da sessão, não só volume.

## Como saber se está funcionando?

Depois de algum tempo de coleta, você deve ver sessões no novo canal, com origens que batem com a lista. Cruze com os eventos de conversão: o que importa é se essas visitas geram contato, lead ou venda. Se o volume for pequeno, é normal. Use o dado para decidir quais páginas reforçar, e não como placar de GEO.

## Perguntas rápidas

:::faq
Q: O GA4 mostra o tráfego do ChatGPT automaticamente?
A: Em geral aparece como referral, misturado a outros sites, e parte chega como Direct. Um grupo de canais personalizado separa o que tem origem identificável.

Q: O tráfego de IA converte mais do que o orgânico?
A: Não afirmo isso. Os números que circulam vêm de estudos de terceiros que não verifiquei. Meça a conversão do seu próprio site.

Q: Dá para medir o Google AI Mode e os AI Overviews no GA4?
A: As fontes consultadas não permitem separar essas visitas do Google comum com segurança. Para isso, consulte a documentação do Google Search Console.

Q: Preciso de uma ferramenta paga?
A: Para o básico, não. O grupo de canais personalizado do GA4 resolve o que tem origem identificável. Ferramentas ajudam em escala, mas várias das fontes lidas as vendem.

Q: Com que frequência revisar a lista de domínios?
A: A cada trimestre, ou quando aparecer uma origem desconhecida nos relatórios.
:::

## Fontes

- [Terminus: The "AI Traffic" Channel in GA4: How to Define It Yourself in 2026](https://www.terminusapp.com/blog/ai-traffic-channel-in-ga4/) (a empresa vende uma plataforma de UTM e taxonomia)
- [Trackingplan: How to track ChatGPT and AI traffic in GA4](https://www.trackingplan.com/guides/track-chatgpt-ai-traffic-ga4) (a empresa vende monitoramento de analytics)
- [Branddi: Como medir tráfego de ChatGPT, Gemini e Perplexity no GA4](https://branddi.com/en/blog/como-medir-trafego-chatgpt-gemini-perplexity-ga4)
- [Seresa: AI Traffic Attribution: Why GA4 Misses Your Best Channel](https://seresa.io/blog/server-side-tracking/ai-traffic-attribution-why-ga4-misses-your-best-channel) (a empresa vende medição server-side)

As fontes acima são de fornecedores de ferramentas. Antes de aplicar, confirme os passos na documentação oficial de grupos de canais do GA4.

Quer estruturar a medição do seu marketing? Veja também [SEO, AEO e GEO: a diferença e por onde começar](/artigos/seo-aeo-geo-diferenca-por-onde-comecar/) ou [fale comigo](#contato).
