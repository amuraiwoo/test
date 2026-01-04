import discord
from discord import app_commands
import asyncio
import os

class App(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.none())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

app = App()

@app.tree.command(
    name="yuupon",
    description="ゆうぽんのアプリ"
)
async def yuupon(interaction: discord.Interaction):
    # ← これが超重要（3秒制限回避）
    await interaction.response.defer()

    # 30回送信
    for i in range(30):
        await asyncio.sleep(0.6)
        await interaction.followup.send("# ゆうぽん万歳wwwwww🤣 🤣 🤣 🤣 🤣 🤣 🤣 🤣 🤣 こんなクソ鯖徹底的に潰してやるわwwwwww何も出来ない特別支援学級のみんなーwwwwwwwwwwwww障害者のみんなwwwwwwwひっひっひwwwゆうぽん万歳！！🤓🤓🤓🤓お前らこの鯖入れよ！ゆうぽん万歳早く入れよ！w🤓🤓🤓🤓この文章読んで画面の前で赤面になってる君！悔しいもんな！悔しいよな！でもお前ら何もできないもんなwww何も言い返せないもんな！www無能な管理人はもっと対策施策でもしたらどうだ？あ、できないからこうなってるんだ！！！‪🤣‬‪🤣‬‪🤣‬‪🤣‬‪🤣https://discord.gg/erRwpctpeN")

TOKEN = os.getenv("TOKEN")
app.run(TOKEN)
