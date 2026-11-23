---
title: Tráfico de IA en GA4: cómo medir ChatGPT y Gemini
description: Las visitas de ChatGPT, Gemini y Perplexity aparecen en GA4 como referral o Direct. Aprende a separar ese tráfico y qué es lo que no puede mostrarte.
slug: trafico-de-ia-en-ga4-como-medir
date: 2026-11-23
updated: 2026-11-23
category: analytics
summary: Para medir el tráfico de asistentes de IA en GA4, crea un grupo de canales personalizado que reúna los orígenes (source) de esos asistentes. Parte de las visitas llega sin referente y cae en Direct, así que el número que ves es un piso, no el total.
---

**El tráfico de IA en GA4 es el conjunto de sesiones que llegan a tu sitio después de un clic en un enlace dentro de un asistente como ChatGPT, Gemini, Perplexity o Claude.** Medirlo exige una agrupación propia, porque GA4 no siempre separa estas visitas del resto de los referrals, y una parte llega sin un origen identificable.

Si estás invirtiendo en contenido para que las IAs lo citen, la siguiente pregunta es obvia: ¿está trayendo visitas? Esta guía muestra cómo montar la medición básica y, con igual importancia, hasta dónde llega.

## ¿Por qué el tráfico de IA se pierde en GA4?

GA4 clasifica cada sesión en canales (Organic Search, Referral, Direct y otros) a partir del origen y el medio. Las visitas de asistentes de IA suelen llegar como referral, con el dominio del asistente como origen, pero dos factores lo complican:

- **Se mezclan con otros referrals.** Sin una regla propia, las visitas de IA se diluyen entre todos los sitios que te enlazan.
- **Visitas sin referente.** Según Terminus, las apps de asistentes en móvil y escritorio normalmente no envían referente, y esas sesiones caen en Direct. Trackingplan dice lo mismo: una visita sin referente entra como Direct y se queda ahí.

Hay además una divergencia entre las fuentes. Terminus y Trackingplan describen un canal estándar de asistentes de IA en GA4, mientras que Seresa afirmó, en octubre de 2026, que Google no había anunciado una agrupación nativa. Revisa lo que muestra tu propia propiedad antes de crear cualquier regla.

## ¿Qué dominios entran en la regla?

La lista siguiente viene de Terminus (actualizada en septiembre de 2026). Úsala como punto de partida y revísala de vez en cuando, porque los productos y dominios cambian.

| Asistente | Origen (source) |
|---|---|
| ChatGPT | chatgpt.com (y el antiguo chat.openai.com) |
| Gemini | gemini.google.com (y el antiguo bard.google.com) |
| Perplexity | perplexity.ai y www.perplexity.ai |
| Claude | claude.ai |
| Copilot | copilot.microsoft.com |
| DeepSeek | chat.deepseek.com |
| Grok | grok.com |
| Otros | meta.ai, you.com, poe.com |

La misma fuente aconseja no incluir dominios genéricos como openai.com, anthropic.com o google.com, porque mezclan tráfico que no viene de asistentes. Esto pesa sobre todo en google.com, donde las fuentes que consulté no permiten separar con seguridad lo que viene de funciones de IA de la búsqueda común.

## ¿Cómo crear un canal de IA en GA4?

El método que describen las fuentes es un grupo de canales personalizado, con una regla sobre el origen de la sesión usando una expresión regular. Paso a paso:

1. **Abre la configuración de grupos de canales** de tu propiedad GA4 y crea un grupo personalizado. Revisa la documentación de Google para el camino exacto en tu panel, porque la interfaz cambia.
2. **Crea un canal llamado, por ejemplo, "Asistentes de IA"** con una condición sobre el origen (source) que coincida con una expresión regular.
3. **Pega la expresión con los dominios.** Terminus publica esta, anclada para coincidir con el origen completo: `^(claude\.ai|perplexity\.ai|www\.perplexity\.ai|meta\.ai|you\.com|poe\.com|chatgpt\.com|chat\.openai\.com|gemini\.google\.com|bard\.google\.com|copilot\.microsoft\.com|chat\.deepseek\.com|grok\.com)$`
4. **Coloca el canal por encima de Referral** en el orden de las reglas. Seresa recomienda darle prioridad sobre el grupo estándar; sin eso, el canal genérico puede clasificar la sesión primero.
5. **Compara con la exploración de origen/medio.** Si aparece un origen de IA que no está en la lista, agrégalo.

