---
title: .yaml Entity Creation
---

## What is an "Entity"?

Skills, NPCs, weapons, items, armor, etc. are all treated as "entities" in the code. Markdown files, text, and cards can be generated for any entity or list of entities.  

## How does this relate to a ".yaml"?

Entities are stored in .yaml files. Entities use only a couple of very basic .yaml features. I'll be explaining all of those in this doc. There are some tutorials and [introductions](https://learnxinyminutes.com/docs/yaml/) to the .yaml file format online if you're interested in really getting into the weeds, but you don't need to.

## What is a .yaml file and how do I edit it?

A .yaml is really just a text file. You'll want a text editor of some kind to edit them. Your system will come with some default text editor, when you try to open a .yaml your system should suggest using it. On Windows this is Notepad, on MacOS this is TextEdit, on Linux you already have strong opinions about text editors.  
Some text editors have autocomplete, syntax highlighting, and all sorts of bells and whistles to make your life easier, some are very minimalist. If you want to upgrade from your system default, I recommend (from less to more complex) Notepad++, Sublime, and Visual Studio Code. All of those editors are available on every OS. I use VSCode because of the available extensions. Quarto has a nice VSCode extension, I would recommend VSCode if you want to mess with Quarto.

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

The pattern here is pretty simple. Every entity starts with a name like this `- name: Eater of Names`. Then any other features that belong to that named entity are listed under it as `  foo: bar` The two spaces in front of the feature are important. It says that the feature belongs to the same entity as the name does. This allows us to list many entities in the same file, like so:

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

The first thing you might notice about the above text is the `>-` in the "flavor" field for "Haver of Flavor". These characters are just a way of telling the .yaml file a couple of things about the text it's going to see next. It says that what is going to show up on the next indented section belongs to "flavor" and is a block of text. It also sets up a couple of rules. When there is one line break, that should be read as a space. If there are any more line breaks after the first, those should be read as normal line breaks. You're also telling the computer to get rid of any trailing spaces or line breaks.  
This is just a little trick to make writing long blocks of text easier without having line breaks added to the text. If we actually do want a line break in our text, we just add an extra line break! So altogether: 

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
- table (NEW!)

