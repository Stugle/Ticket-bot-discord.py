from re import U
from tabnanny import check
from venv import create
import discord
from random import randint
from discord.ext import commands
from discord_buttons_plugin import  *
import time
from base import *

intents = discord.Intents.all()
with db:
    db.create_tables([Ticket,Аdvertising,Channel])
print('Done')
bot = commands.Bot(command_prefix ='=',intents=intents)
client = discord.Client()
create_cooldown = {}
buttons = ButtonsClient(bot)

TOKEN = ""  #bot token

ticket_chose =    #The place where, with the start of the bot, a message will be written with a choice of topic for the ticket
ticket_opo =     #The place where notifications about ticket logs will be written and where they should be taken
ticket_sotr =    #Role to be reminded when a ticket is waiting to be accepted
open_ticket =    #Channel group where all open tickets will be
close_ticket =     #Channel group where all closed tickets will be
bot_id =   #id bot


@bot.event
async def on_ready():                                                 
    await buttons.send(
        content ="",embed=discord.Embed(title="Create a ticket",
                                                    description=f"⚒️ - Category 1\n"
                                                                f"\n"
                                                                f"🍥 - Category 2\n"
                                                                f"\n"
                                                                f"📝 - Category 3\n"
                                                                f"\n"
                                                                f"\n",
                                                                color=0x221b36),
        channel = ticket_chose,
        components = [
            ActionRow([
                Button(
                    label="Category 1",
                    emoji = {
                    "id": None,
                    "name": "⚒️",
                    "animated": False
                    }, 
                    style=ButtonType().Secondary, 
                    custom_id="button_one"          
                ),Button(
                    label="Category 2",
                    emoji = {
                    "id": None,
                    "name": "🍥",
                    "animated": False
                    },
                    style=ButtonType().Secondary,
                    custom_id="button_two"          
                ),Button(
                    label="Category 3",
                    emoji = {
                    "id": None,
                    "name": "📝",
                    "animated": False
                    },
                    style=ButtonType().Secondary,
                    custom_id="button_three"        
                )
            ])
        ]
    )

@buttons.click
async def button_one(ctx):

    if ctx.member in create_cooldown and create_cooldown[ctx.member] > time.time():
        await ctx.reply(f"You have already created a ticket in this category. Wait 10 minutes." , flags = MessageFlags().EPHEMERAL)
        return
    create_cooldown[ctx.member] = time.time()+600
    db = Ticket.create(ticket_cnl = 0, ticket_aut = (ctx.member).id ,ticket_type = 1 )
    user = (ctx.guild).get_member(db.ticket_aut)

    category = discord.utils.get((ctx.guild).categories, id=open_ticket)   
    channel = await category.create_text_channel(f'ticket  {db.nomer}')
    await channel.set_permissions(user, read_messages=True,
                                                send_messages=True)
    db.ticket_cnl = channel.id
    db.save()
    await ctx.reply(f"<#{db.ticket_cnl}> was created!" , flags = MessageFlags().EPHEMERAL)
    Channel.create(channel = channel.id, work = True )

    bot.get_channel(db.ticket_cnl)
    await buttons.send(

		content = "<@"+str(db.ticket_aut)+"> Hi!", embed=discord.Embed(description=f"Your **'Category 1'** ticket has been created\n" 
                                                        f'Your ticket number: {db.nomer}'
                                                        f"\n"
                                                        f"\n"
                                                        f"**Try to put everything you need in 1 message**\n"
                                                        f"\n"
                                                        f"You can close the ticket by clicking on the button below..", color=0x1967d2),
		channel = db.ticket_cnl,
		components = [
			ActionRow([
				Button(
					label="Сlose",
                    emoji = {
		            "id": None,
		            "name": "❌",
		            "animated": False
	                }, 
					style=ButtonType().Secondary, 
					custom_id="xmclose"          
				)
			])
		]
	)

