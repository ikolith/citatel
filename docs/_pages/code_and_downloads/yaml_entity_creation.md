---
title: YAML Entity Creation
toc: true
---

<!-- just grabbing some of the stuff out of the old npc csv doc....and wep doc -->


You can just write out whatever weapon on paper, it doesn't have to follow a specific format. When I give a couple examples later in this doc, I will not be following any particular format. I will be writing weapons in a format similar to what the plaintext generation functions produce based on a weapon entry in the weapons.csv at the time of writing. If you want to know more about adding weapons to the .csv, read the next section, else skip it and head to examples.

## Adding Weapons to the .csv

Weapons are stored in a csv, which should be called weapons.csv. They are transformed into whatever format whether it be, markdown, pdf, printable card, or a plaintext block in discord or on a command line.

The .csv contains the fields 
- name: The name of the weapon with punctuation and capitalization.
- tags: Broad tags like one-handed, two-handed, giant, etc.
- requirements: Required scores for the use of the weapon.
- speed: The attack speeds.
- to_hit: What to add to your to-hit roll.
- basic_attacks: A list of the attacks that are inherent to the weapon.
- effect: Extra text, special features.
- flavor_text: Descriptions, lore, stories.
- filter_tag: Extra tags used in filtering and searches, maybe this weapon is often found in a [swamp] or associated with some specific faction. These do not typically show up in cards and generated text, these are just for searching.
- clean_name: This is generated programmatically. It is the name but where all the letters are lowercase, all the spaces are replaced by underscores, and all the punctuation is removed. This is for easily programmatically referring to the weapon. You don't have to worry about this and it typically doesn't show up in a card or text.

## The Fields in the NPC .csv and What They Do 

The list of columns in the NPC .csv is: name, hp, scores, skills, holds, flavor_text, clean_name. So I'll be explaining each field and concept here. 

### A Basic Explanation of Templating in NPC .csv Based Generation 
The CSVs and associated Python functions support a sort of basic templating. Mark things that should be handled by templating with {}. The dice go first, then the entity. Either can be left out.
An example might be {2d6 curse_eye}. which will be processed as some variable number of Curse Eyes.
If you want the rolling to happen during NPC generation, wrap the roll in {}.  
You can give an NPC {3d10+10} HP, or {2d6x}.
I'm going to describe the syntax here with each optional unit of in parentheses.  
{(#)d#(x)(+ or - #) (entity)}  
Where # is any positive integer and "x" indicates that the die is exploding, that is every time the die lands on its max face, another roll is performed.

### The CSV fields.`

**name** 
The name of the NPC. With capitalization, punctuation, etc. All of this is cleaned later by clean_name, so you don't have to worry about getting the punctuation right when templating or searching.

**hp**
A starting player has 18 HP, you can scale based off of this. 

**scores**
Everything has the same sorts of scores that PCs have. You don't have to mention scores that are 0. Similar to how we deal with PCs, if you don't mention a non-special sort of score like STR, it will be assumed 0. Unmentioned special scores are assumed to not be present. A good rule of thumb is that the NPC should have scores at least high enough to wield whatever it holds and use whatever skills or abilities it has. When determining scores, first consider the standard set of scores: STR, DEX, AGI, CON. Then PERCEPTION, which is generally less important for NPCs. Finally, PERSUASION if that makes sense for the NPC.

**skills**
The set of skills an NPC has can include all of the skills in the game AND an arbitrary number of NPC specific skills. If an NPC skill you've created seems particularly useful, common, or interesting, consider adding it to the NPC skills CSV.

**holds**
What the NPC has, the items it carries, this is an ideal use case for {} curly brace templating.

**flavor_text**
The description of the NPC. Appearance, behavior, light NPC specific lore. You should keep most in-depth lore and history in a separate document.

**filter_tags**
The filter_tags field is just metadata that lets folks more easily search through NPCS, filtering for certain types of NPCs, or excluding certain groups.

**clean_name**
.csv specific. Generated and overwritten by code, just leave this blank.