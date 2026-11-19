# -*- coding: utf-8 -*-
"""python3 build.py <pasta-de-saída> [localfonts]
Gera pt (/), en (/en/), es (/es/), as políticas de privacidade, os artigos (lista + páginas), feeds RSS,
sitemap.xml, llms.txt e a lista de imagens sociais (og-jobs.json, renderizada por og.js)."""
import json, sys, html, pathlib, re, math, datetime
import markdown
from markdown.extensions.toc import slugify_unicode
from i18n import L, ORDER, LABEL, NATIVE, fmt_date

HERE = pathlib.Path(__file__).parent
SITE = "https://rodolfovasco.com.br"
OUT = pathlib.Path(sys.argv[1])
LOCAL = len(sys.argv) > 2 and sys.argv[2] == "localfonts"
local_fonts = (HERE / "localfonts.css").read_text() if LOCAL else ""
PLATES = [("dark", "abyss"), ("light", "stone"), ("dark", "teal"), ("light", "platinum"), ("dark", "abyss"), ("dark", "teal")]
OG_JOBS = []


def esc(t):
    return html.escape(t, quote=False)


def attr(t):
    return html.escape(t, quote=True)


def wa(l):
    return "https://wa.me/5516981739770?text=" + l["wa_text"]


# ------------------------------------------------------------------ artigos
def parse_front(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError("artigo sem front matter")
    fm = {}
    for line in m.group(1).splitlines():
        if not line.strip() or ":" not in line:
            continue
        k, v = line.split(":", 1)
        v = v.strip()
        if len(v) > 1 and v[0] == v[-1] and v[0] in "\"'":
            v = v[1:-1]
        fm[k.strip()] = v
    return fm, m.group(2).strip()


def parse_faq(block):
    items, q, a = [], None, []
    for line in block.splitlines():
        if line.startswith("Q:"):
            if q is not None:
                items.append((q, " ".join(a).strip()))
            q, a = line[2:].strip(), []
        elif line.startswith("A:"):
            a = [line[2:].strip()]
        elif line.strip():
            a.append(line.strip())
    if q is not None:
        items.append((q, " ".join(a).strip()))
    return items


def load_articles():
    arts = {}
    root = HERE / "articles"
    if not root.exists():
        return arts
    for d in sorted(p for p in root.iterdir() if p.is_dir()):
        for c in ORDER:
            f = d / (c + ".md")
            if not f.exists():
                continue
            fm, body = parse_front(f.read_text())
            if fm.get("draft", "").lower() == "true":
                continue
            faq = []
            def grab(m):
                faq.extend(parse_faq(m.group(1)))
                return "\n\n@@FAQ@@\n\n"
            body = re.sub(r":::faq\n(.*?)\n:::", grab, body, flags=re.S)
            md = markdown.Markdown(extensions=["tables", "toc"], extension_configs={"toc": {"slugify": slugify_unicode, "toc_depth": "2"}})
            h = md.convert(body)
            toc = [(t["id"], t["name"]) for t in md.toc_tokens]
            h = h.replace("<table>", '<div class="tbl"><table>').replace("</table>", "</table></div>")
            words = len(re.findall(r"\w+", re.sub(r"[#>*|`\-]", " ", body)))
            arts.setdefault(d.name, {})[c] = dict(
                id=d.name, lang=c, fm=fm, html=h, toc=toc, faq=faq, words=words,
                minutes=max(1, math.ceil(words / 200)),
                url=L[c]["art_path"] + fm["slug"] + "/")
    return arts


ARTS = load_articles()


def lang_articles(c):
    out = [v[c] for v in ARTS.values() if c in v]
    return sorted(out, key=lambda a: a["fm"]["date"], reverse=True)


# ------------------------------------------------------------------ peças comuns
def alternates(urls):
    tags = ['<link rel="alternate" hreflang="%s" href="%s%s">' % (L[c]["hreflang"], SITE, u) for c, u in urls.items()]
    first = urls.get("pt") or next(iter(urls.values()))
    tags.append('<link rel="alternate" hreflang="x-default" href="%s%s">' % (SITE, first))
    return "\n".join(tags)


def lang_switch(cur, urls):
    out = []
    for c in ORDER:
        if c not in urls:
            continue
        l = L[c]
        out.append('<a href="%s" hreflang="%s" lang="%s" data-lang="%s" title="%s"%s>%s</a>'
                   % (urls[c], l["hreflang"], l["hreflang"], c, NATIVE[c], ' aria-current="true"' if c == cur else "", LABEL[c]))
    return "".join(out)


def og_alt(cur, urls):
    return "\n".join('<meta property="og:locale:alternate" content="%s">' % L[o]["og_locale"] for o in urls if o != cur)


def person_node(l):
    return {"@type": "Person", "@id": SITE + "/#rodolfo", "name": "Rodolfo Vasco", "url": SITE + "/",
            "jobTitle": l["job_title"], "description": l["person_desc"],
            "sameAs": ["https://www.linkedin.com/in/rodolfovasco/"], "email": "mailto:rodolfovasco@gmail.com"}


def render(tpl, tokens):
    def sub(m):
        k = m.group(1)
        if k not in tokens:
            raise KeyError("token sem valor: " + k)
        return tokens[k]
    return re.sub(r"\{\{(\w+)\}\}", sub, tpl)


def write(rel, text):
    p = OUT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)
    print("built", rel, len(text))


