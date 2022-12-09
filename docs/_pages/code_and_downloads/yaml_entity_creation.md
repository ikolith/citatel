---
title: .yaml Entity Creation
toc: true
# Embedded .yaml to configure the .yaml doc, ain't that neato?
---

## What is an "Entity"?

Skills, NPCs, weapons, items, armor, etc. are all treated as "entities" in the code. Entities that seem to be fundamentally different (NPCs vs. armor, for example) are not fundamentally different in the .yamls, they're just entities with different names and features (hp, description, effect, etc.). Markdown files, text, and cards can be generated for any entity or list of entities.  

## How does this relate to a ".yaml"?

Entities are stored in .yaml files. The entities in this project use only a couple of very basic .yaml features and I'll be explaining all of those in this doc. There are some tutorials and [introductions](https://learnxinyminutes.com/docs/yaml/) to the .yaml file format online if you're interested in really getting into the weeds, but you don't need to.

## What is a .yaml file and how do I edit it?

A .yaml is really just a text file, like a .txt or a .docx. You'll want a text editor of some kind to edit them. Your system will come with some default text editor and when you try to open a .yaml your system should suggest using it. On Windows this is Notepad, on MacOS this is TextEdit, on Linux you already have strong opinions about text editors.  
Some text editors are just black text on a white background. Some text editors have autocomplete, syntax highlighting, and all sorts of bells and whistles to make your life easier. If you want to upgrade from your system default, I recommend (from less to more complex) Notepad++, Sublime, and Visual Studio Code. All of those are available on every OS. I use VSCode because of the available extensions, I don't really know anything about the other ones.  

## Making and Editing .yaml entities

First, let's get used to what entities in the .yaml files actually look like:  

```yaml
- name: Machete
  tags: one-handed, hilted, bladed
  speed: "(1n1)->(1n2)"
  to_hit: "+STR"
  basic_attacks: "1d6 (S) [swinging: leading]"
  flavor_text: A simple tool for cutting down brush.
  encumbrance: 1
  filter_tags: weapon, basic
```

```yaml
- name: Rucksack
  effect: "Max encumbrance: 6 + STR, [encumbered] threshold: 3 + STR."
  filter_tags: item, bag, basic
```

The pattern here is pretty simple. Every entity starts with a name like this `- name: Eater of Names`. Then any other features that belong to that named entity are listed under it as `feature: Eats names, is allergic to features.` The two spaces in front of the feature are important. It says that the feature belongs to the same entity as the name. This allows us to list many entities in the same file, like so.

```yaml
- name: Haver of HP
  hp: 99
  filter_tags: haver, npc

- name: Haver of Flavor
  flavor: >-
    The Haver of Flavor leaves a strong impression. 
    It looks a certain way, it sounds a certain way, and it tastes a certain way, but it weighs nothing, does nothing, and can't be killed.
  filter_tags: haver
```

The first thing you might notice about the above text is the `>-` in the "flavor" field for "Haver of Flavor". These characters are just a way of telling the .yaml file a couple of things about the text it's going to see next. It says that what is going to show up on the next two-space-indented section belongs "flavor" and is a block of text. It also sets up a couple of rules. When there is one line break, that should be read by a computer as a space. If there are any more line breaks after the first, those should be read as normal line breaks. You're also telling the computer to get rid of any trailing spaces or line breaks.  
This is just a little trick to make writing long blocks of text easier without necessarily having line breaks added to the text. If we actually do want a line break in our text, we just add an extra line break! So altogether: 

```yaml
  flavor: >-
  The Haver of Flavor leaves a strong impression. 
  It looks a certain way, it sounds a certain way, and it tastes a certain way, but it weighs nothing, does nothing, and can't be killed.
```

Will be parsed as:  

```
The Haver of Flavor leaves a strong impression. It looks a certain way, it sounds a certain way, it tastes a certain way, but it weighs nothing, does nothing, and can't be killed.
```

But  

```yaml
  flavor: >-
  The Haver of Flavor leaves a strong impression. 
  
  It looks a certain way, it sounds a certain way, and it tastes a certain way, but it weighs nothing, does nothing, and can't be killed.
```

Will be parsed as:  

```
The Haver of Flavor leaves a strong impression. 
It looks a certain way, it sounds a certain way, and it tastes a certain way, but it weighs nothing, does nothing, and can't be killed.
```

