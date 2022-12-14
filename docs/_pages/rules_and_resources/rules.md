---
title: Rules
toc: true
layout: single
---
<!-- this note likely should be moved... or just put at the first mention of one of these... maybe in one of those sidenote-blocks  -->
Every rule comes with an attached "unless otherwise specified" as is standard in games like this. "GM" is "Game Master" which is interchangeable with "DM"/"Dungeon Master". "TTYGM" is "talk to your GM".

<!-- # How Characters Work -->

## Characters, Scores, and Attributes

The basic character sheet consists of HP, a list of attribute scores, and a defense score. Different types of characters have different base defense, HP etc. The base sheet for a human looks like this:

HP: 18 + (6*CON), Defense: 6, Movement Speed: 4

| ATTRIBUTE | SCORE |
| --------- | ----- |
| STR       | 0     |
| AGI       | 0     |
| DEX       | 0     |
| CON       | 0     |
| PERC      | 0     |
| SOC       | 0     |

> PERC is short for PERCEPTION, SOC is short for SOCIAL

You'll notice that every score on this sheet is 0. A character with 0s all the way down their sheet is analogous to someone who is generally healthy, without any notable deficiencies or strengths. Having 0 in a score does not mean you cannot perform actions related to that score. 

You *can* have a negative score in an attribute. A -3 in a score means you can't perform actions related to that score and anything you do related to that score fails.

All characters, player and non-player characters, use the same system and follow the same rules. Any NPC character sheet could conceivably be used as a player character (subject to GM decisions about balance). 

### What are scores used for?

Scores can show up pretty much anywhere, most commonly they are used as modifiers. For example, if you have 2 STR and use a weapon that is +STR to hit, you add 2 to your roll to-hit. Some weapons also add scores to damage.
Scores are also used as prerequisites for obtaining skills or using a particular weapon. Learning to pick pockets might require some minimum DEX, a giant club might require some minimum STR for effective use.

### "Passive" Scores

When you roll "against" someone else's score the DC is 6 + SCORE. The passive participant doesn't roll (another way of thinking about it is that they are "assumed" to have rolled a 6). This is covered in greater detail in the section on checks and contests.

### How many scores *are* there?

 ¯\\\_(ツ)\_/¯

Practically speaking, any given setting will only have so many scores, but the system has no opinion on what those scores can be. If you're asked to perform a check with a score that you don't see on your sheet, you can assume your score is 0 unless otherwise stated, or unless the score has the [special] tag.

#### [special] Scores

If you attempt to perform any action with a [special] score you don't have, nothing happens. You fail all contests related to the score. PSYCHIC and PYROMANCY are both [special] scores. Having a PYROMANCY of 0 on your sheet means you are a mediocre pyromancer, not having PYROMANCY on your sheet means you are not a pyromancer. Sometimes the [special] tag is notated [s] for the sake of brevity.

#### "Standard" Scores

"Standard" scores are not mechanically special in any way. They are just non-[special] scores that are very common or important in a given setting. When creating a character you should consider what the character would have for each standard score.

As an example, for a fantasy setting STR is important enough that any PC will likely keep track of it on their sheet even if their STR is 0, but MEDICINE is not that important. If you're playing in a sci-fi setting with spying, hacking, and intrigue it could be the case that STR just does not come up enough to be considered "standard" but TECHNOLOGY does. What is "standard" in a setting is just a convention to make character creation/management easier by limiting the number of scores people have to think about, there are no mechanical implications. 

In these docs STR, AGI, DEX, CON, PERCEPTION, and SOCIAL are the standard scores.

### HP and CON

CON is used to resist status effects like POISON and EXHAUSTION. For every point of CON you have you can choose to ignore the effects of 1 stack of any number of status effects you have. You still have the status effect, meaning other effects that rely on that status effect can still be triggered. The ignored status effects are resolved or wear off at the same rate as they would otherwise.  

If you have 1 CON and you've been given 1 bleed and 3 poison, at the beginning of the round you can choose to take 2 damage from the poison and ignore the bleed. You still have that 1 bleed until you remove it.  

CON increases your max health by 6 * CON. 

### Defense

Defense can be raised by actions like “Dodge” and it can be lowered by bulky armor. Skills might also alter it, but the baseline is 6. When someone rolls to hit you, they are rolling their To-Hit check against your current Defense as the DC (or "Difficulty Class"). 

## Character Creation and Management

### Increasing Your Scores
You can increase your scores at any time using skill points. <!--  TODO: I still don't like this, and very likely skill points and score points will become different things, somehow! I dont know! --> The cost of increasing a score from 0 to 1 is 1, the cost of going from 1 to 2 is 2, 2 to 3 is 3, etc. The cost of increasing from X to Y is Y. So, going directly from 0 to 3 costs 1+2+3, or 6 SP.  To go up from a negative score to the next score only costs 1 SP.

How much does it cost to go from 0 straight to…?

| Score | SP Cost |
| ----- | ------- |
| 1     | 1       |
| 2     | 3       |
| 3     | 6       |
| 4     | 10      |
| 5     | 15      |


<!-- why is this here? this really just gestures at the bigger problem that i straightforwardly do not know in what order i should talk about things! it seemed reasonable to me that i should talk about what a character looks like, but then it seems like i should immediately talk about character creation.. and it seems straightforwardly wrong to talk a about character creation before AP?? surely all this character creation and character sheets... should maybe go in another doc entirely? should character creation be part of the base rules? maybe not... maybe not.. -->
### Character Creation

Character creation allows you to modify the basic character sheet, add skills, create a backstory, choose starting equipment, etc. There are two primary ways of doing this, point buy and randomization. Point buy is the simplest and it uses the same mechanics that are used throughout the game to increase scores and buy skills so it will be explained first.

### Point Buy

