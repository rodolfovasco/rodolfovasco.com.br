# -*- coding: utf-8 -*-
"""Conteúdo do site em três idiomas (pt-BR, en, es). Tudo que é texto visível, SEO e schema vive aqui."""

ORDER = ["pt", "en", "es"]
LABEL = {"pt": "PT", "en": "EN", "es": "ES"}
NATIVE = {"pt": "Português", "en": "English", "es": "Español"}

L = {}

# ---------------------------------------------------------------- PORTUGUÊS
L["pt"] = dict(
    code="pt", html_lang="pt-BR", hreflang="pt-BR", og_locale="pt_BR",
    path="/", priv_path="/privacidade/",
    title="IA & Martech | Rodolfo Vasco, Head de Marketing",
    desc="IA & Martech: dados, automação, performance, analytics e SEO/GEO/AEO para marcas de todos os portes. Com Rodolfo Vasco, Head de Marketing, 17 anos de experiência.",
    og_desc="IA, martech, dados e performance: 17 anos na interseção entre marketing e tecnologia.",
    tw_desc="17 anos na interseção entre marketing e tecnologia.",
    skip="Pular para o conteúdo", brand_aria="Rodolfo Vasco, início", nav_aria="Principal", lang_aria="Idioma",
    nav=["Sobre", "Especializações", "Cases", "Formação", "Perguntas"], top_cta="Conversar",
    h1_l1="IA &amp;", h1_l2="Martech",
    role="Head de Marketing & Martech",
    lede="Estratégia, dados e automação com inteligência artificial para transformar marketing em receita. Há 17 anos conectando mídia, tecnologia e dados como uma única engrenagem.",
    btn_talk="Agendar uma conversa", btn_cases="Ver cases",
    wa_text="Ol%C3%A1!%20Vim%20do%20seu%20site%20e%20gostaria%20de%20conversar.",
    rail_sobre="Sobre",
    manifesto="O que o cliente vê é o anúncio. O que decide o resultado do seu negócio precisa ser visto: a medição, a integração entre sistemas, a automação e os dados. É nessa camada que eu trabalho há 17 anos, para que cada real investido em mídia seja rastreado, explicado e otimizado.",
    facts=[("17+", "anos na interseção entre marketing e tecnologia"),
           ("50+", "marcas atendidas, de pequeno a grande porte"),
           ("40+", "certificações profissionais oficiais")],
    rail_esp="Especializações",
    esp_intro="Dados, tecnologia e mídia trabalhando como um único sistema de crescimento.",
    craft=[("Estratégia baseada em dados", "Ecossistemas analíticos avançados que transformam dados brutos em insights de mercado acionáveis."),
           ("Arquitetura de martech", "Desenho e integração de stacks de marketing escaláveis, que elevam a eficiência operacional."),
           ("IA e automação de growth", "Inteligência artificial e automação para otimizar o ciclo de vida do cliente e maximizar o LTV."),
           ("Marketing de performance", "Mídia de alto ROI e crescimento pago que escala a receita com precisão."),
           ("Web analytics", "GA4, protocolos de medição e modelagem de atribuição para resolver problemas complexos de rastreamento."),
           ("SEO, AEO e GEO", "Otimização técnica, busca semântica e construção de autoridade, tanto no Google quanto nas respostas de IA.")],
    rail_cases="Cases",
    cases_intro="Desafios diferentes, a mesma lógica: medir, integrar e escalar.",
    h_challenge="Desafio", h_action="Atuação",
    cases=[("Performance", "Hospital de Amor",
            "Captar doadores e manter o engajamento deles ao longo do tempo.",
            "Transformação digital da captação, com campanhas hiper-segmentadas de Google Ads, Meta Ads e mídia programática."),
           ("Performance internacional", "Votorantim",
            "Globalizar a marca e atrair novos investidores no mercado estrangeiro.",
            "Campanhas de mídia de performance hiper-segmentadas, impactando o investidor em toda a jornada do usuário."),
           ("SEO", "Premix",
            "Ranquear e adquirir tráfego orgânico para os termos-chave da marca.",
            "Redesenho de toda a estrutura técnica dos conteúdos, em busca das primeiras posições do Google."),
           ("Arquitetura de martech", "Audi",
            "Elevar o desempenho do site de uma empresa do setor automobilístico.",
            "Refatoração do site com as melhores práticas do Google PageSpeed e do GTmetrix, com foco em Core Web Vitals."),
           ("Marketing digital", "Kohler Brasil",
            "Vender 5.000 unidades do Moxie, o chuveiro monofuncional, no Brasil.",
            "Estratégia digital full service no lançamento: campanhas patrocinadas, comunicação e martech."),
           ("E-commerce", "Be & Care",
            "Construir a presença digital de um e-commerce de saúde e beleza em vários países.",
            "Campanhas patrocinadas em diversos canais, gerando vendas, aumentando o ticket médio e reduzindo o custo de aquisição.")],
    rail_edu="Formação e certificações",
    edu=[("Universidade Presbiteriana Mackenzie", "Especialização em Marketing"),
         ("FGV, Fundação Getulio Vargas", "Graduação em Análise e Desenvolvimento de Sistemas<br>Pós-graduação em nível de extensão em Gestão da Comunicação"),
         ("ESPM", "Master em Digital Marketing"),
         ("Universidade do Vale do Silício", "Pós-graduação em Marketing Digital")],
    cert_title="Certificações oficiais das plataformas que movem o marketing.",
    certs=["Google Ads Certified", "Meta Blueprint", "HubSpot Expert", "LinkedIn Expert", "Bing Professional",
           "Twitter Flight School", "IA Specialist", "Data Driven Marketing"],
    cert_note="Entre mais de 40 certificações profissionais.",
    rail_faq="Perguntas frequentes",
    faq=[
        ("O que é martech e por que ela importa para o marketing?",
         "Martech (marketing technology) é o conjunto de ferramentas e integrações que sustenta o marketing: CRM, automação, analytics, mídia, CMS e plataformas de dados. É ela que permite medir, segmentar e automatizar. Meu trabalho é desenhar essa stack para que as ferramentas conversem entre si e gerem dado confiável, em vez de virarem uma coleção de assinaturas soltas.", None),
        ("O que é marketing de performance e como saber se está funcionando?",
         "É a gestão de mídia e de canais pagos orientada por resultado mensurável, como leads e vendas, e não por alcance ou cliques. Para saber se funciona, eu acompanho CAC (custo de aquisição de cliente), ROAS (retorno sobre o investimento em anúncios), taxa de conversão e LTV (valor do cliente ao longo do tempo), sempre ligados à receita.", None),
        ("Por que os números do GA4 não batem com os do Google Ads e do Meta Ads?",
         "Porque cada plataforma usa um modelo de atribuição e uma janela de conversão diferentes. Atribuição é a regra que define qual canal recebe o crédito por uma conversão. A saída é padronizar eventos e UTMs, escolher um modelo único para decidir e cruzar tudo com o CRM, que é onde a venda realmente acontece.", None),
        ("Qual é a diferença entre SEO, AEO e GEO?",
         "SEO otimiza páginas para aparecerem nos resultados de busca. AEO (Answer Engine Optimization) estrutura o conteúdo para ser escolhido como resposta direta, em featured snippets, assistentes e AI Overviews. GEO (Generative Engine Optimization) trabalha para que IAs como ChatGPT, Gemini e Perplexity citem a sua marca. Os três dependem de conteúdo claro, dados estruturados (schema), autoridade e SEO técnico em dia.", None),
        ("Como usar inteligência artificial no marketing digital sem perder qualidade?",
         "Use IA onde há volume e repetição: segmentação, automação do ciclo de vida do cliente, análise de dados, rascunhos de conteúdo e testes de criativos. Mantenha revisão humana na estratégia, no tom de voz e nos números. Eu começo por um processo, meço o ganho e só então escalo.", None),
        ("Como montar uma stack de martech para uma empresa pequena ou média?",
         "Comece pelo essencial: um CRM como fonte única de verdade, uma ferramenta de automação de marketing, o GA4 com eventos bem definidos e um gerenciador de tags. Depois integre as mídias pagas e só adicione uma ferramenta nova quando existir um processo que precise dela. Poucas ferramentas bem integradas rendem mais do que uma stack grande e desconectada.", None),
        ("O que faz um Head de Marketing & Martech?",
         "É quem define a estratégia de marketing e a arquitetura tecnológica que a sustenta, ao mesmo tempo: mídia, dados, automação e analytics. Eu lidero essa frente há 17 anos, conectando o investimento em mídia ao resultado do negócio.", None),
        ("Como posso trabalhar com você?",
         "Fale comigo pelo WhatsApp, pelo e-mail rodolfovasco@gmail.com ou pelo LinkedIn. Atendo empresas de pequeno, médio e grande porte em projetos de martech, performance, analytics, IA e SEO, AEO e GEO.",
         'Fale comigo pelo <a href="{WA}" rel="noopener">WhatsApp</a>, pelo e-mail <a href="mailto:rodolfovasco@gmail.com">rodolfovasco@gmail.com</a> ou pelo <a href="https://www.linkedin.com/in/rodolfovasco/" rel="me noopener">LinkedIn</a>. Atendo empresas de pequeno, médio e grande porte em projetos de martech, performance, analytics, IA e SEO, AEO e GEO.'),
    ],
    contact_h2="Vamos conversar.",
    lbl_whatsapp="WhatsApp", lbl_email="E-mail", lbl_linkedin="LinkedIn",
    foot_priv="Política de privacidade", foot_cookies="Preferências de cookies", foot_tag="Marketing, dados e tecnologia",
    consent_aria="Aviso de cookies",
    consent_text='Uso cookies para medir a audiência e melhorar o site. Você escolhe se aceita, e pode mudar de ideia a qualquer momento em "Preferências de cookies", no rodapé.',
    consent_accept="Aceitar", consent_decline="Recusar",
    job_title="Head de Marketing & Martech",
    person_desc="Head de Marketing & Martech com 17 anos de experiência na interseção entre marketing e tecnologia, atendendo marcas de pequeno a grande porte.",
    knows=["Inteligência artificial", "IA aplicada ao marketing", "Marketing digital", "Martech", "Marketing de performance", "Web analytics", "GA4",
           "SEO", "AEO", "GEO", "Automação de growth", "Business Intelligence"],
    llms_summary="IA & Martech: Head de Marketing com 17 anos de experiência na interseção entre marketing e tecnologia. Atendeu mais de 50 marcas, de pequeno a grande porte, e soma mais de 40 certificações profissionais oficiais.",
    llms_contact="Contato", llms_edu="Formação", llms_certs="Certificações", llms_priv="Privacidade", llms_priv_label="Política de privacidade",
    llms_craft="Especializações", llms_cases="Cases",
    # --- privacidade
    priv_title="Política de privacidade | Rodolfo Vasco",
    priv_desc="Como o site de Rodolfo Vasco trata dados pessoais e cookies, seus direitos pela LGPD e como falar sobre privacidade.",
    priv_back="Voltar ao site", priv_back_aria="Rodolfo Vasco, voltar ao início",
    priv_main="""  <h1>Política de privacidade</h1>
  <p class="date">Atualizada em 2 de novembro de 2026</p>
  <p class="lead">Este é um site pessoal e coleta o mínimo necessário. Aqui explico, de forma direta, quais dados são tratados, por quê e como você controla isso, conforme a Lei Geral de Proteção de Dados (LGPD, Lei nº 13.709/2018).</p>

  <h2>1. Quem é o responsável</h2>
  <p>O responsável pelo tratamento dos dados é Rodolfo Vasco, titular do site rodolfovasco.com.br. Para qualquer assunto de privacidade, escreva para <a class="ul" href="mailto:rodolfovasco@gmail.com">rodolfovasco@gmail.com</a>.</p>

  <h2>2. Quais dados são tratados e para quê</h2>
  <ul>
    <li><strong>Dados de navegação, só com o seu aceite.</strong> Se você aceitar os cookies, o Google Tag Manager pode ativar ferramentas de medição, como o Google Analytics. Elas registram informações como páginas visitadas, cliques nos botões de contato, tipo de dispositivo e navegador, localização aproximada e endereço IP (tratado pelo fornecedor). Uso isso para entender como o site é usado e melhorá-lo.</li>
    <li><strong>Dados que você me envia.</strong> O site não tem formulário. Se você me chamar por WhatsApp, e-mail ou LinkedIn, trato seu nome, seu contato e o conteúdo da mensagem apenas para responder e conduzir a conversa.</li>
    <li><strong>Dados técnicos de acesso.</strong> Os servidores que entregam o site (hospedagem no GitHub Pages) e as fontes de letras (Google Fonts) recebem seu endereço IP e dados do navegador para que a página carregue. Isso é inerente ao funcionamento da internet.</li>
  </ul>
  <p>Se, no futuro, eu usar ferramentas de publicidade ou remarketing, elas também só funcionarão com o seu aceite, e esta política será atualizada antes disso.</p>

  <h2>3. Cookies e a sua escolha</h2>
  <p>Na primeira visita, o site mostra um aviso de cookies. Sem o seu aceite, as ferramentas de medição e de publicidade ficam desativadas (Consent Mode v2 do Google).</p>
  <ul>
    <li><strong>Essencial:</strong> <code>rv_consent</code>, guardado no armazenamento local do seu navegador, registra se você aceitou ou recusou. Fica até você apagar os dados do site. O mesmo vale para <code>rv_lang</code>, que guarda o idioma que você escolheu.</li>
    <li><strong>Medição (só com aceite):</strong> cookies do Google Analytics, como <code>_ga</code>, quando essa ferramenta estiver ativa no Tag Manager. O Google define o prazo, em geral de até 2 anos.</li>
  </ul>
  <p>Você pode mudar de ideia quando quiser, ou apagar os dados do site no seu navegador.</p>
  <a class="btn" href="{HOME}#cookies">Alterar minha escolha de cookies</a>

  <h2>4. Com quem os dados podem ser compartilhados</h2>
  <p>Com o Google (Tag Manager, Analytics e Fonts), com o GitHub (hospedagem do site) e com as plataformas de mensagem que você escolher para falar comigo. Não vendo dados pessoais. Alguns desses provedores ficam fora do Brasil, como nos Estados Unidos, e a transferência segue a LGPD, com as garantias oferecidas por eles.</p>

  <h2>5. Por quanto tempo os dados ficam guardados</h2>
  <p>Os dados de medição ficam pelo período definido na própria ferramenta e podem ser apagados a seu pedido quando for possível identificar você. As mensagens de contato ficam pelo tempo necessário para a conversa e para cumprir obrigações legais.</p>

  <h2>6. Seus direitos</h2>
  <p>Pela LGPD, você pode pedir:</p>
  <ul>
    <li>confirmação de que seus dados são tratados e acesso a eles;</li>
    <li>correção de dados incompletos, inexatos ou desatualizados;</li>
    <li>anonimização, bloqueio ou eliminação de dados desnecessários ou tratados em desacordo com a lei;</li>
    <li>portabilidade dos dados;</li>
    <li>informação sobre com quem os dados foram compartilhados;</li>
    <li>revogação do consentimento, a qualquer momento.</li>
  </ul>
  <p>Para exercer qualquer um desses direitos, escreva para <a class="ul" href="mailto:rodolfovasco@gmail.com">rodolfovasco@gmail.com</a>. Respondo em até 15 dias. Você também pode apresentar reclamação à Autoridade Nacional de Proteção de Dados (ANPD), em <a class="ul" href="https://www.gov.br/anpd" rel="noopener">gov.br/anpd</a>.</p>

  <h2>7. Atualizações</h2>
  <p>Posso atualizar esta política quando o site mudar. A data da última revisão está sempre no topo da página.</p>""",
)