If that seems annoying, you can just not use `>-` or [similar little editing tricks](https://learnxinyminutes.com/docs/yaml/), instead just write your text in one big line.  

You'll notice there is a line break between the two entities in the file. This is not for any technical reason, I just think adding a line break between entities makes the file more readable. Line breaks between entities are ignored.  

### Available Features for Entities, What do Different Entities Look Like?

The full list of features an entity can have is:  

- basic_attacks
- cost 
- effect
- encumbrance
- filter_tags
- flavor_text
- holds
- hp
- name
- requirements
- scores
- skills
- speed
- tags
- target
- to_hit
  
These all have special rules for formatting, they can be changed if you want to [plumb the code](https://github.com/ikolith/citatel/blob/main/py_utils/entity_text_generators.py) but you don't need to.  

When you use entity generators (card generators, .md file generators, etc.) the features for the entity will be and added in whatever order they're in in the .yaml. If you choose a weird order nothing bad will happen, but the card might not look like other similar cards.

### Where are the Entity .yamls, where should new ones go?

In the repo, the .yamls live in [./docs/_data/entities](https://github.com/ikolith/citatel/tree/main/docs/_data/entities). There are a bunch of different .yamls for different sorts of entities, different groups of entities, themes, etc. This is just because they are easier to work on this way. This has no impact on the code. The code will just look in the folder and read every .yaml file present, it takes no note of what .yaml an entity is from. In the folder there is one special .yaml, `templates.yaml`. This .yaml has no actual entities in it, the only thing it contains are blank entity examples that have been commented out. These blank templates have all of the fields that the most complicated (typical) example might have. For example, this is the entry for a weapon entity:

```yaml
# typical weapon example:
#
# - name: 
#   tags: 
#   requirements:
#   speed:
#   to_hit:
#   basic_attacks:
#   effect:
#   flavor_text:
#   encumbrance:
#   filter_tags: weapon
```

[Link here](https://github.com/ikolith/citatel/blob/main/docs/_data/entities/templates.yaml). 

If you want to add to the .yaml files you can edit them directly. You can also make your own .yaml in the same folder and it will be picked up with everything else when data is loaded. If you don't want something to be loaded, delete it or just move it out of the folder.

### filter_tags?

`filter_tags` does what it says on the tin, it's set of tags that people can use to filter entities that they see when generating text, cards, or searching through them. You'll notice that `filter_tags` is the only feature that isn't blank in the example above. This is because the example was from the `weapons.yaml`, so presumably any entry would be a weapon. If you want to print cards for every weapon, you would just search for entities with 'weapon' in their `filter_tags`.  

There is no restriction to the number of `filter_tags` an entity can have. You do not have to pick from a restricted set of `filter_tags` and you can add as many `filter_tags` as you want (though of course, common or relevant ones will be much more useful to people).  

The `filter_tags` field shouldn't be confused with the `tags` field. `filter_tags` are for searching and filtering, they have no in-game use. `tags` have in-game mechanical uses, they are things like `bladed` or `two-handed`. In the future this distinction might be ironed out a bit more, but right now just remember that they are totally different things, you cannot filter by `tags` and you cannot use `filter_tags` like normal `tags` in-game.

The only strict rule is that multiple `filter_tags` should be separated by commas. The preferred style for `filter_tags` is all lowercase with no special characters. If you need to add a space, use an underscore.  

Entity type filter tags are very common and useful. These are `invocation, item, npc, skill, weapon`.  

The most important filter tag might be `basic`. `basic` marks entities that any character should know about at the start of the game, these are explicitly *not* spoilers. The `basic` tag allows players and DMs to confidently generate a full list of spoiler-free content from any set of entities.

## Technical Asides (You Can Probably Skip This)

.yamls support many data types but in our case once the .yaml is loaded everything will be cast into a string anyway so don't bother worrying about it. .yaml does not have strict typing, so things that look like strings will be interpreted as strings, but you can make this explicit by wrapping the data in quotation marks or using some sort of [folded or literal block nonsense](https://learnxinyminutes.com/docs/yaml/).

There are some other yamls in the repo like the `navigation.yaml` and `_config.yaml`. .yaml is a common config file format. Those are config files, they have nothing to do with game entities, that's why they look nothing like the entity .yamls I've described.
 