def og_for(kind, c, title="", cat=""):
    if kind == "default":
        rel = "og/default-%s.png" % c
        OG_JOBS.append(dict(out=rel, kind="default", lang=c, title="", cat=""))
    else:
        rel = "og/%s-%s.png" % (kind, c)
        OG_JOBS.append(dict(out=rel, kind="article", lang=c, title=title, cat=cat))
    return SITE + "/" + rel


# ------------------------------------------------------------------ home
def faq_html(l):
    out = []
    for i, (q, a_txt, a_html) in enumerate(l["faq"]):
        body = a_html.replace("{WA}", wa(l)) if a_html else esc(a_txt)
        out.append('      <details%s><summary>%s</summary><div class="ans"><p>%s</p></div></details>' % (" open" if i == 0 else "", esc(q), body))
    return "\n".join(out)


def jsonld(l):
    url = SITE + l["path"]
    person = person_node(l)
    person.update(alumniOf=[
        {"@type": "CollegeOrUniversity", "name": "Universidade Presbiteriana Mackenzie"},
        {"@type": "CollegeOrUniversity", "name": "FGV - Fundação Getulio Vargas"},
        {"@type": "CollegeOrUniversity", "name": "ESPM - Escola Superior de Propaganda e Marketing"},
        {"@type": "CollegeOrUniversity", "name": "Universidade do Vale do Silício"}],
        hasCredential=[{"@type": "EducationalOccupationalCredential", "name": n} for n in l["certs"]],
        knowsAbout=l["knows"], knowsLanguage=["pt-BR", "en", "es"])
    graph = [
        person,
        {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "Rodolfo Vasco",
         "inLanguage": [L[x]["hreflang"] for x in ORDER], "publisher": {"@id": SITE + "/#rodolfo"}},
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": l["title"],
         "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": SITE + "/#rodolfo"}, "inLanguage": l["hreflang"]},
        {"@type": "FAQPage", "@id": url + "#faq", "inLanguage": l["hreflang"],
         "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a, _ in l["faq"]]},
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)


def sections(l):
    facts = "\n".join('        <div class="fact"><strong>%s</strong><span>%s</span></div>' % (n, esc(t)) for n, t in l["facts"])
    craft = "\n".join('        <li class="craft-row"><h3>%s</h3><p>%s</p></li>' % (esc(h), esc(p)) for h, p in l["craft"])
    plates = []
    for (label, name, ch, ac), (th, bg) in zip(l["cases"], PLATES):
        plates.append('''  <article class="plate theme-%s bg-%s">
    <div class="plate-top"><span>%s</span></div>
    <h3 class="plate-name">%s</h3>
    <div class="plate-cols">
      <div><h3>%s</h3><p>%s</p></div>
      <div><h3>%s</h3><p>%s</p></div>
    </div>
  </article>
''' % (th, bg, esc(label), esc(name), esc(l["h_challenge"]), esc(ch), esc(l["h_action"]), esc(ac)))
    edu = []
    for i, (inst, deg) in enumerate(l["edu"]):
        last = ' style="border-bottom:1px solid var(--line)"' if i == len(l["edu"]) - 1 else ""
        edu.append('        <div class="edu-row"%s><h3>%s</h3><p>%s</p></div>' % (last, esc(inst), deg))
    certs = "\n".join("        <li>%s</li>" % esc(c) for c in l["certs"])
    return dict(FACTS_HTML=facts, CRAFT_HTML=craft, CASES_HTML="\n".join(plates), EDU_HTML="\n".join(edu), CERT_HTML=certs)


