import token
import discord

from token import TOKEN
from discord.ext import commands
from discord.ui import Button, View, Select 

# 다움이 BEGINS✨
bot = commands.Bot(
    intents=discord.Intents.all(), 
    command_prefix='!')

@bot.event
async def on_ready():
    print('Done')
    await bot.change_presence(status=discord.Status.online, 
                              activity=None)
             
@bot.command()
async def 다움아놀자(ctx):
    # MBTI BUTTON ----------------------------------------------
    mbti = Button(label="MBTI!", 
                  style=discord.ButtonStyle.primary, 
                  emoji="🧐",
                  custom_id='mbti')
    # MBTI callback
    async def MBTI(interaction):
        select = Select(
            min_values=1,
            max_values=1,
            placeholder="가장 너다운 답을 알려줘움 :D!",
            options=[
                discord.SelectOption(
                    label="집에 있는게.. 아주 그냥 최고지!",
                    emoji="🏠",
                    description="집 나가면 배터리 소모 시작🔋"

                ),
                discord.SelectOption(
                    label="사람은 사람을 만나야지!🥳",
                    emoji="🕺🏻",
                    description="혼자있으면 힘드러..😞"
                ),
            ])
        
        # selection callback
        async def select_cb(interaction):
            choice = select.values[0]
            mbti = 'INFP' if choice == "집에 있는게.. 아주 그냥 최고지!" \
                            else 'ENFP'
            view = View()
            
            # Set the URL
            if mbti == 'INFP':
                mention ="집에 있어도 이쁜 분위기는 포기할 수 없잖움?!"
                url = 'https://oh-lolly-day.com/product/cup-300ml-handle-glassgood-restring/531/category/86/display/1/'
            else: 
                mention = "요즘 힙쟁이들은 이런걸로 포인트를 주더라움! ✨"
                url = 'https://oh-lolly-day.com/product/beanie-old-beanie03/486/category/43/display/1/'
            
            link_bt = Button(label=" 🎁 ", 
                             style=discord.ButtonStyle.link, 
                             url = url)
            
            message = f'"{choice}" 라고 말하는 너는 {mbti}인게 틀.림.없.어! \n(feat. 억지부리는 코난 🕵️)\n\n {mbti}인 너에게 어울릴 거 같은 해피어굿즈를 추천해줄게 :)! 🤗 ' + mention
            view.add_item(link_bt)

            
            await interaction.response.send_message(message)
            await ctx.send(view=view)

        select.callback = select_cb
        view = View()
        view.add_item(select)
        await interaction.response.send_message("MBTI, 좋움! 너는 언제 에너지가 충전돼? 👀")
        await ctx.send(view=view)
        
    mbti.callback = MBTI

    # RSP BUTTON -----------------------------------------------
    rsp = Button(label="가위바위보!", 
                 style=discord.ButtonStyle.green, 
                 emoji="✋",
                 custom_id='rsp')
    # RSP callback
    async def RSP(interaction):
        await interaction.response.send_message("가위바위보 도전?!..은 사실.. 👉👈.. \n PETER가 가위바위보를 아직 안가르쳐줬어! 🫠 \n 다음에 하자움!", ephemeral=True)
    rsp.callback = RSP

    # View Setting ---------------------------------------------
    view = View()
    view.add_item(mbti)
    view.add_item(rsp)
    await ctx.send("좋아! 뭐하고 놀까?!", view=view)


@bot.command()
async def 내통장으로1억입금해줘(ctx):
    await ctx.send("ㅎ..피터먼저 주고..🥲")

@bot.command()
async def 메세지지워줘(ctx):
    await ctx.channel.purge()
    await ctx.send("청소 끝! 🧹")


bot.run(TOKEN)