You get some number of skill points (SP) to spend at character creation; how many points is determined by how exactly you want to start your game, TTYDM. Starting with 0 points to spend is good for a longer campaign where you want to start as entirely mundane commoners -- you might even start with negative points. 9 SP is a good amount to start with to create semi-competent adventurers. Remember that you can spend SP on either scores or skills, the SP cost of a skill and any prerequisites are listed along with the skill.
 
You can lower a standard score to -1 to get a point out of it, you can only do this to 3 standard scores at character creation.
<!-- im considering that it may be a lot more interesting to make more negative scores worse... where... i guess you would have to pay the price of the negative score you are leaving... so -2 -> -1 would be 2 points. -->

### Randomized Character Creation

Alternatively, you can generate a random character by rolling dice for every score. You can decide with your group whether you want to go down your list of stats in order, starting by rolling to determine STR, then AGI, etc. or if you want to roll 6 dice and then be able to allocate them however you want. Choosing your allocation obviously makes it much easier to have a cohesive build.  

#### A Couple of Randomization Schemes

To determine stats at the start of the game, I suggest you either use d4-2 or d6-3. d6-3 is straightforwardly "better" than rolling d4-2. d6-3 is statistically equivalent to putting 1.5 SP into each score. If you are just rolling for the core skills, that's a total value of 6 \* 1.5 = 9. d4-2 is equivalent to 0.75 SP per score, or 6 \* 0.75 = 4.5. Given that standard point buy gets 9, I would give randomized characters 4 or 5 points to spend on skills, depending on how competent you want your character to be right at the beginning of the game.

I recommend d4-2. It gives characters a bit more room to grow and develop during the game. d6-3 will mean that you will likely get a 3 in some stat, which is so valuable it could quickly define your character before you've had a chance to play them.

<!-- ### A Note on Skills and Backgrounds -->
<!-- Consider how your background and the skills you start with might support each other. Picking specific skills for relevance to your background rather than building an optimal character can give your character a lot of interesting moments, especially early on. -->

<!-- ### Aside: Setting Agnosticism and Edge Cases

These rules are setting agnostic. You should be able to play only with material from one setting, or pick and choose mechanics from many settings, or move characters between settings. The rules are written so that the game is easy to extend, modify, and improvise with.

Say you have created a character in a fantasy setting with the standard scores used throughout this doc (STR, AGI, DEX etc.). This character somehow ends up in a sci-fi setting where TECH is a standard score, they went through a portal or something. It would be unreasonable to treat that character's TECH score as 0 given that they've never even seen a computer. They should treat TECH as a [special] score or have a very negative score in TECH, say -5 (expressing that it would take them a good deal of work to get to the point where they can even begin to interact with technology). There is no rule that expresses this. It is expected that if you mix settings and mechanics in this way you will have some edge cases to iron out and you will have to make up some rules on the fly. The rules are (hopefully) written to be flexible, consistent, and simple in a way that makes doing this easy.  -->


## Checks and Contests, "Doing Stuff"
<!-- annoying here that i mention a DC and explain it... though i have previously mentioned the idea of a DC! -->
When you're trying to do something that you might fail at e.g. hitting someone with an axe or jumping over a chasm, you roll two six sided dice (notated 2d6) and add the relevant score. This number is your "roll". To figure out if you succeed, you compare your roll to the "Difficulty Class" (or DC). The DC might be determined by the GM, or it might be determined by something in the world, like another character. If the DC is stable and dependent on something in the world, it's a check. If the DC is dependent on another character's roll, then it's a contest. When two characters roll opposing rolls, that's a contest. When one character rolls, that's a check.

### Performing a Check Against a Score

When a check is made "against a score", the DC is 6 + SCORE. If you're trying to poison someone and have to roll "against" their CON the DC is 6 + CON. The character that initiated the action and rolls is the "active" party, or "attacker". The party that is being rolled against is the "passive" party, or "defender".  
Defender wins ties.

### An Example of a "Contest"

Arm wrestling is a good example of a contest. There's no obvious number you have to beat, you just need to do better than the other guy. When participating in contests, you roll and then compare your roll to the "opposing" roll, that is, the roll representing the efforts of whoever you are trying to beat. If theres is a tie, the person with the higher relevant score wins (having a higher STR score in a STR contest where the rolls are tied means you win. If you rolled 4 and added 3 from STR and the other guy rolled a 7 and added nothing, you win). If _that’s_ a tie, either treat it as a tie in game, or if that makes no sense, do the contest again. 
Contests are good for directly comparing the active efforts of two characters. Grappling is a contest.

### A Simple Example of a "Check"

You might decide that you want to jump a large chasm, your GM tells you to roll agility (AGI), so you roll 2d6 and add your AGI score. The GM knows the DC which in this example might be 8. If you pass the DC you succeed. If you don't, you fail, and the GM decides how that's resolved.  
You will almost never know the DC of a check before you try it, and you might not even know afterwards if the GM decides not to tell you. However, you should be able to get a good idea of a DC by the GMs description of the situation or by asking questions. If the GM describes the chasm as nearly impossible to jump over, you can be sure you're looking at a DC above 10, probably around 12. If the GM says the gap is pretty small, barely worth worrying about, you can guess it's probably a DC around 3 or 4.


### Action Points (AP), Moving, and the AP Tracker

Action Points (AP) are the resource you use to do anything and everything. You get 3 AP per round. Rounds, or the time it takes for everyone to act, take about 6 seconds. All actions have two parts, the AP cost to perform the action, and the number of turns you have to wait to get that AP back. X AP cost, return the AP in Y turns, or X in Y, notated as “(XnY)”. Most basic actions (including moving) are (1n1). You spend 1 AP to do it and you get that AP back at the beginning of your next turn. There are some exhausting or difficult spells that might have a cost like (2n3 or 3n1). If you see "or", you can choose either cost.  

You can move a number of spaces equal to your speed (typically 20 feet or 4 spaces) for every move action you take. Move actions cost (1n1). You could, for example, move for (1n1) do something that costs (1n2) then move for (1n1) again. If you spend your whole turn moving, that’s just 3 move actions, moving you 20\*3 or 60 feet (or 4*3 spaces). If you have enough AP to do something, you can do it.