def home_articles(l):
    arts = lang_articles(l["code"])[:3]
    if not arts:
        return "", ""
    rows = "\n".join('      <a class="art-row" href="%s"><span class="art-meta">%s<br>%s</span><div><h3>%s</h3><p>%s</p></div></a>'
                     % (a["url"], fmt_date(l["code"], a["fm"]["date"]), esc(l["cats"][a["fm"]["category"]]), esc(a["fm"]["title"]), esc(a["fm"]["description"])) for a in arts)
    sec = '''<section class="sec theme-light bg-stone" id="artigos" data-chapter="VII">
  <div class="layout">
    <div class="rail"><b>VII</b>%s</div>
    <div>
      <h2 class="craft-intro">%s</h2>
      <div class="art-list">
%s
      </div>
      <a class="art-more" href="%s">%s</a>
    </div>
  </div>
</section>
''' % (esc(l["rail_art"]), esc(l["home_art_h"]), rows, l["art_path"], esc(l["home_art_all"]))
    return sec, '<a href="#artigos">%s</a>' % esc(l["art_nav"])


# ------------------------------------------------------------------ páginas de artigo e lista
page_tpl = (HERE / "article.template.html").read_text()


def page_tokens(c, urls, **kw):
    l = L[c]
    t = {k: v for k, v in l.items() if isinstance(v, str)}
    t.update(LOCALFONTS=local_fonts, LANG_SWITCH=lang_switch(c, urls), ALTERNATES=alternates(urls), OG_ALT_LOCALES=og_alt(c, urls),
             home=l["path"], back_href=l["art_path"], back_label=l["art_back_list"], feed_url=SITE + l["art_feed"],
             article_id="", article_slug="", EXTRA_META="", og_type="website", theme="dark", theme_color="#04130F")
    t.update(kw)
    return t


def list_page(c):
    l = L[c]
    arts = lang_articles(c)
    urls = {x: L[x]["art_path"] for x in ORDER if lang_articles(x)}
    cats = []
    for a in arts:
        if a["fm"]["category"] not in cats:
            cats.append(a["fm"]["category"])
    filt = ""
    if len(arts) >= 4 and len(cats) > 1:
        filt = '<div class="filters" role="group"><button type="button" data-cat="all" aria-pressed="true">%s</button>%s</div>' % (
            esc(l["art_all"]), "".join('<button type="button" data-cat="%s" aria-pressed="false">%s</button>' % (k, esc(l["cats"][k])) for k in cats))
    items = "\n".join('  <a class="item" href="%s" data-cat="%s"><span class="meta">%s<br>%s · %d %s</span><div><h2>%s</h2><p>%s</p></div></a>'
                      % (a["url"], a["fm"]["category"], esc(l["cats"][a["fm"]["category"]]), fmt_date(c, a["fm"]["date"]), a["minutes"], l["min_read"], esc(a["fm"]["title"]), esc(a["fm"]["description"])) for a in arts)
    body = '<section class="list-head"><h1>%s</h1><p>%s</p></section>\n%s\n<div class="items">\n%s\n</div>' % (esc(l["art_h1"]), esc(l["art_lead"]), filt, items)
    url = SITE + l["art_path"]
    graph = [person_node(l),
             {"@type": "Blog", "@id": url + "#blog", "url": url, "name": l["art_h1"], "description": l["art_list_desc"], "inLanguage": l["hreflang"],
              "author": {"@id": SITE + "/#rodolfo"}, "publisher": {"@id": SITE + "/#rodolfo"},
              "blogPost": [{"@type": "BlogPosting", "@id": SITE + a["url"] + "#article", "headline": a["fm"]["title"], "url": SITE + a["url"], "datePublished": a["fm"]["date"]} for a in arts]},
             {"@type": "BreadcrumbList", "itemListElement": [
                 {"@type": "ListItem", "position": 1, "name": l["art_crumb_home"], "item": SITE + l["path"]},
                 {"@type": "ListItem", "position": 2, "name": l["art_h1"], "item": url}]}]
    t = page_tokens(c, urls, page_title=l["art_list_title"], page_desc=l["art_list_desc"], canonical=url, og_image=og_for("default", c),
                    JSONLD=json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2),
                    BODY=body, back_href=l["path"], back_label=l["art_back_site"], priv_path=l["priv_path"])
    write(l["art_slug_dir"] + "/index.html", render(page_tpl, t))


