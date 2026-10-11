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

GitHub Pages can't process form submissions, so the form posts to our own Cloudflare Worker, kept in the private repo **AccurateTLM13/plinth-support-worker**. The Worker checks the form, emails it (with any files attached) to the support inbox, and sends the merchant an auto-reply, as the Theme Store requires. Until it's deployed, the form is disabled and the page points people to GitHub issues (template: `.github/ISSUE_TEMPLATE/support.yml`).

1. Deploy the Worker by following the README in plinth-support-worker. You'll end up with its URL, for example `https://plinth-support.<your-subdomain>.workers.dev`, and a Cloudflare Turnstile site key.
2. In `_config.yml`, set:
   - `support_form.endpoint` to the Worker URL plus `/submit`.
   - `support_form.turnstile_site_key` to the Turnstile site key. It's public, so committing it is fine. (The secret key only goes into the Worker.)
   - Keep `honeypot_field`, `max_files`, `max_file_mb` and `max_total_mb` the same as the Worker's `HONEYPOT_FIELD`, `MAX_FILES`, `MAX_FILE_MB` and `MAX_TOTAL_MB`.
3. Commit to `main`. GitHub Pages rebuilds in about a minute, and the form is live: the notice disappears, the fields are enabled, and the Turnstile check appears above the button.
4. Send a test message with a file attached, once with JavaScript on and once with it off. With JavaScript on, you should get the notification with the file attached plus the auto-reply, and the page shows a success message. With it off, you should get the notification marked `[unverified]`, no auto-reply, and land on `/support/received/`.

The form sends `name`, `email`, `store_url`, `theme_version`, `topic`, `message`, up to 3 files as `attachments[]` (multipart/form-data), the honeypot `website` (empty for people), the hidden field `theme` (`Plinth`), and the Turnstile token `cf-turnstile-response` when JavaScript is on.

- **With JavaScript:** the browser checks the fields and the files (count, type, size per file and in total), then submits in the background (`fetch` with `FormData` and `Accept: application/json`). The Worker answers with JSON, and its field errors are shown next to the right fields.
- **Without JavaScript:** Turnstile can't run, so the form posts normally. The Worker still delivers the message, marked unverified, but sends no auto-reply (so nobody can use the form to email strangers), then redirects to `/support/received/`, which explains that. Verified posts redirect to `/support/thanks/`. If the Worker rejects a no-JS post, it shows a plain error page with a link back.

## Screenshots

Screenshots in `assets/img/` come from the Plinth demo store. Its product images are AI-generated illustrations, not photographs.

© 2026 JP Pannell. All rights reserved.