Doing basic tasks like pulling a lever or moving an object costs (1n1). Minor tasks like speaking or dropping something are free actions, you can do a “reasonable” amount of free actions during your turn, up to GM discretion.

You are always *conceptually* spending AP to do things, but you only really have to track it when in initiative. (unless, for example, you have some status effect that lowers your max AP, thus making you able to take fewer move actions per turn, making you move slower than the rest of your party. This might be relevant if, for example, you’re trying to travel quickly to get away from something, but you’re not in combat). You can track your AP by using the AP tracker on the top of your character sheet, it looks like four boxes numbered 0-3.

Put some objects, tokens, or dice on the tracker at “0”, these represent your AP. You can spend any AP that is at 0.  

#### Moves that have Multiple Costs
If you see a move that looks like “(1n1)->(2n1)->(3n1)” then the first time you do that action on your turn you pay the first cost, the second time you pay the second cost, the third time you pay the third. You’ll notice there is no fourth cost. If you want to use the move again, you would just pay the last listed cost again, (3n1). 

**All attacks with all weapons count as the “same” sort of move for the purpose of determining the cost of your next attack.**
<!-- hey, maybe this shouldnt be true! i dont remember why it was important that it should be! i see why different attacks with the same weapon should not count as the same.. but why not attacks with different weapons? shouldnt those be different? anyway... one thing i dont love is that you do have to just remember how many times youve attacked in a turn... of course there could be another tracker, but no, thats stupid, one tracker is more than enough. -->

#### An example of tracking AP with the AP tracker

You start with 3 AP at the "0" space, so you have 3 AP to spend. You perform an action that is (2n2) so you move 2 tokens to the “2” square. You then “move”, which is (1n1), so you move 1 token from the "0" square to the “1” square. You're out of AP. At the start of the next round you move all of the tokens one cell to the left, so you have 1 token at “0” and 2 tokens at “1”. That means you can spend 1 AP this turn. You decide to move, which is (1n1), so you move 1 AP to cell “1”. Now you have all 3 tokens on the “1” cell. At the start of the next round, all tokens move one step down, so they all go to the “0” cell and you have 3 AP to spend again.

Using this tracker you should never have to remember how many AP you’re supposed to have or when you get them back, you just spend AP that is at “0” and move all tokens to the left at the start of the round.   


#### Attacking using AP

Let's say you have a longsword in one hand and you're fighting a guy with chainmail armor. The longsword has a Basic Attack AP cost:“(1n1)->(2n1)" and has a slashing (S) [swinging: neutral] move that does a d8 in damage as well as a piercing (P) [thrusting] move that does a d6 of damage. You slash first, paying (1n1). This does poorly against the opponents chain mail, so you try to the (P) piercing attack for (2n1) (the second AP cost, because this is the second time you've used an attack this turn) and this does better. You don't have enough AP to do a third attack, but if you did it would cost (2n1).

## Initiative Rules

The ruleset that follows has not been tested much and will likely see some changes. This is the current state.

A character's initiative is their AGI + or - any relevant bonuses or penalties.

The initiative scores of the players should always be public on some form of initiative tracker. As other characters reveal their initiative, they should be added to the tracker (and removed when they are no longer relevant). 

Every round is divided into two phases, the Beginning Phase and the Main Phase.

### Beginning Phase - "Beginning of the Round"

This is mostly referred to as the "beginning of the round" by skills and effects. The whole table does not need to be synced up for this, everyone can just manage their own character. There are three sub-phases to the beginning of the round. Most of the time this will not matter and you won't have to think about it, but if there are multiple things that happen "at the beginning of the round" this describes the order in which they happen.  
If there are multiple things that happen in the same sub-phase, you get to choose the order in which they happen.

#### 1. Effect Activation

Any *already active* effects that trigger "at the beginning of a round" happen now. They happen before anything else in the round does. This includes taking damage from [poison] or [bleed] or gaining health from [heal]. If you have an effect active that causes you to do some sort of rolls or contests, do those now.

#### 2. Status Management

At this point any effect or mechanic that involves rounds passing is accounted for. AP is regained a, a point of [poison] is removed, a point of [heal] is removed, anything that would end at the "beginning" of this round ends *now*.

#### 3. Moves and Skills

Some moves and skills get can be used "at the beginning of the round". These can only be used *after* effects happen and then are managed and AP is regained.

#### An example

Say you have 1 HP, 1 [poison], and an ability that causes [poison] to heal you instead of harm you which can be used at the beginning of the round. The order in this case matters, do you reduce [poison] by 1 first and avoid the damage? Can you use the ability before the damage from [poison] kicks in? No and no. First damage happens, then you remove the [poison], and then you can use an ability (though in this hypothetical you would already be at 0 HP).  
Let's say that instead of having an ability that lets you heal from [poison], you already have an effect active that makes poison heal you. In this case you would heal 1 HP from the poison damage and then remove the poison.  
An even more complex example: let's say that in addition to the passive healing [poison] effect you have an item that activates when you would take [poison] damage and nullifies the damage. In this case you have two effects that happen in the same phase, so do you heal from the poison or ignore the poison? In the case of this sort of tie, you get to choose. Presumably you would choose to heal which means the item would not be triggered because its no longer the case that you would otherwise take poison damage.

### Main Phase

This is where basically everything in the round happens.

If you want to do something, you say what you want to do. If multiple characters want to do something at the same time, the order they take actions in is based on their initiative. If there is a tie of two or more characters, the character that went most recently goes last, the character that went most recently before them goes second to last, etc. If several characters haven't gone at all, roll a contest between them.

### Interrupting and [interrupt]

If you want to directly interfere with another character's action roll an initiative contest. Spend (1n1) when you attempt the interrupt unless the skill or move has [interrupt].
<!-- actually, this seems kind of broken because youll try and interrupt with an interrupt everytime you get the chance?? -->
If you win you act first. The opponent can still take their action afterwards. You cannot attempt to interrupt the same action twice.

