---
title: Weapon Creation
toc: True
---

The intent is to be able to describe a real or fictional weapon clearly and succinctly so that you capture the intended use and function of the weapon. A person can be better with a certain type of weapon, some skills might only be useful with certain types of weapons, but we don't restrict a given weapon to a rigid and arbitrary typology. We do not care whether a bardiche is an axe, or a glaive is a spear, but the bardiche and the glaive should feel different to the player. Weapons should exist that are crafted for a specific niche, or that straddle the line between different categories. Weapons should feel unique and interesting to find and use.  

## How Weapons are Described and Why

Information about a weapon is stored in two places. The first is in the "Tags" section which includes general information like whether the weapon is [one-handed], [two-handed], [hilted], etc. The second place information is stored is in a given attack, a spear might have an attack that is [thrusting] and does (P) piercing damage.  
Putting these together, a handaxe is a [shafted] weapon with the [one-handed] tag that contains a [swinging: leading] attack that deals slashing (S) damage. Skills might require a certain damage type or a certain tag, but they won't require the use of an axe or a sword. The system has no opinions about what exactly qualifies as an axe or a sword. The system only describes relevant features of the weapon and what you can do with it.  

Why do this? In history (and in various fantasy settings) people did not restrict themselves to making weapons that fit cleanly into one category. Pole weapons were given all sorts of hooks, blades, points, and hammer heads so that they might fill a specific niche at a specific time. Swords were created that specialized in heavy cleaving strikes, like a khopesh, or thrusting through gaps in armor, like an estoc. Swords were created in all sorts of lengths, profiles, weights, and guards so that they might be lighter, easier to travel with, better against armor, better on horseback, have greater reach or be easier to conceal. I'd like a system that captures those different tradeoffs, designs, and functionalities while also being intuitive, easy to use, and lightweight. It shouldn't be the case that a character just holds on to the best plussest sword they've found so far. Players should be thinking about what they might expect to face or what practical tradeoffs are best for their characters.  