def article_page(c, a):
    l = L[c]
    fm = a["fm"]
    urls = {x: ARTS[a["id"]][x]["url"] for x in ORDER if x in ARTS[a["id"]]}
    url = SITE + a["url"]
    cat = l["cats"][fm["category"]]
    img = og_for(a["id"], c, fm["title"], cat)
    prose = a["html"].replace('href="#contato"', 'href="%s#contato"' % l["path"])
    faq = ""
    if a["faq"]:
        faq = '<div class="faq">' + "".join('<details><summary>%s</summary><div class="ans"><p>%s</p></div></details>' % (esc(q), esc(ans)) for q, ans in a["faq"]) + "</div>"
    prose = prose.replace("<p>@@FAQ@@</p>", faq)
    toc = '<nav class="toc" aria-label="%s"><p class="label">%s</p><ol>%s</ol></nav>' % (attr(l["label_toc"]), esc(l["label_toc"]), "".join('<li><a href="#%s">%s</a></li>' % (i, esc(n)) for i, n in a["toc"]))
    updated = ""
    if fm.get("updated") and fm["updated"] != fm["date"]:
        updated = "<span>%s %s</span>" % (l["label_updated"], fmt_date(c, fm["updated"]))
    others = [x for x in lang_articles(c) if x["id"] != a["id"]][:2]
    related = ""
    if others:
        related = '<section class="related"><p class="label">%s</p>%s</section>' % (esc(l["label_related"]), "".join(
            '<a class="item" href="%s"><span class="meta">%s · %s</span><h3>%s</h3></a>' % (x["url"], esc(l["cats"][x["fm"]["category"]]), fmt_date(c, x["fm"]["date"]), esc(x["fm"]["title"])) for x in others))
    body = f'''<article class="post" itemscope itemtype="https://schema.org/BlogPosting">
  <p class="crumb"><a href="{l["path"]}">{esc(l["art_crumb_home"])}</a><span>/</span><a href="{l["art_path"]}">{esc(l["art_h1"])}</a></p>
  <h1 itemprop="headline">{esc(fm["title"])}</h1>
  <p class="post-meta"><span class="cat">{esc(cat)}</span><time datetime="{fm["date"]}">{fmt_date(c, fm["date"])}</time>{updated}<span>{a["minutes"]} {l["min_read"]}</span></p>
  <div class="summary"><p class="label">{esc(l["label_summary"])}</p><p>{esc(fm["summary"])}</p></div>
  {toc}
  <div class="prose" id="prose">
{prose}
  </div>
  <aside class="author" data-section="artigo-autor">
    <img src="/icon-192.png" width="72" height="72" alt="rv." style="border-radius:22%">
    <div><p class="label">{esc(l["author_label"])}</p><p class="nm">Rodolfo Vasco</p><p class="rl">{esc(l["job_title"])}</p>
    <p class="bio">{esc(l["author_bio"])}</p>
    <p class="links"><a href="https://www.linkedin.com/in/rodolfovasco/" rel="me noopener">LinkedIn</a></p></div>
  </aside>
  <section class="cta" data-section="artigo-cta"><div><h2>{esc(l["cta_h"])}</h2><p>{esc(l["cta_p"])}</p></div><a class="btn" href="{wa(l)}" rel="noopener">{esc(l["btn_talk"])}</a></section>
  {related}
</article>'''
    graph = [person_node(l),
             {"@type": "BlogPosting", "@id": url + "#article", "headline": fm["title"], "description": fm["description"], "url": url,
              "mainEntityOfPage": {"@type": "WebPage", "@id": url}, "inLanguage": l["hreflang"], "image": img,
              "datePublished": fm["date"], "dateModified": fm.get("updated", fm["date"]), "wordCount": a["words"], "articleSection": cat,
              "author": {"@id": SITE + "/#rodolfo"}, "publisher": {"@id": SITE + "/#rodolfo"},
              "isPartOf": {"@id": SITE + l["art_path"] + "#blog"}},
             {"@type": "BreadcrumbList", "itemListElement": [
                 {"@type": "ListItem", "position": 1, "name": l["art_crumb_home"], "item": SITE + l["path"]},
                 {"@type": "ListItem", "position": 2, "name": l["art_h1"], "item": SITE + l["art_path"]},
                 {"@type": "ListItem", "position": 3, "name": fm["title"], "item": url}]}]
    if a["faq"]:
        graph.append({"@type": "FAQPage", "@id": url + "#faq", "inLanguage": l["hreflang"],
                      "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans in a["faq"]]})
    extra = '<meta property="article:published_time" content="%s">\n<meta property="article:modified_time" content="%s">\n<meta property="article:author" content="https://www.linkedin.com/in/rodolfovasco/">\n<meta property="article:section" content="%s">' % (
        fm["date"], fm.get("updated", fm["date"]), attr(cat))
    t = page_tokens(c, urls, page_title=(fm["title"] + " | Rodolfo Vasco") if len(fm["title"]) <= 44 else fm["title"], page_desc=fm["description"], canonical=url, og_image=img,
                    JSONLD=json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2), BODY=body,
                    theme="light", theme_color="#E6E4DE", og_type="article", EXTRA_META=extra, article_id=a["id"], article_slug=fm["slug"], priv_path=l["priv_path"])
    write(a["url"].strip("/") + "/index.html", render(page_tpl, t))


# ------------------------------------------------------------------ gera tudo
home_tpl = (HERE / "template.html").read_text()
priv_tpl = (HERE / "privacidade.template.html").read_text()

for c in ORDER:
    l = L[c]
    others = [x for x in ORDER if x != c]
    urls_home = {x: L[x]["path"] for x in ORDER}
    urls_priv = {x: L[x]["priv_path"] for x in ORDER}
    base = {k: v for k, v in l.items() if isinstance(v, str)}
    # menu: o item "Artigos" é o sexto da lista de navegação; só aparece se houver artigos
    for i, n in enumerate(l["nav"][:5]):
        base["nav%d" % i] = n
    sec, nav_art = home_articles(l)
    rss = '<link rel="alternate" type="application/rss+xml" title="%s" href="%s%s">' % (attr(l["feed_title"]), SITE, l["art_feed"]) if lang_articles(c) else ""
    base.update(LOCALFONTS=local_fonts, LANG_SWITCH=lang_switch(c, urls_home), ALTERNATES=alternates(urls_home),
                OG_ALT_LOCALES=og_alt(c, urls_home), canonical=SITE + l["path"], WA=wa(l), FAQ_HTML=faq_html(l),
                ARTICLES_SECTION=sec, NAV_ART=nav_art, contact_chapter="VIII" if sec else "VII", og_image=og_for("default", c), RSS_LINK=rss)
    base.update(sections(l))
    page = home_tpl.replace("{{JSONLD}}", jsonld(l))
    write(("" if c == "pt" else c + "/") + "index.html", render(page, base))

    pb = {k: v for k, v in l.items() if isinstance(v, str)}
    main = l["priv_main"].replace("{HOME}", l["path"])
    pb.update(LOCALFONTS=local_fonts, LANG_SWITCH=lang_switch(c, urls_priv), ALTERNATES=alternates(urls_priv),
              canonical=SITE + l["priv_path"], home=l["path"], PRIV_MAIN=main)
    write(l["priv_path"].strip("/") + "/index.html", render(priv_tpl.replace("{{PRIV_MAIN}}", main), pb))

    if lang_articles(c):
        list_page(c)
        for a in lang_articles(c):
            article_page(c, a)
        # RSS
        items = "\n".join("""    <item>
      <title>%s</title>
      <link>%s%s</link>
      <guid isPermaLink="true">%s%s</guid>
      <pubDate>%s</pubDate>
      <category>%s</category>
      <description>%s</description>
    </item>""" % (esc(a["fm"]["title"]), SITE, a["url"], SITE, a["url"],
                  datetime.datetime.strptime(a["fm"]["date"], "%Y-%m-%d").strftime("%a, %d %b %Y 09:00:00 -0300"),
                  esc(l["cats"][a["fm"]["category"]]), esc(a["fm"]["summary"])) for a in lang_articles(c))
        write(l["art_feed"].strip("/"), '<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n  <channel>\n    <title>%s</title>\n    <link>%s%s</link>\n    <atom:link href="%s%s" rel="self" type="application/rss+xml"/>\n    <description>%s</description>\n    <language>%s</language>\n%s\n  </channel>\n</rss>\n' % (
            esc(l["feed_title"]), SITE, l["art_path"], SITE, l["art_feed"], esc(l["art_list_desc"]), l["hreflang"], items))


write("404.html", (HERE / "404.html").read_text().replace("{{LOCALFONTS}}", local_fonts))

# ---- sitemap com hreflang
def url_block(urls, lastmod, freq, prio, first_lang):
    alts = "\n".join('    <xhtml:link rel="alternate" hreflang="%s" href="%s%s"/>' % (L[x]["hreflang"], SITE, u) for x, u in urls.items())
    alts += '\n    <xhtml:link rel="alternate" hreflang="x-default" href="%s%s"/>' % (SITE, urls.get("pt") or next(iter(urls.values())))
    return "  <url>\n    <loc>%s%s</loc>\n    <lastmod>%s</lastmod>\n    <changefreq>%s</changefreq>\n    <priority>%s</priority>\n%s\n  </url>" % (SITE, urls[first_lang], lastmod, freq, prio, alts)

today = max([a["fm"].get("updated", a["fm"]["date"]) for v in ARTS.values() for a in v.values()] + ["2026-11-02"])
blocks = []
home_urls = {x: L[x]["path"] for x in ORDER}
priv_urls = {x: L[x]["priv_path"] for x in ORDER}
for c in ORDER:
    blocks.append(url_block(home_urls, today, "monthly", "1.0" if c == "pt" else "0.9", c))
if ARTS:
    list_urls = {x: L[x]["art_path"] for x in ORDER if lang_articles(x)}
    for c in list_urls:
        blocks.append(url_block(list_urls, today, "weekly", "0.8", c))
    for aid, v in ARTS.items():
        urls = {x: v[x]["url"] for x in ORDER if x in v}
        for c in urls:
            blocks.append(url_block(urls, v[c]["fm"].get("updated", v[c]["fm"]["date"]), "monthly", "0.8", c))
for c in ORDER:
    blocks.append(url_block(priv_urls, "2026-11-02", "yearly", "0.3", c))
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(blocks) + "\n</urlset>\n")