# ---------------------------------------------------------------- ENGLISH
L["en"] = dict(
    code="en", html_lang="en", hreflang="en", og_locale="en_US",
    path="/en/", priv_path="/en/privacy/",
    title="AI & Martech | Rodolfo Vasco, Head of Marketing",
    desc="AI & Martech: data, automation, performance, analytics and SEO/GEO/AEO for brands of every size. With Rodolfo Vasco, Head of Marketing, 17 years of experience.",
    og_desc="AI, martech, data and performance: 17 years at the intersection of marketing and technology.",
    tw_desc="17 years at the intersection of marketing and technology.",
    skip="Skip to content", brand_aria="Rodolfo Vasco, home", nav_aria="Main", lang_aria="Language",
    nav=["About", "Expertise", "Cases", "Education", "FAQ"], top_cta="Let's talk",
    h1_l1="AI &amp;", h1_l2="Martech",
    role="Head of Marketing & Martech",
    lede="Strategy, data and automation with artificial intelligence to turn marketing into revenue. Seventeen years connecting media, technology and data as one engine.",
    btn_talk="Book a conversation", btn_cases="See cases",
    wa_text="Hi!%20I%20found%20you%20through%20your%20website%20and%20would%20like%20to%20talk.",
    rail_sobre="About",
    manifesto="What the customer sees is the ad. What decides your business results needs to be seen: measurement, system integration, automation and data. That is the layer I have worked on for 17 years, so that every cent invested in media is tracked, explained and optimized.",
    facts=[("17+", "years at the intersection of marketing and technology"),
           ("50+", "brands served, from small to large"),
           ("40+", "official professional certifications")],
    rail_esp="Expertise",
    esp_intro="Data, technology and media working as a single growth system.",
    craft=[("Data-driven strategy", "Advanced analytics ecosystems that turn raw data into actionable market insights."),
           ("Martech architecture", "Design and integration of scalable marketing stacks that raise operational efficiency."),
           ("AI and growth automation", "Artificial intelligence and automation to optimize the customer lifecycle and maximize LTV."),
           ("Performance marketing", "High-ROI media and paid growth that scales revenue with precision."),
           ("Web analytics", "GA4, measurement protocols and attribution modeling to solve complex tracking problems."),
           ("SEO, AEO and GEO", "Technical optimization, semantic search and authority building, both on Google and in AI answers.")],
    rail_cases="Cases",
    cases_intro="Different challenges, the same logic: measure, integrate and scale.",
    h_challenge="Challenge", h_action="Approach",
    cases=[("Performance", "Hospital de Amor",
            "Attract donors and keep them engaged over time.",
            "Digital transformation of fundraising, with hyper-targeted Google Ads, Meta Ads and programmatic media campaigns."),
           ("International performance", "Votorantim",
            "Take the brand global and attract new investors in foreign markets.",
            "Hyper-targeted performance media campaigns, reaching the investor across the entire user journey."),
           ("SEO", "Premix",
            "Rank and acquire organic traffic for the brand's key terms.",
            "Redesign of the entire technical structure of the content, aiming for Google's top positions."),
           ("Martech architecture", "Audi",
            "Raise the performance of an automotive company's website.",
            "Site refactoring following Google PageSpeed and GTmetrix best practices, focused on Core Web Vitals."),
           ("Digital marketing", "Kohler Brasil",
            "Sell 5,000 units of the Moxie, the single-function shower head, in Brazil.",
            "Full-service digital strategy for the launch: sponsored campaigns, communication and martech."),
           ("E-commerce", "Be & Care",
            "Build the digital presence of a health and beauty e-commerce across several countries.",
            "Sponsored campaigns across multiple channels, generating sales, raising average order value and lowering acquisition cost.")],
    rail_edu="Education & certifications",
    edu=[("Universidade Presbiteriana Mackenzie", "Specialization in Marketing"),
         ("FGV, Fundação Getulio Vargas", "Bachelor's degree in Systems Analysis and Development<br>Extension-level postgraduate degree in Communication Management"),
         ("ESPM", "Master in Digital Marketing"),
         ("Universidade do Vale do Silício", "Postgraduate degree in Digital Marketing")],
    cert_title="Official certifications from the platforms that move marketing.",
    certs=["Google Ads Certified", "Meta Blueprint", "HubSpot Expert", "LinkedIn Expert", "Bing Professional",
           "Twitter Flight School", "AI Specialist", "Data Driven Marketing"],
    cert_note="Among more than 40 professional certifications.",
    rail_faq="Frequently asked questions",
    faq=[
        ("What is martech and why does it matter for marketing?",
         "Martech (marketing technology) is the set of tools and integrations that powers marketing: CRM, automation, analytics, media, CMS and data platforms. It is what makes it possible to measure, segment and automate. My job is to design that stack so the tools talk to each other and produce reliable data, instead of becoming a collection of loose subscriptions.", None),
        ("What is performance marketing and how do I know if it is working?",
         "It is the management of media and paid channels driven by measurable results, such as leads and sales, rather than reach or clicks. To know whether it works, I track CAC (customer acquisition cost), ROAS (return on ad spend), conversion rate and LTV (customer lifetime value), always tied to revenue.", None),
        ("Why don't GA4 numbers match Google Ads and Meta Ads?",
         "Because each platform uses a different attribution model and conversion window. Attribution is the rule that decides which channel gets credit for a conversion. The way out is to standardize events and UTMs, pick a single model to make decisions, and cross-check everything against the CRM, which is where the sale actually happens.", None),
        ("What is the difference between SEO, AEO and GEO?",
         "SEO optimizes pages to show up in search results. AEO (Answer Engine Optimization) structures content to be chosen as the direct answer, in featured snippets, assistants and AI Overviews. GEO (Generative Engine Optimization) works so that AIs like ChatGPT, Gemini and Perplexity cite your brand. All three depend on clear content, structured data (schema), authority and up-to-date technical SEO.", None),
        ("How can I use artificial intelligence in digital marketing without losing quality?",
         "Use AI where there is volume and repetition: segmentation, customer lifecycle automation, data analysis, content drafts and creative testing. Keep human review on strategy, tone of voice and the numbers. I start with one process, measure the gain and only then scale.", None),
        ("How do I build a martech stack for a small or mid-sized company?",
         "Start with the essentials: a CRM as the single source of truth, a marketing automation tool, GA4 with well-defined events and a tag manager. Then integrate paid media and only add a new tool when there is a process that needs it. A few well-integrated tools deliver more than a large, disconnected stack.", None),
        ("What does a Head of Marketing & Martech do?",
         "This person defines the marketing strategy and the technology architecture that supports it, at the same time: media, data, automation and analytics. I have led this front for 17 years, connecting media investment to business results.", None),
        ("How can I work with you?",
         "Reach me on WhatsApp, by email at rodolfovasco@gmail.com or on LinkedIn. I work with small, mid-sized and large companies on martech, performance, analytics, AI and SEO, AEO and GEO projects.",
         'Reach me on <a href="{WA}" rel="noopener">WhatsApp</a>, by email at <a href="mailto:rodolfovasco@gmail.com">rodolfovasco@gmail.com</a> or on <a href="https://www.linkedin.com/in/rodolfovasco/" rel="me noopener">LinkedIn</a>. I work with small, mid-sized and large companies on martech, performance, analytics, AI and SEO, AEO and GEO projects.'),
    ],
    contact_h2="Let's talk.",
    lbl_whatsapp="WhatsApp", lbl_email="Email", lbl_linkedin="LinkedIn",
    foot_priv="Privacy policy", foot_cookies="Cookie preferences", foot_tag="Marketing, data and technology",
    consent_aria="Cookie notice",
    consent_text='I use cookies to measure the audience and improve the site. You choose whether to accept, and you can change your mind at any time in "Cookie preferences" in the footer.',
    consent_accept="Accept", consent_decline="Decline",
    job_title="Head of Marketing & Martech",
    person_desc="Head of Marketing & Martech with 17 years of experience at the intersection of marketing and technology, serving brands from small to large.",
    knows=["Artificial intelligence", "AI applied to marketing", "Digital marketing", "Martech", "Performance marketing", "Web analytics", "GA4",
           "SEO", "AEO", "GEO", "Growth automation", "Business Intelligence"],
    llms_summary="AI & Martech: Head of Marketing with 17 years of experience at the intersection of marketing and technology. Has served more than 50 brands, from small to large, and holds more than 40 official professional certifications.",
    llms_contact="Contact", llms_edu="Education", llms_certs="Certifications", llms_priv="Privacy", llms_priv_label="Privacy policy",
    llms_craft="Expertise", llms_cases="Cases",
    priv_title="Privacy policy | Rodolfo Vasco",
    priv_desc="How Rodolfo Vasco's website handles personal data and cookies, your rights under Brazil's LGPD and how to contact me about privacy.",
    priv_back="Back to the site", priv_back_aria="Rodolfo Vasco, back to home",
    priv_main="""  <h1>Privacy policy</h1>
  <p class="date">Updated on November 2, 2026</p>
  <p class="lead">This is a personal website and it collects the minimum necessary. Here I explain, plainly, which data is processed, why, and how you control it, in line with Brazil's General Data Protection Law (LGPD, Law No. 13,709/2018).</p>

  <h2>1. Who is responsible</h2>
  <p>The party responsible for processing the data is Rodolfo Vasco, owner of the website rodolfovasco.com.br. For any privacy matter, write to <a class="ul" href="mailto:rodolfovasco@gmail.com">rodolfovasco@gmail.com</a>.</p>

  <h2>2. What data is processed and why</h2>
  <ul>
    <li><strong>Browsing data, only with your consent.</strong> If you accept cookies, Google Tag Manager may activate measurement tools, such as Google Analytics. They record information such as pages visited, clicks on contact buttons, device and browser type, approximate location and IP address (processed by the provider). I use this to understand how the site is used and to improve it.</li>
    <li><strong>Data you send me.</strong> The site has no form. If you contact me through WhatsApp, email or LinkedIn, I process your name, your contact details and the content of your message only to reply and carry on the conversation.</li>
    <li><strong>Technical access data.</strong> The servers that deliver the site (hosted on GitHub Pages) and the font service (Google Fonts) receive your IP address and browser data so that the page can load. This is inherent to how the internet works.</li>
  </ul>
  <p>If, in the future, I use advertising or remarketing tools, they will also only run with your consent, and this policy will be updated before that happens.</p>

  <h2>3. Cookies and your choice</h2>
  <p>On your first visit, the site shows a cookie notice. Without your consent, measurement and advertising tools stay off (Google Consent Mode v2).</p>
  <ul>
    <li><strong>Essential:</strong> <code>rv_consent</code>, stored in your browser's local storage, records whether you accepted or declined. It stays until you clear the site data. The same applies to <code>rv_lang</code>, which stores the language you chose.</li>
    <li><strong>Measurement (only with consent):</strong> Google Analytics cookies, such as <code>_ga</code>, when that tool is active in Tag Manager. Google sets the duration, usually up to 2 years.</li>
  </ul>
  <p>You can change your mind at any time, or clear the site data in your browser.</p>
  <a class="btn" href="{HOME}#cookies">Change my cookie choice</a>

  <h2>4. Who the data may be shared with</h2>
  <p>With Google (Tag Manager, Analytics and Fonts), with GitHub (site hosting) and with the messaging platforms you choose to contact me. I do not sell personal data. Some of these providers are located outside Brazil, such as in the United States, and the transfer follows the LGPD, with the safeguards they offer.</p>

  <h2>5. How long the data is kept</h2>
  <p>Measurement data is kept for the period set in the tool itself and can be deleted on your request when you can be identified. Contact messages are kept for as long as needed for the conversation and to meet legal obligations.</p>

  <h2>6. Your rights</h2>
  <p>Under the LGPD, you can request:</p>
  <ul>
    <li>confirmation that your data is being processed and access to it;</li>
    <li>correction of incomplete, inaccurate or outdated data;</li>
    <li>anonymization, blocking or deletion of unnecessary data or data processed in violation of the law;</li>
    <li>data portability;</li>
    <li>information about who the data has been shared with;</li>
    <li>withdrawal of consent, at any time.</li>
  </ul>
  <p>To exercise any of these rights, write to <a class="ul" href="mailto:rodolfovasco@gmail.com">rodolfovasco@gmail.com</a>. I reply within 15 days. You may also file a complaint with Brazil's National Data Protection Authority (ANPD) at <a class="ul" href="https://www.gov.br/anpd" rel="noopener">gov.br/anpd</a>. If you are located outside Brazil, you can write to the same address and I will handle your request in line with the applicable law.</p>

  <h2>7. Updates</h2>
  <p>I may update this policy when the site changes. The date of the latest revision is always at the top of the page.</p>""",
)

