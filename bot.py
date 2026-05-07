import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SelectOption

# -----------------------------
# INTENTS + BOT SETUP
# -----------------------------
intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


# -----------------------------
# IMAGE URL DATABASE
# -----------------------------
IMAGE_URLS = {
    "bank": {
        "basement": "https://your-url.com/bank_basement.png",
        "1f": "https://your-url.com/bank_1f.png",
        "2f": "https://your-url.com/bank_2f.png",
        "roof": "https://your-url.com/bank_roof.png"
    },
    "border": {
        "1f": "https://your-url.com/border_1f.png",
        "2f": "https://your-url.com/border_2f.png",
        "roof": "https://your-url.com/border_roof.png"
    },
    "clubhouse": {
        "basement": "https://your-url.com/clubhouse_basement.png",
        "1f": "https://your-url.com/clubhouse_1f.png",
        "2f": "https://your-url.com/clubhouse_2f.png"
    },
    "chalet": {
        "basement": "https://your-url.com/chalet_basement.png",
        "1f": "https://your-url.com/chalet_1f.png",
        "2f": "https://your-url.com/chalet_2f.png"
    },
    "kafe": {
        "1f": "https://cdn.discordapp.com/attachments/1472963714927038566/1472983907606724750/kafe_f1.png?ex=69fc0c6a&is=69fabaea&hm=53230cb9b1dd9f5ca11fc0eb4cd28c30d4496692866213954556d41d327a67d5&",
        "2f": "https://cdn.discordapp.com/attachments/1472963714927038566/1472983951193931807/kafe_f2.png?ex=69fc0c74&is=69fabaf4&hm=4b945062bdb56f8f9d3989c9f40d26f29696f8e94179c6ffd6e2b62d914980fa&",
        "3f": "https://cdn.discordapp.com/attachments/1472963714927038566/1472983973557829905/kafe_f3.png?ex=69fc0c7a&is=69fabafa&hm=0a485f339978034cf85780cdda64b54bf3bfa21df71fa42962507294bd2e0fd3&"
    },
    "oregon": {
        "basement": "https://cdn.discordapp.com/attachments/1472963714927038566/1476946606229159987/oregon_b.png?ex=69fbf677&is=69faa4f7&hm=c9374f526c1caeb1bccd66d9e8e6a4b2bbf58b475b991fe3dedaaf4a63d94106&",
        "1f": "https://cdn.discordapp.com/attachments/1472963714927038566/1476946644682674307/oregon_f1_1.png?ex=69fbf680&is=69faa500&hm=1c57edb5651b67764998aa9863533596c55c722151f4f4e11212e52478e141f2&",
        "2f": "https://cdn.discordapp.com/attachments/1472963714927038566/1476946682775081194/oregon_f2_1.png?ex=69fbf689&is=69faa509&hm=54892d4cbdfc272be0f4b9d696d043160da568ebc8205f07289cf48331f04be4&"
    },
    "consulate": {
        "basement": "https://your-url.com/consulate_basement.png",
        "1f": "https://your-url.com/consulate_1f.png",
        "2f": "https://your-url.com/consulate_2f.png",
        "roof": "https://your-url.com/consulate_roof.png"
    },
    "skyscraper": {
        "1f": "https://your-url.com/skyscraper_1f.png",
        "2f": "https://your-url.com/skyscraper_2f.png"
    },
    "villa": {
        "1f": "https://your-url.com/villa_1f.png",
        "2f": "https://your-url.com/villa_2f.png"
    },
    "labs": {
        "basement": "https://your-url.com/labs_basement.png",
        "1f": "https://your-url.com/labs_1f.png",
        "2f": "https://your-url.com/labs_2f.png"
    },
    "lair": {
        "basement": "https://your-url.com/lair_basement.png",
        "1f": "https://your-url.com/lair_1f.png",
        "2f": "https://your-url.com/lair_2f.png"
    }
}


# -----------------------------
# FLOOR LISTS
# -----------------------------
FLOORS = {
    "bank": ["basement", "1f", "2f", "roof"],
    "border": ["1f", "2f", "roof"],
    "clubhouse": ["basement", "1f", "2f"],
    "chalet": ["basement", "1f", "2f"],
    "kafe": ["1f", "2f", "3f"],
    "oregon": ["basement", "1f", "2f"],
    "consulate": ["basement", "1f", "2f", "roof"],
    "skyscraper": ["1f", "2f"],
    "villa": ["1f", "2f"],
    "labs": ["basement", "1f", "2f"],
    "lair": ["basement", "1f", "2f"]
}


# -----------------------------
# FIRST DROPDOWN — MAP SELECT
# -----------------------------
class MapSelect(nextcord.ui.Select):
    def __init__(self):
        options = [
            SelectOption(label="Bank", value="bank"),
            SelectOption(label="Border", value="border"),
            SelectOption(label="Clubhouse", value="clubhouse"),
            SelectOption(label="Chalet", value="chalet"),
            SelectOption(label="Kafe", value="kafe"),
            SelectOption(label="Oregon", value="oregon"),
            SelectOption(label="Consulate", value="consulate"),
            SelectOption(label="Skyscraper", value="skyscraper"),
            SelectOption(label="Villa", value="villa"),
            SelectOption(label="Nighthaven Labs", value="labs"),
            SelectOption(label="Lair", value="lair")
        ]

        super().__init__(
            placeholder="Choose a map...",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: Interaction):
        map_name = self.values[0]

        # EPHEMERAL RESPONSE
        await interaction.response.send_message(
            f"Selected map: **{map_name.capitalize()}**\nNow choose a floor:",
            view=FloorView(map_name),
            ephemeral=True
        )


class MapView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(MapSelect())


# -----------------------------
# SECOND DROPDOWN — FLOOR SELECT
# -----------------------------
class FloorSelect(nextcord.ui.Select):
    def __init__(self, map_name):
        self.map_name = map_name

        options = [
            SelectOption(label=floor.upper(), value=floor)
            for floor in FLOORS[map_name]
        ]

        super().__init__(
            placeholder="Choose a floor...",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: Interaction):
        floor = self.values[0]
        image_url = IMAGE_URLS[self.map_name][floor]

        embed = nextcord.Embed(
            title=f"{self.map_name.capitalize()} — {floor.upper()}",
            color=0x00AEEF
        )
        embed.set_image(url=image_url)

        # EPHEMERAL RESPONSE
        await interaction.response.send_message(embed=embed, ephemeral=True)


class FloorView(nextcord.ui.View):
    def __init__(self, map_name):
        super().__init__(timeout=None)
        self.add_item(FloorSelect(map_name))


# -----------------------------
# COMMAND
# -----------------------------
@bot.command()
async def map(ctx):
    # PUBLIC MESSAGE
    await ctx.send("Choose a map:", view=MapView())


# -----------------------------
# RUN BOT
# -----------------------------
import os
bot.run(os.getenv("TOKEN"))
