---
title: Curly Templating
toc: True
---

## What is Templating, When to Use Templating

Templating is a standardized way of presenting some sort of information so that code can understand it, process it, and transform it. In this case templating lets you embed some basic instructions or information in order to make automation easier. The .yamls and Python functions support a very basic sort of templating. You can use this templating to refer to other entities, roll dice, or roll dice in order to determine the number of some other entity. This can let you automate things like rolling for HP, loot, generating minions for a Boss-type-enemy, or generating an entire encounter.

## How to Use Templating

Mark things that should be handled by templating with {}. The dice go first, then the entity. Either can be left out. This can be done in any of the fields of an [entity .yaml](yaml_entity_creation.md).

```yaml
- name: Salt Wretch
  hp: "{1d10} or 4"
  scores: 1 STR
  skills: >-
    - Claw (2n1): 1d4 (S). Enemies take damage = to their current SALT on the
    beginning of their turn and lose one SALT when within 1 space of the Wretch.
  holds: "{1d4-3 pickaxe}, {1d4-2 curse_eye}."
  flavor_text: >-
    A bent creature, shriviled and distended. Rattling sandpaper breathing and
    muttering. Eyes shriveled and wasted, or a dull black.
  filter_tags: npc, cave, salt
```

`{1d4-2 curse_eye}` in this case will be processed as some number of Curse Eyes (not less than 0).  

I'm going to describe the syntax here with each optional unit in parentheses.  
`{((#)d#(x)(+ or - #)) (entity)}`  
Where # is any positive integer and "x" indicates that the die is exploding, (every time the die lands on its max face, another roll is performed).  

You can give an NPC `{3d10+10}` HP, or `{2d6x}`, or just `{2d6}`. There is no restriction on where you can use any kind of templating, so you could make the HP of a creature some variable number of Curse Eyes, your only problem will be that people may not understand what you mean by that.

Use templating to set up automation for rolls and to refer to other entities, how templating is actually handled varies from tool to tool, you don't have to worry about that level of implementation when including templated rolls or entities.   

As an example, the basic curly parse command has a lot of options regarding templating. You can generate text entries for entities while not doing anything special with templated `{}` sections and including them as-is in the generated text, or the tool can perform the rolls for you, or the tool can grab the entities within the templated sections, any entities within their templated sections, etc. It can do that recursive entity-fetching while also rolling dice at every step to determine the number of entities. For more detail, consult the code, ask the discord bot for /help, or read the help texts that go with the CLI commands.

## Why "curse_eye" instead of "Curse Eye"?

Names can include special characters, apostrophes, symbols, weird capitalization, etc. This can make working with names a bit of a pain. Within the code, the Names are converted in to `clean_name`s. These are names but lowercase, with all special characters removed, and with spaces replaced by underscores. Numbers are left in, mostly for the sake of certain skill progressions. So "Salt Wretch 2: SALTY!" becomes `salt_wretch_2_salty`.

## TODO:

It should be the case that people can just write {2d4 Salt Wretch} and the name is converted into a clean_name at time of processing (notice that a `clean_name` converted to a `clean_name` is still just a `clean_name` so it doesn't matter whether the conversion was already done for us). It should also be the case that someone can just specify arbitrary die rolls, so `{3+2d10-1d6 Salt Wretch}` should be valid. Neither of these things are true right now. Dropping this TODO here so that I get around to it at some point.

The good news is that when this change does happen, all the old templating will still be valid, so don't worry that the code will change under you as you use it and your old entities won't be valid anymore.

<!-- Die rolling does not support arbitrary equations, kisi and wile. It should, eventually. -->