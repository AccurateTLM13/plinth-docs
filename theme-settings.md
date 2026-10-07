---
layout: default
title: Theme settings
permalink: /theme-settings/
lede: Theme settings apply across your whole store. Open them in the theme editor by selecting the gear icon (Theme settings).
description: A reference for every Plinth theme settings group, with defaults, choices and tips.
---
{%- assign data = site.data.theme_settings -%}
This page lists every setting in Plinth {{ data.theme_version }}, in the same order as the theme editor.

<nav aria-label="Settings groups">
<ul class="toc">
{%- for group in data.groups %}
  <li><a href="#{{ group.slug }}">{{ group.name }}</a></li>
{%- endfor %}
</ul>
</nav>

<div class="settings-groups">
{% for group in data.groups %}
<h2 id="{{ group.slug }}">{{ group.name }}</h2>
{%- assign note = site.data.settings_notes[group.slug] -%}
{%- if note %}
<p>{{ note }}</p>
{%- endif %}
{% include settings-list.html settings=group.settings subhead=3 global=true %}
{% endfor %}
</div>

## Settings in sections

Many options live on individual sections instead, such as search and selectors in the Header, or filtering in Collection products. See [Sections and blocks]({{ '/sections/' | relative_url }}).
