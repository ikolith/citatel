---
title: NPC Creation
toc: True
---

NPCs are described mechanically in the same way that a player is described, so NPC generation doesn't differ much from character creation. NPCs meant for combat are not very different from NPCs not meant for combat.  
NPCs can be generated a variety of ways, there can be simple NPCs with a couple of stats and basic weapons and there can be NPCs like Legions which have a whole unique process for generation.
In this doc I'm going to focus on creating enemies for addition to the NPC .csv, but the same ideas can be used to create NPCs on paper or in some other system. When generating and using NPCs, you should always leave room for improvisation. Like any other system, this system should aid improvisation and spontaneity.

## Why randomize?

Sometimes we roll dice to determine an NPCs, HP, possessions, etc. This is to introduce another layer of unpredictablility. Most players will, intentionally or not, quickly figure out how much HP a mob normally has after a couple of fights. Randomization is used to make NPCs a bit less predictable. Templated randomization is there to do some work for the DM and speed up NPC generation. If the result of randomization doesn't make sense in the context of the game, don't use it. If you think the fight or story would be better if an NPC had or did not have something, just give it to them. At every point randomization and generators should make your life easier. DMs shouldn't defer to them over their own judgment about a situation.   
Most NPCs will carry things like money, bandages, etc. That sort of thing does not necessarily need to be specified.

### What should stats feel like?

This table describes what different STR scores feel like.

| STR Score | Description                                                     |
| --------- | --------------------------------------------------------------- |
| -3        | You need medical attention.                                     |
| -2        | You are extremely weak. You can barely wield a weapon.          |
| -1        | You are very weak.                                              |
| 0         | You are able-bodied.                                            |
| 1         | You are strong. You get a lot of exercise                       |
| 2         | You are extremely strong.                                       |
| 3         | You have reached elite level strength.                          |
| 4         | You are freakishly strong, able to do the seemingly impossible. |

Other qualitative score tables may be added eventually but they're not necessary. These characterizations can be pretty effectively generalized. 0 is an unremarkable quality or level of ability. 1 and 2 indicate unusual proficiency or a notable quality. 3 tends to indicate expert or elite level, anything above that is superhuman.

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

### The CSV fields.

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