These all have special rules for formatting, they can be changed if you want to [plumb the code](https://github.com/ikolith/citatel/blob/7a36a1d906e802601cc6d651087de3e70b0a9100/citutils/citutils/entity_text_generators.py#L103) but you don't need to.

**Every entity can only have one of each feature.** Entities cannot have two `name`s, two sets of `filter_tag`s etc.

When you use entity generators (card generators, .md file generators, etc.) the features for the entity will be presented in whatever order they're in inside of the .yaml. If you choose a weird order nothing bad will happen but the card might not look like other cards.

### Where are the Entity .yamls, where should new ones go?

In the repo, the .yamls live in [./data/entities](https://github.com/ikolith/citatel/tree/main/data/entities). There are a bunch of different .yamls for different sorts of entities, different groups of entities, themes, etc. This is just because they are easier to work on this way. This has no impact on the code. The code will just look in the folder and read every .yaml file present, it takes no note of what .yaml an entity is from. In the folder there is one special .yaml, `templates.yaml`. This .yaml has no actual entities in it, the only thing it contains are blank entity examples that have been commented out. These blank templates have all of the fields that the most complicated (typical) example might have. For example, this is the entry for a weapon entity:

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

[Link here](https://github.com/ikolith/citatel/blob/7a36a1d906e802601cc6d651087de3e70b0a9100/data/entities/templates.yaml#L33). 

If you want to add to the .yaml files you can edit them directly. You can also make your own .yaml in the same folder and it will be picked up with everything else when data is loaded. If you don't want something to be loaded, delete it or just move it out of the folder.

### filter_tags 

`filter_tags` does what it says on the tin, it's set of tags that people can use to filter entities that they see when generating text, cards, or when searching through entities. You'll notice that `filter_tags` is the only feature that isn't blank in the template. This is a weapon template so presumably it would have the weapon tag. If you want to print cards for every weapon you would just search for entities with 'weapon' in their `filter_tags`.  

There is no restriction to the number of `filter_tags` an entity can have. You do not have to pick from a restricted set of `filter_tags` and you can add as many `filter_tags` as you want (though of course, common or relevant ones will be much more useful to people).  

The `filter_tags` field shouldn't be confused with the `tags` field. `filter_tags` are for searching and filtering, they have no in-game use. `tags` have in-game mechanical uses, they are things like `bladed` or `two-handed`. In the future this distinction might be cleaned up, but right now just remember that they are totally different things, you cannot filter by `tags` and you cannot use `filter_tags` like normal `tags` in-game.

The only strict rule is that multiple `filter_tags` should be separated by commas. The preferred style for `filter_tags` is all lowercase with no special characters. If you need to add a space, use an underscore.  

Entity type filter tags are very common and useful. These are `invocation, item, npc, skill, weapon`.  

The most important filter tag might be `basic`. `basic` marks entities that any character should know about at the start of the game, these are explicitly *not* spoilers. The `basic` tag allows players and DMs to confidently generate a full list of spoiler-free content from any set of entities.

### table

Tables are a new feature, and not as well covered in these docs as they should be!

```{yaml}
- name: Haver of Table
  table:
    roll: 1d4 # (Optional)
    outcomes: # (Required)
      1: A bad roll.
      2-3: An okay roll.
      4: A great roll!
      5-6: An impossibly good roll.
```

Every entity can only have one `table` feature, but you can use {} templating to embed any number of tables in an entity, just like you can embed any number of die rolls.

```{yaml}
- name: Roller of Haver of Table
  table:
    outcomes: 
      1: Do nothing.
      2-3: Roll {Haver of Table}
      4: You're very good at rolling. You roll {Haver of Table d4+2}
```

Let's go over these two entities with tables. You'll notice that the table is contained in the `table` feature which itself contains (with indentation!) `outcomes` and `roll`.  

`outcomes` is required. It is what makes up the table, it associates some roll or rolls with some outcome. You can specify some range between X and Y for outcomes. You cannot have overlap, so one table cannot have both ranges from `1-3` and `2-4`.  

`roll` determines what die you roll when rolling on the table. If `roll` is not specified, you roll a single die with the lowest face equal to the minimum outcome and the highest face equal to the maximum outcome.

You'll notice that the Haver of Table has a roll of 1d4 and outcomes from 1-6. This means if you just call `{Haver of Table}`, you'll roll a d4 and you'll never get the `An impossibly good roll.` outcome. Notice also that if you roll a 4 on the `Roller of Haver of Table`s entity, you'll roll `{Haver of Table d4+2}`. This trailing `d4+2` specifies that if the entity `Haver of Table` *has* a table in it, you should ignore it's range and `roll` and roll `d4+2` instead. This means that through rolling a 4 on `Roller of Haver of Table`s table, and then rolling a 4 when you roll `d4+2`, you can get `An impossibly good roll.`!

The way the program determines what to roll on the table is this:  
If the roll was specified after the entity was called, use that roll, whatever it is. Otherwise, use whatever the table in the entity said to roll. If the table in the called entity does not specify a roll, just randomly pick a number between the biggest and smallest outcome.

Being able to specify what die to roll on a table can allow you to reuse tables more easily. You can create one weapon table for a faction which contains 20 weapons ranked in quality. Lower ranked enemies can roll a smaller die to get weaker weapons from this table, while more dangerous enemies can roll something like 1d10+10 on the weapons table, guaranteeing that they have at least the weapon at outcome 11. You can also use this to reuse area generation tables, or to allow a player to be able to add some score when rolling on a table, accessing better outcomes. You can also ignore it entirely.