# Web Extracter

A small Python CLI that **fetches a page** and **lists unique `href` values** from `<a>` tags. Optionally prints the **parsed HTML** (same view Beautiful Soup builds from the response).

---

## Setup

```bash
pip install -r requirements.txt
```

---

## Usage

```bash
python web_extracter.py https://example.com
```

Print parsed HTML first (verbose), then links:

```bash
python web_extracter.py https://example.com --html
```

---

## What it does

| Step | Detail |
|------|--------|
| Fetch | `GET` the URL with a timeout |
| Parse | HTML via Beautiful Soup + `lxml` |
| Output | One unique `href` per line (skips empty duplicates) |

Errors (network, HTTP errors) are printed to stderr and exit with code `1`.

---

## Requirements

- Python 3
- Dependencies: `requests`, `beautifulsoup4`, `lxml`

---

## License

Use and modify freely.