# ---------------------------------------------------------------- ESPAÑOL
L["es"] = dict(
    code="es", html_lang="es", hreflang="es", og_locale="es_LA",
    path="/es/", priv_path="/es/privacidad/",
    title="IA & Martech | Rodolfo Vasco, Head de Marketing",
    desc="IA & Martech: datos, automatización, performance, analítica y SEO/GEO/AEO para marcas de todos los tamaños. Con Rodolfo Vasco, Head de Marketing, 17 años de experiencia.",
    og_desc="IA, martech, datos y performance: 17 años en la intersección entre marketing y tecnología.",
    tw_desc="17 años en la intersección entre marketing y tecnología.",
    skip="Saltar al contenido", brand_aria="Rodolfo Vasco, inicio", nav_aria="Principal", lang_aria="Idioma",
    nav=["Sobre mí", "Especialidades", "Casos", "Formación", "Preguntas"], top_cta="Hablemos",
    h1_l1="IA &amp;", h1_l2="Martech",
    role="Head de Marketing & Martech",
    lede="Estrategia, datos y automatización con inteligencia artificial para convertir el marketing en ingresos. Hace 17 años conectando medios, tecnología y datos como un único engranaje.",
    btn_talk="Agendar una conversación", btn_cases="Ver casos",
    wa_text="%C2%A1Hola!%20Vengo%20de%20tu%20sitio%20y%20me%20gustar%C3%ADa%20conversar.",
    rail_sobre="Sobre mí",
    manifesto="Lo que el cliente ve es el anuncio. Lo que decide el resultado de tu negocio tiene que verse: la medición, la integración entre sistemas, la automatización y los datos. Es en esa capa donde trabajo desde hace 17 años, para que cada centavo invertido en medios sea rastreado, explicado y optimizado.",
    facts=[("17+", "años en la intersección entre marketing y tecnología"),
           ("50+", "marcas atendidas, de pequeñas a grandes"),
           ("40+", "certificaciones profesionales oficiales")],
    rail_esp="Especialidades",
    esp_intro="Datos, tecnología y medios trabajando como un único sistema de crecimiento.",
    craft=[("Estrategia basada en datos", "Ecosistemas analíticos avanzados que convierten datos en bruto en insights de mercado accionables."),
           ("Arquitectura de martech", "Diseño e integración de stacks de marketing escalables que elevan la eficiencia operativa."),
           ("IA y automatización de growth", "Inteligencia artificial y automatización para optimizar el ciclo de vida del cliente y maximizar el LTV."),
           ("Marketing de performance", "Medios de alto ROI y crecimiento pago que escala los ingresos con precisión."),
           ("Analítica web", "GA4, protocolos de medición y modelado de atribución para resolver problemas complejos de rastreo."),
           ("SEO, AEO y GEO", "Optimización técnica, búsqueda semántica y construcción de autoridad, tanto en Google como en las respuestas de IA.")],
    rail_cases="Casos",
    cases_intro="Desafíos distintos, la misma lógica: medir, integrar y escalar.",
    h_challenge="Desafío", h_action="Actuación",
    cases=[("Performance", "Hospital de Amor",
            "Captar donantes y mantener su compromiso a lo largo del tiempo.",
            "Transformación digital de la captación, con campañas hipersegmentadas de Google Ads, Meta Ads y medios programáticos."),
           ("Performance internacional", "Votorantim",
            "Globalizar la marca y atraer nuevos inversionistas en el mercado extranjero.",
            "Campañas de medios de performance hipersegmentadas, impactando al inversionista en todo el recorrido del usuario."),
           ("SEO", "Premix",
            "Posicionar y adquirir tráfico orgánico para los términos clave de la marca.",
            "Rediseño de toda la estructura técnica de los contenidos, en busca de las primeras posiciones de Google."),
           ("Arquitectura de martech", "Audi",
            "Elevar el rendimiento del sitio de una empresa del sector automotriz.",
            "Refactorización del sitio con las mejores prácticas de Google PageSpeed y GTmetrix, con foco en Core Web Vitals."),
           ("Marketing digital", "Kohler Brasil",
            "Vender 5.000 unidades del Moxie, la ducha monofuncional, en Brasil.",
            "Estrategia digital full service en el lanzamiento: campañas patrocinadas, comunicación y martech."),
           ("E-commerce", "Be & Care",
            "Construir la presencia digital de un e-commerce de salud y belleza en varios países.",
            "Campañas patrocinadas en diversos canales, generando ventas, aumentando el ticket promedio y reduciendo el costo de adquisición.")],
    rail_edu="Formación y certificaciones",
    edu=[("Universidade Presbiteriana Mackenzie", "Especialización en Marketing"),
         ("FGV, Fundação Getulio Vargas", "Grado en Análisis y Desarrollo de Sistemas<br>Posgrado de extensión en Gestión de la Comunicación"),
         ("ESPM", "Máster en Digital Marketing"),
         ("Universidade do Vale do Silício", "Posgrado en Marketing Digital")],
    cert_title="Certificaciones oficiales de las plataformas que mueven el marketing.",
    certs=["Google Ads Certified", "Meta Blueprint", "HubSpot Expert", "LinkedIn Expert", "Bing Professional",
           "Twitter Flight School", "IA Specialist", "Data Driven Marketing"],
    cert_note="Entre más de 40 certificaciones profesionales.",
    rail_faq="Preguntas frecuentes",
    faq=[
        ("¿Qué es martech y por qué importa para el marketing?",
         "Martech (marketing technology) es el conjunto de herramientas e integraciones que sostiene el marketing: CRM, automatización, analítica, medios, CMS y plataformas de datos. Es lo que permite medir, segmentar y automatizar. Mi trabajo es diseñar ese stack para que las herramientas se hablen entre sí y generen datos confiables, en lugar de convertirse en una colección de suscripciones sueltas.", None),
        ("¿Qué es el marketing de performance y cómo saber si está funcionando?",
         "Es la gestión de medios y canales pagos orientada a resultados medibles, como leads y ventas, y no al alcance o a los clics. Para saber si funciona, sigo el CAC (costo de adquisición de cliente), el ROAS (retorno de la inversión publicitaria), la tasa de conversión y el LTV (valor del cliente a lo largo del tiempo), siempre ligados a los ingresos.", None),
        ("¿Por qué los números de GA4 no coinciden con los de Google Ads y Meta Ads?",
         "Porque cada plataforma usa un modelo de atribución y una ventana de conversión diferentes. La atribución es la regla que define qué canal recibe el crédito por una conversión. La salida es estandarizar eventos y UTMs, elegir un único modelo para decidir y cruzar todo con el CRM, que es donde la venta realmente ocurre.", None),
        ("¿Cuál es la diferencia entre SEO, AEO y GEO?",
         "SEO optimiza páginas para aparecer en los resultados de búsqueda. AEO (Answer Engine Optimization) estructura el contenido para ser elegido como respuesta directa, en featured snippets, asistentes y AI Overviews. GEO (Generative Engine Optimization) trabaja para que IAs como ChatGPT, Gemini y Perplexity citen tu marca. Los tres dependen de contenido claro, datos estructurados (schema), autoridad y un SEO técnico al día.", None),
        ("¿Cómo usar inteligencia artificial en el marketing digital sin perder calidad?",
         "Usa IA donde hay volumen y repetición: segmentación, automatización del ciclo de vida del cliente, análisis de datos, borradores de contenido y pruebas de creativos. Mantén revisión humana en la estrategia, el tono de voz y los números. Yo empiezo por un proceso, mido la ganancia y solo entonces escalo.", None),
        ("¿Cómo montar un stack de martech para una empresa pequeña o mediana?",
         "Empieza por lo esencial: un CRM como fuente única de verdad, una herramienta de automatización de marketing, GA4 con eventos bien definidos y un gestor de etiquetas. Después integra los medios pagos y solo añade una herramienta nueva cuando exista un proceso que la necesite. Pocas herramientas bien integradas rinden más que un stack grande y desconectado.", None),
        ("¿Qué hace un Head de Marketing & Martech?",
         "Es quien define la estrategia de marketing y la arquitectura tecnológica que la sostiene, al mismo tiempo: medios, datos, automatización y analítica. Yo lidero este frente desde hace 17 años, conectando la inversión en medios con el resultado del negocio.", None),
        ("¿Cómo puedo trabajar contigo?",
         "Escríbeme por WhatsApp, por correo a rodolfovasco@gmail.com o por LinkedIn. Atiendo a empresas pequeñas, medianas y grandes en proyectos de martech, performance, analítica, IA y SEO, AEO y GEO.",
         'Escríbeme por <a href="{WA}" rel="noopener">WhatsApp</a>, por correo a <a href="mailto:rodolfovasco@gmail.com">rodolfovasco@gmail.com</a> o por <a href="https://www.linkedin.com/in/rodolfovasco/" rel="me noopener">LinkedIn</a>. Atiendo a empresas pequeñas, medianas y grandes en proyectos de martech, performance, analítica, IA y SEO, AEO y GEO.'),
    ],
    contact_h2="Hablemos.",
    lbl_whatsapp="WhatsApp", lbl_email="Correo", lbl_linkedin="LinkedIn",
    foot_priv="Política de privacidad", foot_cookies="Preferencias de cookies", foot_tag="Marketing, datos y tecnología",
    consent_aria="Aviso de cookies",
    consent_text='Uso cookies para medir la audiencia y mejorar el sitio. Tú eliges si aceptas, y puedes cambiar de opinión en cualquier momento en "Preferencias de cookies", en el pie de página.',
    consent_accept="Aceptar", consent_decline="Rechazar",
    job_title="Head de Marketing & Martech",
    person_desc="Head de Marketing & Martech con 17 años de experiencia en la intersección entre marketing y tecnología, atendiendo a marcas de pequeñas a grandes.",
    knows=["Inteligencia artificial", "IA aplicada al marketing", "Marketing digital", "Martech", "Marketing de performance", "Analítica web", "GA4",
           "SEO", "AEO", "GEO", "Automatización de growth", "Business Intelligence"],
    llms_summary="IA & Martech: Head de Marketing con 17 años de experiencia en la intersección entre marketing y tecnología. Ha atendido a más de 50 marcas, de pequeñas a grandes, y suma más de 40 certificaciones profesionales oficiales.",
    llms_contact="Contacto", llms_edu="Formación", llms_certs="Certificaciones", llms_priv="Privacidad", llms_priv_label="Política de privacidad",
    llms_craft="Especialidades", llms_cases="Casos",
    priv_title="Política de privacidad | Rodolfo Vasco",
    priv_desc="Cómo el sitio de Rodolfo Vasco trata los datos personales y las cookies, tus derechos según la LGPD de Brasil y cómo contactarme sobre privacidad.",
    priv_back="Volver al sitio", priv_back_aria="Rodolfo Vasco, volver al inicio",
    priv_main="""  <h1>Política de privacidad</h1>
  <p class="date">Actualizada el 2 de noviembre de 2026</p>
  <p class="lead">Este es un sitio personal y recopila lo mínimo necesario. Aquí explico, de forma directa, qué datos se tratan, por qué y cómo puedes controlarlos, conforme a la Ley General de Protección de Datos de Brasil (LGPD, Ley n.º 13.709/2018).</p>

  <h2>1. Quién es el responsable</h2>
  <p>El responsable del tratamiento de los datos es Rodolfo Vasco, titular del sitio rodolfovasco.com.br. Para cualquier asunto de privacidad, escribe a <a class="ul" href="mailto:rodolfovasco@gmail.com">rodolfovasco@gmail.com</a>.</p>

  <h2>2. Qué datos se tratan y para qué</h2>
  <ul>
    <li><strong>Datos de navegación, solo con tu aceptación.</strong> Si aceptas las cookies, Google Tag Manager puede activar herramientas de medición, como Google Analytics. Estas registran información como páginas visitadas, clics en los botones de contacto, tipo de dispositivo y navegador, ubicación aproximada y dirección IP (tratada por el proveedor). Lo uso para entender cómo se usa el sitio y mejorarlo.</li>
    <li><strong>Datos que me envías.</strong> El sitio no tiene formulario. Si me escribes por WhatsApp, correo o LinkedIn, trato tu nombre, tu contacto y el contenido del mensaje únicamente para responder y llevar adelante la conversación.</li>
    <li><strong>Datos técnicos de acceso.</strong> Los servidores que entregan el sitio (alojado en GitHub Pages) y el servicio de fuentes tipográficas (Google Fonts) reciben tu dirección IP y datos del navegador para que la página cargue. Esto es inherente al funcionamiento de internet.</li>
  </ul>
  <p>Si en el futuro uso herramientas de publicidad o remarketing, también funcionarán solo con tu aceptación, y esta política se actualizará antes de eso.</p>

  <h2>3. Cookies y tu elección</h2>
  <p>En la primera visita, el sitio muestra un aviso de cookies. Sin tu aceptación, las herramientas de medición y de publicidad permanecen desactivadas (Consent Mode v2 de Google).</p>
  <ul>
    <li><strong>Esencial:</strong> <code>rv_consent</code>, guardado en el almacenamiento local de tu navegador, registra si aceptaste o rechazaste. Permanece hasta que borres los datos del sitio. Lo mismo vale para <code>rv_lang</code>, que guarda el idioma que elegiste.</li>
    <li><strong>Medición (solo con aceptación):</strong> cookies de Google Analytics, como <code>_ga</code>, cuando esa herramienta esté activa en Tag Manager. Google define el plazo, en general de hasta 2 años.</li>
  </ul>
  <p>Puedes cambiar de opinión cuando quieras, o borrar los datos del sitio en tu navegador.</p>
  <a class="btn" href="{HOME}#cookies">Cambiar mi elección de cookies</a>

  <h2>4. Con quién se pueden compartir los datos</h2>
  <p>Con Google (Tag Manager, Analytics y Fonts), con GitHub (alojamiento del sitio) y con las plataformas de mensajería que elijas para hablar conmigo. No vendo datos personales. Algunos de estos proveedores están fuera de Brasil, como en Estados Unidos, y la transferencia sigue la LGPD, con las garantías que ellos ofrecen.</p>

  <h2>5. Por cuánto tiempo se guardan los datos</h2>
  <p>Los datos de medición se conservan durante el período definido en la propia herramienta y pueden borrarse a tu solicitud cuando sea posible identificarte. Los mensajes de contacto se conservan el tiempo necesario para la conversación y para cumplir obligaciones legales.</p>

  <h2>6. Tus derechos</h2>
  <p>Según la LGPD, puedes solicitar:</p>
  <ul>
    <li>confirmación de que tus datos son tratados y acceso a ellos;</li>
    <li>corrección de datos incompletos, inexactos o desactualizados;</li>
    <li>anonimización, bloqueo o eliminación de datos innecesarios o tratados en desacuerdo con la ley;</li>
    <li>portabilidad de los datos;</li>
    <li>información sobre con quién se compartieron los datos;</li>
    <li>revocación del consentimiento, en cualquier momento.</li>
  </ul>
  <p>Para ejercer cualquiera de estos derechos, escribe a <a class="ul" href="mailto:rodolfovasco@gmail.com">rodolfovasco@gmail.com</a>. Respondo en hasta 15 días. También puedes presentar una reclamación ante la Autoridad Nacional de Protección de Datos de Brasil (ANPD), en <a class="ul" href="https://www.gov.br/anpd" rel="noopener">gov.br/anpd</a>. Si te encuentras fuera de Brasil, puedes escribir a la misma dirección y atenderé tu solicitud conforme a la ley aplicable.</p>

  <h2>7. Actualizaciones</h2>
  <p>Puedo actualizar esta política cuando el sitio cambie. La fecha de la última revisión está siempre en la parte superior de la página.</p>""",
)

