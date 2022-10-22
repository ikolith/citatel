import os
import cli as g
import py_utils.text_utils as t
import argparse
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import asyncio


entities = t.get_entities(os.path.join("docs", "_data", "entities"))
load_dotenv()
TOKEN = os.getenv("TOKEN")
GUILD = os.getenv("GUILD")
bot = commands.Bot(command_prefix="$", intents=discord.Intents.all(), help_command=None)


class abot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=GUILD))
            self.synced = True
        print(f"loggered as {self.user}.")


bot = abot()
tree = app_commands.CommandTree(bot)


async def post_text(text: str, interaction: discord.Interaction) -> None:
    if len(text) < 2000:
        await interaction.response.send_message(text)
    else:
        with open(
            os.path.join("output", "bot_output", "long_message.txt"), mode="w"
        ) as f:
            f.write(text)
        await interaction.response.send_message(
            file=discord.File(
                fp=os.path.join("output", "bot_output", "long_message.txt")
            )
        )


@tree.command(
    name="curly",
    description="Pass in some parsable curly-statement, curly optional. Ex. {sword}, {2d6}, or {2d6 sword}",
    guild=discord.Object(id=GUILD),
)
async def self(
    interaction: discord.Interaction,
    curly: str,
    expand_entities: bool = False,
    roll_dice: bool = False,
) -> None:

    await post_text(
        g.cli_single_curly_parser(curly, entities, expand_entities, roll_dice),
        interaction,
    )


@tree.command(
    name="enlist",
    description="Make a named entity list for /cards to use.",
    guild=discord.Object(id=GUILD),
)
async def self(
    interaction: discord.Interaction,
    filter_tags_include: str = "",
    filter_tags_exclude: str = "",
    list_name: str = "enlist",
) -> None:
    g.enlist(
        entities,
        filter_tags_include,
        filter_tags_exclude,
        os.path.join("output", "bot_output", (list_name + ".txt")),
    )
    await interaction.response.send_message(":white_check_mark:")


@tree.command(
    name="cards",
    description="Make cards, requires a list of entities entered manually or from /enlist.",
    guild=discord.Object(id=GUILD),
)
async def self(
    interaction: discord.Interaction,
    card_type: str = "poker",
    cards: str = "",
    list_name: str = "",
) -> None:
    if list_name == "e":
        list_name = "enlist"
    list_name = (
        os.path.join("output", "bot_output", (list_name + ".txt")) if list_name else ""
    )
    g.command_generate_cards(
        card_type,
        cards,
        list_name,
        os.path.join("output", "bot_output", "cards"),
    )
    await interaction.response.send_message(
        file=discord.File(fp=os.path.join("output", "bot_output", "cards.pdf"))
    )


@tree.command(
    name="help",
    description="What that bot doin?",
    guild=discord.Object(id=GUILD),
)
async def self(
    interaction: discord.Interaction,
) -> None:

    await interaction.response.send_message(
        file=discord.File(fp=os.path.join("py_utils", "help.txt"))
    )


bot.run(TOKEN)
