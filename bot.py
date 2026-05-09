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
        "basement": "https://cdn.discordapp.com/attachments/1502767854439628800/1502768021653950504/image.png?ex=6a00e948&is=69ff97c8&hm=de22d68da053582c400ca9113c4be26f395ff2ffc4b55aff2a99641f0a7db706&",
        "1f": "https://cdn.discordapp.com/attachments/1502767854439628800/1502768003593535568/image.png?ex=6a00e944&is=69ff97c4&hm=ee5db0a1c70e7d60745eebbb6925893bcb14aadf5e51a848bbc7ff5cc5f61e2f&",
        "2f": "https://cdn.discordapp.com/attachments/1502767854439628800/1502767988938379436/image.png?ex=6a00e940&is=69ff97c0&hm=da97adfdd9ebc2601bf42f363297b5adbec74a800b2bcf9cb47518a083b45338&"
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
        "basement": "https://cdn.discordapp.com/attachments/1502767854439628800/1502767968491147344/image.png?ex=6a00e93b&is=69ff97bb&hm=d58c43abf5db2c67f1b680663cd7a0dba91670cf9b6d318302f4e2130759517d&",
        "1f": "https://cdn.discordapp.com/attachments/1502767854439628800/1502767917173964891/image.png?ex=6a00e92f&is=69ff97af&hm=786ef7af4a3bf89643301a5cc844c131c68a4b764277891df37d3361cdcff047&",
        "2f": "https://cdn.discordapp.com/attachments/1502767854439628800/1502767908462264361/image.png?ex=6a00e92d&is=69ff97ad&hm=e985d265823fc8a24a474f6ae346e4ea95da8b8340251ba23bd7bb97921604d4&"
    },
    "kafe": {
        "1f": "https://cdn.discordapp.com/attachments/1472963714927038566/1472983907606724750/kafe_f1.png?ex=69fc0c6a&is=69fabaea&hm=53230cb9b1dd9f5ca11fc0eb4cd28c30d4496692866213954556d41d327a67d5&",
        "2f": "https://cdn.discordapp.com/attachments/1472963714927038566/1472983951193931807/kafe_f2.png?ex=69fc0c74&is=69fabaf4&hm=4b945062bdb56f8f9d3989c9f40d26f29696f8e94179c6ffd6e2b62d914980fa&",
        "3f": "https://cdn.discordapp.com/attachments/1472963714927038566/1472983973557829905/kafe_f3.png?ex=69fc0c7a&is=69fabafa&hm=0a485f339978034cf85780cdda64b54bf3bfa21df71fa42962507294bd2e0fd3&"
    },
    "oregon": {
        "basement": "https://cdn.discordapp.com/attachments/1502767854439628800/1502768185450172446/image.png?ex=6a00e96f&is=69ff97ef&hm=cb8de46fc3c52c3ac533785cbf68a5790d7276f1127887d34f7fb722ad5e6938&",
        "1f": "https://cdn.discordapp.com/attachments/1502767854439628800/1502768173764710571/image.png?ex=6a00e96c&is=69ff97ec&hm=023cb7b6d88dccb1632dd3ca4fdf08f13db430cec3fad3521211aff678dd98ce&",
        "2f": "https://cdn.discordapp.com/attachments/1502767854439628800/1502768145478455296/image.png?ex=6a00e965&is=69ff97e5&hm=1a4268d001d1aa25e89a3cb03e8dc6a527a00c0b493857b2db1a545f7300dfd8&"
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
    "bank": ["basement", "1f", "2f"],
    "border": ["1f", "2f"],
    "clubhouse": ["basement", "1f", "2f"],
    "chalet": ["basement", "1f", "2f"],
    "kafe": ["1f", "2f", "3f"],
    "oregon": ["basement", "1f", "2f"],
    "consulate": ["basement", "1f", "2f"],
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
