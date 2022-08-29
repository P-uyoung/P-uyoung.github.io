---
title: "Project"
layout: archive
permalink: categories/Project
author_profile: true
sidebar_main: true
---
<!-- 카테고리명에 띄어쓰기가 들어가는 경우에는 site.categories.Unreal Engine 으로 할 수가 없어 site.categories[‘Unreal Engine’] 이런 식으로 해야했다는 것이다. -->

{% assign posts = site.categories.Project %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}