# HTML Cheatsheet

## 1) Page Skeleton

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Page Title</title>
  </head>
  <body>
    <h1>Hello</h1>
  </body>
</html>
```

Reference structure:

![html_structure](../figs/html_strucutre.png)

## 2) Core Content Tags

- Headings: `<h1>` to `<h6>`
- Text: `<p>`, `<strong>`, `<em>`, `<br>`
- Containers: `<div>` (block), `<span>` (inline)
- Lists: `<ul>`, `<ol>`, `<li>`
- Code: `<code>`, `<pre>`

## 3) High-Value Attributes

- `id`: unique element identifier
- `class`: reusable styling/JS hook
- `href`: link target (`<a>`)
- `src`, `alt`, `width`, `height`: media (`<img>`, `<video>`, etc.)
- `style`: inline CSS (use sparingly)
- `title`: tooltip/extra info
- `lang`: page language on `<html>`

```html
<a href="https://example.com" title="Go to Example">Visit</a>
<img src="cat.jpg" alt="Orange cat sleeping" width="320" height="200" />
```

## 4) Links, Media, and Tables

```html
<a href="/about">About</a>
<a href="#faq">Jump to FAQ</a>

<img src="photo.png" alt="Team photo" />

<table>
  <tr><th>Name</th><th>Score</th></tr>
  <tr><td>Alice</td><td>95</td></tr>
</table>
```

## 5) Paragraphs

- `<p>` defines a paragraph; each paragraph starts on a new line and browsers add default margin around it.
- In normal HTML text, extra spaces and line breaks in source code are collapsed by the browser.
- Use `<br>` for a single line break without starting a new paragraph.
- Use `<hr>` for a thematic break between sections.
- Use `<pre>` when you need spaces and line breaks preserved.

```html
<p>This is a paragraph.</p>
<p>This is another paragraph.</p>
<p>This is<br>one paragraph<br>with line breaks.</p>
<hr />
<pre>
  Keeps spaces
  and line breaks
</pre>
```

## 6) Tables

- Use `<table>` for tabular data (rows + columns), not for page layout.
- Row: `<tr>`, header cell: `<th>`, data cell: `<td>`.
- Helpful structure tags: `<caption>`, `<thead>`, `<tbody>`, `<colgroup>`, `<col>`.

```html
<table>
  <caption>Student Scores</caption>
  <thead>
    <tr><th>Name</th><th>Score</th></tr>
  </thead>
  <tbody>
    <tr><td>Alice</td><td>95</td></tr>
    <tr><td>Bob</td><td>88</td></tr>
  </tbody>
</table>
```

## 7) Lists

- Unordered list: `<ul>` + `<li>` (bullets).
- Ordered list: `<ol>` + `<li>` (numbered sequence).
- Description list: `<dl>` + `<dt>` + `<dd>` (term + description).

```html
<ul>
  <li>Milk</li>
  <li>Bread</li>
</ul>

<ol>
  <li>Install</li>
  <li>Run</li>
</ol>

<dl>
  <dt>HTML</dt>
  <dd>Markup language for web pages.</dd>
</dl>
```

## 8) `div` vs Semantic Elements

- `<div>` is a generic block container; use it for grouping/styling when no semantic tag fits.
- Semantic elements (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`) describe meaning/role.
- Prefer semantic elements first for readability, accessibility, and maintainability.

```html
<!-- Less semantic -->
<div class="top"></div>
<div class="menu"></div>
<div class="content"></div>

<!-- Better semantic structure -->
<header></header>
<nav></nav>
<main>
  <section>
    <article></article>
  </section>
  <aside></aside>
</main>
<footer></footer>
```

## 9) Best Practices

- Always include `<!DOCTYPE html>`.
- Use lowercase for tags and attributes.
- Use double quotes for attribute values.
- Always provide meaningful `alt` text for images.
- Use heading levels in order (`h1` -> `h2` -> `h3`).
- Prefer external CSS over heavy inline `style`.