### Coordinating Actions around the Table  

Say Alice has 3 initiative, Bob has 2, and both try to do something at the start of every round. Alice is faster than Bob and will always end up going before ("overruling") Bob, but some time is wasted establishing that *every single round*. We want to minimize these sorts of predictable action-taking collisions.  
<!-- TODO: wile made a good case for the y=1 implicitly in XnY, so probably change stuff to fit, or leave this note as a reminder that that is an option! -->

<!-- This method of turn coordination was made to capture three ideas.
- Characters with higher initiative will always overrule characters with lower initiative, so characters with higher initiative should be given an opportunity to go before characters with lower initiative.
- Characters with lower initiatives can't be blocked from taking any action because they can always attempt to interrupt a character with higher initiative.
- Characters with higher initiative can still take actions after characters with lower initiatives have started taking actions. -->

The DM announces the highest level of initiative present according to the initiative tracker and gives those characters a chance to take actions. Once those characters have had a chance to act, the DM announces the next level of initiative and so on down the list. At the end of the list the DM should have a "last call" for actions and then announce the start of a new round.

Slower characters can attempt to interrupt faster characters at any time. Characters can keep acting as long as they have the AP to do so, even if they already had a chance to take actions.  

### Using Only the Amount of Coordination that You Need

In the section above, all of the rules for initiative and when-exactly-effects-happen were explained, but often you won't need to actively use all of these rules. It will probably be useful to make every step very explicit for beginners, but once players have a handle on how this system works, combat should be able to function without every step being made explicit, rules for determining who goes first can just be invoked when there is some conflict. You can choose to invoke rules for "phases" only when there are many effects that seem to happen at the same time and there is some reason why the order matters.

As an example, in a fight between two people the DM doesn't need to be announcing the current highest level of initiative, there are at most two levels! The combatants will quickly figure out who is faster. The DM *will* often have to determine when the new round starts in combat, but this isn't always true either. If there are only two combatants and they're out of AP they can just agree to start a new round. Of course, the DM could still overrule them and describe something external happening that neither expected before they get a chance to start a new round.

## AP Shenanigans: Temp AP, Losing AP, Gaining AP, the "Wait" skill

Temp AP goes right into the “0” cell where you can spend it. It only lasts until the beginning of the next round.

Some moves might make you lose an AP, this means you take the furthest token from 0 off the tracker.  
Some moves and conditions might make you gain an AP. Whenever you gain AP it goes to 0 where you can spend it. If you have less than 3 AP, you just add an AP at 0. If you have 3 AP on the tracker and a move makes you “gain” AP, you don’t get an extra one, you just move one AP that is furthest from 0 to 0. So if you have one token on “2” and two tokens on 3 and something causes you to “gain” an AP, move an AP from square 3 to 0.  

You can always “wait” for a round. If you “wait”, you can do nothing else during that round. Gain 1 AP at the beginning of the next round. if you have no AP to spend, you might as well “wait”.

## Double 1s, Double 6s

Double 1s are critical failures, they are context dependent. If you roll double 1s in combat, your GM might give you a couple different failures you can choose from, or if you are playing a more cinematic game you might improvise a failure. The GM could also just tell you what you do, maybe you are [vulnerable] briefly. If you roll double 6s in combat, roll double damage dice and get 1 Temp AP. If you roll double 6s outside of combat, you perform whatever action you were trying to perform as well as you possibly could, this is very context dependent.

## Weapon Rules

A weapon has a Speed, a To-Hit, and a set of basic attacks. The speed is how much AP it costs to do attacks with the weapon. The "To-Hit" is what you add to the check you perform when attempting to hit an enemy. This looks like "To-Hit: DEX" or "To-Hit: STR + AGI" or similar. To-Hit and Speed is shared for all attacks a weapon has (unless otherwise stated), but each attack a weapon has might have different damage, different damage types, different effects, or a different tag. The three basic damage types are (B)ludgeoning, (P)iercing, and (S)lashing.

Let's go through an example. Let's say the speed of the weapon is (2n1) and the To-Hit is +STR, it has one attack: "1d6+STR (B) [swinging: leading]". When attacking with this weapon, you move 2 AP tokens to the 1 space and roll 2d6+STR for your To-Hit check. If that beats your opponents Defense, roll damage (1d6+STR) and tell the GM that the damage type is (B)ludgeoning in case they need to make an adjustment for armor. 

Some skills require attacks with certain tags like [swinging: leading] or they might only effect certain attack types. Some weapons will have several attacks with different damage types, different damage numbers, different tags, different effects etc. This captures how a rapier is better for piercing than slashing, or a giant curved greatsword would be better at slashing than thrusting but both can be used for both purposes. A weapon like a rondel dagger, which is a long dagger with a narrow but thick blade, might be able to ignore some armor and do pretty good damage with a piercing attack, but it will be a good deal worse at slashing than a kukri. If you're in the jungle being attacked by big furry creatures, take a kukri. If you're assassinating knights, take a rondel dagger.

### Attack Tags in a More Detail

The two major tag types are [thrusting] and [swinging]. [swinging] has three sub-types. Those three types are [swinging: following], [swinging: neutral], [swinging: leading]. The subtype refers roughly to "the position of the striking surface relative to the hand in a given swing" but this is much easier to understand through some examples.

***[swinging: leading]*** is the easiest to understand. It's a swinging attack where the striking head is ahead of the weapon as in a warpick, an axe, or a hammer. The blade of the axe projects in front of your hand, it is "leading" the swing. Attacks with this sort of weapon are typically slower and deal more damage. A (S) [swinging: leading] attack would be like swinging a meat cleaver or an axe, the cut from a [swinging: leading] (S) attack will be relatively short but deep. A [swinging: leading] (B) is like an attack with a hammer, a [swinging: leading] (P) attack is like an attacks with a warpick. You can expect to see attacks with any of the three damage types with this tag.