Skills might capture a proficiency with a broad category of weapon like [one-handed] or [two-handed], but they can also get a lot more specific. A skill can describe the ability to do a devastating cleaving slash that destroys armor. This skill would augment a move with [swinging: leading] (I'll get into what specific sorts of tags mean in a later section) that does slashing (S) damage. This cleaving skill seems like it was probably made with axes in mind rather than a  rapier or a spear, and as you'd expect neither of those weapons have moves that are compatible with the skill. However, both a meat cleaver and a khopesh do have moves compatible with the skill. This should make sense. With its forward curving blade, a khopesh resembles an axe in its intended use much more than it resembles a rapier, though a rapier and a khopesh are both "swords".  

This emerges from how we describe a khopesh and how we describe the move. The person who made the move doesn't have to have any idea what a khopesh is, the person who made the khopesh doesn't need to know about the existence of that particular move, but a player who has been using nothing but [two-handed] axes for a month might find the [one-handed] khopesh and realize that it plays to their strengths and allows them to branch out, maybe they expect to face a lot of ranged weapons for a while and they would like a large shield in their off-hand. Maybe they just think the khopesh looks cool or the khopesh has some magic property that works well with a spell they know.   

Rather than building tables, lists, references, or saying that some weapons are "axe-like" or "straight-sword-like" and constantly dealing with historical and fictional edge cases I've decided instead to attach a stable set of tags to weapons and moves as those qualities come up. Separating moves like this also allows some weapons to be able to both slash and stab but be relatively better at one move than the other.  

## Broad Tags Based on Weapon Construction

This category includes any tag that is not move-specific. There are no strict requirements or restrictions here, weapons don't necessarily have to be described with some minimum number of tags from the standard set I'll describe. No tags are inherently mutually exclusive, a weapon could quite easily be made that is intended to be used either [one-handed] or [two-handed] and has both tags. Though there are not strict requirements, there are basic tags you will see over and over and when making a weapon, you should almost certainly introduce some of these basic tags so existing skills will work well with the weapon.  

You do not have to express every effect and quality purely through tags. You can specify different conditions or behaviours in the text of the weapon or along with specific attacks.

### [one-handed], [two-handed]

These tags capture what you would expect, whether a weapon is meant to be used with one hand or two hands. There are generic rules in the main rules document that allow someone to two-hand a [one-handed] weapon that they might not have the strength to wield, or one-hand a [two-handed] weapon. Most weapons will be built to be either one or two-handed, but some will be designed to be either one or two-handed like a bastard sword. This sort of weapon should be created with tradeoffs in mind. The bastard sword is between the two categories, not quite as fast as a dedicated one-hander, not quite as hard hitting as a dedicated two-hander. When building a weapon like that you can just add both tags so skills for either one or two-handed weapons could be used, or you could specify some different behaviour or effect when the weapon is used with one hand or two.

### [range: X]

The range of a weapon is the number of spaces away from you that you can attack. If no range is included the weapon is treated as being [range: 1]. [range: 0] is a special case. When using a [range: 0] weapon like a dagger or brass knuckles you are treated as moving into the enemies space during your attack and then back out again, though some skills may allow you to fight your enemy within their space which might be advantageous for you. [range: 3] is assumed to mean all the spaces up to 3, i.e. [range: 0-3]. If this isn't the case you can specify the low end of the range. An especially long pike might be [range: 2-4], so that it is completely unusable at close quarters. If you want to specify some specific disadvantage or advantage from range just include the range and then describe that in the weapon text.

### [hilted], [shafted], [flexible]

This is a pretty important category. [shafted] weapons are any weapon that consists of a head mounted on a shaft or pole. Rather than having some set of unambiguous places for one's hands, they have a length along which any place is a valid handle. Axes, every polearm, staves, and spears all fit in this category.  

[hilted] weapons do not necessarily need a pommel or a guard, their defining feature is having some  unambiguous place or set of places for the hands. You are not necessarily meant to slide your hands around when using these weapons. All swords and knives fit in this category, even what is typically called a "zweihander" with its ricasso and parrying hooks fit in this category. In the case of the zweihander you may have more options of where to grab the weapon, but you do not have one large continuous handle as in an axe. The zweihander has distinct set of grips, so it counts as [hilted].  
[flexible] weapons are a pain. There are two general categories of flexible weapon: [flexible: flail] and [flexible: whip]. [flexible: flail] includes any flexible weapon with a striking body at the end such as in a pinyin, hussite flail, or in a simple one-handed flail with a ball and chain. [flexible: whip] includes any flexible weapon without a striking body at the end, such as a whip, or an urumi.  

A weapon is typically only one of [hilted], [shafted], or [flexible]. That being said, there is nothing besides human decency that would keep you from making a swordspear with a ball and chain attached to the shilt (similar to how the flail is attached to the kusarigama). I cannot stop you. I wish I could. You could even make it [one-handed], [two-handed], and completely unusable. In general, resist the urge to create a platypus because it has as all the tags, most weapons in history did not look like that because having all that extra stuff makes the weapon a clumsy mess. It doesn't show up in fantasy because it's ugly. But you can still do it.

## Use-Based Tags

### [stealth] and [finesse]

Both [stealth] and [finesse] are used exclusively to fulfill requirements to use skills. [stealth] expresses a weapon that is small and concealable, useful for sneak attacks. [finesse] expresses weapons that are meant to be able to deflect, redirect, and punish enemy attacks, [finesse] is used for active non-STR based defense. Both of these could and probably should be replaced by just referencing qualities of the weapon.

### [bladed]

[bladed] is a construction tag that is used for currently-in-testing [sharpening] effects. This will probably be replaced by just having whetstones and invocations look for moves that do slashing (S) damage, but that change is not put in place and the tag is still present, so it's included here.

## Move-Based Tags

These are explained quite well in the core rules [here]() and I don't have anything to add to that explanation.

### [ranged]

This captures any ranged attack. The motion is much less important for a ranged attack, presumably you are not in melee when performing it. You should give a range for a ranged attack, and if the attack is a [ranged: throwing] attack you should say so. It's likely obvious (how else would a javelin have a ranged attack?) but for ease of use and to avoid ambiguity with whether a given skill can be used, just specify [ranged: throwing]  
*Some move text*...[ranged: throwing] [range: 5] is fine.

## Requirements vs Scaling and a Note on Weapon Sizes

When in doubt use requirements to balance weapons instead of score based damage scaling (+SCORE to damage). Fast weapons should very rarely get score based damage scaling. Slower weapons should be much more likely to get score based damage scaling. In general (but especially in the case of faster weapons) score based damage scaling should be a remarkable feature of weapon, not a standard part of an attack. It's totally fine for weapons of a higher quality to be straightforwardly better than simpler or more common weapons.  
Versatile weapons (that is to say, weapons that are good at multiple types of attacks, and don't necessarily specialize) like straight swords do not generally scale with stats, they just have higher requirements. There are skills for more advanced characters to use to do more damage, this is where most extra damage should come from. Some weapons like hammers might add STR to damage, and many ranged weapons might add PERCEPTION or DEX to their damage, but their base damage is lower to compensate. For these weapons, the idea is to express that relatively more of the damage comes from how hard you can swing the hammer or where you place your shots.  
Of course, where you hit with a sword matters too, but it's not considered to be the main component. The reason for this admittedly arbitrary distinction is mostly a mechanical one.
Let's say you add STR scaling to a weapon. You can expect most players using that weapon to have 2 or 3 effective STR. The expected value of a die where the max roll is x is x/2 + 0.5, so the expected value of a d6 is 3.5. If you add DEX damage scaling to a weapon that does a d4 for damage and the player has 2 DEX, then the expected value is 3.5 + 2 or 5.5, the same expected value from as an attack from a d10 weapon, this is a huge jump.  
Additionally, adding scaling is a much bigger deal for faster weapons than slower weapons, as attacking three times with a weapon that has +DEX scaling means you add it three times in that turn, so if you had 2 DEX you're suddenly doing 6 extra damage, or equivalent to an exra d11.
Slower weapons and two-handed weapons already have the disadvantage that they eat up more AP, restricting your options within a move. You can also just miss your one attack with a slow weapon, and with a two-handed weapon you don't get a shield or anything else in your offhand. Damage scaling can be used to combat this, giving players more of a reason to use larger slower weapons, especially if it plays to their strengths. 
You'll notice that generally [two-handed], slower, larger weapons generally do more damage per turn than smaller, faster, [one-handed] weapons, this is intentional. As explained above, smaller faster [one-handed] weapons already have a lot of advantages and flexibility. [two-handed], slower, larger weapons generally need more features and more damage to balance them out. When making a larger weapon, you have to include mechanics and features to try and express the advantage of having more reach and more power than your opponent.

## Weapon Weight

If you`re playing with encumbrance, [one-handed] weapons are 1 enc unless they are [range: 0], [range: 0] is just a small item. [two-handed] weapons are 2 enc, heavy weapons are an extra enc, having a reach over 3 (non-flexible) adds an enc.

## Weapon Attack Speeds / Types, [BA] Cost Patterns

[This ends up being tied up with the action economy and the standard AP, see the linked doc.]()

## Attack damage

Damage for 1 handed weapons is centered around 1d8 (4.5). Two-handed weapons are centered around 2d6 (7). 

### Multiple Damage Types

It's possible for a weapon to do multiple damage types, e.g. a club covered in spikes. In this case, just add both sorts of damage to the same attack, say, 1d6 (B) + 2 (P). Be aware that adding flat damage raises the expected value of the damage by more than you would expect, 1d6 + 2 is equivalent to 1d10.  
A giant club with spikes might be 2d6 (B) + 1d6 (P).  
If a weapon deals multiple damage types, both damage types are affected by armor separately. That is, if there is armor that blocks 4 (B) and 2 (P), you attack with the club that deals 1d6 (B) + 2 (P), and roll a 5, you do 1 damage in total, so doing multiple damage types in one hit is a bad bet against armor, though it might just be free damage otherwise.

### One-handed examples:

1d4+ (light), small weapons, dagger, shiv, small club, push dagger.

1d6+ (light-medium), smaller weapons, aggressive scaling weapons (+2*Stat), finesse weapons with scaling, hatchets.

1d8 (medium), normal sword, club, lightly scaling weapons.

1d10 (medium), high quality weapons, martial weapons.

1d12 (medium), very high quality weapons.

### Two-handed examples:

1d10, 1d12 (light-medium), low quality weapon or aggressive scaling weapon.

2d6 (medium), typical two-handed weapon.

2d8 (medium-heavy), high-requirement two-handed weapon, high quality.

3d6, 4d4, 2d10 (heavy), high quality, heavy weapons.

3d8 (heavy), giant weapons.

## Making Weapons

This has been a long document. Understanding what each tag is meant to represent and how a given tag follows from the construction and use of a weapon requires a fair bit of explanation, but it shouldn't require so much knowledge to use, the work of weapon interpretation should be done almost entirely in the process of creating it, players should get a relatively concise and straightforward statblock, something that easily fits in a card, with each potentially mechanical tag in brackets "[]".

## Actually Making a Weapon, Finally

Let's make a simple one-handed spear using this framework.

Spear <-- The name, easy.  
Requirements: <-- If there are no requirements we can leave this blank or omit it entirely.  
Tags: [one-handed], [shafted] <-- Some basic tags.  
Speed: (2n1) <-- Just one attack speed.  
To-Hit: +AGI <-- All basic moves share one to-hit score unless otherwise stated.
- 1d8 (P) [thrusting] <-- The attacks (or "attack" in this case). Damage roll, damage type, then any tags.
*"A large iron head fastened to the end of a simple hardwood shaft."* <-- A brief description.

There are plenty of skills that one can use with this weapon, such as Defensive Perimiter. You do not have to call that out in the description. Striking with the butt end of the spear does not have to be included either, though it is something a player could do.

Now without notes.

Spear
Tags: [one-handed], [shafted]
Speed: (1n1)->(2n1)
To-Hit: +AGI
- 1d8 (P) [thrusting]
- *"A large iron head fastened to the end of a simple hardwood shaft."*

Not every spear needs to look like this. I choose to not give it requirements, give it a solid d8, make it a bit slower than a comparable sword, and describe it as a simple stout spear. You could create a lighter [one-handed] spear with a d6 damage die, make it a bit faster, and give it a [range: throwing] ranged attack. Maybe it's of higher quality, and it does all this while getting a d8 (try to avoid doing this too much to avoid power creep).

You can go the other way and create a heavy [one-handed] spear, here I'm going to use the historical example of the pilum.

Pilum
Requirements: 1 AGI, 1 STR
Tags: [one-handed], [shafted], [reach: 2]
Speed: (2n1)
To-Hit: +AGI
- 1d10 (P) [thrusting]
- AGI+PERCEPTION To-Hit, 1d12 (P) [ranged: thrown], [range: 3+STR]
  
Ignore STR armor in melee, 2*STR armor when thrown.

*"A heavy throwing spear. The narrow pyramid head is mounted on a long iron shank."*

Pilum historically came in a wide variety of lengths and weights. They all had a long iron shank, they tended to be heavy for a throwing spear. Some controversial theories say that the thin shank was meant to bend down after the head buries itself in the opponent's shield, making the shield much less useful. If you think that's a cool mechanic, add it into a pilum or some other thrown weapon. maybe the pilum requires a high STR check and a lot of time to remove from a shield and while it's in the shield the opponent can't use shield skills, their movement or AGI is lower while they're carrying it, something like that.  
The pilum seems like it was designed to punch through armor, so it ignores some armor on hit. You'll notice that the thrown move is quite strong, a d12 for a one-handed weapon. This was done for a couple reasons. First, the pilum is a specialized military weapon, meant for throwing at short range at an armored target, it should be very good in that context and it shouldn't be terribly common. Second, it is very slow at (2n1). Throwing the pilum is probably all you are doing in that turn. This is a good weapon, and in a certain context against a certain sort of enemy at a certain range, it can be really exceptional. However, once you throw it it's gone, and throwing it is going to take forever. A character might decide to throw it at the beginning of a fight, right before melee range and then get out their main weapon. This happens to be how the pilum was likely used. 
The point is not to make an extremely powerful weapon a character will definitely pick up and use for the rest of the game, nor is it to make an ideal historical simulation. Instead, just capture what it is that sets this weapon apart from others.

Now for something less serious.

## TODO: create some fantasy nonsense, probably that climbing hook/scythe idea.

And of course, for more examples you can just go through the existing weapons.

Weapons are classified loosely by weight and ease-of-handling which determines how quick their attacks are. Daggers and finesse weapons are light, most swords, clubs, and basic hammers are medium, and giant weapons are heavy. 

### Light Weapons:

- [1n1] 3 attacks per turn. shivs. 
- [1n1], [1n1], [1n2]* 2.5 attacks per turn.

### Medium Weapons:

- [1n1], [1n2] 2 attacks per turn.
- [1n1], [2n1] 2 attacks per turn, no options.

### Heavy Weapons

- [1n2], [2n1] 1.5 attacks per turn.

### Giant Weapons:
(clearly you should be able to trade a 2n1 for 1n3)...

- [1n3], [2n1] 2->1->1... bit over 1 per turn.
- [2n1]* 1 per turn.
- 
<!--

as a table now...
the thing really to note here is the size of the 2 SCORE bonus, how a [1n1] doing 1d4+SCORE does an expected 13.5 per turn, with 3 SCORE its 16.5!
which is equivalent to 5d6-1 when maybe you would have expected 3d4

| Speed  | AP Costs             | Max Attacks Per Turn | Notes/Context                                                                  | 2 SCORE Bonus |
| ------ | -------------------- | -------------------- | ------------------------------------------------------------------------------ | ------------- |
| Light  | [1n1]                | 3                    | Most flexible. Likely range: 0.                                                | 6             |
|        | [1n1], [1n1], [1n2]* | 2.5                  | Relatively rare speed.                                                         | 5             |
| Medium | [1n1], [1n2]         | 2                    | Either 2 attacks per turn or 3, then 1, then 3, etc. Still very flexible.      | 4             |
|        | [1n1], [2n1]         | 2                    | Not very flexible.                                                             | 4             |
| Heavy  | [1n2], [2n1]         | 1.5                  | Should hit very hard.                                                          | 3             |
| Giant  | [1n3], [2n1]         | 1.5                  | A little bit over 1, really. Can do two attacks if have both AP. Big AP drain. | 3             |
|        | [2n1]*               | 1                    | Very inflexible.                                                               | 2             |
         
useful table for me, probably should build this into the docs

| Qualitative                                 | Light                | Actions Per Turn | Damage Per Attack | Platos Weapon Closet | Damage Per Turn | w/ + 2 SCORE | w/ + 3 SCORE |
| ------------------------------------------- | -------------------- | ---------------- | ----------------- | -------------------- | --------------- | ------------ | ------------ |
|                                             |                      |                  |                   |                      |                 | 2            | 3            |
|                                             |                      |                  |                   |                      |                 |              |              |
| LIGHT, brass knuckles, small enemy          | [1n1]                | 3                | 1                 | "Unarmed"            | 3               | 9            | 12           |
| LIGHT, very fast, very fast knife or a shiv | [1n1]                | 3                | 2.5               | 1d4                  | 7.5             | 13.5         | 16.5         |
| LIGHT, large knives, small fast weapons     | [1n1], [1n1], [1n2]* | 2.5              | 3.5               | 1d6                  | 8.75            | 13.75        | 16.25        |
| MEDIUM, single handed weapon                | [1n1], [1n2]         | 2                | 4.5               | Medium 1d8           | 9               | 13           | 15           |
| HEAVY, heavy weapon, hits very hard         | [1n2], [2n1]         | 1.5              | 6.5               | Heavy 1d12           | 9.75            | 12.75        | 14.25        |
| GIANT weapons                               | [1n3], [2n1]         | 1.3              | 11                | Giant 2d10           | 14.3            | 16.9         | 18.2         |
| GIANT heavy weapons                         | [2n1]                | 1                | 13.5              | Giant 3d8            | 13.5            | 15.5         | 16.5         |

-->



"*" Indicates that a weapon attack speed/series is less common.

If you want to add weapons to the .yamls so that you can use the Python/automation tools to generate cards etc. head over to [the .yaml entity creation doc](./../code_and_downloads/yaml_entity_creation.qmd).