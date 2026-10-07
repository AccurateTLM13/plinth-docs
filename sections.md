---
layout: default
title: Sections and blocks
permalink: /sections/
lede: Sections are the building blocks of each page. Blocks are the smaller pieces inside a section, like a single feature or question.
description: Every Plinth section, what it does, its key settings, its blocks and tips.
---
{%- assign sections = site.data.sections -%}
In the theme editor, choose **Add section** to add a section, drag sections to reorder them, and use the eye icon to hide one without losing its content. Most content sections hide themselves on your store when they're empty.

<nav aria-label="Section categories">
<ul class="toc">
{%- for cat in site.data.section_categories %}
  <li><a href="#{{ cat.id }}">{{ cat.name }}</a></li>
{%- endfor %}
</ul>
</nav>

{% for cat in site.data.section_categories %}
<h2 id="{{ cat.id }}">{{ cat.name }}</h2>
<p>{{ cat.intro }}</p>
{%- for s in sections -%}
{%- assign note = site.data.section_notes[s.type] -%}
{%- if note.category == cat.id %}
<section class="section-ref" aria-labelledby="section-{{ s.type }}">
  <h3 id="section-{{ s.type }}">{{ s.name }}</h3>
  <p>{{ note.summary }}</p>
  <ul class="section-ref__facts" role="list">
    {%- if s.addable %}<li>Can be added with Add section</li>{% elsif cat.id == "pages" %}<li>Main section of its template</li>{% elsif cat.id == "system" %}<li>Built in</li>{% endif %}
    {%- for a in s.availability %}<li>{{ a }}</li>{% endfor %}
    {%- if s.used_in.size > 0 %}<li>Included by default in: {{ s.used_in | join: ", " }}</li>{% endif %}
    {%- if s.max_blocks %}<li>Up to {{ s.max_blocks }} blocks</li>{% endif %}
  </ul>
  {%- if s.settings.size > 0 %}
  <h4>Settings</h4>
  {% include settings-list.html settings=s.settings subhead=5 %}
  {%- endif %}
  {%- if s.blocks.size > 0 %}
  <h4>Blocks</h4>
  {%- for b in s.blocks %}
  <div class="block-ref">
    <h5>{{ b.name }}{% if b.limit == 1 %} <span class="badge">One per section</span>{% endif %}</h5>
    {%- if b.type == "@app" %}
    <p>Add blocks from installed apps that support theme app extensions.</p>
    {%- elsif b.settings.size > 0 %}
    {% include settings-list.html settings=b.settings subhead=6 %}
    {%- else %}
    <p>No settings. Drag it to change where it appears.</p>
    {%- endif %}
  </div>
  {%- endfor %}
  {%- endif %}
  {%- if note.tips %}
  <h4>Tips</h4>
  <ul>
    {%- for tip in note.tips %}<li>{{ tip | markdownify | remove: "<p>" | remove: "</p>" | strip }}</li>{% endfor %}
  </ul>
  {%- endif %}
</section>
{%- endif -%}
{%- endfor %}
{% endfor %}