***[swinging: neutral]*** is the middleground, attacks of this type will be faster than [swinging: leading] but do less damage. This is where the striking surface is in line with the hand as in a longsword, a quarter staff, or some sickles. You'll see (S) and (B) attacks of this type most often. In general (P) damage is less common for [swinging: neutral] attacks. Of course, (P) damage is *extremely* common for [thrusting] attacks.

***[swinging: following]*** is the oddest of the bunch. Attacks of this sort tend to be the fastest and weakest, relying on skills, conditions, or just an overwhelming flurry of attacks for damage. The central example of [swinging: following] is a curved dueling sabre. These attacks will nearly always be (S). You can construct weapons that have (P) [swinging: following] attacks, but they don't make a huge amount of sense. What would a (B) [swinging: following] attack be? Maybe hitting a guy with the scabbard for your saber, again, not very common. Magic abilities, skills, and exotic weapons can flesh out this category but there aren't many historical examples of [swinging: following] besides curved swords and some glaives.

***[thrusting]*** includes thrusts with a spear, sword, or dagger. The vast majority of thrusting attacks have the (P) damage type.

These tags describe something physical about the weapon, "striking surface relative to swing" or just the motion as in the [thrusting] tag, but more importantly the tags describe the way the weapon is *used* for the attack. They describe what sort of attack the attack is, so a slow-ish sword with a slightly curved blade might still be counted as [swinging: neutral] if it makes more sense for skills, etc. If you want more info about these distinctions and how weapons are made, refer to the [Weapon Creation doc](weapon_creation.md).



#### An Aside on Notation

Unfortunately, [swinging: leading] ends up taking about as much space as the rest of the attack and it's one of the less important elements of the attack! However [S: L], [S: N] is ugly and incomprehensible. When making cards or other reference material we replace these tags with glyps. ▲ for [thrusting], ▷▷▶ for [swinging: leading], ▶▷▷for [swinging: following] etc. These are rendered a little more nicely in pdf reference material. The glyphs should be pretty intuitive, the filled triangle indicates the striking head relative to the swing (or the subjective "aggressiveness" of the attack).

<!-- probably... probably this section should go somewhere else... maybe its helpful in rules? dont know -->
<!-- #### Why use this system?

Say you have a character who gets some bonus with axes and hammers, this expresses that you're a strong character who does overwhelming strikes with heavy STR-based weapons, you're not some sort of saber duelist. Do you get advantage with a warhammer? What if you're trying to use the pick side of a warhammer? Using the pick is the same motion as using the hammer, and its the same weapon, so shouldn't you get the same bonus? Doesn't it follow, then, that you should get the same bonus with warpicks? What if you find a sword with a forward curving blade so dramatic that the sword is basically just an axe with a hilt? Shouldn't you get your axe bonus with that? This is without getting into the migraine that is "pole weapons" (poleaxe, bill, partizan, halberd, bardiche, glaive, pike...). This system allows us to neatly avoid the question of what weapon or what attack is axe-like or spear-like in some context or another and it allows us to avoid having a rigid taxonomy of weapons all while still engaging with the different advantages or features of different weapons. It also lets us create all sorts of goofy fantasy weapons without having to quickly change the taxonomy, all we do is describe how the fantasy weapon is built and the attacks you do with it and the weapon will work with existing skills and characters.

In this system we just describe the weapon itself and some basic qualities about the attack. A particular poleaxe is just a [two-handed] [shafted] weapon with [reach: 1-3] a particular Speed and To-Hit, and a couple moves. Maybe it has an axe head, a pick, and a spear. So it has a (P) [thrusting] attack, an (S) [swinging: leading] and a (P) [swinging: leading]. Maybe you have skills that work very well with axes, but you expect that this sort of multi-use weapon with a lot of reach might come in handy for hunting down a specific type of monster. You might choose then to take this pole-weapon with a relatively better (S) [swinging: leading] attack so you can leverage the axe-related skills you already have. This also helps us express skill transfer from different types of weapons. Your character is very good at two-handed axes and you find a one-handed axe that is really useful in some situations, maybe it applies some particular status effect. There's going to be a lot of skill overlap, you just won't get anything that requires [two-handed]. That's all there is to it. -->
### Weapon Switching

Dropping a weapon is a free action. Putting a second (open) hand on a one-handed weapon is a free action, same for removing a hand from a weapon or any such minor adjustment, if in doubt TTYDM.
Drawing a weapon is (1n1). Picking a weapon up off the ground is (1n1) and you're [vulnerable] while you're doing it, you can be interrupted with an attack while you duck down to grab a weapon. Putting a weapon away is (1n1).
An example: You want to drop your [two-handed] greatsword, pick up a handaxe from the ground, and draw your dagger. Dropping the sword is free, picking up the handaxe is (1n1), as is picking up the dagger. You've spent 2 AP, and you were [vulnerable] for a bit.  

### Being Below a Weapon’s Requirements

If you’re below a weapon’s requirements, you get no score based damage scaling (+SCORE) when using that weapon. Your max + To-Hit is 0 with that weapon. For every point you are below a score requirement, drop a damage die. If there is only one damage die left, make it one die smaller. If you get below d4 you cannot wield the weapon at all. Weapons without specific requirements can be treated as having a requirement for -1 of whatever score is used to hit. 

### Two-handing a [one-handed] weapon, One-handing a [two-handed] weapon

If you’re 2 STR above the requirements for a [two-handed] weapon, you can effectively wield it with one hand. If you use two hands on a [one-handed] weapon, raise your effective STR with the weapon by 2. 

### Throwing a spear or a dagger without a specific [thrown] move

For every point you are below requirements for the weapon, reduce range by 2. 
Throwing a spear or dagger is (2n1), uses PERCEPTION and AGI to hit, has no damage scaling, 3 + AGI spaces for range. Drop a damage die from an attack to determine damage and damage type, if there is only one damage die, lower it. 

## Resting and Healing

