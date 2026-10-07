#!/usr/bin/env python3
"""Generate the settings and sections reference data for the Plinth docs.

Reads the theme's schema (config/settings_schema.json, sections/*.liquid
{% schema %} blocks, templates/*.json and section group JSON) and the English
schema locale, and writes merchant-facing labels only (no theme code) to:

  _data/theme_settings.json
  _data/sections.json

Usage:
  python3 tools/generate-reference.py /path/to/plinth-theme

The theme source itself stays in its private repository; only resolved labels,
defaults and help text are written here. Hand-written descriptions and tips
live in _data/section_notes.yml and _data/settings_notes.yml.
"""
import glob
import html
import json
import os
import re
import sys

if len(sys.argv) != 2:
    sys.exit(__doc__)
ROOT = os.path.abspath(sys.argv[1])
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_data")

with open(os.path.join(ROOT, "locales", "en.default.schema.json")) as fh:
    LOCALE = json.load(fh)


def t(value):
    """Resolve a t: translation key to its English text."""
    if isinstance(value, str) and value.startswith("t:"):
        node = LOCALE
        for part in value[2:].split("."):
            node = node.get(part) if isinstance(node, dict) else None
        if node is None:
            raise SystemExit(f"Missing translation for {value}")
        return node
    return value


TYPE_NAMES = {
    "checkbox": "Checkbox", "text": "Text", "textarea": "Multi-line text",
    "richtext": "Rich text", "range": "Slider", "select": "Dropdown",
    "color": "Color", "font_picker": "Font", "image_picker": "Image",
    "url": "Link", "product": "Product", "collection": "Collection",
    "link_list": "Menu", "liquid": "Liquid code", "number": "Number",
    "radio": "Choice", "video_url": "Video link", "html": "HTML",
    "page": "Page", "blog": "Blog", "article": "Article",
}


def font_name(handle):
    family, _, variant = handle.rpartition("_")
    weight = variant[1:] + "00" if variant[:1] in "ni" and variant[1:].isdigit() else ""
    name = " ".join(w.capitalize() for w in family.split("_"))
    return f"{name}, weight {weight}" if weight else name


def default_text(setting):
    d = setting.get("default")
    kind = setting["type"]
    if d is None or d == "":
        return ""
    if kind == "checkbox":
        return "On" if d else "Off"
    if kind == "font_picker":
        return font_name(d)
    if kind in ("select", "radio"):
        for opt in setting.get("options", []):
            if opt["value"] == d:
                return t(opt["label"])
    if kind == "range":
        return f"{d}{setting.get('unit', '')}"
    if kind == "link_list":
        return f"{d} menu"
    if kind == "richtext":
        return html.unescape(re.sub(r"<[^>]+>", "", t(d))).strip()
    return str(t(d))


def convert_settings(settings):
    out = []
    for s in settings:
        kind = s["type"]
        if kind in ("header", "paragraph"):
            out.append({"kind": kind, "text": t(s.get("content", ""))})
            continue
        item = {
            "kind": "setting",
            "id": s.get("id", ""),
            "type": TYPE_NAMES.get(kind, kind),
            "label": t(s.get("label", "")),
            "info": t(s.get("info", "")) or "",
            "default": default_text(s),
        }
        if kind == "color" and s.get("default"):
            item["swatch"] = s["default"]
        if kind in ("select", "radio"):
            item["options"] = [t(o["label"]) for o in s.get("options", [])]
        if kind == "range":
            unit = s.get("unit", "")
            item["range"] = f"{s['min']}–{s['max']}{unit}"
        out.append(item)
    return out


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


# Theme settings ------------------------------------------------------------
with open(os.path.join(ROOT, "config", "settings_schema.json")) as fh:
    schema = json.load(fh)
info = schema[0]
groups = []
for group in schema[1:]:
    name = t(group["name"])
    groups.append({"name": name, "slug": slug(name),
                   "settings": convert_settings(group.get("settings", []))})