@buttons.click
async def button_two(ctx):

    if ctx.member in create_cooldown and create_cooldown[ctx.member] > time.time():
        await ctx.reply(f"You have already created a ticket in this category. Wait 10 minutes." , flags = MessageFlags().EPHEMERAL)
        return
    create_cooldown[ctx.member] = time.time()+600
    db = Ticket.create(ticket_cnl = 0, ticket_aut = (ctx.member).id ,ticket_type = 2 )
    user = (ctx.guild).get_member(db.ticket_aut)

    category = discord.utils.get((ctx.guild).categories, id=open_ticket)   
    channel = await category.create_text_channel(f'ticket  {db.nomer}')
    await channel.set_permissions(user, read_messages=True,
                                                send_messages=True)
    db.ticket_cnl = channel.id
    db.save()
    await ctx.reply(f"<#{db.ticket_cnl}> was created!" , flags = MessageFlags().EPHEMERAL)
    Channel.create(channel = channel.id, work = True )

    bot.get_channel(db.ticket_cnl)
    await buttons.send(

		content = "<@"+str(db.ticket_aut)+"> Hi!", embed=discord.Embed(description=f"Your **'Category 2'** ticket has been created\n" 
                                                        f'Your ticket number: {db.nomer}'
                                                        f"\n"
                                                        f"\n"
                                                        f"**Try to put everything you need in 1 message**\n"
                                                        f"\n"
                                                        f"You can close the ticket by clicking on the button below.", color=0x1967d2),
		channel = db.ticket_cnl,
		components = [
			ActionRow([
				Button(
					label="Сlose",
                    emoji = {
		            "id": None,
		            "name": "❌",
		            "animated": False
	                }, 
					style=ButtonType().Secondary, 
					custom_id="xmclose"          
				)
			])
		]
	)

@buttons.click
async def button_three(ctx):
    if ctx.member in create_cooldown and create_cooldown[ctx.member] > time.time():
        await ctx.reply(f"You have already created a ticket in this category. Wait 10 minutes." , flags = MessageFlags().EPHEMERAL)
        return
    create_cooldown[ctx.member] = time.time()+600
    db = Ticket.create(ticket_cnl = 0, ticket_aut = (ctx.member).id ,ticket_type = 3 )
    user = (ctx.guild).get_member(db.ticket_aut)

    category = discord.utils.get((ctx.guild).categories, id=open_ticket)   
    channel = await category.create_text_channel(f'ticket  {db.nomer}')
    await channel.set_permissions(user, read_messages=True,
                                                send_messages=True)
    db.ticket_cnl = channel.id
    db.save()
    await ctx.reply(f"<#{db.ticket_cnl}> was created!" , flags = MessageFlags().EPHEMERAL)
    Channel.create(channel = channel.id, work = True )

    bot.get_channel(db.ticket_cnl)
    await buttons.send(

		content = "<@"+str(db.ticket_aut)+"> Hi!", embed=discord.Embed(description=f"Your **'Category 3'** ticket has been created\n" 
                                                        f'Your ticket number: {db.nomer}'
                                                        f"\n"
                                                        f"\n"
                                                        f"**Try to put everything you need in 1 message**\n"
                                                        f"\n"
                                                        f"You can close the ticket by clicking on the button below.", color=0x1967d2),
		channel = db.ticket_cnl,
		components = [
			ActionRow([
				Button(
					label="Сlose",
                    emoji = {
		            "id": None,
		            "name": "❌",
		            "animated": False
	                }, 
					style=ButtonType().Secondary, 
					custom_id="xmclose"          
				)
			])
		]
	)

@bot.event
async def on_message(message):
    if (message.channel).id == ticket_opo:
        db3 = Channel.get_or_create(channel = (message.channel).id, defaults={'channel': (message.channel).id, 'work': True} )
    db1 = Channel.get_or_create(channel = (message.channel).id, defaults={'channel': (message.channel).id, 'work': False} )
    db1 = Channel.get(Channel.channel == (message.channel).id)
    if db1.work == False:
        return
    if (message.author).id != bot_id:
        db = Ticket.get(Ticket.ticket_cnl == (message.channel).id)
        if (message.author).id != bot_id and (message.channel).id == db.ticket_cnl and db.ticket_question == False and db.ticket_aut == (message.author).id:
            print ('Done!')
            db.ticket_question = True
            db.save()

            await message.channel.send("We have heard! Wait for your ticket to be accepted...")
            max_add = Аdvertising.select(fn.MAX(Аdvertising.nomer)).scalar()
            random = randint(1, max_add)
            print (random)
            advertising = Аdvertising.get(Аdvertising.nomer == random)     #The bot can write ads to send a gif when he answered the person, what do you expect. Here's what it looks like: https://prnt.sc/wPu5AtwxuFQi. 
            await message.channel.send(advertising.text)                   #You just need to go to the database and enter the necessary information
            if db.ticket_type == 1:
                text = "Category 1"
            elif db.ticket_type == 2:
                text = "Category 2"
            elif db.ticket_type == 3:
                text = "Category 3"

            await buttons.send(

                content = f"<@&{ticket_sotr}> new ticket!", embed=discord.Embed(description=
                                                        f"Ticket on the topic **'{text}'** \n" 
                                                        f'User ticket: <@{db.ticket_aut}> \n'
                                                        f'Ticket number: {db.nomer} \n' 
                                                        f"\n" 
                                                        f"Ticket text: **\n" +str(message.content)+
                                                        f"**\n"
                                                        f"\n"
                                                        f"To get a ticket, click on the button below", color=0x561ef1),
                channel = ticket_opo,
                components = [
                    ActionRow([
                        Button(
                            label="Take!",
                            emoji = {
                            "id": None,
                            "name": "🟩",
                            "animated": False
                            }, 
                            style=ButtonType().Secondary, 
                            custom_id="sotrvz"          
                        )
                    ])
                ]
            )


    if message.author.id == bot_id and message.channel.id == ticket_opo and message.content == f"<@&{ticket_sotr}> new ticket!":
        msg = message.embeds[0].description
        nomer = msg.split('Ticket number:')[1].split('\n')[0]
        db = Ticket.get(Ticket.nomer == nomer)
        db.msg_sotr = message.id
        db.save()