For every 6 Max HP your character has, they get one recovery die. The recovery die is a d6. At every long rest (a rest of 8 or more hours), you regain all of your recovery dice. For every hour you rest, you can choose to use one recovery die, rolling it and adding it to your health.

## Death and Dying

### Dying Immediately or Being Stabilized

If you are reduced to -(Max HP/2) you die immediately.  

If your HP is above 0, you are stabilized. If you are stabilized but you haven't reached 6 HP, rest (rolling recovery dice) until you reach 6 HP. If you're brought back to 6 HP or more, regain consciousness.

#### Being Reduced to 0 HP, Being "Downed"

You can end up with negative HP. You can stabilize with negative HP, but you have to reach 6 HP from either healing rest before you regain consciousness.

When a player is reduced to 0 but not killed, they are "down" and they are unconscious. If they are not stabilized, they are unable to take any sort of action besides rolling death checks. They are [vulnerable].

When a player is downed the DM sets a death DC by rolling 2d6 with no modifiers. The DM does not tell the player what their DC is.  

On the turn a player is downed and on every subsequent turn, the player rolls a death check and tells the DM their roll. If their roll matches or passes the DC it's a success. If the roll is below the DC, it's a failure. If the roll is a failure, the DM notes by how much the roll failed, DC - roll. This difference will be used to determine the consequence of the failure using the consequence table. Don't make any extra rolls to resolve consequences at this point as other characters might use medicine to improve the outcome, skills might be triggered, etc. Consequences are only resolved if/when the character survives.

3 successes means the character stabilizes at their current HP. 3 failures means they die.

Once they either hit 3 successes or 3 failures, the DM tells them to stop rolling. They are not told whether they died or not or what consequences they might have. They only find out once someone goes to check on their character. 

If you're hit while you're down, take the damage and add a failed death check.

### Consequence Tables

| Failure     | Consequence                           |
| ----------- | ------------------------------------- |
| -1          | [weak] (1 Hour)                       |
| -2          | [weak] (8 Hours)                      |
| -3          | Scars, [frail] (8 Hours),             |
| -4          | Scars, [frail] (1 Day), Lower 1 Stat  |
| -5          | Scars, [frail] (2 Days), Lower 1 Stat |
| -6, -7      | Scars, Lame                           |
| -8, -9, -10 | Lose a Limb                           |

#### Consequences

***[weak]***

-1 STR, -1 CON  
This is and [frail] should have more involved penalties, rather than just stats, I would think.

***[frail]***

-1 STR, -2 CON, -1 AGI

***Scars***

Scars are completely cosmetic and up to DM discretion. The scar might be from the blow that downed the character or they might be from some other large blow received in the same fight. 

***Lower a Stat***

Lower a stat by 1 by rolling a d4 using the following table:

| Stat | Roll |
| ---- | ---- |
| STR  | 1    |
| AGI  | 2    |
| DEX  | 3    |
| CON  | 4    |

***Lame***

Take your first move action as normal. Every subsequent move action is slower by 1 space.

***Lose a Limb***

Determine Limb loss by rolling on the following table:

| Stat | Roll |
| ---- | ---- |
| 1    | Arm  |
| 2    | Leg  |
| 3    | Eye  |
| 4    | Ear  |

## SOCIAL Rolls

Now for the least important part of playing a TTRPG, interacting with other people.

This system is designed to allow a characters skills and stats to *augment* their social actions. The emphasis is not on getting good rolls, but on saying or doing the right thing. Rolls are used to express a particular character's social talents, but they don't replace the content of what the character does or doesn't do.
A DM can use a check to determine success if they really do not know whether a given social action should or shouldn't work on some character, and neither a success nor failure would be especially interesting. Even in this case, difficulty should be determined contextually. 
Grading numerical difficulty for a social interaction is generally difficult. A DM cannot prepare beforehand for the things a player will ask another character so DCs have to be set on the fly. Sometimes they are set incorrectly or something breaks. In this case, ignore the system/roll and do whatever is the most sensible/interesting/funny.

Social skills are divided roughly into two sets: communicative skills and perceptive skills.
communicative skills include persuasion, deception, and performance. Perceptive skills include sensing motives, detecting deceit, and gaining insight into another character's emotional state.

### Communicative Skills, Bias, and Reputation

| Score | Name              | Description                                                                                                                                                                                                                                                             |
| ----- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -6    | Reviled           | You are vilified and reviled. Your name, face, and terrible actions are known. A group will send paid assassins and soldiers after you. An individual will go to great lengths and take on great risk and personal cost in order to do as much harm as possible to you. |
| -5    | Despised          | You will be attacked on sight. There is probably a bounty on your head.                                                                                                                                                                                                 |
| -4    | Hated             | You will be attacked. If someone is attacking you, they will be given help.                                                                                                                                                                                             |
| -3    | Loathed           | You are a pariah.  A group might throw you in jail, an individual might do you harm opportunistically. People will actively try to get rid of you.                                                                                                                      |
| -2    | Strongly Disliked | People do not want to talk or trade. They want you to go away.                                                                                                                                                                                                          |
| -1    | Disliked          | People will give you bad deals in trade. They do not particularly want to talk to you. They do not want to barter.                                                                                                                                                      |
| 0     | Neutral           | People don't think much of you one way or another. They have the time to talk.                                                                                                                                                                                          |
| 1     | Liked             | You are liked. People want to talk and barter.                                                                                                                                                                                                                          |
| 2     | Well-Liked        | You are liked quite a bit. People are willing to help you out. They want to see you do well.                                                                                                                                                                            |
| 3     | Trusted           | You are trusted and valued. People will go out of their way to help you.                                                                                                                                                                                                |
| 4     | Admired           | You are seen as an example to be followed, people will give your words great weight. They will go out of their way to help you out.                                                                                                                                     |
| 5     | Loved             | You are set apart from others, distinctly trustworthy, valued, and important.                                                                                                                                                                                           |
| 6     | Revered           | You are seen as almost otherwordly, beyond reproach.                                                                                                                                                                                                                    |

