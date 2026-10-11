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

GitHub Pages can't process form submissions, so the form posts to a form service, [FormBackend](https://www.formbackend.com). Until it's set up, the form is disabled and the page points people to GitHub issues (template: `.github/ISSUE_TEMPLATE/support.yml`).

The Theme Store requires the support form to accept file uploads and send an auto-responder. On FormBackend that needs the **Simple** plan ($5/month, or yearly billing with 2 months free) or higher. The free plan has neither.

1. Sign up at https://www.formbackend.com, choose the Simple plan, and create a form (for example "Plinth support"). Set it to send submission emails to the support inbox.
2. In the form's settings:
   - **Auto-response:** turn on the auto-response email to the submitter. FormBackend sends it to the field named `email`, which the form already uses. Suggested text: "Thanks for contacting Plinth support. We've received your request and will reply to this address. Please don't reply with passwords or customer data."
   - **Spam:** keep the honeypot field name `formbackend_nono` (the default), and add `https://accuratetlm13.github.io` under Whitelisted domains.
   - **Data retention:** set auto-delete to 90 days. The support page tells people submissions are deleted after 90 days, so change that text if you choose a different period.
   - **Email attachments:** optionally attach uploaded files to the notification emails.
3. Copy the form's endpoint URL (`https://www.formbackend.com/f/<token>`) into `support_form.endpoint` in `_config.yml`.
4. Commit to `main`. GitHub Pages rebuilds in about a minute, and the form is live: the notice disappears and the fields are enabled.
5. Send a test message with a file attached, once with JavaScript on and once with it off, and confirm that the submission arrives with its file, the auto-response is delivered, and the no-JS submission lands on `/support/thanks/`.

The form sends `name`, `email`, `store_url`, `theme_version`, `topic`, `message` and up to 3 files as `attachments[]` (multipart/form-data). It also sends the hidden fields from `support_form.hidden_fields`: `theme` (`Plinth`) and `_redirect`, which is FormBackend's special field for the no-JS confirmation page. With JavaScript, the browser checks the fields and the files (count, type, and `max_file_mb` per file) and submits in the background (`fetch` with `FormData` and `Accept: application/json`). Without JavaScript the form posts normally, and FormBackend redirects to `/support/thanks/`. Browsers can't check file sizes without JavaScript, so the service's own limits apply there.

## Screenshots

Screenshots in `assets/img/` come from the Plinth demo store. Its product images are AI-generated illustrations, not photographs.

© 2026 JP Pannell. All rights reserved.