@buttons.click
async def sotrvz(ctx):
    db = Ticket.get(Ticket.msg_sotr == (ctx.message).id)
    if db.ticket_status_sotr == False:
        await bot.get_channel(db.ticket_cnl).send("<@"+str(db.ticket_aut)+">" ,embed=discord.Embed(description="Your ticket has been taken by an employee <@"+str(ctx.member.id)+">\n", color=0x6a158a))
        db.ticket_status_sotr = True
        db.ticket_sotr = ctx.member.id
        db.save()
        channel = bot.get_channel(db.ticket_cnl)
        await channel.set_permissions(ctx.member, read_messages=True,
                                                send_messages=True)

        await ctx.reply(f"<#{db.ticket_cnl}> took: <@"+str(ctx.member.id)+">\n")
    else:
        await ctx.reply("Someone already took this ticket, look somewhere above -_-" , flags = MessageFlags().EPHEMERAL)


@buttons.click
async def xmclose(ctx):
    db = Ticket.get(Ticket.ticket_cnl == (ctx.channel).id)
    if db.ticket_close == False:
        msg = await ctx.reply("Are you sure you want to close the ticket?")
        await buttons.send(
        content = "",
        channel = ctx.channel.id,
        components = [
            ActionRow([
                Button(
                    label="Confirm",
                    emoji = {
                    "id": None,
                    "name": "🟩",
                    "animated": False
                    }, 
                    style=ButtonType().Secondary, 
                    custom_id="close"          
                ),Button(
                    label="Cancel",
                    emoji = {
                    "id": None,
                    "name": "🟥",
                    "animated": False
                    },
                    style=ButtonType().Secondary,
                    custom_id="noclose"          
                )
            ])
        ]
        )
        
        @buttons.click
        async def noclose(ctx):
            message2 = ctx.message
            who = ctx.member
            guild = ctx.guild
            await message2.delete()
            await ctx.reply("Ticket closing canceled: <@"+str(who.id)+">")



        @buttons.click
        async def close(ctx):
            message2 = ctx.message
            channel = ctx.channel.id
            who = ctx.member
            await message2.delete()
            bot.get_channel(ctx.channel.id)
            await ctx.reply("Ticket closed: <@"+str(who.id)+">")
            channel = bot.get_channel(db.ticket_cnl)
            user = (ctx.guild).get_member(db.ticket_aut)
            user_sotr = (ctx.guild).get_member(db.ticket_sotr)
            await channel.set_permissions(user, read_messages=False,
                                                        send_messages=False)
            await channel.edit(name=f"closed-{db.nomer}")
            categorys = discord.utils.get((ctx.guild).categories, id=close_ticket)
            await channel.edit(category=categorys)
            create_cooldown[user] = time.time()

            db.ticket_close = True
            db.save()

            if db.msg_sotr != 0:
                await bot.get_channel(ticket_opo).send(embed=discord.Embed(description=f"**Ticket №{db.nomer}** closed by <@"+str(who.id)+">", color=0x6a158a))
                channel = bot.get_channel(ticket_opo) 
                msg = await channel.fetch_message(db.msg_sotr) 
                await msg.delete() 

    else:
        await ctx.reply("You can't close what's already closed")


bot.run(TOKEN)