The framework for setting a DC for a given social roll and the framework for reputation management are the same and they can be used in combination. Both systems share the same table of scores with rough characterizations of what each score "feels" like.

The scores range from -6 ("Reviled") to +6 ("Revered"). These scores can be used by a DM to easily keep track of relationships and attitudes. They are also mechanical modifiers. If a character is at -2 ("Strongly Disliked") with some group or individual, you treat their social roll as lowered by 2 (or you can just raise the DC by 2).  

You can use these scores to set a sort of "default" attitude or bias for NPCs. The kindly innkeeper in a small peaceful town might treat every new person at around +2 ("Well-Liked"). The sneering guards in front of a keep might treat everyone at -2 ("Strongly Disliked"). Another traveler on the road just trying to get to where they're going might be at -1 ("Disliked") just because they really don't want to stop and chat. The same traveler might, if you help them out, switch to +1 ("Liked").  

The purpose of social rolls is to be able to, in a given interaction, change the way people perceive you or interact with you. Remember that rolling checks with the SOCIAL score does not replace the content of what a character does but just augments it. If a player passes the DC, treat their interaction as happening at 1 point higher than it would be otherwise. If the player exceeds the DC by more than 3, you can treat the interaction as being at 2 points higher than it would be otherwise.  

Say a player character is in a town in which they are at -3 ("Loathed"). Typically, this would mean that they are treated as a pariah, people are unwilling to talk to them and will actively attempt to get rid of them, they might be thrown in jail on made up charges. Guards will not come to their aid. If they are very charismatic they may be able to walk into a shop, attempt to talk the owner into selling them something and succeed by 4 on a roll. The shop owner thinks that the player character really doesn't seem quite so bad, he thinks that maybe he is misremembering something or getting this person confused with someone else. He is still wary, however. He still treats the character as -1 or "Disliked", he will tend not to want to barter, and he'll want to get through the interaction quickly. Similarly, a guard treating everyone at -2 might be persuaded to relax a bit and just talk to the player character on neutral terms (-2 -> 0).  

Of course, there are plenty of things besides social interaction that might raise or lower someone's opinion of you, and if the content of what a player character said is something that another character would naturally agree with or go along with, then no roll is necessary. If a roll is performed you can treat the NPC as having already shifted their bias.  

Remember that the good will from one positive social interaction does not last forever. Actions will tend to have more of an effect on someone for longer than words. If you just stabbed someone, you are not going to be able to smooth that over with your witty charm, you do not even get to roll. 

The table with specific characterizations is useful, but it can be boiled down to some rules of thumb. 0 is neutral. From +1 to +3 the character is favored. Persuasion, information gathering, and bartering will be easier. People give you the benefit of the doubt. From +3 to +6 people will go out of their way to help you, they will likely come to your aid in combat or follow you into combat. From -1 to -3 people dislike you and generally do not want to have anything to do with you. -4 to -6 is when you start seeing a lot of unprovoked violence.

This framework is largely for the benefit of the DM, to allow them to easily keep track of attitudes and relationships and to quickly create DCs and resolve rolls in a way that rewards the skills of the player as well as the skills of the character. 

There are several different ways a DM can deal with this system in game. The system can be player-facing, that is to say, you could tell your players their numerical reputation among different groups or numerical values for the attitudes of various characters (along with descriptions). I do not recommend this. You could gate numerical information behind something like a good insight roll. This is fine, but even in this case you should lean on qualitative descriptions of how some character treats a player character. You can also keep the entire system completely to yourself, as a useful tool for the DM to structure descriptions and interactions. In this approach players do not get to actually know numerical values and you never have to reveal or justify movements in numerical values. This is probably your best bet. In this case the framework is still useful for figuring out how much the charisma of the character has helped the efforts of the player.

### Social Perception

"Social perception" is used here to refer to skills that allow you to roll to sense motives, detect deceit, and gain insight into another character's emotional state. It's important here to establish when *exactly* these skills are used and checks are made.

When a player asks a question that would fall under "social perception" about another character, they should first be given a superficial description of the character and their apparent emotional state. If the character in question seems to be at ease, the DM should just say so. This is true even if the character in question is only pretending to be at ease, but plans to attack or betray the player's character. It does not take a roll or a question from the player for them to be told that someone yelling and brandishing a knife is probably somewhat unhappy. The rules and skills for social perception are not meant to cover the superficial. These rules are for attempts to read another character.

Social perception rolls are very similar to other character conflicts, they can be either a check or a contest.

### Social Checks

When the roll is a check, the DC will likely be a default DC of 6 + SOCIAL (and/or relevant skills). If you are trying to read a character who is is lying the DC will be set by their initial attempt to lie, which will have been a check + SOCIAL (and/or relevant skills) against your passive social perception. If they attempt to lie and fail this check, then whatever they said will be described as highly suspicious or likely a lie. If they succeed in their initial check, but you pass their DC when you attempt to read them, you will notice that something seems wrong, or suspicious, or you'll notice strange nervous habits.

Social perception rolls are almost always checks. If you are lying to someone, you perform a check. If they are trying to figure out if you are lying, they perform a check. If someone is trying to convince you of something and you think they might be lying, you perform a check.

If every lie was a contest, the fact that you had a contest to begin with would tip you off to the lie.

#### Social Check Resolution

In the case of a tie, resolution is the same as any other check. Defender wins. Otherwise there are four possible outcomes. 

***If you pass the check more than 3, Complete Success:***

You read them like an open book. You get a full answer to whatever question you were asking, or as full an answer as you could get from watching someone. They crumble at your gaze. Maybe they are so caught off guard that they fumble and make an embarrassing mistake, mentioning something they should not have.

***If you pass the check by 3 or less, Moderate Success:***