theme_settings = {"theme_name": info.get("theme_name"),
                  "theme_version": info.get("theme_version"),
                  "groups": groups}

# Where each section is used ------------------------------------------------
TEMPLATE_NAMES = {"index": "Home page", "product": "Default product",
                  "product.flagship": "Product (flagship)", "collection": "Collection",
                  "list-collections": "Collections list", "search": "Search",
                  "cart": "Cart", "page": "Page", "page.contact": "Contact page",
                  "blog": "Blog", "article": "Blog post", "404": "404 page",
                  "password": "Password page"}
used_in = {}
for path in sorted(glob.glob(os.path.join(ROOT, "templates", "*.json"))):
    tpl = os.path.basename(path)[:-5]
    with open(path) as fh:
        raw = re.sub(r"^\s*/\*.*?\*/", "", fh.read(), flags=re.S)
    for sec in json.loads(raw).get("sections", {}).values():
        used_in.setdefault(sec["type"], []).append(TEMPLATE_NAMES.get(tpl, tpl))
for group_file, label in (("header-group.json", "Header group"), ("footer-group.json", "Footer group")):
    path = os.path.join(ROOT, "sections", group_file)
    if os.path.exists(path):
        with open(path) as fh:
            raw = re.sub(r"^\s*/\*.*?\*/", "", fh.read(), flags=re.S)
        for sec in json.loads(raw).get("sections", {}).values():
            used_in.setdefault(sec["type"], []).append(label)

# Sections -----------------------------------------------------------------
sections = []
for path in sorted(glob.glob(os.path.join(ROOT, "sections", "*.liquid"))):
    with open(path) as fh:
        src = fh.read()
    m = re.search(r"{%-?\s*schema\s*-?%}(.*?){%-?\s*endschema\s*-?%}", src, re.S)
    if not m:
        continue
    sch = json.loads(m.group(1))
    stype = os.path.basename(path)[:-7]
    blocks = []
    for b in sch.get("blocks", []):
        if b["type"] == "@app":
            blocks.append({"type": "@app", "name": "App blocks", "limit": None, "settings": []})
            continue
        blocks.append({"type": b["type"], "name": t(b.get("name", b["type"])),
                       "limit": b.get("limit"), "settings": convert_settings(b.get("settings", []))})
    where = []
    if sch.get("enabled_on", {}).get("groups"):
        where.append("Only in: " + ", ".join(g + " group" for g in sch["enabled_on"]["groups"]))
    if sch.get("enabled_on", {}).get("templates"):
        where.append("Only on: " + ", ".join(sch["enabled_on"]["templates"]) + " templates")
    if sch.get("disabled_on", {}).get("groups"):
        where.append("Not available in: " + ", ".join(g + " group" for g in sch["disabled_on"]["groups"]))
    sections.append({
        "type": stype,
        "name": t(sch.get("name", stype)),
        "addable": "presets" in sch,
        "max_blocks": sch.get("max_blocks"),
        "availability": where,
        "used_in": sorted(set(used_in.get(stype, []))),
        "settings": convert_settings(sch.get("settings", [])),
        "blocks": blocks,
    })

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "theme_settings.json"), "w") as fh:
    json.dump(theme_settings, fh, indent=2, ensure_ascii=False)
    fh.write("\n")
with open(os.path.join(OUT, "sections.json"), "w") as fh:
    json.dump(sections, fh, indent=2, ensure_ascii=False)
    fh.write("\n")

# Warn about sections or groups without hand-written notes.
notes_path = os.path.join(OUT, "section_notes.yml")
if os.path.exists(notes_path):
    with open(notes_path) as fh:
        noted = set(re.findall(r"^([a-z0-9-]+):\s*$", fh.read(), re.M))
    missing = [s["type"] for s in sections if s["type"] not in noted]
    if missing:
        print("WARNING: no notes in _data/section_notes.yml for:", ", ".join(missing))
print(f"Wrote {len(groups)} settings groups and {len(sections)} sections (theme {info.get('theme_version')}).")