# ---------------------------------------------------------------- ARTIGOS (textos de interface)
MONTHS = {
    "pt": ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"],
    "en": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    "es": ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
}

def fmt_date(lang, iso):
    y, m, d = (int(x) for x in iso.split("-"))
    if lang == "en":
        return "%s %d, %d" % (MONTHS["en"][m - 1], d, y)
    return "%d de %s de %d" % (d, MONTHS[lang][m - 1], y)

L["pt"].update(
    art_nav="Artigos", art_path="/artigos/", art_feed="/artigos/feed.xml", art_slug_dir="artigos",
    art_list_title="Artigos sobre IA, martech e marketing digital | Rodolfo Vasco",
    art_list_desc="Artigos de Rodolfo Vasco sobre inteligência artificial, martech, performance, analytics e SEO, AEO e GEO, com a experiência de 17 anos de mercado.",
    art_h1="Artigos",
    art_lead="Ideias, métodos e exemplos sobre IA, martech, performance, analytics e busca, escritos por quem trabalha com isso há 17 anos.",
    art_all="Todos", art_back_list="Todos os artigos", art_back_site="Voltar ao site", art_crumb_home="Início",
    label_summary="Resumo", label_toc="Neste artigo", min_read="min de leitura", label_updated="Atualizado em", label_published="Publicado em",
    author_label="Escrito por",
    author_bio="Há 17 anos conecto mídia, tecnologia e dados. Escrevo aqui sobre IA, martech e marketing digital, com base no que funciona na prática.",
    cta_h="Quer aplicar isso no seu negócio?", cta_p="Fale comigo e conte o seu cenário.",
    label_related="Continue lendo", feed_title="Rodolfo Vasco: artigos",
    home_art_h="Ideias sobre IA, martech e marketing digital.", home_art_all="Ver todos os artigos", rail_art="Artigos",
    read_progress="Progresso de leitura",
    cats=dict(ia="IA", martech="Martech", performance="Performance", analytics="Analytics", seo="SEO, AEO e GEO"),
)
L["en"].update(
    art_nav="Articles", art_path="/en/articles/", art_feed="/en/articles/feed.xml", art_slug_dir="en/articles",
    art_list_title="Articles on AI, martech and digital marketing | Rodolfo Vasco",
    art_list_desc="Articles by Rodolfo Vasco on artificial intelligence, martech, performance, analytics and SEO, AEO and GEO, drawing on 17 years in the market.",
    art_h1="Articles",
    art_lead="Ideas, methods and examples on AI, martech, performance, analytics and search, written by someone who has worked in this field for 17 years.",
    art_all="All", art_back_list="All articles", art_back_site="Back to the site", art_crumb_home="Home",
    label_summary="In short", label_toc="In this article", min_read="min read", label_updated="Updated on", label_published="Published on",
    author_label="Written by",
    author_bio="For 17 years I have connected media, technology and data. Here I write about AI, martech and digital marketing, based on what works in practice.",
    cta_h="Want to apply this to your business?", cta_p="Talk to me and tell me about your situation.",
    label_related="Keep reading", feed_title="Rodolfo Vasco: articles",
    home_art_h="Ideas on AI, martech and digital marketing.", home_art_all="See all articles", rail_art="Articles",
    read_progress="Reading progress",
    cats=dict(ia="AI", martech="Martech", performance="Performance", analytics="Analytics", seo="SEO, AEO and GEO"),
)
L["es"].update(
    art_nav="Artículos", art_path="/es/articulos/", art_feed="/es/articulos/feed.xml", art_slug_dir="es/articulos",
    art_list_title="Artículos sobre IA, martech y marketing digital | Rodolfo Vasco",
    art_list_desc="Artículos de Rodolfo Vasco sobre inteligencia artificial, martech, performance, analítica y SEO, AEO y GEO, con la experiencia de 17 años de mercado.",
    art_h1="Artículos",
    art_lead="Ideas, métodos y ejemplos sobre IA, martech, performance, analítica y búsqueda, escritos por alguien que trabaja en esto hace 17 años.",
    art_all="Todos", art_back_list="Todos los artículos", art_back_site="Volver al sitio", art_crumb_home="Inicio",
    label_summary="En resumen", label_toc="En este artículo", min_read="min de lectura", label_updated="Actualizado el", label_published="Publicado el",
    author_label="Escrito por",
    author_bio="Desde hace 17 años conecto medios, tecnología y datos. Aquí escribo sobre IA, martech y marketing digital, a partir de lo que funciona en la práctica.",
    cta_h="¿Quieres aplicar esto en tu negocio?", cta_p="Habla conmigo y cuéntame tu situación.",
    label_related="Sigue leyendo", feed_title="Rodolfo Vasco: artículos",
    home_art_h="Ideas sobre IA, martech y marketing digital.", home_art_all="Ver todos los artículos", rail_art="Artículos",
    read_progress="Progreso de lectura",
    cats=dict(ia="IA", martech="Martech", performance="Performance", analytics="Analítica", seo="SEO, AEO y GEO"),
)
for _c in ORDER:
    L[_c]["nav"] = L[_c]["nav"] + [L[_c]["art_nav"]]
