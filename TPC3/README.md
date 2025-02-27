# TPC3
## 2025-02-26

**Nome** José Rafael de Oliveira Vilas Boas

**Número** A76350

**Foto** ![Foto](../foto.jpg)

## Introdução

Criação de um conversor de MarkDown para HTML, para alguns elementos sintáticos base, utilizando expressões regulares e implementado em python.

## Elementos sintáticos para conversão

* [**Cabeçalhos**](#cabeçalhos)

    `h1`, `h2` e `h3`, linhas iniciadas por `# texto`, `## texto` e `## texto`, respetivamente

* [**Bold**](#bold)

    `<b>texto</b>`, texto entre `**`, `**texto**`

* [**Itálico**](#itálico)

    `<i>texto</i>`, texto entre `*`, `*texto*`

* [**Lista numerada**](#lista-numerada)

    `<ol> <li>Primeiro item</li> </ol>`, linhas que contenham `1. texto`

* [**Link**](#link)

    `<a href="url">texto</a>`, texto no formato `[texto](url)` 

* [**Imagem**](#imagem)

    `<img src="url" alt="texto"/>`, texto no formato `![texto](url)`

### Resumo da conversão

|  |  **input**  |  |    **output**    |  |
|--|:------------|--|:-----------------|--|
|  | `# texto`   |  | `<h1>texto</h1>` |  |
|  | `## texto`  |  | `<h2>texto</h2>` |  |
|  | `### texto` |  | `<h3>texto</h3>` |  |
|  | `**texto**` |  | `<b>texto</b>` |  |
|  | `*texto*` |  | `<i>texto</i>` |  |
|  | `1. Primeiro item`<br>`2. Segundo item`<br>`3. Terceiro item` |  | `<ol>`<br>&nbsp;&nbsp;`<li>Primeiro item</li>`<br>&nbsp;&nbsp;`<li>Segundo item</li>`<br>&nbsp;&nbsp;`<li>Terceiro item</li>`<br>`</ol>` |  |
|  | `[texto](url)` |  | `<a href="url">texto</a>` |  |
|  | `![texto](caminho)` |  | `<img src="caminho" alt="texto"/>` |  |

## Utilização

Correr o programa no terminal com o nome do ficheiro markdown e o ficheiro de saída

``` bash
$ py conv_md_html.py exemplo.md exemplo_convertido.html
```

## Resultados

Foram criadas expressões regulares para encontrar cada um dos elementos sintáticos de markdown a substituir pela correspondente expressão em html

### **Cabeçalhos**

```python
md_header1 = r"^#[\s]+(.+)(?:\n)"
md_header2 = r"^##[\s]+(.+)(?:\n)"
md_header3 = r"^###[\s]+(.+)(?:\n)"

html_header1 = r"<h1>\1</h1>\n"
html_header2 = r"<h2>\1</h2>\n"
html_header3 = r"<h3>\1</h3>\n"

re.sub(md_header1, html_header1, texto)
re.sub(md_header2, html_header1, texto)
re.sub(md_header3, html_header1, texto)
```

### **Bold**

```python
md_bold = r"\*\*(.+?)\*\*"

html_bold = r"<b>\1</b>"

re.sub(md_bold, html_bold, texto)
```

### **Itálico**

```python
md_italic = r"\*(.+?)\*"

html_italic = r"<i>\1</i>"

re.sub(md_italic, html_italic, texto)
```

### **Lista numerada**

```python
md_ordered_list = r"^(\d+\. .*(?:\n\d+\. .*)*)"
md_list_item = r"^\d+\. ([^\n]+)"

html_ordered_list = r"<ol>\n\1\n</ol>"
html_list_item = r'<li>\1</li>'

re.sub(md_ordered_list, html_ordered_list, texto)
re.sub(md_list_item, html_list_item, texto)
```

### **Link**

```python
md_link = r"\[([\d\w]+)\]\((.+)\)"

html_link = r'<a href="\2">\1</a>'

re.sub(md_link, html_link, texto)
```

### **Imagem**

```python
md_image = r"\!\[([\d\w]+)\]\((.+)\)"

html_image = r'<img src="\2" alt="\1"/>'

re.sub(md_image, html_image, texto)
```