Una nota sobre UTM: según Terminus, ChatGPT también añade `utm_source=chatgpt.com` a los enlaces de cita, así que parte de ese tráfico llega etiquetada además de referida. Solo una de las fuentes que leí lo afirma, y no pude confirmarlo en la documentación de OpenAI durante esta investigación. No armes informes que dependan de ese detalle sin probarlo.

## ¿Qué hacer con el tráfico que cae en Direct?

No asumas que Direct es IA. Branddi, citando el soporte de Google Analytics, recuerda que "(direct) / (none)" significa falta de un origen claro, y que ese grupo no debe asignarse a la IA por suposición.

Lo que se puede hacer con seguridad:

- **Mirar señales indirectas.** Trackingplan sugiere observar aumentos de Direct en páginas internas profundas, que casi nadie escribe a mano.
- **Preguntar en el origen.** Un campo "¿cómo nos conociste?" en los formularios captura lo que el analytics no ve.
- **Reportar el piso.** Presenta el número del canal de IA como el mínimo observado y dilo en el informe.
- **Evaluar la medición en el servidor.** Seresa sostiene que el server-side recupera parte de esas visitas. La empresa vende una solución de ese tipo, así que trátalo como hipótesis a probar, no como garantía.

## Errores comunes

- **Comparar el canal de IA con Organic Search como si fueran equivalentes.** El primero es un piso; el segundo tiene mucha más cobertura.
- **Usar una regex sin anclar y capturar dominios que no son asistentes.** Prueba la expresión antes.
- **Comparar períodos sin revisar el alcance de la regla.** Confirma en la documentación de Google si la agrupación se aplica a datos históricos antes de comparar.
- **Sacar conclusiones de negocio solo con visitas.** Mira conversiones y calidad de la sesión, no solo volumen.

## ¿Cómo saber si está funcionando?

Tras un tiempo de recolección, deberías ver sesiones en el nuevo canal, con orígenes que coinciden con tu lista. Cruza con los eventos de conversión: lo que importa es si esas visitas generan contactos, leads o ventas. Un volumen bajo es normal. Usa el dato para decidir qué páginas reforzar, no como marcador de GEO.

## Preguntas rápidas

:::faq
Q: ¿GA4 muestra automáticamente el tráfico de ChatGPT?
A: En general aparece como referral, mezclado con otros sitios, y parte llega como Direct. Un grupo de canales personalizado separa lo que tiene origen identificable.

Q: ¿El tráfico de IA convierte mejor que el orgánico?
A: No lo afirmo. Las cifras que circulan vienen de estudios de terceros que no verifiqué. Mide la conversión en tu propio sitio.

Q: ¿Puedo medir Google AI Mode y AI Overviews en GA4?
A: Las fuentes que consulté no permiten separar esas visitas del Google común con seguridad. Para eso, consulta la documentación de Google Search Console.

Q: ¿Necesito una herramienta de pago?
A: Para lo básico, no. El grupo de canales personalizado de GA4 resuelve lo que tiene origen identificable. Las herramientas ayudan a escala, pero varias de las fuentes que leí las venden.

Q: ¿Cada cuánto revisar la lista de dominios?
A: Cada trimestre, o cuando aparezca un origen desconocido en tus informes.
:::

## Fuentes

- [Terminus: The "AI Traffic" Channel in GA4: How to Define It Yourself in 2026](https://www.terminusapp.com/blog/ai-traffic-channel-in-ga4/) (la empresa vende una plataforma de UTM y taxonomía)
- [Trackingplan: How to track ChatGPT and AI traffic in GA4](https://www.trackingplan.com/guides/track-chatgpt-ai-traffic-ga4) (la empresa vende monitoreo de analytics)
- [Branddi: How to Measure Traffic from ChatGPT, Gemini, and Perplexity in GA4](https://branddi.com/en/blog/como-medir-trafego-chatgpt-gemini-perplexity-ga4)
- [Seresa: AI Traffic Attribution: Why GA4 Misses Your Best Channel](https://seresa.io/blog/server-side-tracking/ai-traffic-attribution-why-ga4-misses-your-best-channel) (la empresa vende medición server-side)

Estas fuentes son de proveedores de herramientas. Antes de aplicar los pasos, confírmalos en la documentación oficial de grupos de canales de GA4.

¿Quieres estructurar la medición de tu marketing? Mira también [SEO, AEO y GEO: la diferencia y por dónde empezar](/es/articulos/seo-aeo-geo-diferencia-por-donde-empezar/) o [habla conmigo](#contato).