You get some insight into the question you were asking. If you are trying to see if someone is lying, you'll know that they're certainly not telling the whole truth, that they are actively misleading you. If you're trying to get insight into someone's emotional state, you get a good idea of how they are feeling. You might be able to tell that someone is distressed and trying to hide it. This is a pretty good read of someone, and they do not know that you know anything.

***If you fail the check by 3 or less, Moderate Failure:***

You have no answer to your question at all and the person you were attempting to read knows the vague shape of the question you asked or that you have a question at all. If you were trying to figure out if someone was lying about a specific claim they might know that you don't trust them or that you suspect them in some way. Otherwise you might just be staring and it's a little weird.

***If you fail the check by more than 3, Catastrophic Failure:***

God have mercy on your soul. You completely give yourself away, your interests and your question are written all over your face. Spaghetti is falling out of your pockets. If you are trying to catch a lie, not only is it clear what exactly you think is being lied about, it's clear that you have *no* idea if they're lying.

Some examples: maybe you scoffed at a specific claim, maybe you blurt out "But the stone of Macguffin!" at exactly the wrong time. Your face is probably red.

### Contests

Contests are far rarer than checks. Social perception contests happen in contexts where it is understood that both parties are trying to advance their own interests and, if not outright lying, being very selective with the truth. Some examples of this would be a tense negotiation, an official dinner of ambassadors whose states are on the brink of war, a game of poker, spies meeting to trade secrets while not revealing their true intentions. In these cases checks would be happening simultaneously anyway, and the information that someone might doubt what you are saying or that they might not be telling the whole truth wouldn't be very meaningful.

Contest Resolution is just about the same as check resolution. The difference between the rolls of the two characters determines which character succeeds and which fails, and to what degree. This success and failure are captured by the same event. For example one character might give away information they shouldn't have, which captures both the success of one character and the failure of another.

Ties are just ties, a staredown, a tense silence. If your group prefers, ties can be resolved in the normal way for a contest: win goes to the higher modifier, if that's a tie, it's a tie in game, if that makes no sense, do it again.

## Odds and Ends

Some rules that did not fit nicely into a cohesive category.

### Stealth

Stealth is an AGI check (+STEALTH if you have it) against the defender’s passive perception. It’s a check against a passive score, and that is always 6 + SCORE.

### Grappling

Entering grappling takes (2n1), it's an attack + AGI To-Hit followed by a STR contest. If the part entering the grapple wins, both parties are [grappling] but only the defender is [vulnerable]. Defender can spend (2n1) to trigger another STR contest to try and break free. Defender can do nothing else.

#### Taking a Hostage

Same as above, but the attacker rolls one fewer die on the initial grapple check but can attack the defender in the grapple provided they have a [range: 0] weapon.

### Fall Damage

Fall damage is a d6 for every 6 spaces up to 25d6.

### Taking 10

You can take 10 minutes to work at something (that you can try repeatedly at where there is no cost for failure) to treat your check as a 10 + relevant modifiers.

## Encumbrance and Rations

Encumbrance is measured in encs. Encs are a combined measure of weight and unwieldiness. Most weapons are 1 enc. A [heavy] weapon is 2 encs. A days worth of food and water is 1. 3 small items, like a book, a dagger, and some bandages together take 1 enc. Negligible items like quills and needles don't take up any encs, unless the DM determines you are carrying "way too many".  

Players must describe and account for how they are moving their things. They take "reasonable" penalties for impractical methods. If they tie a bunch of swords together and then hang that off of their neck, they will have a hard time stealthing. If they fall over while wearing the described necklace of dangerous wind chimes they're going to have a bad time.

### Storage Spaces, The "Personal" Space and Bags

"Storage space" is used to broadly refer to any place you can put things. Each storage space you have can be thought of as a source of a max encumbrance and a source of an [encumbered] threshold. Most of the time you will have two storage spaces: 

- Your "personal" space, which includes anything you're carrying that isn't itself a storage space. Most often this would be your weapons and armor. 

- Your bag. This is most often some kind of backpack.

You have a personal [encumbered] threshold. This is used for the weapons and armor you are carrying without a bag.
Your personal [encumbered] threshold is 3 + STR. Your personal max encumbrance is 6 + STR encs.

The primary use of a bag is to give you more [encumbered] thresholds and to change your maximum encumbrance.

Bags have varying [encumbered] thresholds and max encumbrances. If a bag does not say it has an [encumbrance] threshold, then it never makes you [encumbered]. This is common for small bags that don't have a max encumbrance high enough to be able to encumber, or bags that are designed not to encumber.

Removing a bag is (2n1).

Searching a bag is (2n1).

### The [encumbered] Threshold and Maximum Encumbrance

If you are past any encumbrance threshold in any storage space, you are [encumbered], you have the [encumbered] status.

The [encumbered] status lowers your move speed by 1. Your to-hit DC, the DC that enemy attacks roll against, is lowered by 3. Additionally, take a -1 to all AGI checks.

If you aren't wearing heavy armor but you're carrying enough in your bag to pass the bag's encumbrance threshold, you are [encumbered]. Less obviously, this also means that if you are past your personal encumbrance threshold (most likely from carrying weapons and wearing armor that are too heavy for you to move freely with) but you are not past your [encumbered] threshold for your bag, you are still [encumbered].  

In order to avoid passing an [encumbered] threshold you likely want to spread the weight around multiple storage spaces, keeping under all of their [encumbered] thresholds, or you might want to just put everything in a bag so that in a fight you can take it off quickly and not be [encumbered].

You cannot carry more encs in total than your single highest max encumbrance score. This does not mean that having one storage space where you can carry 8 encs means that you must be able to carry 8 encs in every storage space, it just means that all together you can't carry more than 8 encs.

Unless otherwise specified, you can only use one bag at a time. If some mechanic allows you to use multiple bags, you cannot carry in total more than your highest max encumbrance from a single source, though you can move encs around to try to avoid the [encumbered] status effect.

Your [encumbered] threshold and your maximum encumbrance can be affected by status effects or skills, but most often they will be affected by the bag you are using. 