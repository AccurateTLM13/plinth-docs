# Plinth docs

Documentation and support site for **Plinth**, a Shopify theme.
Live at **https://accuratetlm13.github.io/plinth-docs/**.

This repository holds documentation only. The theme's source code lives in a separate private repository and is never copied here.

## How it works

- Plain [Jekyll](https://jekyllrb.com/) (version 3, the one GitHub Pages runs), with no plugins or theme gem. GitHub Pages builds and deploys the site from the `main` branch root on every push, so no Actions workflow is needed.
- Pages are Markdown or HTML at the repository root (`getting-started.md`, `support.html`, and so on). The sidebar order is in `_data/nav.yml`.
- Styles are in `assets/css/docs.css`. The only scripts are `assets/js/docs.js` (collapses the menu on mobile) and `assets/js/support.js` (support form).

### Reference pages are generated from the theme

`theme-settings.md` and `sections.md` render `_data/theme_settings.json` and `_data/sections.json`. Those files hold merchant-facing labels, defaults and help text only. They're generated from the theme's real schema:

```bash
python3 tools/generate-reference.py /path/to/plinth-theme
```

Run it after any schema change, and commit the updated JSON. Hand-written descriptions and tips are in `_data/section_notes.yml`, `_data/section_categories.yml`, `_data/settings_notes.yml` and `_data/setting_notes.yml`. The script warns if a section has no notes.

### Preview locally

```bash
gem install jekyll -v '~> 3.10' kramdown-parser-gfm webrick
jekyll serve   # http://127.0.0.1:4000/plinth-docs/
```

## Activating the support form

GitHub Pages can't process form submissions, so the form posts to a form service. Until one is set up, the form is disabled and the page points people to GitHub issues (template: `.github/ISSUE_TEMPLATE/support.yml`).

1. Create a free form at a service of your choice (for example Formspree, Basin or Web3Forms), set to deliver submissions to your support inbox. Allow `https://accuratetlm13.github.io` as a domain if the service asks.
2. In `_config.yml`, set `support_form.endpoint` to the form's POST URL, for example `https://formspree.io/f/abcd1234`.
3. Set `support_form.honeypot_field` to the spam-trap field name your service expects (Formspree uses `_gotcha`, Web3Forms uses `botcheck`; check your service's docs). If your service needs extra hidden fields, such as Web3Forms' `access_key`, add them under `support_form.hidden_fields`.
4. Commit to `main`. GitHub Pages rebuilds in about a minute, and the form is live: the notice disappears and the fields are enabled.
5. Send a test message, with JavaScript on and off, and confirm it arrives.

The form sends: `name`, `email`, `store_url`, `theme_version`, `topic` and `message`. With JavaScript it validates inline and submits in the background (`Accept: application/json`). Without JavaScript it posts normally, and the service shows its own confirmation page.

## Screenshots

Screenshots in `assets/img/` come from the Plinth demo store. Its product images are AI-generated illustrations, not photographs.

© 2026 JP Pannell. All rights reserved.