# ---- llms.txt
def llms_section(l, top):
    h = "#" if top else "##"
    sub = "##" if top else "###"
    o = ["%s %s" % (h, "Rodolfo Vasco" if top else NATIVE[l["code"]]), "", "> " + l["llms_summary"], ""]
    arts = lang_articles(l["code"])
    if arts:
        o += ["%s %s" % (sub, l["art_h1"])] + ["- [%s](%s%s): %s" % (a["fm"]["title"], SITE, a["url"], a["fm"]["description"]) for a in arts] + [""]
    o += ["%s %s" % (sub, l["llms_craft"])] + ["- " + x for x, _ in l["craft"]] + [""]
    o += ["%s %s" % (sub, l["llms_cases"])] + ["- %s: %s" % (n, ch) for _, n, ch, _ in l["cases"]] + [""]
    o += ["%s %s" % (sub, l["llms_edu"])] + ["- %s: %s" % (i, d.replace("<br>", "; ")) for i, d in l["edu"]] + [""]
    o += ["%s %s" % (sub, l["llms_certs"]), ", ".join(l["certs"]), ""]
    o += ["%s %s" % (sub, l["llms_contact"]), "- Site: %s%s" % (SITE, l["path"]), "- LinkedIn: https://www.linkedin.com/in/rodolfovasco/", "- E-mail: rodolfovasco@gmail.com", ""]
    o += ["%s %s" % (sub, l["llms_priv"]), "- %s: %s%s" % (l["llms_priv_label"], SITE, l["priv_path"]), ""]
    return "\n".join(o)

write("llms.txt", llms_section(L["pt"], True) + "\n" + llms_section(L["en"], False) + "\n" + llms_section(L["es"], False))

# ---- lista de imagens sociais (renderizada por og.js)
(HERE / "og-jobs.json").write_text(json.dumps(OG_JOBS, ensure_ascii=False, indent=1))
print("og jobs:", len(OG_JOBS))
