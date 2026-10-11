# Plinth docs

Documentation and support site for **Lemonteed Themes**, starting with **Plinth**.
Live at **https://accuratetlm13.github.io/plinth-docs/** today. Moving to **https://themes.lemonteed.com/plinth/** (see "Custom domain" below).

This repository holds documentation only. The theme's source code lives in a separate private repository and is never copied here.

## How it works

- Plain [Jekyll](https://jekyllrb.com/) (version 3, the one GitHub Pages runs), with one plugin GitHub Pages supports out of the box, `jekyll-redirect-from` (for the old-path redirects), and no theme gem. GitHub Pages builds and deploys the site from the `main` branch root on every push, so no Actions workflow is needed.
- Site layout: `/` is a small Lemonteed Themes landing page (`index.html`, `_layouts/landing.html`). Plinth's pages live in `plinth/` and are served under `/plinth/` (`plinth/getting-started.md` is `/plinth/getting-started/`, and so on). A future theme gets its own folder and `/<theme>/` path next to it. The sidebar order is in `_data/nav.yml`.
- Each Plinth page has `redirect_from: /<old-path>/`, so links to the old URLs keep working. After the custom domain is on, GitHub 301-redirects `accuratetlm13.github.io/plinth-docs/<path>` to `themes.lemonteed.com/<path>` (dropping the repo name), and the stub there forwards to `/plinth/<path>`.
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
gem install jekyll-redirect-from -v 0.16.0
jekyll serve   # http://127.0.0.1:4000/  (Plinth docs at /plinth/)
```

## Activating the support form

GitHub Pages can't process form submissions, so the form posts to our own Cloudflare Worker, kept in the private repo **AccurateTLM13/plinth-support-worker**. The Worker checks the form, emails it (with any files attached) to the support inbox, and sends the merchant an auto-reply, as the Theme Store requires. Until it's deployed, the form is disabled and the page points people to GitHub issues (template: `.github/ISSUE_TEMPLATE/support.yml`).

1. Deploy the Worker by following the README in plinth-support-worker. You'll end up with its URL, for example `https://plinth-support.<your-subdomain>.workers.dev`, and a Cloudflare Turnstile site key.
2. In `_config.yml`, set:
   - `support_form.endpoint` to the Worker URL plus `/submit`.
   - `support_form.turnstile_site_key` to the Turnstile site key. It's public, so committing it is fine. (The secret key only goes into the Worker.)
   - Keep `honeypot_field`, `max_files`, `max_file_mb` and `max_total_mb` the same as the Worker's `HONEYPOT_FIELD`, `MAX_FILES`, `MAX_FILE_MB` and `MAX_TOTAL_MB`.
3. Commit to `main`. GitHub Pages rebuilds in about a minute, and the form is live: the notice disappears, the fields are enabled, and the Turnstile check appears above the button.
4. Send a test message with a file attached, once with JavaScript on and once with it off. With JavaScript on, you should get the notification with the file attached plus the auto-reply, and the page shows a success message. With it off, you should get the notification marked `[unverified]`, no auto-reply, and land on `/plinth/support/received/`.

The form sends `name`, `email`, `store_url`, `theme_version`, `topic`, `message`, up to 3 files as `attachments[]` (multipart/form-data), the honeypot `website` (empty for people), the hidden field `theme` (`Plinth`), and the Turnstile token `cf-turnstile-response` when JavaScript is on.

- **With JavaScript:** the browser checks the fields and the files (count, type, size per file and in total), then submits in the background (`fetch` with `FormData` and `Accept: application/json`). The Worker answers with JSON, and its field errors are shown next to the right fields.
- **Without JavaScript:** Turnstile can't run, so the form posts normally. The Worker still delivers the message, marked unverified, but sends no auto-reply (so nobody can use the form to email strangers), then redirects to `/plinth/support/received/`, which explains that. Verified posts redirect to `/plinth/support/thanks/`. If the Worker rejects a no-JS post, it shows a plain error page with a link back.

## Custom domain (themes.lemonteed.com)

The `CNAME` file holds `themes.lemonteed.com`. Because Pages builds from `main`, **merging the `CNAME` file switches the site to the custom domain**: github.io starts redirecting there straight away. So do things in this order:

1. In GitHub account **Settings > Pages > Verified domains**, verify `lemonteed.com` (GitHub gives a TXT record to add in Cloudflare DNS). This stops anyone else claiming `themes.lemonteed.com` for their Pages site.
2. In Cloudflare DNS for lemonteed.com, add `themes` as **A** records (`185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`) and **AAAA** records (`2606:50c0:8000::153` through `2606:50c0:8003::153`), all **DNS only** (grey cloud). Use A/AAAA rather than a CNAME, because `themes` also needs MX and TXT records for `support@themes.lemonteed.com`, and a CNAME can't share its name with other records.
3. Merge to `main`. Then, in repo **Settings > Pages**, confirm the custom domain shows `themes.lemonteed.com` with a green DNS check, wait for the certificate, and tick **Enforce HTTPS**.
4. Check that `https://accuratetlm13.github.io/plinth-docs/faq/` ends up on `https://themes.lemonteed.com/plinth/faq/`.
5. Update the Worker's allowed origin and URLs, and the theme's `settings_schema.json` documentation and support URLs, to the new domain (see plinth-support-worker's README).

Support email: `support@themes.lemonteed.com` (`support_email` in `_config.yml`) is forwarded to our inbox by Cloudflare Email Routing. Resend sends the form's notification and auto-reply from the same address.

## Screenshots

Screenshots in `assets/img/` come from the Plinth demo store. Its product images are AI-generated illustrations, not photographs.

© 2026 JP Pannell. All rights reserved.
