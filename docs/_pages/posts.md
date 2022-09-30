---
title: Posts
layout: single
---

These are generally written in a less serious tone than the rest of the site.

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>