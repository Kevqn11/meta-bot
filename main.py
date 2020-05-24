# -----Bot version 2.0.1-----
# STABLE BUILD
# Made : May 9, 20


import discord
import os
import datetime
from discord.ext import tasks
import asyncio


spawner_rates = [[
    ['undeadhorses', '2500000'],
    ['undeadhorse', '2500000'],
    ['undeads', '2500000'],
    ['undead', '2500000'],
    ['skeletonhorses', '2500000'],
    ['skeletonhorse', '2500000'],
    ['skelehorses', '2500000'],
    ['skelehorse', '2500000'],
    ['witherskeletons', '1200000'],
    ['witherskeleton', '1200000'],
    ['witherskeles', '1200000'],
    ['witherskele', '1200000'],
    ['wskeles', '1200000'],
    ['wskele', '1200000'],
    ['pigzombies', '900000'],
    ['pigzombie', '900000'],
    ['pigmans', '900000'],
    ['pigman', '900000'],
    ['zombiepigs', '900000'],
    ['zombiepig', '900000'],
    ['zp', '900000'],
    ['pigs', '25000'],
    ['pig', '25000'],
    ['wolves', '30000'],
    ['wolf', '30000'],
    ['ocelots', '30000'],
    ['ocelot', '30000'],
    ['rabbits', '37500'],
    ['rabbit', '37500'],
    ['sheeps', '45000'],
    ['sheep', '45000'],
    ['chickens', '55000'],
    ['chicken', '55000'],
    ['cows', '65000'],
    ['cow', '65000'],
    ['mooshrooms', '65000'],
    ['mooshroom', '65000'],
    ['horses', '90000'],
    ['horse', '90000'],
    ['silverfishes', '100000'],
    ['silverfish', '100000'],
    ['sfs', '100000'],
    ['sf', '100000'],
    ['slimes', '175000'],
    ['slime', '175000'],
    ['endermites', '210000'],
    ['endermite', '210000'],
    ['emites', '210000'],
    ['emite', '210000'],
    ['cavespiders', '250000'],
    ['cavespider', '250000'],
    ['spiders', '250000'],
    ['spider', '250000'],
    ['squids', '280000'],
    ['squid', '280000'],
    ['skeletons', '375000'],
    ['skeleton', '375000'],
    ['skeles', '375000'],
    ['skele', '375000'],
    ['guardians', '425000'],
    ['guardian', '425000'],
    ['magmacubes', '500000'],
    ['magmacube', '500000'],
    ['magmas', '500000'],
    ['magma', '500000'],
    ['villagers', '750000'],
    ['villager', '750000'],
    ['villes', '750000'],
    ['ville', '750000'],
    ['ghasts', '825000'],
    ['ghast', '825000'],
    ['zombies', '325000'],
    ['zombie', '325000'],
    ['blazes', '950000'],
    ['blaze', '950000'],
    ['witches', '1100000'],
    ['witch', '1100000'],
    ['enderman', '1400000'],
    ['endermen', '1400000'],
    ['eman', '1400000'],
    ['emen', '1400000'],
    ['creepers', '1750000'],
    ['creeper', '1750000'],
    ['mobhoppers', '600000'],
    ['mobhopper', '600000'],
    ['mhoppers', '600000'],
    ['mhopper', '600000'],
    ['hoppers', '25000'],
    ['hopper', '25000']],[

    ['pigzombies', '1500000'],
    ['pigzombie', '1500000'],
    ['pigmans', '1500000'],
    ['pigman', '1500000'],
    ['zombiepigs', '1500000'],
    ['zombiepig', '1500000'],
    ['zp', '1500000'],
    ['pigs', '25000'],
    ['pig', '25000'],
    ['wolves', '150000'],
    ['wolf', '150000'],
    ['ocelots', '150000'],
    ['ocelot', '150000'],
    ['rabbits', '70000'],
    ['rabbit', '70000'],
    ['sheeps', '35000'],
    ['sheep', '35000'],
    ['chickens', '50000'],
    ['chicken', '50000'],
    ['cows', '90000'],
    ['cow', '90000'],
    ['mooshrooms', '50000'],
    ['mooshroom', '50000'],
    ['horses', '100000'],
    ['horse', '100000'],
    ['slimes', '190000'],
    ['slime', '190000'],
    ['cavespiders', '215000'],
    ['cavespider', '215000'],
    ['spiders', '215000'],
    ['spider', '215000'],
    ['squids', '170000'],
    ['squid', '170000'],
    ['skeletons', '300000'],
    ['skeleton', '300000'],
    ['skeles', '300000'],
    ['skele', '300000'],
    ['guardians', '500000'],
    ['guardian', '500000'],
    ['magmacubes', '250000'],
    ['magmacube', '250000'],
    ['magmas', '250000'],
    ['magma', '25w0000'],
    ['villagers', '1250000'],
    ['villager', '1250000'],
    ['villes', '1250000'],
    ['ville', '1250000'],
    ['zombies', '200000'],
    ['zombie', '200000'],
    ['blazes', '1000000'],
    ['blaze', '1000000'],
    ['witches', '900000'],
    ['witch', '900000'],
    ['enderman', '700000'],
    ['endermen', '700000'],
    ['eman', '1400000'],
    ['emen', '1400000'],
    ['creepers', '1000000'],
    ['creeper', '1000000'],
    ['hoppers', '25000'],
    ['hopper', '25000']]

]

#Library

nextline = """
"""
def ceil(var):
    if var%1 > 0:
        return int(var//1 + 1)
    else:
        return int(var)

def pure_int(var):
    if type(var) == int:
        return True
    try:
        if int(eval(str(var))) == eval(var):
            return True
        else:
            return False
    except:
        return False

def checkDir(var1):
    if str(os.path.exists(var1)) == 'False':
        os.mkdir(var1)
    else:
        pass

def checkTxt(var1, var2):
    if str(os.path.exists(var1)) == 'False':
        with open(var1, 'w+') as a:
            a.write(var2)
    else:
        pass

def split_space(var1) :
    if var1.find(' ') == -1 :
        return ''

    else:
        return var1[var1.find(' ')+1:]

def split_space_list(var):

    _list = []
    while len(var) > 0:
        if ' ' in var:
            _list.append(var[: var.find(' ')])
            var = var[var.find(' ') + 1 :]
        else:

            _list.append(var)
            var = ''
    if _list == []:
        _list = ['']
    return _list

def sortkey(var):
    return int(eval(str(var[19:])))

def commas(var):
    if var.startswith('-'):
        var = "".join(reversed(var[1:]))
        var2 = ''
        i = 1
        while i <= len(var):
            if i%3 == 0 and i != len(var):
                var2 = var2 + var[i-1] + ','
            else:
                var2 = var2 + var[i-1]
            i = i+1

        return f'-{"".join(reversed(var2))}'
    else:
        var = "".join(reversed(var))
        var2 = ''
        i = 1
        while i <= len(var):
            if i%3 == 0 and i != len(var):
                var2 = var2 + var[i-1] + ','
            else:
                var2 = var2 + var[i-1]
            i = i+1

        return "".join(reversed(var2))

dateformat = "%a %d %b '%y at %H:%M:%S GMT"
def create_wall_code(id, settings):
    code = f"""
@tasks.loop(minutes = {float(settings[1][2])}, count = 1000)
async def wall_alert{id}():
    ch = client.get_channel({settings[1][5]})
    perms = client.permissions_in(ch)
    if perms.read_message_history:
        messages = await ch.history(limit=30).flatten()
        for i in messages :
            if i.author.id == client.user.id :
                if len(i.embeds) == 1:
                    try:
                        if split_space(i.embeds[0].title).startswith('Time to check walls'):
                            if perms.manage_messages:
                                await i.delete()
                            break
                    except:
                        pass
    if perms.send_messages:
        td = {settings[1][2]}*(wall_alert{id}.current_loop+1)+{settings[1][1]}
        if td%60 == 0:
            embed = discord.Embed(title = ':no_entry: Time to check walls!', description = f'It has been `{{td//60}} hours` since the last wall-check.', color = discord.Colour.red())
        elif td<60:
            embed = discord.Embed(title = ':no_entry: Time to check walls!', description = f'It has been `{{td}} minutes` since the last wall-check.', color = discord.Colour.red())
        else:
            embed = discord.Embed(title = ':no_entry: Time to check walls!', description = f'It has been `{{td//60}} hours and {{td%60}} minutes` since the last wall-check.', color = discord.Colour.red())
        embed.set_footer(text = f'''Wall-Check Alert | {{datetime.datetime.utcnow().strftime("%a %d %b '%y at %H:%M:%S GMT")}}''')
        msg = await ch.send(content = 'Check now <@&{settings[1][6]}> !!', embed = embed)
        if perms.add_reactions:
            await msg.add_reaction('\U00002705')
            await msg.add_reaction('\U0001F4A3')

@wall_alert{id}.before_loop
async def before_wall{id}():
    await client.wait_until_ready()
    await asyncio.sleep({settings[1][1]*60})
    ch = client.get_channel({settings[1][5]})
    perms = client.permissions_in(ch)
    if perms.read_message_history:
        messages = await ch.history(limit=30).flatten()
        for i in messages :
            if i.author.id == client.user.id:
                if len(i.embeds) == 1:
                    try:
                        title = i.embeds[0].title
                        if split_space(title).startswith('Time to check walls'):
                            if perms.manage_messages:
                                await i.delete()
                            break
                        elif title.endswith('walls clear.'):
                            if perms.manage_messages:
                                await i.clear_reactions()
                            break
                    except:
                        pass
    if perms.send_messages:
        embed = discord.Embed(title = ':warning: Time to check walls!', description = 'It has been `{settings[1][1]} minutes` since the last wall-check.', color = discord.Colour.gold())
        embed.set_footer(text = f'''Wall-Check Alert | {{datetime.datetime.utcnow().strftime("%a %d %b '%y at %H:%M:%S GMT")}}''')
        if {settings[1][7]}:
            msg = await ch.send(content = 'Check now <@&{settings[1][6]}>', embed = embed)
        else:
            msg = await ch.send(embed = embed)
        if perms.add_reactions:
            await msg.add_reaction('\U00002705')
            await msg.add_reaction('\U0001F4A3')
    await asyncio.sleep({settings[1][2]*60})

wall_alert{id}.start()"""
    return code

def create_buffer_code(id, settings):
    code = f"""
@tasks.loop(minutes = {float(settings[2][2])}, count = 1000)
async def buffer_alert{id}():
    ch = client.get_channel({settings[2][5]})
    perms = client.permissions_in(ch)
    if perms.read_message_history:
        messages = await ch.history(limit=50).flatten()
        for i in messages :
            if i.author.id == client.user.id :
                if len(i.embeds) == 1:
                    try:
                        if split_space(i.embeds[0].title).startswith('Time to check buffers'):
                            if perms.manage_messages:
                                await i.delete()
                            break
                    except:
                        pass
    if perms.send_messages:
        td = {settings[2][2]}*(buffer_alert{id}.current_loop+1)+{settings[2][1]}
        if td%60 == 0:
            embed = discord.Embed(title = ':no_entry: Time to check buffers!', description = f'It has been `{{td//60}} hours` since the last buffer-check.', color = discord.Colour.red())
        elif td<60:
            embed = discord.Embed(title = ':no_entry: Time to check buffers!', description = f'It has been `{{td}} minutes` since the last buffer-check.', color = discord.Colour.red())
        else:
            embed = discord.Embed(title = ':no_entry: Time to check buffers!', description = f'It has been `{{td//60}} hours and {{td%60}} minutes` since the last buffer-check.', color = discord.Colour.red())
        embed.set_footer(text = f'''Buffer-Check Alert | {{datetime.datetime.utcnow().strftime("%a %d %b '%y at %H:%M:%S GMT")}}''')
        msg = await ch.send(content = 'Check now <@&{settings[2][6]}> !!', embed = embed)
        if perms.add_reactions:
            await msg.add_reaction('\U00002705')
            await msg.add_reaction('\U0001F4A3')

@buffer_alert{id}.before_loop
async def before_buffer{id}():
    await client.wait_until_ready()
    await asyncio.sleep({settings[2][1]*60})
    ch = client.get_channel({settings[2][5]})
    perms = client.permissions_in(ch)
    if perms.read_message_history:
        messages = await ch.history(limit=50).flatten()
        for i in messages :
            if i.author.id == client.user.id:
                if len(i.embeds) == 1:
                    try:
                        if split_space(i.embeds[0].title).startswith('Time to check buffers'):
                            if perms.manage_messages:
                                await i.delete()
                            break
                        elif title.endswith('buffers clear.'):
                            if perms.manage_messages:
                                await i.clear_reactions()
                            break
                    except:
                        pass
    if perms.send_messages:
        embed = discord.Embed(title = ':warning: Time to check buffers!', description = 'It has been `{settings[2][1]} minutes` since the last buffer-check.', color = discord.Colour.gold())
        embed.set_footer(text = f'''Buffer-Check Alert | {{datetime.datetime.utcnow().strftime("%a %d %b '%y at %H:%M:%S GMT")}}''')
        if {settings[2][7]}:
            msg = await ch.send(content = 'Check now <@&{settings[2][6]}>', embed = embed)
        else:
            msg = await ch.send(embed = embed)
        if perms.add_reactions:
            await msg.add_reaction('\U00002705')
            await msg.add_reaction('\U0001F4A3')
    await asyncio.sleep({settings[2][2]*60})

buffer_alert{id}.start()"""
    return code

valueLogsDir = os.path.join(os.getcwd(), 'valueLogs')
wallsLogsDir = os.path.join(os.getcwd(), 'wallsLogs')
buffersLogsDir  = os.path.join(os.getcwd(), 'buffersLogs')
valueDir = os.path.join(os.getcwd(), 'rsrc')
wallsDir = os.path.join(os.getcwd(), 'wallschecks')
buffersDir = os.path.join(os.getcwd(), 'bufferchecks')
prefixDir = os.path.join(os.getcwd(), 'prefixes')
todayDir = os.path.join(os.getcwd(), 'todayadded')
infoTxt = os.path.join(os.getcwd(), 'info.txt')
client = discord.Client()

with open('token.txt', 'r') as file:
    token = file.read()

skinsDir = os.path.join(os.getcwd(), 'skins')

settingsDir = os.path.join(os.getcwd(), 'settings')

@client.event
async def on_ready():
    print('---------Bot Version 2.0.1-----------')
    print(f'Logged in as : {client.user}')
    checkDir(valueDir)
    checkDir(valueLogsDir)
    checkDir(wallsLogsDir)
    checkDir(buffersLogsDir)
    checkDir(wallsDir)
    checkDir(buffersDir)
    checkDir(skinsDir)
    checkDir(settingsDir)
    checkDir(prefixDir)
    checkDir(todayDir)
    print('Currently Joined Servers - ')
    with open(infoTxt, 'w+') as file:
        file.write(datetime.datetime.utcnow().strftime(dateformat))

    for a in client.guilds:
        try:
            checkTxt(os.path.join(valueDir, str(a.id)+'.txt'), '')
            checkTxt(os.path.join(wallsDir, str(a.id)+'.txt'), '')
            checkTxt(os.path.join(buffersDir, str(a.id)+'.txt'), '')
            checkTxt(os.path.join(skinsDir, str(a.id)+'.txt'), '')
            checkTxt(os.path.join(todayDir, str(a.id)+'.txt'), '')
            checkTxt(os.path.join(prefixDir, str(a.id)+'.txt'), '??')
            checkTxt(os.path.join(valueLogsDir, str(a.id)+'.txt'), f":smiley: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** Invited **ValueBot** to the server.")
            checkTxt(os.path.join(wallsLogsDir, str(a.id)+'.txt'), f":smiley: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** Invited **ValueBot** to the server.")
            checkTxt(os.path.join(buffersLogsDir, str(a.id)+'.txt'), f":smiley: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** Invited **ValueBot** to the server.")
            print(f'{str(a.id)} - {a.name}')
            perms = a.me.guild_permissions
            found = False
            if not perms.manage_roles:
                found = True
            elif not perms.manage_channels:
                found = True
            elif not perms.read_messages:
                found = True
            elif not perms.send_messages:
                found = True
            elif not perms.manage_messages:
                found = True
            elif not perms.embed_links:
                found = True
            elif not perms.read_message_history:
                found = True
            elif not perms.mention_everyone:
                found = True
            elif not perms.add_reactions:
                found = True
            if found:
                for i in a.text_channels:
                    if i.name =='value-added':
                        if i.permissions_for(a.me).send_messages:
                            embed = discord.Embed(title = ':gear: Not enough permissions.', description = 'The bot does not have the required permissions. Re-invite the bot using this [link](https://discordapp.com/api/oauth2/authorize?client_id=637575751583137822&permissions=268659792&scope=bot) or just give the bot admin.', color = discord.Colour.blue())
                            await i.send(embed = embed)
                            break
            else:
                with open(os.path.join(prefixDir, str(a.id)+'.txt'), 'r') as file:
                    prefix = file.read()
                if os.path.exists(os.path.join(settingsDir, str(a.id)+'.txt')):
                    with open(os.path.join(settingsDir, str(a.id)+'.txt'), 'r') as file:
                        settings = eval(file.read())
                    change = False
                    if settings[0][0]:
                        if client.get_channel(settings[0][3]) == None:
                            found = False
                            for i in a.text_channels:
                                if i.name == 'value-added':
                                    found = True
                                    if i.permissions_for(a.me).send_messages:
                                        embed = discord.Embed(title = ':gear: Settings - Channel - Value Management', description = f'Could not find the previously set value channel, so this channel has been automatically selected and will be used in the future to post embeds regarding value addition/removal.\n\nTo set a different channel for value embeds, do\n```{prefix}settings channel value <mention the channel>```', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                                        await i.send(embed = embed)
                                    settings[0][3] = i.id
                                    break
                            if not found:
                                if a.me.guild_permissions.manage_channels:
                                    ch = await a.create_text_channel(name = 'value-added')
                                    embed = discord.Embed(title = f'Settings - Channel - Value Management', description = f'Could not find the previously set value channel, so this channel has been created and will be used in the future to post embeds regarding value addition.\n\nTo set a different channel for value embeds, do\n```{prefix}settings channel value <mention the channel>```', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                                    await ch.send(embed=embed)
                                settings[0][3] = ch.id
                            change = True
                        if a.get_role(settings[0][4]) == None:
                            found = False
                            ch = client.get_channel(settings[0][3])
                            for i in a.roles:
                                if i.name == 'Faction Member':
                                    found = True
                                    perms = ch.permissions_for(a.me)
                                    if perms.send_messages:
                                        embed = discord.Embed(title = ':gear: Settings - Role - Value', description = f'Could not find previously set role for __value module__.\nTo overcome this issue, the {i.mention} has been selected.\n\nTo change the role for __value module__,\n```{prefix}settings role value <mention the role>```', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}')
                                        await ch.send(embed = embed)
                                    settings[0][4] = i.id
                                    change = True
                                    if perms.manage_roles:
                                        await ch.set_permissions(i, read_messages = True, send_messages = True)
                            if not found:
                                if a.me.guild_permissions.manage_roles:
                                    r = await a.create_role(name = 'Faction Member')
                                    perms = ch.permissions_for(a.me)
                                    if perms.send_messages:
                                        embed = discord.Embed(title = ':gear: Settings - Role - Value', description = f'Could not find previously set role for __value module__.\nTo overcome this issue, the {r.mention} has been created.\n\nTo change the role for __value module__,\n```{prefix}settings role value <mention the role>```', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}')
                                        await ch.send(embed = embed)
                                    settings[0][4] = r.id
                                    change = True
                                    if perms.manage_roles:
                                        await ch.set_permissions(r, read_messages = True, send_messages = True)
                    if settings[1][0]:
                        if client.get_channel(settings[1][5]) == None:
                            found = False
                            for i in a.text_channels:
                                if i.name == 'wall-check':
                                    found = True
                                    if i.permissions_for(a.me).send_messages:
                                        embed = discord.Embed(title = ':gear: Settings - Channel - Wall-Checks', description = f'Could not find the previously set walls channel, so this channel has been automatically selected and will be used in the future for wall-check alerts.\n\nTo set a different walls channel, do\n```{prefix}settings channel walls <mention the channel>```', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                                        await i.send(embed = embed)
                                    settings[1][5] = i.id
                                    break
                            if not found:
                                if a.me.guild_permissions.manage_channels:
                                    ch = await a.create_text_channel(name = 'wall-check')
                                    embed = discord.Embed(title = f'Settings - Channel - Wall-Checks', description = f'Could not find the previously set walls channel, so this channel has been created and will be used in the future for wall-check alerts.\n\nTo set a different walls channel, do\n```{prefix}settings channel walls <mention the channel>```', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                                    await ch.send(embed=embed)
                                settings[1][5] = ch.id
                            change = True
                        if a.get_role(settings[1][6]) == None:
                            found = False
                            ch = client.get_channel(settings[1][5])
                            for i in a.roles:
                                if i.name == 'Faction Member':
                                    found = True
                                    perms = ch.permissions_for(a.me)
                                    if perms.send_messages:
                                        embed = discord.Embed(title = ':gear: Settings - Role - Wall-Checks', description = f'Could not find previously set role for __wall-check module__.\nTo overcome this issue, the {i.mention} has been selected.\n\nTo change the role for __wall-check module__,\n```{prefix}settings role walls <mention the role>```', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}')
                                        await ch.send(embed = embed)
                                    settings[1][6] = i.id
                                    change = True
                                    if perms.manage_roles:
                                        await ch.set_permissions(i, read_messages = True, send_messages = True)
                            if not found:
                                if a.me.guild_permissions.manage_roles:
                                    r = await a.create_role(name = 'Faction Member')
                                    perms = ch.permissions_for(a.me)
                                    if perms.send_messages:
                                        embed = discord.Embed(title = ':gear: Settings - Role - Wall-Checks', description = f'Could not find previously set role for __wall-check module__.\nTo overcome this issue, the {r.mention} has been created.\n\nTo change the role for __wall-check module__,\n```{prefix}settings role walls <mention the role>```', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}')
                                        await ch.send(embed = embed)
                                    settings[1][6] = r.id
                                    change = True
                                    if perms.manage_roles:
                                        await ch.set_permissions(r, read_messages = True, send_messages = True)
                        if settings[1][3] == None:
                            settings[1][3] = datetime.datetime.utcnow().strftime(dateformat)
                            change = True
                    if settings[2][0]:
                        if client.get_channel(settings[2][5]) == None:
                            found = False
                            for i in a.text_channels:
                                if i.name == 'buffer-check':
                                    found = True
                                    if i.permissions_for(a.me).send_messages:
                                        embed = discord.Embed(title = ':gear: Settings - Channel - Buffer-Checks', description = f'Could not find the previously set buffers channel, so this channel has been automatically selected and will be used in the future for buffer-check alerts.\n\nTo set a different buffers channel, do\n```{prefix}settings channel buffers <mention the channel>```', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                                        await i.send(embed = embed)
                                    settings[2][5] = i.id
                                    break
                            if not found:
                                if a.me.guild_permissions.manage_channels:
                                    ch = await a.create_text_channel(name = 'buffer-check')
                                    embed = discord.Embed(title = f'Settings - Channel - Buffer-Checks', description = f'Could not find the previously set buffers channel, so this channel has been created and will be used in the future for buffer-check alerts.\n\nTo set a different buffers channel, do\n```{prefix}settings channel buffers <mention the channel>```', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                                    await ch.send(embed=embed)
                                settings[2][5] = ch.id
                            change = True
                        if a.get_role(settings[2][6]) == None:
                            found = False
                            ch = client.get_channel(settings[2][5])
                            for i in a.roles:
                                if i.name == 'Faction Member':
                                    found = True
                                    perms = ch.permissions_for(a.me)
                                    if perm.send_messages:
                                        embed = discord.Embed(title = ':gear: Settings - Role - Buffer-Checks', description = f'Could not find previously set role for __buffer-check module__.\nTo overcome this issue, the {i.mention} has been selected.\n\nTo change the role for __buffer-check module__,\n```{prefix}settings role buffers <mention the role>```', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}')
                                        await ch.send(embed = embed)
                                    settings[2][6] = i.id
                                    change = True
                                    if perms.manage_roles:
                                        await ch.set_permissions(i, read_messages = True, send_messages = True)
                            if not found:
                                if a.me.guild_permissions.manage_roles:
                                    r = await a.create_role(name = 'Faction Member')
                                    perms = ch.permissions_for(a.me)
                                    if perms.manage_roles:
                                        await ch.set_permissions(r, read_messages = True, send_messages = True)
                                    if perms.send_messages:
                                        embed = discord.Embed(title = ':gear: Settings - Role - Buffer-Checks', description = f'Could not find previously set role for __buffer-check module__.\nTo overcome this issue, the {r.mention} has been created.\n\nTo change the role for __buffer-check module__,\n```{prefix}settings role buffers <mention the role>```', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}')
                                        await ch.send(embed = embed)
                                    settings[2][6] = r.id
                                    change = True
                        if settings[2][3] == None:
                            settings[2][3] = datetime.datetime.utcnow().strftime(dateformat)
                            change = True
                    if change:
                        with open(os.path.join(settingsDir, str(a.id)+'.txt'), 'w') as file:
                            file.write(str(settings))
                else:
                    #          [status, realm, goal, ch, role], [status, checkfreq, remFreq, lastcheck, player, channel, role, tag on 1st alert], [same as previous]
                    settings = [[True, 'WITHER', None, None, None],[False, 30, 10, None, None, None, None, False],[False, 30, 10, None, None, None, None, False]]
                    found = False
                    for i in a.text_channels:
                        if i.name == 'value-added':
                            found = True
                            # embed = discord.Embed(title = ':gear: Settings - Channel - Value Management', description = f'Could not find the previously set value channel, so this channel has been automatically selected and will be used in the future to post embeds regarding value addition/removal.\n\nTo set a different channel for value embeds, do\n```{prefix}settings channel value <mention the channel>```', color = discord.Colour.blue())
                            # embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                            # await i.send(embed = embed)
                            settings[0][3] = i.id
                            break
                    if not found:
                        if a.me.guild_permissions.manage_channels:
                        ch = await a.create_text_channel(name = 'value-added')
                        # embed = discord.Embed(title = f'Settings - Channel - Value Management', description = f'Could not find the previously set value channel, so this channel has been created and will be used in the future to post embeds regarding value addition.\n\nTo set a different channel for value embeds, do\n```{prefix}settings channel value <mention the channel>```', color = discord.Colour.blue())
                        # embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                        # await ch.send(embed=embed)
                        settings[0][3] = ch.id
                    found = False
                    ch = client.get_channel(settings[0][3])
                    for i in a.roles:
                        if i.name == 'Faction Member':
                            found = True
                            # embed = discord.Embed(title = ':gear: Settings - Role - Value', description = f'Could not find previously set role for __value module__.\nTo overcome this issue, the {i.mention} has been selected.\n\nTo change the role for __value module__,\n```{prefix}settings role value <mention the role>```', color = discord.Colour.blue())
                            # embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}')
                            # await ch.send(embed = embed)
                            settings[0][4] = i.id
                            change = True
                            if ch.permissions_for(a.me).manage_roles:
                                await ch.set_permissions(i, read_messages = True, send_messages = True)
                    if not found:
                        if a.me.guild_permissions.manage_roles:
                            r = await a.create_role(name = 'Faction Member')
                            if ch.permissions_for(a.me).manage_roles:
                                await ch.set_permissions(r, read_messages = True, send_messages = True)
                        # embed = discord.Embed(title = ':gear: Settings - Role - Value', description = f'Could not find previously set role for __value module__.\nTo overcome this issue, the {r.mention} has been created.\n\nTo change the role for __value module__,\n```{prefix}settings role value <mention the role>```', color = discord.Colour.blue())
                        # embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}')
                        # await ch.send(embed = embed)
                        settings[0][4] = r.id
                        change = True
                    with open(os.path.join(settingsDir, str(a.id)+'.txt'), 'w+') as file:
                        file.write(str(settings))

                if settings[1][0]:
                    try:
                        exec(f'wall_alert{a.id}.cancel()', globals())
                        exec(f'del wall_alert{a.id}', globals())
                    except:
                        pass
                    exec(create_wall_code(a.id, settings), globals())

                if settings[2][0]:
                    try:
                        exec(f'buffer_alert{a.id}.cancel()', globals())
                        exec(f'del buffer_alert{a.id}', globals())
                    except:
                        pass
                    exec(create_buffer_code(a.id, settings), globals())
        except:
            pass

    daily_report.start()
@client.event
async def on_guild_join(a):

    print(f'\nJoined a new guild.\n{str(a.id)} - {a.name}\n')
    checkTxt(os.path.join(valueDir, str(a.id)+'.txt'), '')
    checkTxt(os.path.join(wallsDir, str(a.id)+'.txt'), '')
    checkTxt(os.path.join(buffersDir, str(a.id)+'.txt'), '')
    checkTxt(os.path.join(skinsDir, str(a.id)+'.txt'), '')
    checkTxt(os.path.join(todayDir, str(a.id)+'.txt'), '')
    checkTxt(os.path.join(prefixDir, str(a.id)+'.txt'), '??')
    checkTxt(os.path.join(valueLogsDir, str(a.id)+'.txt'), f":smiley: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** Invited **ValueBot** to the server.")
    checkTxt(os.path.join(wallsLogsDir, str(a.id)+'.txt'), f":smiley: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** Invited **ValueBot** to the server.")
    checkTxt(os.path.join(buffersLogsDir, str(a.id)+'.txt'), f":smiley: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** Invited **ValueBot** to the server.")
    perms = a.me.guild_permissions
    found = False
    if not perms.manage_roles:
        found = True
    elif not perms.manage_channels:
        found = True
    elif not perms.read_messages:
        found = True
    elif not perms.send_messages:
        found = True
    elif not perms.manage_messages:
        found = True
    elif not perms.embed_links:
        found = True
    elif not perms.read_message_history:
        found = True
    elif not perms.mention_everyone:
        found = True
    elif not perms.add_reactions:
        found = True
    if found:
        for i in a.text_channels:
            if i.name =='value-added':
                try:
                    embed = discord.Embed(title = ':gear: Not enough permissions.', description = 'The bot does not have the required permissions. Re-invite the bot using this [link](https://discordapp.com/api/oauth2/authorize?client_id=637575751583137822&permissions=268659792&scope=bot). If you are having problems, you can join the support [discord server](https://discord.gg/bnKE45S).', color = discord.Colour.blue())
                    await i.send(embed = embed)
                    break
                except:
                    pass
    else:
        with open(os.path.join(prefixDir, str(a.id)+'.txt'), 'r') as file:
            prefix = file.read()
        if os.path.exists(os.path.join(settingsDir, str(a.id)+'.txt')):
            with open(os.path.join(settingsDir, str(a.id)+'.txt'), 'r') as file:
                settings = eval(file.read())
            change = False
            if settings[0][0]:
                if client.get_channel(settings[0][3]) == None:
                    found = False
                    for i in a.text_channels:
                        if i.name == 'value-added':
                            found = True
                            embed = discord.Embed(title = ':gear: Settings - Channel - Value Management', description = f'Could not find the previously set value channel, so this channel has been automatically selected and will be used in the future to post embeds regarding value addition/removal.\n\nTo set a different channel for value embeds, do\n```{prefix}settings channel value <mention the channel>```', color = discord.Colour.blue())
                            embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                            await i.send(embed = embed)
                            settings[0][3] = i.id
                            break
                    if not found:
                        ch = await a.create_text_channel(name = 'value-added')
                        embed = discord.Embed(title = f'Settings - Channel - Value Management', description = f'Could not find the previously set value channel, so this channel has been created and will be used in the future to post embeds regarding value addition.\n\nTo set a different channel for value embeds, do\n```{prefix}settings channel value <mention the channel>```', color = discord.Colour.blue())
                        embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                        await ch.send(embed=embed)
                        settings[0][3] = ch.id
                    change = True
                if a.get_role(settings[0][4]) == None:
                    found = False
                    ch = client.get_channel(settings[0][3])
                    for i in a.roles:
                        if i.name == 'Faction Member':
                            found = True
                            embed = discord.Embed(title = ':gear: Settings - Role - Value', description = f'Could not find previously set role for __value module__.\nTo overcome this issue, the {i.mention} has been selected.\n\nTo change the role for __value module__,\n```{prefix}settings role value <mention the role>```', color = discord.Colour.blue())
                            embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}')
                            await ch.send(embed = embed)
                            settings[0][4] = i.id
                            change = True
                            await ch.set_permissions(i, read_messages = True, send_messages = True)
                    if not found:
                        r = await a.create_role(name = 'Faction Member')
                        embed = discord.Embed(title = ':gear: Settings - Role - Value', description = f'Could not find previously set role for __value module__.\nTo overcome this issue, the {r.mention} has been created.\n\nTo change the role for __value module__,\n```{prefix}settings role value <mention the role>```', color = discord.Colour.blue())
                        embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}')
                        await ch.send(embed = embed)
                        settings[0][4] = r.id
                        change = True
                        await ch.set_permissions(r, read_messages = True, send_messages = True)
            if settings[1][0]:
                if client.get_channel(settings[1][5]) == None:
                    found = False
                    for i in a.text_channels:
                        if i.name == 'wall-check':
                            found = True
                            embed = discord.Embed(title = ':gear: Settings - Channel - Wall-Checks', description = f'Could not find the previously set walls channel, so this channel has been automatically selected and will be used in the future for wall-check alerts.\n\nTo set a different walls channel, do\n```{prefix}settings channel walls <mention the channel>```', color = discord.Colour.blue())
                            embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                            await i.send(embed = embed)
                            settings[1][5] = i.id
                            break
                    if not found:
                        ch = await a.create_text_channel(name = 'wall-check')
                        embed = discord.Embed(title = f'Settings - Channel - Wall-Checks', description = f'Could not find the previously set walls channel, so this channel has been created and will be used in the future for wall-check alerts.\n\nTo set a different walls channel, do\n```{prefix}settings channel walls <mention the channel>```', color = discord.Colour.blue())
                        embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                        await ch.send(embed=embed)
                        settings[1][5] = ch.id
                    change = True
                if a.get_role(settings[1][6]) == None:
                    found = False
                    ch = client.get_channel(settings[1][5])
                    for i in a.roles:
                        if i.name == 'Faction Member':
                            found = True
                            embed = discord.Embed(title = ':gear: Settings - Role - Wall-Checks', description = f'Could not find previously set role for __wall-check module__.\nTo overcome this issue, the {i.mention} has been selected.\n\nTo change the role for __wall-check module__,\n```{prefix}settings role walls <mention the role>```', color = discord.Colour.blue())
                            embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}')
                            await ch.send(embed = embed)
                            settings[1][6] = i.id
                            change = True
                            await ch.set_permissions(i, read_messages = True, send_messages = True)
                    if not found:
                        r = await a.create_role(name = 'Faction Member')
                        embed = discord.Embed(title = ':gear: Settings - Role - Wall-Checks', description = f'Could not find previously set role for __wall-check module__.\nTo overcome this issue, the {r.mention} has been created.\n\nTo change the role for __wall-check module__,\n```{prefix}settings role walls <mention the role>```', color = discord.Colour.blue())
                        embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}')
                        await ch.send(embed = embed)
                        settings[1][6] = r.id
                        change = True
                        await ch.set_permissions(r, read_messages = True, send_messages = True)
                if settings[1][3] == None:
                    settings[1][3] = datetime.datetime.utcnow().strftime(dateformat)
                    change = True
            if settings[2][0]:
                if client.get_channel(settings[2][5]) == None:
                    found = False
                    for i in a.text_channels:
                        if i.name == 'buffer-check':
                            found = True
                            embed = discord.Embed(title = ':gear: Settings - Channel - Buffer-Checks', description = f'Could not find the previously set buffers channel, so this channel has been automatically selected and will be used in the future for buffer-check alerts.\n\nTo set a different buffers channel, do\n```{prefix}settings channel buffers <mention the channel>```', color = discord.Colour.blue())
                            embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                            await i.send(embed = embed)
                            settings[2][5] = i.id
                            break
                    if not found:
                        ch = await a.create_text_channel(name = 'buffer-check')
                        embed = discord.Embed(title = f'Settings - Channel - Buffer-Checks', description = f'Could not find the previously set buffers channel, so this channel has been created and will be used in the future for buffer-check alerts.\n\nTo set a different buffers channel, do\n```{prefix}settings channel buffers <mention the channel>```', color = discord.Colour.blue())
                        embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                        await ch.send(embed=embed)
                        settings[2][5] = ch.id
                    change = True
                if a.get_role(settings[2][6]) == None:
                    found = False
                    ch = client.get_channel(settings[2][5])
                    for i in a.roles:
                        if i.name == 'Faction Member':
                            found = True
                            embed = discord.Embed(title = ':gear: Settings - Role - Buffer-Checks', description = f'Could not find previously set role for __buffer-check module__.\nTo overcome this issue, the {i.mention} has been selected.\n\nTo change the role for __buffer-check module__,\n```{prefix}settings role buffers <mention the role>```', color = discord.Colour.blue())
                            embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}')
                            await ch.send(embed = embed)
                            settings[2][6] = i.id
                            change = True
                            await ch.set_permissions(i, read_messages = True, send_messages = True)
                    if not found:
                        r = await a.create_role(name = 'Faction Member')
                        embed = discord.Embed(title = ':gear: Settings - Role - Buffer-Checks', description = f'Could not find previously set role for __buffer-check module__.\nTo overcome this issue, the {r.mention} has been created.\n\nTo change the role for __buffer-check module__,\n```{prefix}settings role buffers <mention the role>```', color = discord.Colour.blue())
                        embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}')
                        await ch.send(embed = embed)
                        settings[2][6] = r.id
                        change = True
                        await ch.set_permissions(r, read_messages = True, send_messages = True)
                if settings[2][3] == None:
                    settings[2][3] = datetime.datetime.utcnow().strftime(dateformat)
                    change = True
            if change:
                with open(os.path.join(settingsDir, str(a.id)+'.txt'), 'w') as file:
                    file.write(str(settings))
        else:
            #          [status, realm, goal, ch, role], [status, checkfreq, remFreq, lastcheck, player, channel, role, tag on 1st alert], [same as previous]
            settings = [[True, 'WITHER', None, None, None],[False, 30, 10, None, None, None, None, False],[False, 30, 10, None, None, None, None, False]]
            found = False
            for i in a.text_channels:
                if i.name == 'value-added':
                    found = True
                    embed = discord.Embed(title = ':gear: Settings - Channel - Value Management', description = f'Could not find the previously set value channel, so this channel has been automatically selected and will be used in the future to post embeds regarding value addition/removal.\n\nTo set a different channel for value embeds, do\n```{prefix}settings channel value <mention the channel>```', color = discord.Colour.blue())
                    embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                    await i.send(embed = embed)
                    settings[0][3] = i.id
                    break
            if not found:
                ch = await a.create_text_channel(name = 'value-added')
                embed = discord.Embed(title = f'Settings - Channel - Value Management', description = f'Could not find the previously set value channel, so this channel has been created and will be used in the future to post embeds regarding value addition.\n\nTo set a different channel for value embeds, do\n```{prefix}settings channel value <mention the channel>```', color = discord.Colour.blue())
                embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                await ch.send(embed=embed)
                settings[0][3] = ch.id
            found = False
            ch = client.get_channel(settings[0][3])
            for i in a.roles:
                if i.name == 'Faction Member':
                    found = True
                    embed = discord.Embed(title = ':gear: Settings - Role - Value', description = f'Could not find previously set role for __value module__.\nTo overcome this issue, the {i.mention} has been selected.\n\nTo change the role for __value module__,\n```{prefix}settings role value <mention the role>```', color = discord.Colour.blue())
                    embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}')
                    await ch.send(embed = embed)
                    settings[0][4] = i.id
                    change = True
                    await ch.set_permissions(i, read_messages = True, send_messages = True)
            if not found:
                r = await a.create_role(name = 'Faction Member')
                embed = discord.Embed(title = ':gear: Settings - Role - Value', description = f'Could not find previously set role for __value module__.\nTo overcome this issue, the {r.mention} has been created.\n\nTo change the role for __value module__,\n```{prefix}settings role value <mention the role>```', color = discord.Colour.blue())
                embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}')
                await ch.send(embed = embed)
                settings[0][4] = r.id
                change = True
                await ch.set_permissions(r, read_messages = True, send_messages = True)
            with open(os.path.join(settingsDir, str(a.id)+'.txt'), 'w+') as file:
                file.write(str(settings))

        if settings[1][0]:
            try:
                exec(f'wall_alert{a.id}.cancel()', globals())
                exec(f'del wall_alert{a.id}', globals())
            except:
                pass
            exec(create_wall_code(a.id, settings), globals())


        if settings[2][0]:
            try:
                exec(f'buffer_alert{a.id}.cancel()', globals())
                exec(f'del buffer_alert{a.id}', globals())
            except:
                pass
            exec(create_buffer_code(a.id, settings), globals())

@client.event
async def on_message(msg):


    # print(f'[{msg.guild.name}][#{msg.channel.name}] {msg.author.name} : {msg.content}')
    if msg.author != client.user:
        with open(os.path.join(prefixDir, str(msg.guild.id)+'.txt'), 'r') as file:
            prefix = file.read()
        if msg.content.lower().startswith('??invite'):
            embed = discord.Embed(title = discord.Embed.Empty, description = "Invite me to your server using this [link](https://discordapp.com/api/oauth2/authorize?client_id=637575751583137822&permissions=268659792&scope=bot)\nMake sure to give all the required permissions to ensure proper performance.\n\nYou can also join the [discord server](https://discord.gg/bnKE45S) if you want. Feel free to report bugs / give suggestions there. Just don't expect anything crazy" , color = discord.Colour.gold())
            embed.set_author(name = 'Support | Meta Factions Bot', icon_url = client.user.avatar_url)
            embed.set_footer(text = '<3')
            await msg.channel.send(embed = embed)
            await msg.author.send(embed = embed)
        elif msg.content.lower().startswith('??credits') or  msg.content.lower().startswith('??credit') or  msg.content.lower().startswith('??info'):
            embed = discord.Embed(title = discord.Embed.Empty, description = 'This bot was made by `Kevqn#0869` and is being hosted by `xNightmare#9571`.\nIf you have any problems/suggestions, feel free to join the [support server](https://discord.gg/bnKE45S).', color = discord.Colour.blue())
            embed.set_author(name = 'Credits | Meta Factions Bot', icon_url = client.user.avatar_url)
            embed.set_footer(text = '<3')
            await msg.channel.send(embed =embed)
        if os.path.exists(os.path.join(settingsDir, str(msg.guild.id)+'.txt')):
            if msg.content.startswith(prefix):
                cmd = split_space_list(msg.content)[0][len(prefix):].lower()
                if cmd == 'help':
                    if msg.channel.permissions_for(msg.guild.me).send_messages:
                        # kevqn = client.get_user(268671188459454464)
                        cmd = split_space_list(split_space(msg.content))[0].lower()
                        if cmd == 'value':
                            with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                settings = eval(file.read())
                            if settings[0][0]:
                                message = '`ENABLED` :white_check_mark:'
                            else:
                                message = '`DISABLED` :x:'
                            embed = discord.Embed(title = '\U0001F4D4 Help - Value', description = f"**This module is currently** {message}\n\nThis module is made specifically for the __SaicoPvP__ server. This is useful to keep track of most contributing players and then distribute the rewards accordingly or whatever.\n\n**{prefix}add** - Add value to the faction. This command accepts spawner names.\n**{prefix}remove** - Remove value from other your/other player's account.\n**{prefix}top** or  **{prefix}highscore** -  Shows the top contributers.\n**{prefix}dailygoal** - See your Faction's daily progress.\n**{prefix}history** or **{prefix}log** - Show the history of executed commands. Value addition/removal and settings updates are shown here.\n\nDo `{prefix}help <command>` to find out more.\nDo `{prefix}settings value` for more info on settings for the __value module__.", color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                        elif cmd in ('walls', 'wall'):
                            with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                settings = eval(file.read())
                            if settings[1][0]:
                                message = '`ENABLED` :white_check_mark:'
                            else:
                                message = '`DISABLED` :x:'
                            embed = discord.Embed(title = '\U0001F4D4 Help - Walls', description = f"**This module is currently** {message}\n\nThis module sends alerts in a specific channel. \n\n**{prefix}clear** - Mark the walls clear.\n**{prefix}weewoo** - WE ARE GETTING RAIDED!! GET ON U BASTARDS!!\n**{prefix}lastcheck** - See the most recent wallcheck.\n**{prefix}setscore** - Set a user's score to a specific value.\n**{prefix}top** or **{prefix}highscores** - See the top wall checkers.\n**{prefix}log** or **{prefix}history** - See the history of executed commands.(related to walls module)\n\nDo `{prefix}help <command>` for more info.\nDo `{prefix}settings walls` for more info about the settings for __wall check__ module.", color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                        elif cmd in ('buffers', 'buffer'):
                            with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                settings = eval(file.read())
                            if settings[2][0]:
                                message = '`ENABLED` :white_check_mark:'
                            else:
                                message = '`DISABLED` :x:'
                            embed = discord.Embed(title = '\U0001F4D4 Help - Buffers', description = f"**This module is currently** {message}\n\nThis module is very similar to the walls module.(some might say that i just copy pasted from the walls module but ignore that).\n\n**{prefix}clear** - Mark the buffers clear.\n**{prefix}weewoo** - WE ARE GETTING RAIDED!! GET ON U BASTARDS!!\n**{prefix}lastcheck** - See the most recent buffercheck.\n**{prefix}setscore** - Set a user's score to a specific value.\n**{prefix}top** or **{prefix}highscores** - See the top buffer checkers.\n**{prefix}log** or **{prefix}history** - See the history of executed commands.(related to buffers module)\n\nDo `{prefix}help <command>` for more info.\nDo `{prefix}settings buffers` for more info about the settings for __buffer check__ module.", color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                        elif cmd in ('last', 'lastcheck', 'recent'):
                            embed = discord.Embed(title = f'\U0001f4d4 Help - {prefix}lastcheck', description = f'You can use this command to see the most recent wall/buffer check.\n**Usage-**\n```{prefix}lastcheck <walls/buffers>```', color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                        elif cmd == 'setscore':
                            embed = discord.Embed(title = f'\U0001f4d4 Help - {prefix}setscore', description = f'You can use this command to set the __wall/buffer__ check score of any user.\n**Usage-**\n```{prefix}setscore <walls/buffers> <score> <mention the user>```', color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                        elif cmd == 'add':
                            embed = discord.Embed(title = f'\U0001F4D4 Help - {prefix}add', description = f"This command is used to add value to the faction. Instead of going through the trouble to calculate how much the spawners you just added were worth, just enter what spawners you added and how many.\n**Usage**\n```{prefix}add <no. of spawners> <name of spawner>```\nThe bot accepts most shortforms. Example - `{prefix}add 15 sf` or `{prefix}add skele 10` or `{prefix}add 420k`\n\nThe spawner prices are different in different realms. So you can change your realm using `{prefix}settings realm`.", color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                        elif cmd == 'remove':
                            embed = discord.Embed(title = f'\U0001F4D4 Help - {prefix}remove', description = f"If you've accidentally added a couple billion dollars worth of value, worry not. Use this command to remove value from your account. Or you're an admin and you want to punish someone for being an asshole, you can use the __remove__ command. \n\nThe input is similar to the {prefix}add command. Admins can @mention other players to remove value from their account.\n\n**Usage :**\n```{prefix}remove <amount> <mention the player>```", color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                        elif cmd in ('dailygoals', 'dailygoal', 'goals', 'goal'):
                            embed = discord.Embed(title = '\U0001F4D4 - Help - Daily Goals', description = f"Set daily goals for your faction to reach. Once these goals are reached, a message is sent in the value channel. This feature comes with a command `{prefix}goal`. This shows the percentage of daily goal reached and also shows the amount added during the day till then.\n\nTo set this feature off, set the daily goal to `None`.\nTo set a custom value, do\n```{prefix}settings dailygoal <amount/None>```", color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                        elif cmd == 'clear':
                            with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                settings = eval(file.read())
                            ch = []
                            try:
                                ch.append(client.get_channel(settings[1][5]).mention)
                            except:
                                ch.append('None')
                            try:
                                ch.append(client.get_channel(settings[2][5]).mention)
                            except:
                                ch.append('None')
                            r = []
                            try:
                                r.append(msg.guild.get_role(settings[1][6]).mention)
                            except:
                                r.append('None')
                            try:
                                r.append(msg.guild.get_role(settings[2][6]).mention)
                            except:
                                r.append('None')
                            embed = discord.Embed(title = f'\U0001F4D4 Help - {prefix}clear', description = f"Use this command to mark the walls/buffers clear. If only one of these modules is enabled, then it will always clear that particular module. But if both the modules are enabled, then,\n\nTo clear the walls, do `{prefix}clear` in the walls channel (currently set to {ch[0]}) or just do `{prefix}clear walls` in any channel.\n\nTo clear the buffers, do `{prefix} clear` in the buffers channel (currently set to {ch[1]}) or just do `{prefix}clear buffers` in any channel.\n\nYou the appropriate role to mark the walls/buffers clear.\n**Walls Role**   - {r[0]}\n**Buffers Role** - {r[1]}", color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                        elif cmd == 'weewoo':
                            with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                settings = eval(file.read())
                            try:
                                r = msg.guild.get_role(settings[1][6]).mention
                            except:
                                r = 'None'
                            embed = discord.Embed(title = f'\U0001F4D4 Help - {prefix}weewoo', description = f"Use this command to send multiple alerts in hope that some players get on to support you in defending the base against the raiders. ~~(or you could be an asshole and do it for no reason)~~\nYou need the walls module's role to execute this command. (currently set to {r})", color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                        elif cmd in ('log', 'logs', 'history'):
                            with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                settings = eval(file.read())
                            ch = []
                            try:
                                ch.append(client.get_channel(settings[0][3]).mention)
                            except:
                                ch.append('None')
                            try:
                                ch.append(client.get_channel(settings[1][5]).mention)
                            except:
                                ch.append('None')
                            try:
                                ch.append(client.get_channel(settings[2][5]).mention)
                            except:
                                ch.append('None')
                            embed = discord.Embed(title = f'\U0001F4D4 Help - {prefix}history', description = f"Use this command to see the history of the major commands executed in specific modules. Otherwise, you would have to execute the command in that module's channel or specify the module in the command.\n\nTo see the __value module's__ history, do `{prefix}history` in the value channel (currently set to {ch[0]}) or do `{prefix}history value` in any channel.\n\nTo see the __walls module's__ history, do `{prefix}history` in the walls channel (currently set to {ch[1]}) or do `{prefix}history walls` in any channel.\n\nTo see the __buffer module's__ history, do `{prefix}history` in the buffers channel (currently set to {ch[2]}) or do `{prefix}history buffers` in any channel.\n\nYou will need the module's role to view it's history.", color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                        elif cmd in ('highscores', 'highscore', 'top'):
                            with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                settings = eval(file.read())
                            ch = []
                            try:
                                ch.append(client.get_channel(settings[0][3]).mention)
                            except:
                                ch.append('None')
                            try:
                                ch.append(client.get_channel(settings[1][5]).mention)
                            except:
                                ch.append('None')
                            try:
                                ch.append(client.get_channel(settings[2][5]).mention)
                            except:
                                ch.append('None')
                            embed = discord.Embed(title = f'\U0001F4D4 Help - {prefix}highscore', description = f"Use this command to see the highscores of the module.\n\nTo see the __value module's__ highscores, do `{prefix}top` in the value channel (currently set to {ch[0]}) or do `{prefix}top value` in any channel.\n\nTo see the __walls module's__ highscores, do `{prefix}top` in the walls channel (currently set to {ch[1]}) or do `{prefix}top walls` in any channel.\n\nTo see the __buffer module's__ highscores, do `{prefix}top` in the buffers channel (currently set to {ch[2]}) or do `{prefix}top buffers` in any channel.\n\nYou will need the module's role to view it's highscores.", color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                        else:
                            embed = discord.Embed(title = '\U0001F4D4 Help', description = 'There are 3 separate modules of the bot.', color = discord.Colour.blue())
                            embed.add_field(name = ':money_with_wings: **Value Management Module**', value = f'This module has commands related to value addition/removal. This enabled you to keep track of the contribution of each player. Do `{prefix}help value` to see a detailed page of the value module and its commands.' , inline = False)
                            embed.add_field(name = ':alarm_clock: **Wall-Check Module**', value = f'This module has commands related to walls. You get alerted every few minutes (which you can configure) to check walls. Score is kept track of. Do `{prefix}help walls` to see a detailed page of the walls module and its commands.', inline = False)
                            embed.add_field(name = ':stopwatch: **Buffer-Check Module**', value = f'Similar to the wall-check module, this module sends alerts to check buffers. Do `{prefix}help buffers` to see a detailed page of buffers module and its commands.', inline = False)
                            embed.add_field(name = '**Other Commands**', value = f'Some other commands include -\n`{prefix}prefix`, `{prefix}skin`, `{prefix}invite`, `{prefix}info`.\n\nTo see detailed info about a particular command, do `{prefix}help <command>` or do the command with no arguments.', inline = False)
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                elif cmd == 'clear':
                    perms = msg.channel.permissions_for(msg.guild.me)
                    if len(msg.mentions) > 1:
                        if perms.send_messages:
                            await msg.channel.send('You can mention only one person.')
                    else:
                        if len(msg.mentions) == 1:
                            target = msg.mentions[0]
                        else:
                            target = msg.author
                        with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                            settings = eval(file.read())
                        i = False
                        if settings[1][0] and settings[2][0]:
                            cmd = split_space(msg.content).replace(' ', '').replace(f'<@!{target.id}>', '').lower()
                            if cmd == '':
                                if msg.channel.id == settings[1][5]:
                                    i = 'walls'
                                elif msg.channel.id == settings[2][5]:
                                    i = 'buffers'
                                else:
                                    if perms.send_messages:
                                        embed = discord.Embed(title = 'Settings - Check Alerts', description = f'To clear the walls, either do `{prefix}clear` in {client.get_channel(settings[1][5]).mention} or do `{prefix}clear walls` in any channel the bot can see.\n\nTo clear the buffers, either do `{prefix}clear` in {client.get_channel(settings[2][5]).mention} or do `{prefix}clear buffers` in any channel the bot can see.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                            elif cmd == 'walls' or cmd == 'wall':
                                    i = 'walls'
                            elif cmd == 'buffer' or cmd == 'buffers':
                                    i = 'buffers'
                            else:
                                if perms.send_messages:
                                    embed = discord.Embed(title = 'Settings - Check Alerts', description = f'Unknown argument - `{cmd}`\n\nTo mark walls clear, either do `{prefix}clear` in {client.get_channel(settings[1][5]).mention} or do `{prefix}clear walls` in any channel the bot can see.\n\nTo mark the buffers clear, either do `{prefix}clear` in {client.get_channel(settings[2][5]).mention} or do `{prefix}clear buffers` in any channel the bot can see.', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed = embed)
                        elif settings[1][0]:
                            i = 'walls'
                        elif settings[2][0]:
                            i = 'buffers'
                        else:
                            if perms.send_messages:
                                embed = discord.Embed(title = 'Settings - Check Alerts', description = f'This command cannot be used since both __wall & buffer__ check alerts have been turned `OFF`. To enable them, do\n```{prefix}settings <walls/buffers> on```')
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed = embed)
                        if not i == False:
                            if i == 'walls':
                                role = msg.guild.get_role(settings[1][6])
                                if role in msg.author.roles or msg.author.guild_permissions.administrator:
                                    ct = datetime.datetime.utcnow()
                                    td = ct - datetime.datetime.strptime(settings[1][3], dateformat)
                                    if td.seconds >= 10:
                                        if perms.manage_messages:
                                            await msg.delete()
                                        exec(f'wall_alert{msg.guild.id}.cancel()', globals())
                                        exec(f'del wall_alert{msg.guild.id}', globals())
                                        ch = client.get_channel(settings[1][5])
                                        perms = ch.permissions_for(msg.guild.me)
                                        if perms.read_message_history:
                                            messages = await ch.history(limit=30).flatten()
                                            for i in messages:
                                                if i.author.id == client.user.id:
                                                    if len(i.embeds) == 1:
                                                        try:
                                                            title = i.embeds[0].title
                                                            if split_space(title) == 'Time to check walls!':
                                                                if perms.manage_messages:
                                                                    await i.delete()
                                                                break
                                                            elif title.endswith('walls clear.'):
                                                                if perms.manage_messages:
                                                                    await i.clear_reactions()
                                                                break
                                                        except:
                                                            pass
                                        with open(os.path.join(wallsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                            text = file.read().split('\n')
                                            found = False
                                            if text == ['']:
                                                text = [f'{target.id} 1']
                                                score = '1'
                                            else:
                                                for i in range(len(text)):
                                                    if text[i].startswith(str(target.id)):
                                                        score = str(int(split_space(text[i]))+1)
                                                        text[i] = text[i][:19] + score
                                                        found = True
                                                if not found:
                                                    text.append(f'{target.id} 1')
                                                    score = '1'
                                            file.truncate(0)
                                            file.seek(0,0)
                                            file.write('\n'.join(text))
                                        with open(os.path.join(wallsLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                            text = file.read()
                                            file.seek(0,0)
                                            if target.id == msg.author.id:
                                                file.write(f":white_check_mark: **[{ct.strftime(dateformat)}]:** {target.mention}" + '\n' + text)
                                            else:
                                                file.write(f":white_check_mark: **[{ct.strftime(dateformat)}]:** {target.mention} ({msg.author.mention})" + '\n' + text)
                                        if perms.send_messages:
                                            with open(os.path.join(skinsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                                text = file.read().split('\n')
                                            found = False
                                            for i in text:
                                                if i.startswith(str(target.id)):
                                                    skin = f'https://minotar.net/avatar/{i[19:]}'
                                                    found = True
                                                    break
                                            if not found:
                                                skin = ''

                                            embed = discord.Embed(title = f':white_check_mark: **{target.display_name}** has marked walls clear.', color = discord.Colour.green())
                                            embed.add_field(name = 'Checked by', value = target.mention, inline = True)
                                            embed.add_field(name = 'Score', value = score, inline = True)
                                            td = datetime.timedelta(days = td.days, seconds = td.seconds)
                                            embed.add_field(name = 'Time Taken', value = str(td), inline = True)
                                            embed.add_field(name = 'Time Checked', value = ct.strftime(dateformat))
                                            embed.set_footer(text = msg.author.display_name, icon_url = msg.author.avatar_url)
                                            embed.set_thumbnail(url = skin)
                                            msg = await ch.send(embed = embed)
                                            if perms.add_reactions:
                                                await msg.add_reaction('\u2705')
                                                await msg.add_reaction('\U0001f4a3')
                                        settings[1][3] = datetime.datetime.utcnow().strftime(dateformat)
                                        settings[1][4] = target.id
                                        with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                            file.write(str(settings))
                                        exec(create_wall_code(msg.guild.id, settings), globals())
                                    else:
                                        if perms.send_messages:
                                            await msg.channel.send('You are doing that too quickly, try slowing down.')
                                else:
                                    if perms.send_messages:
                                        embed = discord.Embed(title = ':gear: Settings - Wall-Check', description = f'You cannot use this command because you do not have the {role.mention} role.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}')
                                        await msg.channel.send(embed=embed)
                            else:
                                role = msg.guild.get_role(settings[2][6])
                                if role in msg.author.roles or msg.author.guild_permissions.administrator:
                                    ct = datetime.datetime.utcnow()
                                    td = ct - datetime.datetime.strptime(settings[2][3], dateformat)
                                    if td.seconds >= 10:
                                        if perms.manage_messages:
                                            await msg.delete()
                                        exec(f'buffer_alert{msg.guild.id}.cancel()', globals())
                                        exec(f'del buffer_alert{msg.guild.id}', globals())
                                        ch = client.get_channel(settings[2][5])
                                        perms = ch.permissions_for(msg.guild.me)
                                        if perms.read_message_history:
                                            messages = await ch.history(limit=30).flatten()
                                            for i in messages:
                                                if i.author.id == client.user.id:
                                                    if len(i.embeds) == 1:
                                                        try:
                                                            title = i.embeds[0].title
                                                            if split_space(title) == 'Time to check buffers!':
                                                                if perms.manage_messages:
                                                                    await i.delete()
                                                                break
                                                            elif title.endswith('buffers clear.'):
                                                                if perms.manage_messages:
                                                                    await i.clear_reactions()
                                                                break
                                                        except:
                                                            pass
                                        with open(os.path.join(buffersDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                            text = file.read().split('\n')
                                            found = False
                                            if text == ['']:
                                                text = [f'{target.id} 1']
                                                score = '1'
                                            else:
                                                for i in range(len(text)):
                                                    if text[i].startswith(str(target.id)):
                                                        score = str(int(split_space(text[i]))+1)
                                                        text[i] = text[i][:19] + score
                                                        found = True
                                                if not found:
                                                    text.append(f'{target.id} 1')
                                                    score = '1'
                                            file.truncate(0)
                                            file.seek(0,0)
                                            file.write('\n'.join(text))
                                        with open(os.path.join(buffersLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                            text = file.read()
                                            file.seek(0,0)
                                            if target.id == msg.author.id:
                                                file.write(f":white_check_mark: **[{ct.strftime(dateformat)}]:** {target.mention}" + '\n' + text)
                                            else:
                                                file.write(f":white_check_mark: **[{ct.strftime(dateformat)}]:** {target.mention} ({msg.author.mention})" + '\n' + text)

                                        if perms.send_messages:
                                            with open(os.path.join(skinsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                                text = file.read().split('\n')
                                            found = False
                                            for i in text:
                                                if i.startswith(str(target.id)):
                                                    skin = f'https://minotar.net/avatar/{i[19:]}'
                                                    found = True
                                                    break
                                            if not found:
                                                skin = ''
                                            embed = discord.Embed(title = f':white_check_mark: **{target.display_name}** has marked buffers clear.', color = discord.Colour.green())
                                            embed.add_field(name = 'Checked by', value = target.mention, inline = True)
                                            embed.add_field(name = 'Score', value = score, inline = True)
                                            td = datetime.timedelta(days = td.days, seconds = td.seconds)
                                            embed.add_field(name = 'Time Taken', value = str(td), inline = True)
                                            embed.add_field(name = 'Time Checked', value = ct.strftime(dateformat))
                                            embed.set_footer(text = msg.author.display_name, icon_url = msg.author.avatar_url)
                                            embed.set_thumbnail(url = skin)
                                            msg = await ch.send(embed = embed)
                                            if perms.add_reactions:
                                                await msg.add_reaction('\u2705')
                                                await msg.add_reaction('\U0001f4a3')
                                        settings[2][3] = datetime.datetime.utcnow().strftime(dateformat)
                                        settings[2][4] = target.id
                                        with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                            file.write(str(settings))
                                        exec(create_buffer_code(msg.guild.id, settings), globals())
                                    else:
                                        if perms.send_messages:
                                            await msg.channel.send('You are doing that too quickly, try slowing down.')
                                else:
                                    if perms.send_messages:
                                        embed = discord.Embed(title = ':gear: Settings - Buffer-Check', description = f'You cannot use this command because you do not have the {role.mention} role.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}')
                                        await msg.channel.send(embed=embed)
                elif cmd == 'add':
                    with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                        settings = eval(file.read())
                    perms = msg.channel.permissions_for(msg.guild.me)
                    if settings[0][0] :
                        role = msg.guild.get_role(settings[0][4])
                        if role in msg.author.roles or msg.author.guild_permissions.administrator:
                            cmdraw = split_space(msg.content)
                            cmd = split_space(msg.content).replace(' ', '').lower()
                            if cmd == '':
                                if perms.send_messages:
                                    embed = discord.Embed(title = f':gear: Help - {prefix}Add', description = f'You can use this command to add value to the faction.\n\n**Usage**\n\n```{prefix}add <no. of spawners> <spawner name>```\n__Example__ - `{prefix}add 12 blazes` or `{prefix}add sf 20`.\n\n```{prefix}add <amount>```\n*__Example__- `{prefix}add 30mil` or `{prefix}add 420k`', color = discord.Colour.blue())
                                    embed.set_footer(text=f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed = embed)
                            else:
                                target = msg.mentions
                                if len(target) > 1:
                                    if perms.send_messages:
                                        await msg.channel.send('You can only mention one person.')
                                else:
                                    if len(target) ==1:
                                        target = target[0]
                                        if f'<@!{target.id}>' in cmd:
                                            cmdraw = cmdraw.replace(f'<@!{target.id}>', '')
                                            cmd = cmd.replace(f'<@!{target.id}>', '')
                                        elif f'<@{target.id}>' in cmd:
                                            cmdraw = cmdraw.replace(f'<@{target.id}>', '')
                                            cmd = cmd.replace(f'<@{target.id}>', '')
                                    else:
                                        target = msg.author
                                    if pure_int(cmd):
                                        cmd = int(eval(cmd))
                                    else:
                                        cmd = cmd.replace(',', '')
                                        found = False
                                        if settings[0][1] in ('OVERLORD', 'WARLOCK'):
                                            for i in spawner_rates[1]:
                                                if i[0] in cmd:
                                                    found = True
                                                    if not cmd.replace(i[0], '').replace(' ', '') == '':
                                                        cmd = f"{cmd.replace(i[0], '')}*{i[1]}"
                                                    else:
                                                        cmd = int(i[1])
                                                    break
                                        else:
                                            for i in spawner_rates[0]:
                                                if i[0] in cmd:
                                                    found = True
                                                    if not cmd.replace(i[0], '').replace(' ', '') == '':
                                                        cmd = f"{cmd.replace(i[0], '')}*{i[1]}"
                                                    else:
                                                        cmd = int(i[1])
                                                    break
                                        if not found:
                                            for i in [
                                                ['k', '1000'],
                                                ['billion', '1000000000'],
                                                ['bill', '1000000000'],
                                                ['bil', '1000000000'],
                                                ['b', '1000000000'],
                                                ['million', '1000000'],
                                                ['mill', '1000000'],
                                                ['mil', '1000000'],
                                                ['m', '1000000']]:
                                                if i[0] in cmd:
                                                    cmd = int(eval(cmd.replace(i[0], f'*{i[1]}')))
                                                    break
                                        if not pure_int(cmd):
                                            if perms.send_messages:
                                                await msg.channel.send('Invalid input.')
                                        else:
                                            try:
                                                cmd = int(eval(cmd))
                                            except:
                                                pass
                                    try:
                                        if eval(str(cmd)) < 0 :
                                            if perms.send_messages:
                                                await msg.channel.send('You cannot add negative value.')
                                        else:
                                            with open(os.path.join(valueDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                                text = file.read().split('\n')
                                                if text == ['']:
                                                    text = [f'{target.id} {cmd}']
                                                    score = str(cmd)
                                                    total = score
                                                else:
                                                    found = False
                                                    total = 0
                                                    for i in range(len(text)):
                                                        if text[i].startswith(str(target.id)):
                                                            score = str(int(int(eval(text[i][19:]))+cmd))
                                                            text[i] = text[i][:19] + score
                                                            found = True
                                                        total += int(text[i][19:])
                                                    if not found:
                                                        text.append(f'{target.id} {cmd}')
                                                        score = cmd
                                                        total += cmd
                                                file.truncate(0)
                                                file.seek(0,0)
                                                file.write('\n'.join(text))
                                            if perms.manage_messages:
                                                await msg.delete()
                                            ch = client.get_channel(settings[0][3])
                                            perms = ch.permissions_for(msg.guild.me)
                                            if perms.send_messages:
                                                with open(os.path.join(skinsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                                    text = file.read().split('\n')
                                                found = False
                                                for i in text:
                                                    if i.startswith(str(target.id)):
                                                        skin = f'https://minotar.net/avatar/{i[19:]}'
                                                        found = True
                                                        break
                                                if not found:
                                                    skin = ''
                                                embed = discord.Embed(title = f':heavy_plus_sign: **{msg.author.name}** added value using ``{prefix}add``.')
                                                embed.add_field(name = 'Added By', value = target.mention, inline = True)
                                                embed.add_field(name = 'Added value', value = f'{cmdraw} = {commas(str(cmd))}', inline = True)
                                                embed.add_field(name = 'Total Score', value = f'{commas(str(score))} $', inline = True)
                                                embed.add_field(name = 'Fac Value', value = f'{commas(str(total))} $', inline = True)
                                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                                embed.set_thumbnail(url = skin)
                                                await ch.send(embed = embed)

                                            if target == msg.author:
                                                with open(os.path.join(valueLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                                    text = file.read()
                                                    file.seek(0,0)
                                                    file.write(f":moneybag: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {target.mention} : added `{cmdraw}`.\n{text}")
                                            else:
                                                with open(os.path.join(valueLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                                    text = file.read()
                                                    file.seek(0,0)
                                                    file.write(f":moneybag: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {target.mention} ({msg.author.mention}) : added `{cmdraw}`.\n{text}")
                                            if not settings[0][3] == None:
                                                with open(os.path.join(todayDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                                    text = file.read().split('\n')
                                                    if text == ['']:
                                                        text = [f'{target.id} {cmd}']
                                                        total = cmd
                                                    else:
                                                        found = False
                                                        total = 0
                                                        for i in range(len(text)):
                                                            if text[i].startswith(str(target.id)):
                                                                found = True
                                                                text[i] = text[i][:19] + str(int(int(eval(text[i][19:]))+cmd))
                                                            total += int(text[i][19:])
                                                        if not found:
                                                            text.append(f'{target.id} {cmd}')
                                                            total += cmd
                                                    if not settings[0][2] == None  and total > settings[0][2] and total - cmd < settings[0][2]:
                                                        if perms.send_messages:
                                                            embed = discord.Embed(title = ':tada: We have reached our daily goal. :tada:', description = f"Good job everyone! We have reached our daily goal of **{commas(str(settings[0][2]))} $**.\nKeep up the good work. Let's see how higher we can go.\nDo `{prefix}goal` for more info.", color = discord.Colour.gold())
                                                            await ch.send(embed = embed)
                                                    file.truncate(0)
                                                    file.seek(0,0)
                                                    file.write('\n'.join(text))
                                    except SyntaxError:
                                        pass

                        else:
                            if perms.send_messages:
                                embed = discord.Embed(title = ':gear: Settings - Value', description = f'You cannot use that command because you do not have the {role.mention} role.', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed = embed)
                    else:
                        if perms.send_messages:
                            embed = discord.Embed(title = 'Settings - Value Management', description = ':x: You cannot use that command because the __Value Management__ module has been turned `OFF`.', color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed=embed)
                elif cmd == 'remove':
                    with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                        settings = eval(file.read())
                    if settings[0][0]:
                        r = msg.guild.get_role(settings[0][4])
                        if r in msg.author.roles or msg.author.guild_permissions.administrator:
                            cmdraw = split_space(msg.content)
                            cmd = split_space(msg.content).replace(' ', '').lower()
                            if cmd == '':
                                embed = discord.Embed(title = f'\U0001F4D4 Help - {prefix}remove', description = f"If you've accidentally added a couple billion dollars worth of value, worry not. Use this command to remove value from your account. Or you're an admin and you want to punish someone for being an asshole, you can use the __remove__ command. \n\nThe input is similar to the {prefix}add command. Admins can @mention other players to remove value from their account.\n\n**Usage :**\n```{prefix}remove <amount> <mention the player>```", color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed = embed)
                            else:
                                target = msg.mentions
                                if len(target) > 1:
                                    await msg.channel.send('You can only mention one person.')
                                else:
                                    if len(target) ==1:
                                        target = target[0]
                                        if f'<@!{target.id}>' in cmd:
                                            cmdraw = cmdraw.replace(f'<@!{target.id}>', '')
                                            cmd = cmd.replace(f'<@!{target.id}>', '')
                                        elif f'<@{target.id}>' in cmd:
                                            cmdraw = cmdraw.replace(f'<@{target.id}>', '')
                                            cmd = cmd.replace(f'<@{target.id}>', '')
                                    else:
                                        target = msg.author
                                    if target == msg.author or msg.author.guild_permissions.administrator:
                                        if pure_int(cmd):
                                            cmd = int(eval(cmd))
                                        else:
                                            cmd = cmd.replace(',', '')
                                            found = False
                                            if settings[0][1] in ('OVERLORD', 'WARLOCK'):
                                                for i in spawner_rates[1]:
                                                    if i[0] in cmd:
                                                        found = True
                                                        if not cmd.replace(i[0], '').replace(' ', '') == '':
                                                            cmd = f"{cmd.replace(i[0], '')}*{i[1]}"
                                                        else:
                                                            cmd = int(i[1])
                                                        break
                                            else:
                                                for i in spawner_rates[0]:
                                                    if i[0] in cmd:
                                                        found = True
                                                        if not cmd.replace(i[0], '').replace(' ', '') == '':
                                                            cmd = f"{cmd.replace(i[0], '')}*{i[1]}"
                                                        else:
                                                            cmd = int(i[1])
                                                        break
                                            if not found:
                                                for i in [
                                                    ['k', '1000'],
                                                    ['billion', '1000000000'],
                                                    ['bill', '1000000000'],
                                                    ['bil', '1000000000'],
                                                    ['b', '1000000000'],
                                                    ['million', '1000000'],
                                                    ['mill', '1000000'],
                                                    ['mil', '1000000'],
                                                    ['m', '1000000']]:
                                                    if i[0] in cmd:
                                                        cmd = int(eval(cmd.replace(i[0], f'*{i[1]}')))
                                                        break
                                            if not pure_int(cmd):
                                                await msg.channel.send('Invalid input.')
                                            else:
                                                try:
                                                    cmd = int(eval(cmd))
                                                except:
                                                    pass
                                        if eval(str(cmd)) < 0 :
                                            await msg.channel.send('You cannot enter negative amount.')
                                        else:
                                            with open(os.path.join(valueDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                                text = file.read().split('\n')
                                                if text == ['']:
                                                    await msg.channel.send("User's account was not found.")
                                                    change = False
                                                else:
                                                    found = False
                                                    change = False
                                                    for i in range(len(text)):
                                                        if text[i].startswith(str(target.id)):
                                                            score = int(int(eval(text[i][19:]))-cmd)
                                                            if score < 0:
                                                                await msg.channel.send('User does not have that much amount.')
                                                            else:
                                                                text[i] = text[i][:19] + str(score)
                                                                change = True
                                                            found = True
                                                            break

                                                    if not found:
                                                        await ("User's account was not found.")

                                                if change:
                                                    file.truncate(0)
                                                    file.seek(0,0)
                                                    file.write('\n'.join(text))
                                                    await client.get_channel(settings[0][3]).send(f"{msg.author.mention} removed **{commas(str(cmd))} $** from {target.mention}'s account.")
                                                    if target == msg.author:
                                                        with open(os.path.join(valueLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                                            text = file.read()
                                                            file.seek(0,0)
                                                            file.write(f":warning: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : removed `{cmdraw}` from their account.\n{text}")
                                                    else:
                                                        with open(os.path.join(valueLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                                            text = file.read()
                                                            file.seek(0,0)
                                                            file.write(f":warning: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : removed `{cmdraw}` from {target.mention}'s account.\n{text}")
                                                    with open(os.path.join(todayDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                                        text = file.read().split('\n')
                                                        if text == ['']:
                                                            text = f'{target.id} -{cmd}'
                                                        else:
                                                            found = 0
                                                            for i in range(len(text)):
                                                                if text[i].startswith(str(target.id)):
                                                                    found = True
                                                                    text[i] = text[i][:19] + str(int(int(eval(text[i][19:]))-cmd))
                                                                    break
                                                            if not found:
                                                                text.append(f'{target.id} -{cmd}')
                                                        file.truncate(0)
                                                        file.seek(0,0)
                                                        file.write('\n'.join(text))
                                    else:
                                        embed = discord.Embed(title = f':gear: Settings - {prefix}remove', description = ":X: You do not have permission to remove value from someone else's account.", color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                        else:
                            embed = discord.Embed(title = ':gear: Settings - Value', description = f'You cannot use that command because you do not have the {role.mention} role.', color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                    else:
                        embed = discord.Embed(title = 'Settings - Value Management', description = ':x: You cannot use that command because the __Value Management__ module has been turned `OFF`.', color = discord.Colour.blue())
                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                        await msg.channel.send(embed=embed)
                elif cmd == 'setscore':
                    with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                        settings = eval(file.read())
                    cmd = split_space_list(split_space(msg.content))[0].lower()
                    score = False
                    name = False
                    if cmd in ('walls','wall'):
                        name = 'wall'
                        if settings[1][0]:
                            score = wallsDir
                            logs = wallsLogsDir
                    elif cmd in ('buffers', 'buffer'):
                        name = 'buffer'
                        if settings[2][0]:
                            score = buffersDir
                            logs = buffersLogsDir

                    if name == False:
                        embed = discord.Embed(title  = f'\U0001f4d4 Help - {prefix}setscore', description = f'You can use this command to set the wall/buffer check score to a certain value.\n**Usage-**\n```{prefix}setscore <walls/buffers> <mention the user>```', color = discord.Colour.blue())
                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                        await msg.channel.send(embed = embed)
                    else:
                        if msg.author.guild_permissions.administrator:
                            if score == False:
                                embed = discord.Embed(title  = f':gear: - Setttings - {prefix}setscore', description = f':x: You cannot use that command because the __{name}s__ module is `DISABLED`.', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed = embed)
                            else:
                                target = msg.mentions
                                if len(target)> 1:
                                    await msg.channel.send('You can only mention one person.')
                                else:
                                    cmd = split_space(split_space(msg.content)).replace(' ','')
                                    if len(target) == 0:
                                        target = msg.author
                                    elif len(target) == 1:
                                        target = target[0]
                                        if f'<@!{target.id}>' in cmd:
                                            cmd = cmd.replace(f'<@!{target.id}>', '')
                                        elif f'<@{target.id}>' in cmd:
                                            cmd = cmd.replace(f'<@{target.id}>', '')
                                    try:
                                        cmd = int(eval(str(cmd)))
                                    except:
                                        await msg.channel.send('Invalid input.')
                                    else:
                                        with open(os.path.join(score, str(msg.guild.id)+'.txt'), 'r+') as file:
                                            text = file.read().split('\n')
                                            if text == ['']:
                                                text = [f'{target.id} {cmd}']
                                            else:
                                                found = False
                                                for i in range(len(text)):
                                                    if text[i].startswith(str(target.id)):
                                                        found = True
                                                        text[i] = f'{target.id} {cmd}'
                                                        break
                                                if not found:
                                                    text.append(f'{target.id} {cmd}')
                                            file.truncate(0)
                                            file.seek(0,0)
                                            file.write('\n'.join(text))
                                        with open(os.path.join(logs, str(msg.guild.id)+'.txt'), 'r+') as file:
                                            text = file.read()
                                            file.seek(0,0)
                                            if msg.author == target:
                                                file.write(f':gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : set their score to `{cmd}`.\n{text}')
                                            else:
                                                file.write(f":gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention}: set {target.mention}'s score to {cmd}.\n{text}")
                                        await msg.channel.send(f"{msg.author.mention} has set {target.mention}'s __{name}-check__ score to {cmd}.")
                        else:
                            embed = discord.Embed(title  = f':gear: Settings - {prefix}setscore', description = f':x: You do not have permission to execute that command.', color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                elif cmd == 'weewoo':
                    with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                        settings = eval(file.read())
                    r = msg.guild.get_role(settings[1][6])
                    if r in msg.author.roles or msg.author.guild_permissions.administrator:
                        if settings[1][0]:
                            ct = datetime.datetime.utcnow().strftime(dateformat)
                            td = ct - datetime.datetime.strptime(settings[1][3], dateformat)
                            if td.seconds >= 10:
                                ch = client.get_channel(settings[1][5])
                                exec(f'wall_alert{msg.guild.id}.cancel()', globals())
                                exec(f'del wall_alert{msg.guild.id}')
                                if settings[2][0]:
                                    exec(f'buffer_alert{msg.guild.id}.cancel()', globals())
                                    exec(f'del buffer_alert{msg.guild.id}')
                                messages = await ch.history(limit=30).flatten()
                                for i in messages:
                                    if i.author.id == client.user.id:
                                        if len(i.embeds) == 1:
                                            try:
                                                if split_space(i.embeds[0].title) == 'Time to check walls!':
                                                    await i.delete()
                                                    break
                                            except:
                                                pass
                                embed = discord.Embed(title = '', description = '```WeeWoo! We are being raided! Help!```', color = discord.Colour.red())
                                embed.add_field(name = 'Triggered by', value = msg.author.display_name)
                                embed.add_field(name = 'Time', value = ct)
                                embed.set_author(name = 'We are being raided! Help! Get online!', icon_url = 'https://www.logolynx.com/images/logolynx/6f/6f5bdc86a8c983a9a266765b10f1debd.png')
                                embed.set_footer(text = 'stop reading this and GET ON!')
                                embed.set_thumbnail(url = 'https://www.logolynx.com/images/logolynx/6f/6f5bdc86a8c983a9a266765b10f1debd.png')
                                await ch.send(embed = embed)
                                await ch.send(f'Weewoo! We are being raided! Get on! <@&{msg.guild.get_role(settings[1][6]).id}>\n'*3)
                                with open(os.path.join(wallsLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                    text = file.read()
                                    file.seek(0,0)
                                    file.write(f':bomb: **[{ct}]:** {msg.author.mention}\n{text}')
                                with open(os.path.join(buffersLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                    text = file.read()
                                    file.seek(0,0)
                                    file.write(f':bomb: **[{ct}]:** {msg.author.mention}\n{text}')
                                settings[1][3] = ct
                                settings[1][4] = msg.author.id
                                with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                    file.write(str(settings))
                                exec(create_wall_code(msg.guild.id, settings), globals())
                                if settings[2][0]:
                                    exec(create_buffer_code(msg.guild.id, settings), globals())
                            else:
                                if msg.channel.permissions_for(msg.guild.me).send_messages:
                                    await msg.channel.send('You are doing that too quickly, try slowing down.')
                        else:
                            embed = discord.Embed(title = ':gear: Settings - Walls', description = f':x: You cannot use that command because the __wall check__ module is `DISABLED`.\nTo enable the __wall check__ module, do `{prefix}settings walls on`', color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                    else:
                        embed = discord.Embed(title = ':gear: Settings - Walls', description = ':x: You do not have permission to execute that command.', color = discord.Colour.blue())
                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                        await msg.channel.send(embed = embed)
                elif cmd in ('last', 'recent', 'lastcheck'):
                    with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                        settings = eval(file.read())
                    if settings[1][0] and settings[2][0]:
                        cmd = split_space_list(split_space(msg.content))[0].lower()
                        if cmd in ('wall', 'walls'):
                            cmd = 'walls'
                        elif cmd in ('buffer', 'buffers'):
                            cmd = 'buffers'
                        elif msg.channel.id == settings[1][5]:
                            cmd = 'walls'
                        elif msg.channel.id == settings[2][5]:
                            cmd = 'buffers'
                        else:
                            cmd = None
                            embed = discord.Embed(title = f':gear: Settings - {prefix}clear', description = f':x: You cannot use that command because both walls and buffers are `ENABLED`.\n\nTo see the recent __wall-check__, do `{prefix}lastcheck` in {client.get_channel(settings[1][5]).mention} or do `{prefix}last walls` in any channel.\n\nTo see the recent __buffer-check__, do `{prefix}lastcheck` in {client.get_channel(settings[2][5]).mention} or do `{prefix}last buffers` in any channel.', color = discord.Colour.blue())
                            embed.set_footer(f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                    elif cmd in ('buffers', 'buffer'):
                        if settings[2][0]:
                            cmd = 'buffers'
                        else:
                            cmd = None
                            embed = discord.Embed(title = f':gear: Settings - {prefix}clear', description = f':x: You cannot use that command because __buffer-check__ is `DISABLED`.\nTo turn it on, do\n```{prefix}settings buffers on```', color = discord.Colour.blue())
                            embed.set_footer(f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                    elif cmd in ('wall', 'walls'):
                        if settings[2][0]:
                            cmd = 'walls'
                        else:
                            cmd = None
                            embed = discord.Embed(title = f':gear: Settings - {prefix}clear', description = f':x: You cannot use that command because __wall-check__ is `DISABLED`.\nTo turn it on, do\n```{prefix}settings walls on```', color = discord.Colour.blue())
                            embed.set_footer(f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                    elif settings[1][0]:
                        cmd = 'walls'
                    elif settings[2][0]:
                        cmd = 'buffers'
                    else:
                        embed = discord.Embed(title = f':gear: Settings - {prefix}clear', description = f':x: You cannot use that command because both walls and buffers are `DISABLED`.\nTo turn them on, do\n```{prefix}settings <walls/buffers> on```', color = discord.Colour.blue())
                        embed.set_footer(f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                        await msg.channel.send(embed = embed)
                        cmd = None
                    if not cmd == None:
                        if cmd == 'walls':
                            logs = wallsLogsDir
                            e = ':alarm_clock:'
                            r = msg.guild.get_role(settings[1][6])
                        elif cmd == 'buffers':
                            logs = buffersLogsDir
                            e = ':stopwatch:'
                            r = msg.guild.get_role(settings[2][6])
                        if r in msg.author.roles or msg.author.guild_permissions.administrator:
                            with open(os.path.join(logs, str(msg.guild.id)+'.txt'), 'r') as file:
                                found = False
                                while not found:
                                    text = file.readline()
                                    if text.startswith(':white_check_mark:'):
                                        found = True
                                        break
                                    elif text == '':
                                        break
                            if not found:
                                embed = discord.Embed(title = f'{e} Recent {cmd}-check', description = 'Not found.')
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}')
                                await msg.channel.send(embed=embed)
                            else:
                                ct = datetime.datetime.utcnow()
                                lt = text[22:][:text[22:].find('**')-2]
                                td = ct - datetime.datetime.strptime(lt, dateformat)
                                td = td.seconds //60
                                if td >60:
                                    td = f'{td//60} hours and {td%60} minutes'
                                else:
                                    td = f'{td} minutes'
                                user = text[22:][text[22:].find('**')+3:]
                                embed = discord.Embed(title = f'{e} Recent {cmd}-check', description = f'It has been `{td}` since the last {cmd}-check at\n`{lt}` by {user}', color = discord.Colour.blue())
                                user = user[3:21]
                                with open(os.path.join(skinsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                    text = file.read().split('\n')
                                found = False
                                for i in text:
                                    if i.startswith(user):
                                        skin = i[19:]
                                        found = True
                                        break
                                if not found:
                                    skin = ''
                                embed.set_thumbnail(url = skin)
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed = embed)
                        else:
                            embed = discord.Embed(title = f':gear: Settings - {prefix}clear', description = f':x: You do not have permission to execute that command because you do not have the {r.mention} role.', color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                elif cmd in ('goal', 'dailygoal', 'progress'):
                    with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                        settings = eval(file.read())
                    if settings[0][2] == None:
                        embed = discord.Embed(title = ':gear: Settings - Daily Goals', description = f':x: You cannot use that command because the daily goals are `DISABLED` i.e. set to `None`.\nDo `{prefix}help goals` for more info.', color = discord.Colour.blue())
                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                        await msg.channel.send(embed = embed)
                    else:
                        r = msg.guild.get_role(settings[0][4])
                        if r in msg.author.roles or msg.author.guild_permissions.administrator:
                            with open(os.path.join(todayDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                text = file.read().split('\n')
                            if text == ['']:
                                embed = discord.Embed(title = 'Daily Progress', description = f"**Goal :** `{commas(str(settings[0][2]))}`\n\n**Value added till now :** `0`\n\n*Stop slacking guys and get to work.*", color = discord.Colour.gold())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed = embed)
                            else:
                                text.sort(key = sortkey, reverse = True)
                                total = 0
                                for i in range(len(text)):
                                    total += int(eval(text[i][19:]))
                                    text[i] = f'**{i+1}.** <@!{text[i][:18]}> {commas(text[i][19:])}'
                                p = round(total/settings[0][2]*100, 3)
                                if total < 0:
                                    message = "I don't even know how that's possible."
                                elif p > 100:
                                    message = "Hurray! We're already past our goal! Good job! but keep going anyway."
                                elif p > 90:
                                    message = 'So close...'
                                elif p > 75:
                                    message = "We're almost there! Just a few more spawners. "
                                elif p//1 == 69:
                                    message = "Nice."
                                elif p > 50:
                                    message = "We are more than halfway through."
                                elif p > 25:
                                    message = "put a message here"
                                elif p > 0:
                                    message = "Go go go! We got a long way to go."
                                elif p == 0:
                                    message = 'Stop slacking guys and get to work.'
                                text = '\n'.join(text)
                                embed = discord.Embed(title = 'Daily Progress', description = f"**Goal :** `{commas(str(settings[0][2]))}`\n\n**Value added till now :**\n    `{commas(str(total))}` __{p}%__\n\n*\"{message}\"*\n\n**Top Contributers of the day - **\n{text}", color = discord.Colour.gold())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed = embed)

                        else:
                            embed = discord.Embed(title = ':gear: Settings - Daily Goal', description = f':x: You do not have permission to execute that command because you do not have the {r.mention} role.', color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                elif cmd in ('settings', 'setting'):
                    cmd = split_space(msg.content).lower()
                    cmdword = split_space_list(cmd)[0]
                    if cmdword in ('valuemanagement', 'value') :
                        cmd = split_space(cmd).replace(' ', '')
                        if cmd == 'on' or cmd == 'enable':
                            if msg.author.guild_permissions.administrator:
                                with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r+')  as file:
                                    settings = eval(file.read())
                                    if settings[0][0]:
                                        embed = discord.Embed(title = ':gear: Settings - Value - Status', description = 'The __Value Management__ module is already set to `ENABLED`  :white_check_mark: .', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed=embed)
                                    else:
                                        settings[0][0] = True
                                        if client.get_channel(settings[0][3]) == None:
                                            found = False
                                            for i in msg.guild.text_channels:
                                                if i.name == 'value-added':
                                                    found = True
                                                    embed = discord.Embed(title = ':gear: Settings - Channel - Value Management', description = f'Could not find the previously set value channel, so this channel has been automatically selected and will be used in the future to post embeds regarding value addition/removal.\n\nTo set a different channel for value embeds, do\n```{prefix}settings channel value <mention the channel>```', color = discord.Colour.blue())
                                                    embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                                                    await i.send(embed = embed)
                                                    settings[0][3] = i.id
                                                    break
                                            if not found:
                                                ch = await msg.guild.create_text_channel(name = 'value-added')
                                                embed = discord.Embed(title = f'Settings - Channel - Value Management', description = f'Could not find the previously set value channel, so this channel has been created and will be used in the future to post embeds regarding value addition.\n\nTo set a different channel for value embeds, do\n```{prefix}settings channel value <mention the channel>```', color = discord.Colour.blue())
                                                embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                                                await ch.send(embed=embed)
                                                settings[0][3] = ch.id
                                            change = True
                                        if msg.guild.get_role(settings[0][4]) == None:
                                            found = False
                                            ch = client.get_channel(settings[0][3])
                                            for i in msg.guild.roles:
                                                if i.name == 'Faction Member':
                                                    found = True
                                                    embed = discord.Embed(title = ':gear: Settings - Role - Value', description = f'Could not find previously set role for __value module__.\nTo overcome this issue, the {i.mention} has been selected.\n\nTo change the role for __value module__,\n```{prefix}settings role value <mention the role>```', color = discord.Colour.blue())
                                                    embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}')
                                                    await ch.send(embed = embed)
                                                    settings[0][4] = i.id
                                                    change = True
                                                    await ch.set_permissions(i, read_messages = True, send_messages = True)
                                            if not found:
                                                r = await msg.guild.create_role(name = 'Faction Member')
                                                embed = discord.Embed(title = ':gear: Settings - Role - Value', description = f'Could not find previously set role for __value module__.\nTo overcome this issue, the {r.mention} has been created.\n\nTo change the role for __value module__,\n```{prefix}settings role value <mention the role>```', color = discord.Colour.blue())
                                                embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}')
                                                await ch.send(embed = embed)
                                                settings[0][4] = r.id
                                                change = True
                                                await ch.set_permissions(r, read_messages = True, send_messages = True)
                                        file.truncate(0)
                                        file.seek(0,0)
                                        file.write(str(settings))
                                        embed = discord.Embed(title = ':gear: Settings - Value - Status', description = f'The __Value Management__ module has been set to `ENABLED` :white_check_mark:\nEmbeds will be sent in {client.get_channel(settings[0][3]).mention}. To change the value channel, do `{prefix}settings channel value <mention the channel>`', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed=embed)
                                        with open(os.path.join(valueLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file2:
                                            text = file2.read()
                                            file2.seek(0,0)
                                            file2.write(f":gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : set Value module to `ENABLED`.\n"+text)
                            else:
                                embed = discord.Embed(title = ':gear: Settings - Value - Status', description = 'You do not have permission to execute that command.', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed = embed)
                        elif cmd == 'off' or cmd == 'disable':
                            if msg.author.guild_permissions.administrator:
                                with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r+')  as file:
                                    settings = eval(file.read())
                                    if not settings[0][0]:
                                        embed = discord.Embed(title = ':gear: Settings - Value - Status', description = 'The __Value Management__ module is already set to `DISABLED`  :x: .', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed=embed)
                                    else:
                                        settings[0][0] = False
                                        file.truncate(0)
                                        file.seek(0,0)
                                        file.write(str(settings))
                                        embed = discord.Embed(title = ':gear: Settings - Value - Status', description = 'The __Value Management__ module has been set to `DISABLED`  :x:', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed=embed)
                                        with open(os.path.join(valueLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file2:
                                            text = file2.read()
                                            file2.seek(0,0)
                                            file2.write(f":gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : set Value module to `DISABLED`.\n"+text)
                            else:
                                embed = discord.Embed(title = ':gear: Settings - Value - Status', description = 'You do not have permission to execute that command.', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed = embed)
                        else:
                            with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                settings = eval(file.read())
                            embed = discord.Embed(title = ':gear: Settings - Value', description = f'Settings for __value__ related commands. Do `{prefix}help value` for more info.', color = discord.Colour.blue())

                            if settings[0][0]:
                                message = '`ENABLED`  :white_check_mark:'
                            else:
                                message = '`DISABLED`  :x:'
                            embed.add_field(name = ':unlock: **Status**', value = message + f'\n__Enable/Disable__ the Value Management module using this setting.\n```{prefix}settings value <on/off/enable/disable>```', inline = False)
                            embed.add_field(name = ':earth_americas: **Realm / Planet**', value = f"**Currently set to** `{settings[0][1]}`.\nChange the __spawner rates__ used for calculation by changing your realm.\n```{prefix}settings realm <realm>```", inline = False)
                            embed.add_field(name = ':goal: **Daily Goal**', value = f"**Currently set to** `{settings[0][2]}`.\nSet your daily goal.\n```{prefix}settings goal <goal>```", inline = False)
                            try:
                                r = msg.guild.get_role(settings[0][4]).mention
                            except:
                                r = 'None'
                            embed.add_field(name = ':label: **Role**', value = f"Currently set to** {r}.\nSet which role has access to __value module__ commands.\n```{prefix}settings role value <mention the role>```", inline = False)
                            try:
                                ch = client.get_channel(settings[0][3]).mention
                            except:
                                ch = 'None'
                            embed.add_field(name = ':tv: **Channel**', value = f"**Currently set to** {ch}.\nSet the channel in which the embeds are posted.\n```{prefix}settings channel value <mention the channel>```\n\n__Note__: Some settings conditionally accept `None` as a valid input.")
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                    elif cmdword == 'realm':
                        cmd = split_space(cmd).replace(' ', '').replace('realm', '')
                        if cmd == '':
                            with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                settings = eval(file.read())
                            embed = discord.Embed(title = ':gear: Settings - Realm', description = f"Saico realms have different spawener rates. You can set which realm you play on to set spawner prices right.\n\n:earth_americas: **Currently set to** `{settings[0][1]}`\n\n To set your realm, use the command\n```{prefix}settings realm <realm>```", color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed=embed)
                        elif cmd.upper() in ('WITHER', 'SKELETON', 'ZOMBIE', 'GUARDIAN', 'MAGMA', 'BLAZE', 'WITCH', 'OVERLORD', 'WARLOCK'):
                            cmd = cmd.upper()
                            if msg.author.guild_permissions.administrator:
                                with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                    settings = eval(file.read())
                                    if settings[0][1] == cmd:
                                        embed = discord.Embed(title = ':gear: Settings - Realm', description = f':white_check_mark: The realm is already set to `{cmd}`.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                    else:
                                        settings[0][1] = cmd
                                        file.truncate(0)
                                        file.seek(0,0)
                                        file.write(str(settings))
                                        embed = discord.Embed(title = ':gear: Settings - Realm', description = f':white_check_mark: Your realm has been set to `{cmd}`.', color = discord.Color.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                        with open(os.path.join(valueLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file2:
                                            text = file2.read()
                                            file2.seek(0,0)
                                            file2.write(f":gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : set realm to `{cmd}`.\n"+text)
                            else:
                                embed = discord.Embed(title = ':gear: Settings - Realm', description = ':x: You do not have permission to execute that command.', color = discord.Color.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed=embed)
                        else:
                            embed = discord.Embed(title = ':gear: Settings - Realm', description = ':x: That is not a valid realm.', color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed=embed)
                    elif cmdword in ('goal', 'dailygoal', 'goals', 'dailygoals'):
                        cmd = split_space(cmd).replace(' ', '').lower()
                        if cmd == '':
                            with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                settings = eval(file.read())
                            embed = discord.Embed(title = ':gear: Settings - Daily Goals', description = f'Set daily goals for your faction.\nDo `{prefix}help goals` for more info.\n\n:goal: **Currently set to** `{settings[0][2]}`\n\nTo set your daily goal,\n```{prefix}settings goal <goal>```', color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                        elif cmd == 'none':
                            with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                settings = eval(file.read())
                                if settings[0][2] == None:
                                    embed = discord.Embed(title = ':gear: Settings - Daily Goals', description = ':white_check_mark: The daily goal is already set to `None`.', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed = embed)
                                elif msg.author.guild_permissions.administrator:
                                    settings[0][2] = None
                                    file.truncate(0)
                                    file.seek(0,0)
                                    file.write(str(settings))
                                    embed = discord.Embed(title = ':gear: Settings - Daily Goals', description = ':white_check_mark: The daily goal has been set to `None`.', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed = embed)
                                else:
                                    embed = discord.Embed(title = ':gear: Settings - Daily Goals', description = ':x: You do not have permission to execute that command.', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed = embed)
                        else:
                            replacement = [
                                ['billion', '1000000000'],
                                ['bill', '1000000000'],
                                ['bil', '1000000000'],
                                ['b', '1000000000'],
                                ['million', '1000000'],
                                ['mill', '1000000'],
                                ['mil', '1000000'],
                                ['m', '1000000'],
                                ['k', '1000']
                                ]

                            for i in replacement:
                                if i[0] in cmd:
                                    cmd = cmd.replace(i[0], f'*{i[1]}')
                                    break
                            if not pure_int(cmd):
                                embed = discord.Embed(title=':gear: Settings - Daily Goals', description = ':x: Please enter a valid value.', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed = embed)
                            else:
                                if msg.author.guild_permissions.administrator:
                                    cmd = int(eval(cmd))
                                    with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                        settings = eval(file.read())
                                        if settings[0][2] == cmd:
                                            embed = discord.Embed(title = ':gear: Settings - Daily Goals', description = f':white_check_mark: The daily goal is already set to `{commas(str(cmd))}`.', color = discord.Colour.blue())
                                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                            await msg.channel.send(embed = embed)
                                        else:
                                            settings[0][2] = cmd
                                            file.truncate(0)
                                            file.seek(0,0)
                                            file.write(str(settings))
                                            embed = discord.Embed(title = ':gear: Settings - Daily Goal', description = f':white_check_mark: The daily goal has been set to `{commas(str(cmd))}`.', color = discord.Colour.blue())
                                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                            await msg.channel.send(embed = embed)
                                            with open(os.path.join(valueLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file2:
                                                text = file2.read()
                                                file2.seek(0,0)
                                                file2.write(f":gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : set daily goal to `{commas(str(cmd))}`.\n"+text)
                                else:
                                    embed = discord.Embed(title = ':gear: Settings - Daily Goals', description = ':x: You do not have permission to execute that command.', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed = embed)
                    elif cmdword in ('walls', 'wall', 'wallcheck', 'wallchecks'):
                        cmd = split_space(cmd).replace(' ', '')
                        if cmd in ('on', 'enable'):
                            if msg.author.guild_permissions.administrator:
                                with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                    settings = eval(file.read())
                                    if client.get_channel(settings[1][5]) == None:
                                        found = False
                                        for i in msg.guild.text_channels:
                                            if i.name == 'wall-check':
                                                found = True
                                                embed = discord.Embed(title = ':gear: Settings - Channel - Wall-Checks', description = f'Could not find the previously set walls channel, so this channel has been automatically selected and will be used in the future for wall-check alerts.\n\nTo set a different walls channel, do\n```{prefix}settings channel walls <mention the channel>```', color = discord.Colour.blue())
                                                embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                                                await i.send(embed = embed)
                                                settings[1][5] = i.id
                                                break
                                        if not found:
                                            ch = await msg.guild.create_text_channel(name = 'wall-check')
                                            embed = discord.Embed(title = f'Settings - Channel - Wall-Checks', description = f'Could not find the previously set walls channel, so this channel has been created and will be used in the future for wall-check alerts.\n\nTo set a different walls channel, do\n```{prefix}settings channel walls <mention the channel>```', color = discord.Colour.blue())
                                            embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                                            await ch.send(embed=embed)
                                            settings[1][5] = ch.id
                                        change = True
                                    if msg.guild.get_role(settings[1][6]) == None:
                                        found = False
                                        ch = client.get_channel(settings[1][5])
                                        for i in msg.guild.roles:
                                            if i.name == 'Faction Member':
                                                found = True
                                                embed = discord.Embed(title = ':gear: Settings - Role - Wall-Checks', description = f'Could not find previously set role for __wall-check module__.\nTo overcome this issue, the {i.mention} has been selected.\n\nTo change the role for __wall-check module__,\n```{prefix}settings role walls <mention the role>```', color = discord.Colour.blue())
                                                embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}')
                                                await ch.send(embed = embed)
                                                settings[1][6] = i.id
                                                change = True
                                                await ch.set_permissions(i, read_messages = True, send_messages = True)
                                        if not found:
                                            r = await msg.guild.create_role(name = 'Faction Member')
                                            embed = discord.Embed(title = ':gear: Settings - Role - Wall-Checks', description = f'Could not find previously set role for __wall-check module__.\nTo overcome this issue, the {r.mention} has been created.\n\nTo change the role for __wall-check module__,\n```{prefix}settings role walls <mention the role>```', color = discord.Colour.blue())
                                            embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}')
                                            await ch.send(embed = embed)
                                            settings[1][6] = r.id
                                            change = True
                                            await ch.set_permissions(r, read_messages = True, send_messages = True)
                                    if settings[1][0]:
                                        embed = discord.Embed(title = ':gear: Settings - WallCheck Alerts', description = f':white_check_mark: The WallCheck module is already set to `ENABLED`.\nAlerts will be sent in {client.get_channel(settings[1][5]).mention}.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                    else:
                                        settings[1][0] = True
                                        settings[1][3] = datetime.datetime.utcnow().strftime(dateformat)
                                        file.truncate(0)
                                        file.seek(0,0)
                                        file.write(str(settings))
                                        try:
                                            exec(f'wall_alert{msg.guild.id}.cancel()', globals())
                                            exec(f'del wall_alert{msg.guild.id}', globals())
                                        except:
                                            pass
                                        exec(create_wall_code(msg.guild.id, settings), globals())
                                        embed = discord.Embed(title = ':gear: Settings - WallCheck Alerts', description = f':white_check_mark: The WallCheck module has been set to `ENABLED`.\nAlerts will be sent in {client.get_channel(settings[1][5]).mention}.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                        with open(os.path.join(wallsLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file2:
                                            text = file2.read()
                                            file2.seek(0,0)
                                            file2.write(f':gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : set wallchecks module to `ENABLED`.\n'+text)
                            else:
                                embed = discord.Embed(title = ':gear: Settings - WallCheck Alerts', description = 'You do not have permission to execute that command.', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed = embed)
                        elif cmd in ('off', 'disable'):
                            if msg.author.guild_permissions.administrator:
                                with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                    settings = eval(file.read())
                                    if not settings[1][0]:
                                        embed = discord.Embed(title = ':gear: Settings - WallCheck Alerts', description = ':x: The WallCheck module is already set to `DISABLED`.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                    else:
                                        settings[1][0] = False
                                        file.truncate(0)
                                        file.seek(0,0)
                                        file.write(str(settings))
                                        try:
                                            exec(f'wall_alert{msg.guild.id}.cancel()', globals())
                                            exec(f'del wall_alert{msg.guild.id}', globals())
                                        except:
                                            pass
                                        embed = discord.Embed(title = ':gear: Settings - WallCheck Alerts', description = ':x: The WallCheck module has been set to `DISABLED`.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                        with open(os.path.join(wallsLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file2:
                                            text = file2.read()
                                            file2.seek(0,0)
                                            file2.write(f':gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : set wallchecks module to `DISABLED`.\n'+text)
                            else:
                                embed = discord.Embed(title = ':gear: Settings - WallCheck Alerts', description = 'You do not have permission to execute that command.', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed = embed)
                        else:
                            with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                settings = eval(file.read())
                            embed = discord.Embed(title = ':gear: Settings - WallCheck Alerts', description = f'Settings for __wall check__ related commands/features. Do `{prefix}settings <setting>` for more info.', color = discord.Colour.blue())
                            if settings[1][0]:
                                embed.add_field(name = ':green_circle: **Status**', value = f'**Currently set to** `ENABLED` :white_check_mark:\n__Enable/Disable__ the WallCheck module for the bot.\n```{prefix}settings walls <on/off/enable/disable>```', inline = False)
                            else:
                                embed.add_field(name = ':red_circle: **Status**', value = f'**Currently set to** `DISABLED` :x:\n__Enable/Disable__ the WallCheck module for the bot.\n```{prefix}settings walls <on/off/enable/disable>```', inline = False)

                            embed.add_field(name = ':alarm_clock: **Check Frequency**', value = f'**Currently set to** `{settings[1][1]} minutes`\nSet the frequency of wallcheck alerts.\n```{prefix}settings checkFrequency walls <minutes>```', inline = False)
                            embed.add_field(name = ':bell: **Reminder Frequency**', value = f'**Currently set to** `{settings[1][2]} minutes`\nSet the time after which reminders should be sent.\n```{prefix}settings reminderFrequency walls <minutes>```', inline = False)
                            embed.add_field(name = ':exclamation: **Tag On First Alert**', value = f'**Currently set to** `{settings[1][7]}`\nIf you want the role to be tagged on the first alert/reminder, then set this to true.\n```{prefix}settings tagonfirstalert walls <on/off/true/false>```', inline = False)
                            try:
                                r = msg.guild.get_role(settings[1][6]).mention
                            except:
                                r = 'None'
                            embed.add_field(name = ':label: **Role**', value = f"**Currently set to** {r}.\nSet which role has access to __wall-check module__ commands.\n```{prefix}settings role walls <mention the role>```", inline = False)
                            try:
                                ch = client.get_channel(settings[1][5]).mention
                            except:
                                ch = 'None'
                            embed.add_field(name = ':tv: **Channel**', value = f'**Currently set to** {ch}\nSet the channel where the alerts are posted.\n```{prefix}settings channel walls <mention the channel>```\n\n__Note__: Some settings conditionally accept `None` as a valid input.')
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                    elif cmdword in ('buffer', 'buffers', 'buffercheck', 'bufferchecks'):
                        cmd = split_space(cmd).replace(' ', '')
                        if cmd in ('on', 'enable'):
                            if msg.author.guild_permissions.administrator:
                                with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                    settings = eval(file.read())
                                    if client.get_channel(settings[2][5]) == None:
                                        found = False
                                        for i in msg.guild.text_channels:
                                            if i.name == 'buffer-check':
                                                found = True
                                                embed = discord.Embed(title = ':gear: Settings - Channel - Buffer-Checks', description = f'Could not find the previously set buffers channel, so this channel has been automatically selected and will be used in the future for buffer-check alerts.\n\nTo set a different buffers channel, do\n```{prefix}settings channel buffers <mention the channel>```', color = discord.Colour.blue())
                                                embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                                                await i.send(embed = embed)
                                                settings[2][5] = i.id
                                                break
                                        if not found:
                                            ch = await msg.guild.create_text_channel(name = 'buffer-check')
                                            embed = discord.Embed(title = f'Settings - Channel - Buffer-Checks', description = f'Could not find the previously set buffers channel, so this channel has been created and will be used in the future for buffer-check alerts.\n\nTo set a different buffers channel, do\n```{prefix}settings channel buffers <mention the channel>```', color = discord.Colour.blue())
                                            embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                                            await ch.send(embed=embed)
                                            settings[2][5] = ch.id
                                        change = True
                                    if msg.guild.get_role(settings[2][6]) == None:
                                        found = False
                                        ch = client.get_channel(settings[2][5])
                                        for i in msg.guild.roles:
                                            if i.name == 'Faction Member':
                                                found = True
                                                embed = discord.Embed(title = ':gear: Settings - Role - Buffer-Checks', description = f'Could not find previously set role for __buffer-check module__.\nTo overcome this issue, the {i.mention} has been selected.\n\nTo change the role for __buffer-check module__,\n```{prefix}settings role buffers <mention the role>```', color = discord.Colour.blue())
                                                embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}')
                                                await ch.send(embed = embed)
                                                settings[2][6] = i.id
                                                change = True
                                                await ch.set_permissions(i, read_messages = True, send_messages = True)
                                        if not found:
                                            r = await msg.guild.create_role(name = 'Faction Member')
                                            embed = discord.Embed(title = ':gear: Settings - Role - Buffer-Checks', description = f'Could not find previously set role for __buffer-check module__.\nTo overcome this issue, the {r.mention} has been created.\n\nTo change the role for __buffer-check module__,\n```{prefix}settings role buffers <mention the role>```', color = discord.Colour.blue())
                                            embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}')
                                            await ch.send(embed = embed)
                                            settings[2][6] = r.id
                                            change = True
                                            await ch.set_permissions(r, read_messages = True, send_messages = True)
                                    if settings[2][0]:
                                        embed = discord.Embed(title = ':gear: Settings - BufferCheck Alerts', description = f':white_check_mark: The BufferCheck module is already set to `ENABLED`.\nAlerts will be sent in {client.get_channel(settings[2][5]).mention}.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                    else:
                                        settings[2][0] = True
                                        settings[2][3] = datetime.datetime.utcnow().strftime(dateformat)
                                        file.truncate(0)
                                        file.seek(0,0)
                                        file.write(str(settings))
                                        try:
                                            exec(f'buffer_alert{msg.guild.id}.cancel()', globals)
                                            exec(f'del buffer_alert{msg.guild.id}', globals)
                                        except:
                                            pass
                                        exec(create_buffer_code(msg.guild.id, settings), globals())
                                        embed = discord.Embed(title = ':gear: Settings - BufferCheck Alerts', description = f':white_check_mark: The BufferCheck module has been set to `ENABLED`.\nAlerts will be sent in {client.get_channel(settings[2][5]).mention}.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                        with open(os.path.join(wallsLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file2:
                                            text = file2.read()
                                            file2.seek(0,0)
                                            file2.write(f':gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : set bufferchecks module to `ENABLED`.\n'+text)
                            else:
                                embed = discord.Embed(title = ':gear: Settings - BufferCheck Alerts', description = 'You do not have permission to execute that command.', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed = embed)
                        elif cmd in ('off', 'disable'):
                            if msg.author.guild_permissions.administrator:
                                with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                    settings = eval(file.read())
                                    if not settings[2][0]:
                                        embed = discord.Embed(title = ':gear: Settings - BufferCheck Alerts', description = ':x: The BufferCheck module is already set to `DISABLED`.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                    else:
                                        settings[2][0] = False
                                        file.truncate(0)
                                        file.seek(0,0)
                                        file.write(str(settings))
                                        try:
                                            exec(f'buffer_alert{msg.guild.id}.cancel()', globals())
                                            exec(f'del buffer_alert{msg.guild.id}', globals())
                                        except:
                                            pass
                                        embed = discord.Embed(title = ':gear: Settings - BufferCheck Alerts', description = ':x: The BufferCheck module has been set to `DISABLED`.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                        with open(os.path.join(wallsLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file2:
                                            text = file2.read()
                                            file2.seek(0,0)
                                            file2.write(f':gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : set bufferchecks module to `DISABLED`.\n'+text)
                            else:
                                embed = discord.Embed(title = ':gear: Settings - BufferCheck Alerts', description = 'You do not have permission to execute that command.', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed = embed)
                        else:
                            with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                settings = eval(file.read())
                            embed = discord.Embed(title = ':gear: Settings - Buffercheck Alerts', description = f'Settings for __buffer check__ related commands/features. Do `{prefix}settings <setting>` for more info.', color = discord.Colour.blue())
                            if settings[2][0]:
                                embed.add_field(name = ':green_circle: **Status**', value = f'**Currently set to** `ENABLED` :white_check_mark:\n__Enable/Disable__ the BufferCheck module for the bot.\n```{prefix}settings buffers <on/off/enable/disable>```', inline = False)
                            else:
                                embed.add_field(name = ':red_circle: **Status**', value = f'**Currently set to** `DISABLED` :x:\n__Enable/Disable__ the BufferCheck module for the bot.\n```{prefix}settings buffers <on/off/enable/disable>```', inline = False)

                            embed.add_field(name = ':alarm_clock: **Check Frequency**', value = f'**Currently set to** `{settings[2][1]} minutes`\nSet the frequency of BufferCheck alerts.\n```{prefix}settings checkFrequency buffers <minutes>```', inline = False)
                            embed.add_field(name = ':bell: **Reminder Frequency**', value = f'**Currently set to** `{settings[2][2]} minutes`\nSet the time after which reminders should be sent.\n```{prefix}settings reminderFrequency buffers <minutes>```', inline = False)
                            embed.add_field(name = ':exclamation: **Tag On First Alert**', value = f'**Currently set to** `{settings[2][7]}`\nIf you want the role to be tagged on the first alert/reminder, then set this to true.\n```{prefix}settings tagonfirstalert buffers <on/off/true/false>```', inline = False)
                            try:
                                r = msg.guild.get_role(settings[2][6]).mention
                            except:
                                r = 'None'
                            embed.add_field(name = ':label: **Role**', value = f"**Currently set to** {r}.\nSet which role has access to __buffer-check module__ commands.\n```{prefix}settings role buffers <mention the role>```", inline = False)
                            try:
                                ch = client.get_channel(settings[2][5]).mention
                            except:
                                ch = 'None'
                            embed.add_field(name = ':tv: **Channel**', value = f'**Currently set to** {ch}\nSet the channel where the alerts are posted.\n```{prefix}settings channel buffers <mention the channel>```\n\n__Note__: Some settings conditionally accept `None` as a valid input.')
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                    elif cmdword in ('checkfrequency', 'checkfreq'):
                        cmd = split_space(cmd)
                        if split_space_list(cmd)[0] in ('wall', 'walls'):
                            cmd = split_space(cmd).replace(' ', '')
                            if cmd == '':
                                with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                    settings = eval(file.read())
                                embed = discord.Embed(title = ':gear: Settings - Check Frequency - Walls', description = f'**Currently set to** `{settings[1][1]}`\nTo change the walls check frequency,\n```{prefix}settings <checkFrequency/checkFreq> walls <minutes>```', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed=embed)
                            elif pure_int(cmd):
                                if msg.author.guild_permissions.administrator:
                                    cmd = int(cmd)
                                    with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                        settings = eval(file.read())
                                        if settings[1][1] == cmd:
                                            embed = discord.Embed(title = ':gear: Settings - Check Frequency - Walls', description = f':white_check_mark: The __Walls__ Check Frequency is already set to `{cmd} minutes`.', color = discord.Colour.blue())
                                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                            await msg.channel.send(embed = embed)
                                        else:
                                            settings[1][1] = cmd
                                            file.truncate(0)
                                            file.seek(0,0)
                                            file.write(str(settings))
                                            embed = discord.Embed(title = ':gear: Settings - Check Frequency - Walls', description = f':white_check_mark: The __Walls__ Check Frequency has been set to `{cmd} minutes`.', color = discord.Colour.blue())
                                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                            await msg.channel.send(embed=embed)
                                            with open(os.path.join(wallsLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file2:
                                                text = file2.read()
                                                file2.seek(0,0)
                                                file2.write(f":gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : set walls check frequency to `{cmd} minutes`.\n"+text)
                                else:
                                    embed = discord.Embed(title = ':gear: Settings - Check Frequency - Walls', description = 'You do not have permission to execute that command.', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed= embed)
                            else:
                                embed = discord.Embed(title = ':gear: Settings - Check Frequency - Walls', description = 'Please enter a valid value.', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed=embed)
                        elif split_space_list(cmd)[0] in ('buffer', 'buffers'):
                            cmd = split_space(cmd).replace(' ', '')
                            if cmd == '':
                                with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                    settings = eval(file.read())
                                embed = discord.Embed(title = ':gear: Settings - Check Frequency - Buffers', description = f'**Currently set to** `{settings[2][1]}`\nTo change the buffers check frequency,\n```{prefix}settings <checkFrequency/checkFreq> buffers <minutes>```', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed=embed)
                            elif pure_int(cmd):
                                if msg.author.guild_permissions.administrator:
                                    cmd = int(cmd)
                                    with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                        settings = eval(file.read())
                                        if settings[2][1] == cmd:
                                            embed = discord.Embed(title = ':gear: Settings - Check Frequency - Buffers', description = f':white_check_mark: The __Buffers__ Check Frequency is already set to `{cmd} minutes`.', color = discord.Colour.blue())
                                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                            await msg.channel.send(embed = embed)
                                        else:
                                            settings[2][1] = cmd
                                            file.truncate(0)
                                            file.seek(0,0)
                                            file.write(str(settings))
                                            embed = discord.Embed(title = ':gear: Settings - Check Frequency - Buffers', description = f':white_check_mark: The __Buffers__ Check Frequency has been set to `{cmd} minutes`.', color = discord.Colour.blue())
                                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                            await msg.channel.send(embed=embed)
                                            with open(os.path.join(buffersLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file2:
                                                text = file2.read()
                                                file2.seek(0,0)
                                                file2.write(f":gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : set buffers check frequency to `{cmd} minutes`.\n"+text)
                                else:
                                    embed = discord.Embed(title = ':gear: Settings - Check Frequency - Buffers', description = 'You do not have permission to execute that command.', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed= embed)
                            else:
                                embed = discord.Embed(title = ':gear: Settings - Check Frequency - Buffers', description = 'Please enter a valid value.', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed=embed)
                        else:
                            with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt') ,'r') as file:
                                settings = eval(file.read())
                            embed = discord.Embed(title = ':gear: Settings - Check Frequency', description = 'Check Frequency refers to the time between wallchecks/bufferchecks. It is the amount of time after which the bot sends a fresh check alert.', color = discord.Colour.blue())
                            embed.add_field(name = '**Walls Check Frequency**', value = f'**Currently set to** `{settings[1][1]} minutes`\nTo change __walls__ check frequency,\n```{prefix}settings <checkFrequency/checkFreq> walls <minutes>```', inline = False)
                            embed.add_field(name = '**Buffers Check Frequency**', value = f'**Currently set to** `{settings[2][1]} minutes`\nTo change __buffers__ check frequency,\n```{prefix}settings <checkFrequency/checkFreq> buffers <minutes>```')
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed=embed)
                    elif cmdword in ('reminderfrequency', 'reminderfreq'):
                        cmd = split_space(cmd)
                        if split_space_list(cmd)[0] in ('wall', 'walls'):
                            cmd = split_space(cmd).replace(' ', '')
                            if cmd == '':
                                with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                    settings = eval(file.read())
                                embed = discord.Embed(title = ':gear: Settings - Reminder Frequency - Walls', description = f'**Currently set to** `{settings[1][2]}`\nTo change the walls reminder frequency,\n```{prefix}settings <reminderFrequency/reminderFreq> walls <minutes>```', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed=embed)
                            elif pure_int(cmd):
                                if msg.author.guild_permissions.administrator:
                                    cmd = int(cmd)
                                    with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                        settings = eval(file.read())
                                        if settings[1][2] == cmd:
                                            embed = discord.Embed(title = ':gear: Settings - Reminder Frequency - Walls', description = f':white_check_mark: The __Walls__ Reminder Frequency is already set to `{cmd} minutes`.', color = discord.Colour.blue())
                                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                            await msg.channel.send(embed = embed)
                                        else:
                                            settings[1][2] = cmd
                                            file.truncate(0)
                                            file.seek(0,0)
                                            file.write(str(settings))
                                            embed = discord.Embed(title = ':gear: Settings - Reminder Frequency - Walls', description = f':white_check_mark: The __Walls__ Reminder Frequency has been set to `{cmd} minutes`.', color = discord.Colour.blue())
                                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                            await msg.channel.send(embed=embed)
                                            with open(os.path.join(wallsLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file2:
                                                text = file2.read()
                                                file2.seek(0,0)
                                                file2.write(f":gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : set walls reminder frequency to `{cmd} minutes`.\n"+text)
                                else:
                                    embed = discord.Embed(title = ':gear: Settings - Reminder Frequency - Walls', description = 'You do not have permission to execute that command.', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed= embed)
                            else:
                                embed = discord.Embed(title = ':gear: Settings - Reminder Frequency - Walls', description = 'Please enter a valid value.', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed=embed)
                        elif split_space_list(cmd)[0] in ('buffer', 'buffers'):
                            cmd = split_space(cmd).replace(' ', '')
                            if cmd == '':
                                with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                    settings = eval(file.read())
                                embed = discord.Embed(title = ':gear: Settings - Reminder Frequency - Buffers', description = f'**Currently set to** `{settings[2][2]}`\nTo change the buffers reminder frequency,\n```{prefix}settings <reminderFrequency/reminderFreq> buffers <minutes>```', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed=embed)
                            elif pure_int(cmd):
                                if msg.author.guild_permissions.administrator:
                                    cmd = int(cmd)
                                    with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                        settings = eval(file.read())
                                        if settings[2][2] == cmd:
                                            embed = discord.Embed(title = ':gear: Settings - Reminder Frequency - Buffers', description = f':white_check_mark: The __Buffers__ Reminder Frequency is already set to `{cmd} minutes`.', color = discord.Colour.blue())
                                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                            await msg.channel.send(embed = embed)
                                        else:
                                            settings[2][2] = cmd
                                            file.truncate(0)
                                            file.seek(0,0)
                                            file.write(str(settings))
                                            embed = discord.Embed(title = ':gear: Settings - Reminder Frequency - Buffers', description = f':white_check_mark: The __Buffers__ Reminder Frequency has been set to `{cmd} minutes`.', color = discord.Colour.blue())
                                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                            await msg.channel.send(embed=embed)
                                            with open(os.path.join(buffersLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file2:
                                                text = file2.read()
                                                file2.seek(0,0)
                                                file2.write(f":gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : set buffers reminder frequency to `{cmd} minutes`.\n"+text)
                                else:
                                    embed = discord.Embed(title = ':gear: Settings - Reminder Frequency - Buffers', description = 'You do not have permission to execute that command.', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed= embed)
                            else:
                                embed = discord.Embed(title = ':gear: Settings - Reminder Frequency - Buffers', description = 'Please enter a valid value.', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed=embed)
                        else:
                            with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt') ,'r') as file:
                                settings = eval(file.read())
                            embed = discord.Embed(title = ':gear: Settings - Reminder Frequency', description = 'Reminder Frequency refers to the time between wallchecks/bufferchecks. It is the amount of time after which the bot sends a fresh check alert.', color = discord.Colour.blue())
                            embed.add_field(name = '**Walls Reminder Frequency**', value = f'**Currently set to** `{settings[1][2]} minutes`\nTo change __walls__ reminder frequency,\n```{prefix}settings <reminderFrequency/reminderFreq> walls <minutes>```', inline = False)
                            embed.add_field(name = '**Buffers Reminder Frequency**', value = f'**Currently set to** `{settings[2][2]} minutes`\nTo change __buffers__ reminder frequency,\n```{prefix}settings <reminderFrequency/reminderFreq> buffers <minutes>```')
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed=embed)
                    elif cmdword == 'channel':
                        with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                            settings = eval(file.read())
                        cmd = split_space(cmd).lower()
                        cmdword = split_space_list(cmd)[0]
                        if cmdword == 'value':
                            target = msg.channel_mentions
                            if len(target) > 1:
                                embed = discord.Embed(title = ':gear: Settings - Channel - Value', description = 'You can only mention one channel.', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed=embed)
                            elif len(target) == 0:
                                if cmd.replace(' ', '') == 'None':
                                    if settings[0][3] == None:
                                        embed = discord.Embed(title = ':gear: Settings - Channel - Value', description = ':white_check_mark: The channel for __value management__ module is already set to `None`.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed=embed)
                                    else:
                                        if msg.author.guild_permissions.administrator:
                                            if settings[0][0]:
                                                embed = discord.Embed(title = ':gear: Settings - Channel - Value', description = ':x: You cannot set the channel to `None` while the module is `ENABLED`.', color = discord.Colour.blue())
                                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                                await msg.channel.send(embed=embed)
                                            else:
                                                settings[0][3] = None
                                                with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                                    file.write(str(settings))
                                                embed = discord.Embed(title = ':gear: Settings - Channel - Value', description = ':white_check_mark: The channel for __value management__ module has been set to `None`.', color = discord.Colour.blue())
                                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                                await msg.channel.send(embed = embed)
                                        else:
                                            embed = discord.Embed(title = ':gear: Settings - Channel - Value', description = 'You do not have permission to execute that command.', color = discord.Colour.blue())
                                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                            await msg.channel.send(embed = embed)
                                else:
                                    try:
                                        ch = client.get_channel(settings[0][3])
                                    except:
                                        ch = 'None'
                                    embed = discord.Embed(title = ':gear: Settings - Channel - Value', description = f'**Currently set to** {ch}\n\nThis setting allows you to set where the embeds related to value addition and removal are posted.\nTo change the channel for the __value management__ module,\n```{prefix}settings channel value <mention the channel>```', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed = embed)
                            else:
                                target = target[0]
                                if target.id == settings[0][3]:
                                    embed = discord.Embed(title = ':gear: Settings - Channel - Value', description = f':white_check_mark: The channel for the __value management__ module is already set to {target.mention}.', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed = embed)
                                else:
                                    if msg.author.guild_permissions.administrator:
                                        settings[0][3] = target.id
                                        with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                            file.write(str(settings))
                                        embed = discord.Embed(title = ':gear: Settings - Channel - Value', description = f':white_check_mark: The channel for __value management__ module has been set to {target.mention}.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                    else:
                                        embed = discord.Embed(title = ':gear: Settings - Channel - Value', description = 'You do not have permission to execute that command.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed=embed)
                        elif cmdword in ('wall', 'walls'):
                            target = msg.channel_mentions
                            if len(target) > 1:
                                embed = discord.Embed(title = ':gear: Settings - Channel - Walls', description = 'You can only mention one channel.', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed=embed)
                            elif len(target) == 0:
                                if cmd.replace(' ', '') == 'None':
                                    if settings[1][5] == None:
                                        embed = discord.Embed(title = ':gear: Settings - Channel - Walls', description = ':white_check_mark: The channel for __wall check__ module is already set to `None`.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed=embed)
                                    else:
                                        if msg.author.guild_permissions.administrator:
                                            if settings[1][0]:
                                                embed = discord.Embed(title = ':gear: Settings - Channel - Walls', description = ':x: You cannot set the channel to `None` while the module is `ENABLED`.', color = discord.Colour.blue())
                                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                                await msg.channel.send(embed=embed)
                                            else:
                                                settings[1][5] = None
                                                with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                                    file.write(str(settings))
                                                embed = discord.Embed(title = ':gear: Settings - Channel - Walls', description = ':white_check_mark: The channel for __wall check__ module has been set to `None`.', color = discord.Colour.blue())
                                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                                await msg.channel.send(embed = embed)
                                        else:
                                            embed = discord.Embed(title = ':gear: Settings - Channel - Walls', description = 'You do not have permission to execute that command.', color = discord.Colour.blue())
                                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                            await msg.channel.send(embed = embed)
                                else:
                                    try:
                                        ch = client.get_channel(settings[1][5])
                                    except:
                                        ch = 'None'
                                    embed = discord.Embed(title = ':gear: Settings - Channel - Walls', description = f'**Currently set to** {ch}\n\nThis setting allows you to set where the __wall check alerts__ are posted.\nTo change the channel for the __wall check__ module,\n```{prefix}settings channel walls <mention the channel>```', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed = embed)
                            else:
                                target = target[0]
                                if target.id == settings[1][5]:
                                    embed = discord.Embed(title = ':gear: Settings - Channel - Walls', description = f':white_check_mark: The channel for the __wall check__ module is already set to {target.mention}.', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed = embed)
                                else:
                                    if msg.author.guild_permissions.administrator:
                                        settings[1][5] = target.id
                                        with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                            file.write(str(settings))
                                        embed = discord.Embed(title = ':gear: Settings - Channel - Walls', description = f':white_check_mark: The channel for __wall check__ module has been set to {target.mention}.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                    else:
                                        embed = discord.Embed(title = ':gear: Settings - Channel - Walls', description = 'You do not have permission to execute that command.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed=embed)
                        elif cmdword in('buffer', 'buffers'):
                            target = msg.channel_mentions
                            if len(target) > 1:
                                embed = discord.Embed(title = ':gear: Settings - Channel - Buffers', description = 'You can only mention one channel.', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed=embed)
                            elif len(target) == 0:
                                if cmd.replace(' ', '') == 'None':
                                    if settings[2][5] == None:
                                        embed = discord.Embed(title = ':gear: Settings - Channel - Buffers', description = ':white_check_mark: The channel for __buffer check__ module is already set to `None`.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed=embed)
                                    else:
                                        if msg.author.guild_permissions.administrator:
                                            if settings[2][0]:
                                                embed = discord.Embed(title = ':gear: Settings - Channel - Buffers', description = ':x: You cannot set the channel to `None` while the module is `ENABLED`.', color = discord.Colour.blue())
                                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                                await msg.channel.send(embed=embed)
                                            else:
                                                settings[2][5] = None
                                                with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                                    file.write(str(settings))
                                                embed = discord.Embed(title = ':gear: Settings - Channel - Buffers', description = ':white_check_mark: The channel for __buffer check__ module has been set to `None`.', color = discord.Colour.blue())
                                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                                await msg.channel.send(embed = embed)
                                        else:
                                            embed = discord.Embed(title = ':gear: Settings - Channel - Buffers', description = 'You do not have permission to execute that command.', color = discord.Colour.blue())
                                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                            await msg.channel.send(embed = embed)
                                else:
                                    try:
                                        ch = client.get_channel(settings[2][5])
                                    except:
                                        ch = 'None'
                                    embed = discord.Embed(title = ':gear: Settings - Channel - Buffers', description = f'**Currently set to** {ch}\n\nThis setting allows you to set where the __buffer check alerts__ are posted.\nTo change the channel for the __buffer check__ module,\n```{prefix}settings channel buffers <mention the channel>```', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed = embed)
                            else:
                                target = target[0]
                                if target.id == settings[2][5]:
                                    embed = discord.Embed(title = ':gear: Settings - Channel - Buffers', description = f':white_check_mark: The channel for the __buffer check__ module is already set to {target.mention}.', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed = embed)
                                else:
                                    if msg.author.guild_permissions.administrator:
                                        settings[2][5] = target.id
                                        with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                            file.write(str(settings))
                                        embed = discord.Embed(title = ':gear: Settings - Channel - Buffers', description = f':white_check_mark: The channel for __buffer check__ module has been set to {target.mention}.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                    else:
                                        embed = discord.Embed(title = ':gear: Settings - Channel - Buffers', description = 'You do not have permission to execute that command.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed=embed)
                        else:
                            embed = discord.Embed(title = ':gear: Settings - Channel', description = 'This setting allows you to change the channel for the specific modules of the bot. This affects where the alerts/embeds are posted.\n', color = discord.Colour.blue())
                            try:
                                ch = client.get_channel(settings[0][3]).mention
                            except:
                                ch = 'None'
                            embed.add_field(name = ':money_with_wings: **Value Module**', value = f'**Currently set to** {ch}\nTo change where the embeds related to value addition/removal are posted,\n```{prefix}settings channel value <mention the channel>```', inline = False)
                            try:
                                ch = client.get_channel(settings[1][5]).mention
                            except:
                                ch = 'None'
                            embed.add_field(name = ':alarm_clock: **Wall-Check Module**', value = f'**Currently set to** {ch}\nTo change where the wall-check alerts are posted,\n```{prefix}settings channel walls <mention the channel>```', inline = False)
                            try:
                                ch = client.get_channel(settings[1][5]).mention
                            except:
                                ch = 'None'
                            embed.add_field(name = ':stopwatch: **Buffer-Check Module**', value = f'**Currently set to** {ch}   \nTo change where the buffer-check alerts are posted,\n```{prefix}settings channel buffers <mention the channel>```', inline = False)
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                    elif cmdword == 'role':
                        cmd = split_space(cmd)
                        cmdword = split_space_list(cmd)[0]
                        if cmdword == 'value':
                            target = msg.role_mentions
                            if len(target)>1:
                                embed = discord.Embed(title = ':gear: Settings - Role - Value', description = 'You can only mention one role.', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed = embed)
                            elif len(target) == 0:
                                with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                    settings = eval(file.read())
                                if split_space(cmd).startswith('none'):
                                    if settings[0][0]:
                                        embed = discord.Embed(title = ':gear: Settings - Role - Value', description = ':x: You cannot set the role to `None` while the module is `ENABLED`.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                    elif settings [0][4] == None:
                                        embed = discord.Embed(title = ':gear: Settings - Role - Value', description = ':white_check_mark: Role for __value module__ is already set to `None`.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                    elif msg.author.guild_permissions.administrator:
                                        settings[0][4] = None
                                        with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                            file.write(str(settings))
                                        embed = discord.Embed(title = ':gear: Settings - Role - Value', description = ':white_check_mark: Role for __value module__ has been set to `None`.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                        with open(os.path.join(valueLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                            text = file.read()
                                            file.seek(0,0)
                                            file.write(f':gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : set role to `None`.\n{text}')
                                    else:
                                        embed = discord.Embed(title = ':gear: Settings - Role - Value', description = 'You do not have permission to execute that command.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                else:
                                    try:
                                        role = msg.guild.get_role(settings[0][4]).mention
                                    except:
                                        role = 'None'
                                    embed = discord.Embed(title = ':gear: Settings - Role - Value', description = f'**Currently set to** {role}\n\nTo change which role has access to the commands in the value module, like - `{prefix}add`,\n\n```{prefix}settings role value <mention the role>```.', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed = embed)
                            else:
                                target = target[0]
                                with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                    settings = eval(file.read())
                                if settings[0][4] == target.id:
                                    embed = discord.Embed(title = ':gear: Settings - Role - Value', description = f':white_check_mark: Role for __value module__ is already set to {target.mention}.', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed = embed)
                                elif not msg.author.guild_permissions.administrator:
                                    embed = discord.Embed(title = ':gear: Settings - Role - Value', description = 'You do not have permission to execute that command.', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed = embed)
                                else:
                                    try:
                                        await client.get_channel(settings[0][3]).set_permissions(target, read_messages = True, send_messages = True)
                                    except:
                                        pass
                                    settings[0][4] = target.id
                                    with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                        file.write(str(settings))
                                    embed = discord.Embed(title = ':gear: Settings - Role - Value', description = f':white_check_mark: Role for __value module__ has been set to {target.mention}.', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed = embed)
                                    with open(os.path.join(valueLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                        text = file.read()
                                        file.seek(0,0)
                                        file.write(f':gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : set role to {target.mention}.\n{text}')
                        elif cmdword in ('walls', 'wall'):
                            target = msg.role_mentions
                            if len(target)>1:
                                embed = discord.Embed(title = ':gear: Settings - Role - Walls', description = 'You can only mention one role.', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed = embed)
                            elif len(target) == 0:
                                with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                    settings = eval(file.read())
                                if split_space(cmd).startswith('none'):
                                    if settings[1][0]:
                                        embed = discord.Embed(title = ':gear: Settings - Role - Walls', description = ':x: You cannot set the role to `None` while the module is `ENABLED`.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                    elif settings [1][6] == None:
                                        embed = discord.Embed(title = ':gear: Settings - Role - Walls', description = ':white_check_mark: Role for __wall-check module__ is already set to `None`.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                    elif msg.author.guild_permissions.administrator:
                                        settings[1][6] = None
                                        with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                            file.write(str(settings))
                                        embed = discord.Embed(title = ':gear: Settings - Role - Walls', description = ':white_check_mark: Role for __wall-check module__ has been set to `None`.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                        with open(os.path.join(wallsLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                            text = file.read()
                                            file.seek(0,0)
                                            file.write(f':gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : set role to `None`.\n{text}')
                                    else:
                                        embed = discord.Embed(title = ':gear: Settings - Role - Walls', description = 'You do not have permission to execute that command.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                else:
                                    try:
                                        role = msg.guild.get_role(settings[1][6]).mention
                                    except:
                                        role = 'None'
                                    embed = discord.Embed(title = ':gear: Settings - Role - Walls', description = f'**Currently set to** {role}\n\nTo change the role which has access to the wall-check channel and commands like - `{prefix}clear`,\n\n```{prefix}settings role walls <mention the role>```.', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed = embed)
                            else:
                                target = target[0]
                                with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                    settings = eval(file.read())
                                if settings[1][6] == target.id:
                                    embed = discord.Embed(title = ':gear: Settings - Role - Walls', description = f':white_check_mark: Role for __wall-check module__ is already set to {target.mention}.', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed = embed)
                                elif not msg.author.guild_permissions.administrator:
                                    embed = discord.Embed(title = ':gear: Settings - Role - Walls', description = 'You do not have permission to execute that command.', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed = embed)
                                else:
                                    try:
                                        await client.get_channel(settings[0][3]).set_permissions(target, read_messages = True, send_messages = True)
                                    except:
                                        pass
                                    settings[1][6] = target.id
                                    with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                        file.write(str(settings))
                                    embed = discord.Embed(title = ':gear: Settings - Role - Walls', description = f':white_check_mark: Role for __wall-check module__ has been set to {target.mention}.', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed = embed)
                                    with open(os.path.join(wallsLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                        text = file.read()
                                        file.seek(0,0)
                                        file.write(f':gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : set role to {target.mention}.\n{text}')
                        elif cmdword in ('buffers', 'buffer'):
                            target = msg.role_mentions
                            if len(target)>1:
                                embed = discord.Embed(title = ':gear: Settings - Role - Buffers', description = 'You can only mention one role.', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed = embed)
                            elif len(target) == 0:
                                with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                    settings = eval(file.read())
                                if split_space(cmd).startswith('none'):
                                    if settings[2][0]:
                                        embed = discord.Embed(title = ':gear: Settings - Role - Buffers', description = ':x: You cannot set the role to `None` while the module is `ENABLED`.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                    elif settings [1][6] == None:
                                        embed = discord.Embed(title = ':gear: Settings - Role - Buffers', description = ':white_check_mark: Role for __buffer-check module__ is already set to `None`.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                    elif msg.author.guild_permissions.administrator:
                                        settings[2][6] = None
                                        with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                            file.write(str(settings))
                                        embed = discord.Embed(title = ':gear: Settings - Role - Buffers', description = ':white_check_mark: Role for __buffer-check module__ has been set to `None`.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                        with open(os.path.join(buffersLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                            text = file.read()
                                            file.seek(0,0)
                                            file.write(f':gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : set role to `None`.\n{text}')
                                    else:
                                        embed = discord.Embed(title = ':gear: Settings - Role - Buffers', description = 'You do not have permission to execute that command.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                else:
                                    try:
                                        role = msg.guild.get_role(settings[2][6]).mention
                                    except:
                                        role = 'None'
                                    embed = discord.Embed(title = ':gear: Settings - Role - Buffers', description = f'**Currently set to** {role}\n\nTo change the role which has access to the buffer-check channel and commands like - `{prefix}clear`,\n\n```{prefix}settings role buffers <mention the role>```.', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed = embed)
                            else:
                                target = target[0]
                                with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                    settings = eval(file.read())
                                if settings[2][6] == target.id:
                                    embed = discord.Embed(title = ':gear: Settings - Role - Buffers', description = f':white_check_mark: Role for __buffer-check module__ is already set to {target.mention}.', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed = embed)
                                elif not msg.author.guild_permissions.administrator:
                                    embed = discord.Embed(title = ':gear: Settings - Role - Buffers', description = 'You do not have permission to execute that command.', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed = embed)
                                else:
                                    try:
                                        await client.get_channel(settings[0][3]).set_permissions(target, read_messages = True, send_messages = True)
                                    except:
                                        pass
                                    settings[2][6] = target.id
                                    with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                        file.write(str(settings))
                                    embed = discord.Embed(title = ':gear: Settings - Role - Buffers', description = f':white_check_mark: Role for __buffer-check module__ has been set to {target.mention}.', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed = embed)
                                    with open(os.path.join(buffersLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                        text = file.read()
                                        file.seek(0,0)
                                        file.write(f':gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : set role to {target.mention}.\n{text}')
                        else:
                            with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                settings = eval(file.read())
                            embed = discord.Embed(title = ':gear: Settings - Role', description = 'This setting allows you to set the role which will have access to specific modules. You can set all the perms to one role or different roles as per your choice.', color = discord.Colour.blue())
                            try:
                                role = msg.guild.get_role(settings[0][4]).mention
                            except:
                                role = 'None'
                            embed.add_field(name = ':money_with_wings: **Value Module**', value = f'**Currently set to** {role}\nChange which role has access to value module commands.\n```{prefix}settings role value <mention the role>```', inline = False)
                            try:
                                role = msg.guild.get_role(settings[1][6]).mention
                            except:
                                role = 'None'
                            embed.add_field(name = ':alarm_clock: **Wall-Check Module**', value = f'**Currently set to** {role}\nChange which role has access to wallcheck module commands.\n```{prefix}settings role walls <mention the role>```', inline = False)
                            try:
                                role = msg.guild.get_role(settings[2][6]).mention
                            except:
                                role = 'None'
                            embed.add_field(name = ':stopwatch: **Buffer-Check Module**', value = f'**Currently set to** {role}\nChange which role has access to buffercheck module commands.\n```{prefix}settings role buffers <mention the role>```', inline = False)
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                    elif cmdword == 'prefix':
                        cmd = split_space_list(split_space(cmd))[0]
                        if cmd == '':
                            embed = discord.Embed(title = ':gear: Settings - Prefix', description = f'**Currently set to** `{prefix}`\n\nTo change the prefix of the bot for your server, do\n```{prefix}settings prefix <new prefix>```\nIf you somehow manage to set your prefix to an unrecognized character, then do `??resetprefix` to set the prefix to `??`.', color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                        elif '`' in cmd:
                            embed = discord.Embed(title = ':gear: Settings - Prefix', description = ':x: Prefix cannot contain ` because it can mess up the embeds sent by the bot.', color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                        elif '*' in cmd:
                            embed = discord.Embed(title = ':gear: Settings - Prefix', description = ':x: Prefix cannot contain * because it can mess up the embeds sent by the bot.', color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                        elif ' ' in cmd:
                            embed = discord.Embed(title = ':gear: Settings - Prefix', description = ':x: Prefix cannot contain spaces because it can mess up the commands.', color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                        elif cmd == prefix:
                            embed = discord.Embed(title = ':gear: Settings - Prefix', description = f':white_check_mark: Prefix is already set to `{cmd}`.', color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                        elif msg.author.guild_permissions.administrator:
                            try:
                                with open(os.path.join(prefixDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                    file.write(cmd)
                            except:
                                with open(os.path.join(prefixDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                    file.write(prefix)
                                embed = discord.Embed(title = ':gear: Settings - Prefix', description = f':x: Error while setting prefix. Prefix not changed. Current Prefix - `{prefix}`.', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed = embed)
                            else:
                                embed = discord.Embed(title = ':gear: Settings - Prefix', description = f':white_check_mark: Prefix has been set to `{cmd}`.', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed = embed)
                        else:
                            embed = discord.Embed(title = ':gear: Settings - Prefix', description = ':x: You do not have permission to execute that command.', color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                    elif cmdword in ('tagonfirstalert', 'tagonfirstreminder'):
                        cmd = split_space(cmd)
                        cmdword = split_space_list(cmd)[0]
                        if cmdword in ('wall', 'walls'):
                            cmdword = 'Wall'
                            n = 1
                            logs = wallsLogsDir
                        elif cmdword in ('buffer', 'buffers'):
                            cmdword = 'Buffer'
                            n = 2
                            logs = buffersLogsDir
                        else:
                            cmdword = None
                        if cmdword == None:
                            with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                settings = eval(file.read())
                            embed = discord.Embed(title = ':gear: Settings - TagOnFirstAlert', description = f'This option allows you to specify if you want the checker role to be tagged/mentioned on the first check alert.\n\n**For walls,** currently set to `{settings[1][7]}`\n```{prefix}settings tagonfirstalert walls <on/off/true/false>```\n\n**For buffers,** currently set to `{settings[2][7]}`\n```{prefix}settings tagonfirstalert buffers <on/off/true/false>```', color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                        else:
                            cmd = split_space_list(split_space(cmd))[0]
                            if cmd in ('on', 'true', 'enable'):
                                if msg.author.guild_permissions.administrator:
                                    with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                        settings = eval(file.read())
                                    if settings[n][7]:
                                        embed = discord.Embed(title = f':gear: Settings - TagOnFirstAlert - {cmdword}s', description = f':white_check_mark: __TagOnFirstAlert__ is already set to `True` for __{cmdword.lower()}-checks__.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                    else:
                                        settings[n][7] = True
                                        with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                            file.write(str(settings))
                                        with open(os.path.join(logs, str(msg.guild.id)+'.txt'), 'r+') as file:
                                            text = file.read()
                                            file.seek(0,0)
                                            file.write(f':gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : set TagOnFirstAlert to `True`.\n{text}')
                                        embed = discord.Embed(title = f':gear: Settings - TagOnFirstAlert - {cmdword}s', description = f':white_check_mark: __TagOnFirstAlert__ has been set to `True` for __{cmdword.lower()}-checks__.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                else:
                                    embed = discord.Embed(title = f':gear: Settings - TagOnFirstAlert - {cmdword}s', description = ':x: You do not have permission to execute that command.', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed = embed)
                            elif cmd in ('off', 'false', 'disable'):
                                if msg.author.guild_permissions.administrator:
                                    with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                        settings = eval(file.read())
                                    if not settings[n][7]:
                                        embed = discord.Embed(title = f':gear: Settings - TagOnFirstAlert - {cmdword}s', description = f':white_check_mark: __TagOnFirstAlert__ is already set to `False` for __{cmdword.lower()}-checks__.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                    else:
                                        settings[n][7] = False
                                        with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                            file.write(str(settings))
                                        with open(os.path.join(logs, str(msg.guild.id)+'.txt'), 'r+') as file:
                                            text = file.read()
                                            file.seek(0,0)
                                            file.write(f':gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : set TagOnFirstAlert to `False`.\n{text}')
                                        embed = discord.Embed(title = f':gear: Settings - TagOnFirstAlert - {cmdword}s', description = f':white_check_mark: __TagOnFirstAlert__ has been set to `False` for __{cmdword.lower()}-checks__.', color = discord.Colour.blue())
                                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                        await msg.channel.send(embed = embed)
                                else:
                                    embed = discord.Embed(title = f':gear: Settings - TagOnFirstAlert - {cmdword}s', description = ':x: You do not have permission to execute that command.', color = discord.Colour.blue())
                                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                    await msg.channel.send(embed = embed)
                            else:
                                with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                    settings = eval(file.read())
                                embed = discord.Embed(title = f':gear: Settings - TagOnFirstAlert - {cmdword}', description = f'**Currently set to** - `{settings[n][7]}`\n\nYou can use this option to specify if you want to mention the {cmdword.lower()}-checker role on the first alert.\n\n**Usage-**\n```{prefix}settings tagonfirstalert {cmdword.lower()} <on/off/true/false>```', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed = embed)
                    else:
                        with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                            settings = eval(file.read())
                        embed = discord.Embed(title = ':gear: Settings',description = f'Use the format `{prefix}settings <setting>` to change the setting or for more info.', colour = discord.Colour.blue())

                        if settings[0][0]:
                            embed.add_field(name = ':money_with_wings: **Value Management**  :white_check_mark:', value = f'\n**Status** - `ENABLED`\n**Realm** - `{settings[0][1]}`\n**Daily Goal** - `{settings[0][2]} $`\n**Channel** - {client.get_channel(settings[0][3]).mention}\n**Role** - {msg.guild.get_role(settings[0][4]).mention}\n\n', inline = False)
                        else:
                            try:
                                ch = client.get_channel(settings[0][3]).mention
                            except:
                                ch = 'None'
                            try:
                                r = msg.guild.get_role(settings[0][4]).mention
                            except:
                                r = 'None'
                            embed.add_field(name = ':money_with_wings: **Value Management**  :x:', value = f'\n**Status** - `DISABLED`\n**Realm** - `{settings[0][1]}`\n**Daily Goal** - `{settings[0][2]} $`\n**Channel** - {ch}\n**Role** - {r}\n\n', inline = False)

                        if settings[1][0]:
                            embed.add_field(name = ':alarm_clock: **Wall check Alerts**  :white_check_mark:', value = f'\n**Status** - `ENABLED`\n**Check Frequency** - `{settings[1][1]} min`\n**Reminder Frequency** - `{settings[1][2]} min`\n**Channel** - {client.get_channel(settings[1][5]).mention}\n**Role** - {msg.guild.get_role(settings[1][6]).mention}\n**Tag on first alert** - `{settings[1][7]}`\n\n', inline = False)
                        else:
                            try:
                                ch = client.get_channel(settings[1][5]).mention
                            except:
                                ch = 'None'
                            try:
                                r = msg.guild.get_role(settings[1][6]).mention
                            except:
                                r = 'None'
                            embed.add_field(name = ':alarm_clock: **Wall check Alerts**  :x:', value = f'\n**Status** - `DISABLED`\n**Check Frequency** - `{settings[1][1]} min`\n**Reminder Frequency** - `{settings[1][2]} min`\n**Channel** - {ch}\n**Role** - {r}\n**Tag role on first alert** - `{settings[1][7]}`\n\n', inline = False)

                        if settings[2][0]:
                            embed.add_field(name = ':stopwatch: **Buffer check Alerts**  :white_check_mark:', value = f'\n**Status** - `ENABLED`\n**Check Frequency** - `{settings[2][1]} min`\n**Reminder Frequency** - `{settings[2][2]} min`\n**Channel** - {client.get_channel(settings[2][5]).mention}\n**Role** - {msg.guild.get_role(settings[2][6]).mention}\n**Tag role on first alert** - `{settings[2][7]}`\n\nDo `{prefix}settings <settings>` for more info.', inline = False)
                        else:
                            try:
                                ch = client.get_channel(settings[2][5]).mention
                            except:
                                ch = 'None'
                            try:
                                r = msg.guild.get_role(settings[2][6]).mention
                            except:
                                r = 'None'
                            embed.add_field(name = ':stopwatch: **Buffer check Alerts**  :x:', value = f'\n**Status** - `DISABLED`\n**Check Frequency** - `{settings[2][1]} min`\n**Reminder Frequency** - `{settings[2][2]} min`\n**Channel** - {ch}\n**Role** - {r}\n**Tag role on first alert** - `{settings[2][7]}`\n\nDo `{prefix}settings <settings>` for more info.', inline = False)

                        embed.add_field(name = ':grey_question: **Other**', value = f'**Prefix** - `{prefix}`', inline = False)
                        embed.set_footer(text = f"{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}", icon_url = msg.author.avatar_url)
                        await msg.channel.send(embed=embed)
                elif cmd in ('history', 'log'):
                    with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                        settings = eval(file.read())
                    if msg.content.replace(' ', '') == prefix+cmd:
                        cmd = ''
                    else:
                        cmd = split_space_list(msg.content)[1]
                    if cmd == 'value':
                        cmd = 'Value'
                        logs = valueLogsDir
                        role = msg.guild.get_role(settings[0][4])
                        color = discord.Colour.dark_green()
                    elif cmd in ('walls', 'wall'):
                        cmd = 'Walls'
                        logs = wallsLogsDir
                        role = msg.guild.get_role(settings[1][6])
                        color = discord.Colour.from_rgb(105, 105, 105)
                    elif cmd in ('buffers', 'buffer'):
                        cmd = 'Buffers'
                        logs = buffersLogsDir
                        role = msg.guild.get_role(settings[2][6])
                        color = discord.Colour.from_rgb(138, 98, 76)
                    elif msg.channel.id == settings[0][3]:
                        cmd = 'Value'
                        logs = valueLogsDir
                        role = msg.guild.get_role(settings[0][4])
                        color = discord.Colour.dark_green()
                    elif msg.channel.id == settings[1][5]:
                        cmd = 'Walls'
                        logs = wallsLogsDir
                        role = msg.guild.get_role(settings[1][6])
                        color = discord.Colour.from_rgb(105, 105, 105)
                    elif msg.channel.id == settings[2][5]:
                        cmd = 'Buffers'
                        logs = buffersLogsDir
                        role = msg.guild.get_role(settings[2][6])
                        color = discord.Colour.from_rgb(138, 98, 76)
                    else:
                        cmd = 'none'
                    if cmd == 'none':
                        embed = discord.Embed(title = f":page_facing_up: {msg.guild.name}'s History", description = f'This command allows you to see the history of the commands used for specific modules.', color = discord.Colour.blue())
                        try:
                            ch = client.get_channel(settings[0][3]).mention
                            embed.add_field(name = ':money_with_wings: **Value Module**', value = f'To see the history of __value module__ commands, do `{prefix}history` in {ch} or do\n```{prefix}log value <page>```', inline = False)
                        except:
                            embed.add_field(name = ':money_with_wings: **Value Module**', value = f'To see the history of __value module__ commands,\n```{prefix}log value <page>```', inline = False)
                        try:
                            ch = client.get_channel(settings[1][5]).mention
                            embed.add_field(name = ':alarm_clock: **Wall-Check Module**', value = f'To see the history of __wall-check module__ commands, do `{prefix}history` in {ch} or do\n```{prefix}log walls <page>```', inline = False)
                        except:
                            embed.add_field(name = ':alarm_clock: **Wall-Check Module**', value = f'To see the history of __wall-check module__ commands,\n```{prefix}log walls <page>```', inline = False)
                        try:
                            ch = client.get_channel(settings[2][5]).mention
                            embed.add_field(name = ':stopwatch: **Buffer-Check Module**', value = f'To see the history of __buffer-check module__ commands, do `{prefix}history` in {ch} or do\n```{prefix}log buffers <page>```', inline = False)
                        except:
                            embed.add_field(name = ':stopwatch: **Buffer-Check Module**', value = f'To see the history of __buffer-check module__ commands,\n```{prefix}log buffers <page>```', inline = False)
                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                        await msg.channel.send(embed = embed)
                    else:
                        if role == None or role in msg.author.roles or msg.author.guild_permissions.administrator:
                            try:
                                page = split_space_list(msg.content)[2]
                            except:
                                page = 1
                            else:
                                if page == '' or not pure_int(page):
                                    page = 1
                                elif int(eval(page)) < 1:
                                    page = 1
                                else:
                                    page = int(eval(page))
                            with open(os.path.join(logs, str(msg.guild.id)+'.txt'), 'r') as file:
                                text = file.readlines()
                            total = 1
                            message = ''
                            var = ''
                            for i in text:
                                if len(var + i) < 2048:
                                    var = var + i
                                else:
                                    var = i
                                    total += 1
                                if total == page:
                                    message = message + i
                            if message == '':
                                message = var
                                page = total
                            embed = discord.Embed(title = f":page_facing_up: {msg.guild.name}'s {cmd} History", description = message, color = color)
                            embed.set_footer(text = f'{msg.author.display_name} | Page {page} out of {total}\nDo {prefix}history {cmd.lower()} <page no> to goto a specific page or just react with the arrows.', icon_url = msg.author.avatar_url)
                            msg = await msg.channel.send(embed = embed)
                            await msg.add_reaction('\u23ea')
                            await msg.add_reaction('\u25c0')
                            await msg.add_reaction('\u23f9')
                            await msg.add_reaction('\u25b6')
                            await msg.add_reaction('\u23e9')
                            def reaction_check(reaction, user):
                                e = reaction.emoji.encode('unicode-escape').decode('ASCII')
                                return user != client.user and reaction.message.id == msg.id and e in (r'\u23ea', r'\u25c0', r'\u23f9', r'\u25b6', r'\u23e9')
                            while True:
                                try:
                                    r, user = await client.wait_for('reaction_add',timeout = 120.0, check = reaction_check)
                                    await msg.clear_reactions()
                                    e = r.emoji.encode('unicode-escape').decode('ASCII')
                                    if e == r'\u23ea':
                                        page = page - 5
                                    elif e == r'\u25c0':
                                        page = page -1
                                    elif e == r'\u23f9':
                                        raise asyncio.TimeoutError
                                    elif e == r'\u25b6':
                                        page = page + 1
                                    elif e == r'\u23e9':
                                        page = page + 5
                                    if page < 1:
                                        page = 1
                                    total = 1
                                    message = ''
                                    var = ''
                                    for i in text:
                                        if len(var + i) < 2048:
                                            var = var + i
                                        else:
                                            var = i
                                            total += 1
                                        if total == page:
                                            message = message + i
                                    if message == '':
                                        message = var
                                        page = total
                                    embed = discord.Embed(title = f":page_facing_up: {msg.guild.name}'s {cmd} History", description = message, color = color)
                                    embed.set_footer(text = f'{user.display_name} | Page {page} out of {total}\nDo `{prefix}history {cmd.lower()} <page no>` to goto a specific page or just react with the arrows.', icon_url = user.avatar_url)
                                    await msg.edit(embed = embed)
                                    await msg.add_reaction('\u23ea')
                                    await msg.add_reaction('\u25c0')
                                    await msg.add_reaction('\u23f9')
                                    await msg.add_reaction('\u25b6')
                                    await msg.add_reaction('\u23e9')
                                except asyncio.TimeoutError:
                                    await msg.clear_reactions()
                        else:
                            embed = discord.Embed(title = f':gear: Settings - {prefix}highscore', description = f':x: You do not have permission to execute that command because you do not have the {role.mention} role.', color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                elif cmd in ('top', 'highscore', 'highscores'):
                    with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                        settings = eval(file.read())
                    if split_space(msg.content).replace(' ', '') == '':
                        cmd = ''
                    else:
                        cmd = split_space_list(split_space(msg.content))[0]
                    if cmd == 'value':
                        cmd = 'Value'
                        cmdraw = 'value'
                        logs = valueDir
                        role = msg.guild.get_role(settings[0][4])
                        color = discord.Colour.dark_green()
                    elif cmd in ('walls', 'wall'):
                        cmd = 'Wall-Check'
                        cmdraw  = 'walls'
                        logs = wallsDir
                        role = msg.guild.get_role(settings[1][6])
                        color = discord.Colour.from_rgb(105, 105, 105)
                    elif cmd in ('buffers', 'buffer'):
                        cmd = 'Buffer-Check'
                        cmdraw = 'buffers'
                        logs = buffersDir
                        role = msg.guild.get_role(settings[2][6])
                        color = discord.Colour.from_rgb(138, 98, 76)
                    elif msg.channel.id == settings[0][3]:
                        cmd = 'Value'
                        cmdraw = 'value'
                        logs = valueDir
                        role = msg.guild.get_role(settings[0][4])
                        color = discord.Colour.dark_green()
                    elif msg.channel.id == settings[1][5]:
                        cmd = 'Wall-Check'
                        cmdraw = 'walls'
                        logs = wallsDir
                        role = msg.guild.get_role(settings[1][6])
                        color = discord.Colour.from_rgb(105, 105, 105)
                    elif msg.channel.id == settings[2][5]:
                        cmd = 'Buffer-Check'
                        cmdraw = 'buffers'
                        logs = buffersDir
                        role = msg.guild.get_role(settings[2][6])
                        color = discord.Colour.from_rgb(138, 98, 76)
                    else:
                        cmd = 'none'
                    if cmd == 'none':
                        embed = discord.Embed(title = f":page_facing_up: {msg.guild.name}'s Highscores", description = f'This command allows you to see the highscores for your faction.', color = discord.Colour.blue())
                        try:
                            ch = client.get_channel(settings[0][3]).mention
                            embed.add_field(name = ':money_with_wings: **Value Module**', value = f'To see the __value__ highscores, do `{prefix}highscore` in {ch} or do\n```{prefix}top value <page>```', inline = False)
                        except:
                            embed.add_field(name = ':money_with_wings: **Value Module**', value = f'To see the __value__ highscores,\n```{prefix}top value <page>```', inline = False)
                        try:
                            ch = client.get_channel(settings[1][5]).mention
                            embed.add_field(name = ':alarm_clock: **Wall-Check Module**', value = f'To see the __wall-check__ highscores, do `{prefix}highscore` in {ch} or do\n```{prefix}top walls <page>```', inline = False)
                        except:
                            embed.add_field(name = ':alarm_clock: **Wall-Check Module**', value = f'To see the __wall-check__ highscores,\n```{prefix}top walls <page>```', inline = False)
                        try:
                            ch = client.get_channel(settings[2][5]).mention
                            embed.add_field(name = ':stopwatch: **Buffer-Check Module**', value = f'To see the __buffer-check__ highscores, do `{prefix}highscore` in {ch} or do\n```{prefix}top buffers <page>```', inline = False)
                        except:
                            embed.add_field(name = ':stopwatch: **Buffer-Check Module**', value = f'To see the __buffer-check__ highscores,\n```{prefix}top buffers <page>```', inline = False)
                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                        await msg.channel.send(embed = embed)
                    else:
                        if role == None or role in msg.author.roles or msg.author.guild_permissions.administrator:
                            try:
                                page = split_space_list(msg.content)[2]
                            except:
                                page = 1
                            else:
                                if page == '' or not pure_int(page):
                                    page = 1
                                elif int(eval(page)) < 1:
                                    page = 1
                                else:
                                    page = int(eval(page))
                            with open(os.path.join(logs, str(msg.guild.id)+'.txt'), 'r') as file:
                                text = file.read().split('\n')
                            if text == ['']:
                                embed = discord.Embed(title = f":page_facing_up: {msg.guild.name}'s {cmd} Highscores", description = 'Nothing to show here.', color = color)
                                embed.set_footer(text = f'{msg.author.display_name} | Page 1 out of 1', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed = embed)
                            else:
                                total = ceil(len(text)/10)
                                text.sort(key=sortkey, reverse = True)
                                for i in range(len(text)):
                                    text[i] = f'**{i+1}.** <@{text[i][:18]}> {commas(str(text[i][19:]))}'
                                if page > total:
                                    page = total
                                if total == 1 or page == total:
                                    message = '\n'.join(text[(page-1)*10:])
                                else:
                                    message = '\n'.join(text[(page-1)*10:page*10])
                                embed = discord.Embed(title = f":page_facing_up: {msg.guild.name}'s {cmd} Highscores", description = message, color = color)
                                embed.set_footer(text = f'{msg.author.display_name} | Page {page} out of {total}\nDo {prefix}top {cmdraw} <page no> to goto a specific page or just react with the arrows.', icon_url = msg.author.avatar_url)
                                msg = await msg.channel.send(embed = embed)
                                await msg.add_reaction('\u23ea')
                                await msg.add_reaction('\u25c0')
                                await msg.add_reaction('\u23f9')
                                await msg.add_reaction('\u25b6')
                                await msg.add_reaction('\u23e9')
                                def reaction_check(reaction, user):
                                    e = reaction.emoji.encode('unicode-escape').decode('ASCII')
                                    return user != client.user and reaction.message.id == msg.id and e in (r'\u23ea', r'\u25c0', r'\u23f9', r'\u25b6', r'\u23e9')
                                while True:
                                    try:
                                        r, user = await client.wait_for('reaction_add',timeout = 120.0, check = reaction_check)
                                        await msg.clear_reactions()
                                        e = r.emoji.encode('unicode-escape').decode('ASCII')
                                        if e == r'\u23ea':
                                            page = page - 5
                                        elif e == r'\u25c0':
                                            page = page -1
                                        elif e == r'\u23f9':
                                            raise asyncio.TimeoutError
                                        elif e == r'\u25b6':
                                            page = page + 1
                                        elif e == r'\u23e9':
                                            page = page + 5
                                        if page < 1:
                                            page = 1
                                        if page > total:
                                            page = total
                                        if total == 1 or page == total:
                                            message = '\n'.join(text[(page-1)*10:])
                                        else:
                                            message = '\n'.join(text[(page-1)*10:page*10])
                                        embed = discord.Embed(title = f":page_facing_up: {msg.guild.name}'s {cmd} Highscores", description = message, color = color)
                                        embed.set_footer(text = f'{user.display_name} | Page {page} out of {total}\nDo {prefix}top {cmdraw} <page no> to goto a specific page or just react with the arrows.', icon_url = user.avatar_url)
                                        await msg.edit(embed = embed)
                                        await msg.add_reaction('\u23ea')
                                        await msg.add_reaction('\u25c0')
                                        await msg.add_reaction('\u23f9')
                                        await msg.add_reaction('\u25b6')
                                        await msg.add_reaction('\u23e9')
                                    except asyncio.TimeoutError:
                                        await msg.clear_reactions()
                        else:
                            embed = discord.Embed(title = f':gear: Settings - {prefix}highscore', description = f':x: You do not have permission to execute that command because you do not have the {role.mention} role.', color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                elif cmd == 'reset':
                    cmd = split_space_list(split_space(msg.content))[0].lower()
                    if cmd == 'value':
                        cmd = 'value'
                        logs = valueLogsDir
                        score = valueDir
                    elif cmd in ('wall', 'walls'):
                        cmd = 'walls'
                        logs = wallsLogsDir
                        score = wallsDir
                    elif cmd in ('buffer', 'buffers'):
                        cmd = 'buffers'
                        logs = buffersLogsDir
                        score = buffersDir
                    elif cmd == 'all':
                        pass
                    else:
                        cmd = None
                    if cmd == None:
                        embed = discord.Embed(title = f"\U0001f4d4 Help - {prefix}reset", description = f'Use this command to reset the highscores and history for specific modules.\n```{prefix}reset <value/walls/buffers/all>```', color = discord.Colour.blue())
                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                        await msg.channel.send(embed = embed)
                    elif msg.author.guild_permissions.administrator:
                        if cmd == 'all':
                            await msg.channel.send(f':warning: **You are about to reset __ALL__ modules**\n{msg.author.mention} Type `CONFIRM RESET` in chat within the next 10 seconds to confirm the reset.')
                            def check(var):
                                return var.author == msg.author and var.channel == msg.channel and var.content == 'CONFIRM RESET'
                            try:
                                msg = await client.wait_for('message', timeout = 10, check = check)
                            except asyncio.TimeoutError:
                                await msg.channel.send('Reset has been aborted.')
                            else:
                                with open(os.path.join(valueLogsDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                    file.write(f':gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : reset the `highscores` and `history` for __ALL__ modules.')
                                with open(os.path.join(wallsLogsDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                    file.write(f':gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : reset the `highscores` and `history` for __ALL__ modules.')
                                with open(os.path.join(buffersLogsDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                    file.write(f':gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : reset the `highscores` and `history` for __ALL__ modules.')
                                with open(os.path.join(valueDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                    pass
                                with open(os.path.join(wallsDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                    pass
                                with open(os.path.join(buffersDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                    pass
                                embed =  discord.Embed(title = f':gear: Settings - {prefix}reset', description = f':white_check_mark: **RESET CONFIRMED**\nThe highscores and history of __ALL__ modules have been deleted.\nHope you had a good map.', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed = embed)
                        else:
                            await msg.channel.send(f':warning: **You are about to reset the __{cmd}__ module**\n{msg.author.mention} Type `CONFIRM RESET` in chat within the next 10 seconds to confirm the reset.')
                            def check(var):
                                return var.author == msg.author and var.channel == msg.channel and var.content == 'CONFIRM RESET'
                            try:
                                msg = await client.wait_for('message', timeout = 10, check = check)
                            except asyncio.TimeoutError:
                                await msg.channel.send('Reset has been aborted.')
                            else:
                                with open(os.path.join(logs, str(msg.guild.id)+'.txt'), 'w+') as file:
                                    file.write(f':gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : reset the `highscores` and `history` for the __{cmd}__ module.')
                                with open(os.path.join(score, str(msg.guild.id)+'.txt'), 'w+') as file:
                                    pass
                                embed =  discord.Embed(title = f':gear: Settings - {prefix}reset', description = f':white_check_mark: **RESET CONFIRMED**\nThe highscores and history of the __{cmd}__ module have been deleted.\nHope you had a good map.', color = discord.Colour.blue())
                                embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                                await msg.channel.send(embed = embed)
                    else:
                        embed = discord.Embed(title = f':gear: Settings - {prefix}reset', description = 'You do not have the permission to execute that command.', color = discord.Colour.blue())
                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                        await msg.channel.send(embed = embed)
                elif cmd in ('iam', 'skin'):
                    cmd = split_space_list(split_space(msg.content))[0]
                    if cmd == '':
                        embed = discord.Embed(title = '\U0001F4D4 Help - Skin', description = f'Use this command to associate your skin to your discord account.\n```{prefix}skin <username>```', color = discord.Colour.blue())
                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                        await msg.channel.send(embed = embed)
                    elif len(cmd)<3 or len(cmd) > 16:
                        embed = discord.Embed(title = '\U0001F4D4 Help - Skin', description = ':x: Invalid Username\nUsername must be between 3 and 16 characters.', color = discord.Colour.blue())
                        embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                        await msg.channel.send(embed=embed)
                    else:
                        found = False
                        for i in cmd:
                            if i.lower() not in ['a','b','c','d','e','f','g','h','i','j','k', 'l', 'm','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','_']:
                                found = True
                                break
                        if found:
                            embed = discord.Embed(title = '\U0001F4D4 Help - Skin', description = ":x: Invalid username\nUsername must only consist of alphanumerics and underscore.", color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                        else:
                            with open(os.path.join(skinsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                text = file.read().split('\n')
                                if text == ['']:
                                    text = [f'{msg.author.id} {cmd}']
                                else:
                                    found = False
                                    for i in range(len(text)):
                                        if text[i].startswith(str(msg.author.id)):
                                            found = True
                                            text[i] = text[i][:19] + cmd
                                            break
                                    if not found:
                                        text.append(f'{msg.author.id} {cmd}')
                                file.truncate(0)
                                file.seek(0,0)
                                file.write('\n'.join(text))
                            embed = discord.Embed(title = ':gear: Settings - Skin', description = f':white_check_mark: Your account has been connected to the minecraft account **{cmd}**.', color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                elif cmd == 'prefix':
                    embed = discord.Embed(title = ':gear: Settings - Prefix', description = f'The prefix for this server is - `{prefix}`.', color = discord.Colour.blue())
                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                    await msg.channel.send(embed = embed)
                elif cmd == 'invite' and prefix!='??':
                    embed = discord.Embed(title = discord.Embed.Empty, description = "Invite me to your server using this [link](https://discordapp.com/api/oauth2/authorize?client_id=637575751583137822&permissions=268659792&scope=bot)\nMake sure to give all the required permissions to ensure proper performance.\n\nYou can also join the [discord server](https://discord.gg/bnKE45S) if you want. Feel free to report bugs / give suggestions there. Just don't expect anything crazy" , color = discord.Colour.gold())
                    embed.set_author(name = 'Support | Meta Factions Bot', icon_url = client.user.avatar_url)
                    embed.set_footer(text = '<3')
                    await msg.channel.send(embed = embed)
                    await msg.author.send(embed = embed)
                elif cmd in ('credits', 'credit', 'info') and prefix !='??':
                    embed = discord.Embed(title = discord.Embed.Empty, description = 'This bot was made by `Kevqn#0869` and is being hosted by `xNightmare#9571`.\nIf you have any problems/suggestions, feel free to join the [support server](https://discord.gg/bnKE45S).', color = discord.Colour.blue())
                    embed.set_author(name = 'Credits | Meta Factions Bot', icon_url = client.user.avatar_url)
                    embed.set_footer(text = '<3')
                    await msg.channel.send(embed =embed)
                elif cmd == 'restartinfo':
                    with open(infoTxt, 'r') as file:
                        text = file.read()
                    embed = discord.Embed(title = ':gear: Info', description = f'Last login - {text}')
                    await msg.channel.send(embed = embed)
                elif cmd == 'forcedailyreset':
                    if msg.author.guild_permissions.administrator:
                        with open(os.path.join(todayDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                            pass
                        with open(os.path.join(valueLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                            text = file.read()
                            file.seek(0,0)
                            file.write(f":gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {msg.author.mention} : forced daily reset.\n{text}")
                        if msg.channel.permissions_for(msg.guild.me).send_messages:
                            embed = discord.Embed(title = 'Forced Daily Reset', description = ':white_check_mark: Daily scores have been reset.', color = discord.Colour.gold())
                            embed.set_footer(text = f'{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                            await msg.channel.send(embed = embed)
                    else:
                        if msg.channel.permissions_for(msg.guild.me).send_messages:
                            embed = discord.Embed(title = ':gear: Daily Reset', description = ':x: You do not have permission to execute this command.', color = discord.Colour.blue())
                            embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)\
                            await msg.channel.send(embed = embed)
            if msg.content == '??resetprefix':
                if msg.author.guild_permissions.administrator:
                    with open(os.path.join(prefixDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                        file.write('??')
                    embed = discord.Embed(title = ':gear: Settings - Prefix', description = f':white_check_mark: Prefix has been set to the default `??`.', color = discord.Colour.blue())
                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                    await msg.channel.send(embed = embed)
                else:
                    embed = discord.Embed(title = ':gear: Settings - Prefix', description = ':x: You do not have permission to execute that command.', color = discord.Colour.blue())
                    embed.set_footer(text = f'{msg.author.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = msg.author.avatar_url)
                    await msg.channel.send(embed = embed)
        else:
            perms = msg.guild.me.guild_permissions
            found = False
            if not perms.manage_roles:
                found = True
            elif not perms.manage_channels:
                found = True
            elif not perms.read_messages:
                found = True
            elif not perms.send_messages:
                found = True
            elif not perms.manage_messages:
                found = True
            elif not perms.embed_links:
                found = True
            elif not perms.read_message_history:
                found = True
            elif not perms.mention_everyone:
                found = True
            elif not perms.add_reactions:
                found = True
            if found:
                pass
            else:
                #          [status, realm, goal, ch, role], [status, checkfreq, remFreq, lastcheck, player, channel, role], [same as previous]
                settings = [[True, 'WITHER', None, None, None],[False, 30, 10, None, None, None, None],[False, 30, 10, None, None, None, None]]
                found = False
                for i in msg.guild.text_channels:
                    if i.name == 'value-added':
                        found = True
                        settings[0][3] = i.id
                        break
                if not found:
                    ch = await msg.guild.create_text_channel(name = 'value-added')
                    settings[0][3] = ch.id
                found = False
                ch = client.get_channel(settings[0][3])
                for i in msg.guild.roles:
                    if i.name == 'Faction Member':
                        found = True
                        settings[0][4] = i.id
                        change = True
                        try:
                            await ch.set_permissions(i, read_messages = True, send_messages = True)
                        except:
                            pass
                if not found:
                    r = await msg.guild.create_role(name = 'Faction Member')
                    settings[0][4] = r.id
                    change = True
                    try:
                        await ch.set_permissions(r, read_messages = True, send_messages = True)
                    except:
                        pass
                with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                    file.write(str(settings))


@client.event
async def on_reaction_add(reaction, user):
    if user != client.user:
        msg = reaction.message
        if msg.author.id == client.user.id:
            if len(msg.embeds) == 1:
                title = msg.embeds[0].title
                found = False
                try:
                    if split_space(title) == 'Time to check walls!':
                        found = 'alert'
                        messages = await msg.channel.history(limit=30).flatten()
                        for i in messages:
                            if i.author == client.user:
                                if len(i.embeds) == 1:
                                    try:
                                        if i.embeds[0].title.endswith('walls clear.'):
                                            await i.clear_reactions()
                                            break
                                    except:
                                        pass
                    elif title.endswith('walls clear.'):
                        found = 'clear'
                except:
                    pass
                else:
                    if not found == False:
                        with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                            settings = eval(file.read())
                        if settings[1][0]:
                            if msg.guild.get_role(settings[1][6]) or user.guild_permissions.administrator:
                                e = reaction.emoji.encode('unicode-escape').decode('ASCII')
                                if e == r'\u2705':
                                    try:
                                        await msg.remove_reaction('\u2705', client.user)
                                    except:
                                        pass
                                    else:
                                        if found == 'alert':
                                            await msg.delete()
                                        else:
                                            await msg.clear_reactions()
                                        exec(f'wall_alert{msg.guild.id}.cancel()', globals())
                                        exec(f'del wall_alert{msg.guild.id}', globals())
                                        ct = datetime.datetime.utcnow()
                                        with open(os.path.join(prefixDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                            prefix = file.read()
                                        with open(os.path.join(wallsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                            text = file.read().split('\n')
                                            found = False
                                            if text == ['']:
                                                text = [f'{user.id} 1']
                                                score = '1'
                                            else:
                                                for i in range(len(text)):
                                                    if text[i].startswith(str(user.id)):
                                                        found = True
                                                        score = str(int(text[i][19:])+1)
                                                        text[i] = text[i][:19] + score
                                                        break
                                                if not found:
                                                    text.append(f'{user.id} 1')
                                                    score = '1'
                                            file.seek(0,0)
                                            file.write('\n'.join(text))
                                        with open(os.path.join(wallsLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                            text = file.read()
                                            file.seek(0,0)
                                            file.write(f":white_check_mark: **[{ct.strftime(dateformat)}]:** {user.mention}\n" + text)
                                        with open(os.path.join(skinsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                            text = file.read().split('\n')
                                        found = False
                                        for i in text:
                                            if i.startswith(str(user.id)):
                                                skin = f'https://minotar.net/avatar/{i[19:]}'
                                                found = True
                                                break
                                        if not found:
                                            skin = ''
                                        embed = discord.Embed(title = f':white_check_mark: **{user.display_name}** has marked walls clear.', color = discord.Colour.green())
                                        embed.add_field(name = 'Checked by', value = user.mention, inline = True)
                                        embed.add_field(name = 'Score', value = score, inline = True)
                                        td = ct - datetime.datetime.strptime(settings[1][3], dateformat)
                                        td = datetime.timedelta(days = td.days, seconds = td.seconds)
                                        embed.add_field(name = 'Time Taken', value = str(td), inline = True)
                                        embed.add_field(name = 'Time Checked', value = ct.strftime(dateformat))
                                        embed.set_footer(text = user.display_name, icon_url = user.avatar_url)
                                        embed.set_thumbnail(url = skin)
                                        settings[1][3] = ct.strftime(dateformat)
                                        settings[1][4] = user.id
                                        with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                            file.write(str(settings))
                                        exec(create_wall_code(msg.guild.id, settings), globals())
                                        msg = await msg.channel.send(embed = embed)
                                        await msg.add_reaction('\u2705')
                                        await msg.add_reaction('\U0001f4a3')
                                elif e == r'\U0001f4a3':
                                    try:
                                        await msg.remove_reaction('\U0001f4a3', client.user)
                                    except:
                                        pass
                                    else:
                                        if found == 'alert':
                                            await msg.delete()
                                        else:
                                            await msg.clear_reactions()
                                        ct = datetime.datetime.utcnow().strftime(dateformat)
                                        exec(f'wall_alert{msg.guild.id}.cancel()', globals())
                                        exec(f'del wall_alert{msg.guild.id}', globals())
                                        if settings[2][0]:
                                            exec(f'buffer_alert{msg.guild.id}.cancel()', globals())
                                            exec(f'del buffer_alert{msg.guild.id}', globals())
                                        messages = await msg.channel.history(limit=30).flatten()
                                        for i in messages:
                                            if i.author.id == client.user.id:
                                                if len(i.embeds) == 1:
                                                    try:
                                                        if split_space(i.embeds[0].title) == 'Time to check walls!':
                                                            await i.delete()
                                                            break
                                                    except:
                                                        pass
                                        embed = discord.Embed(title = '', description = '```WeeWoo! We are being raided! Help!```', color = discord.Colour.red())
                                        embed.add_field(name = 'Triggered by', value = user.display_name)
                                        embed.add_field(name = 'Time', value = ct)
                                        embed.set_author(name = 'We are being raided! Help! Get online!', icon_url = 'https://www.logolynx.com/images/logolynx/6f/6f5bdc86a8c983a9a266765b10f1debd.png')
                                        embed.set_footer(text = 'stop reading this and GET ON!')
                                        embed.set_thumbnail(url = 'https://www.logolynx.com/images/logolynx/6f/6f5bdc86a8c983a9a266765b10f1debd.png')
                                        with open(os.path.join(wallsLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                            text = file.read()
                                            file.seek(0,0)
                                            file.write(f':bomb: **[{ct}]:** {user.mention}\n{text}')
                                        with open(os.path.join(buffersLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                            text = file.read()
                                            file.seek(0,0)
                                            file.write(f':bomb: **[{ct}]:** {user.mention}\n{text}')
                                        settings[1][3] = ct
                                        settings[1][4] = msg.author.id
                                        with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                            file.write(str(settings))
                                        exec(create_wall_code(msg.guild.id, settings), globals())
                                        if settings[2][0]:
                                            exec(create_buffer_code(msg.guild.id, settings), globals())
                                        await msg.channel.send(embed = embed)
                                        await msg.channel.send(f'Weewoo! We are being raided! Get on! <@&{msg.guild.get_role(settings[1][6]).id}>\n'*3)
                    else:
                        if split_space(title) == 'Time to check buffers!':
                            found = 'alert'
                            messages = await msg.channel.history(limit=30).flatten()
                            for i in messages:
                                if i.author == client.user:
                                    if len(i.embeds) == 1:
                                        if i.embeds[0].title.endswith('buffers clear.'):
                                            await i.clear_reactions()
                                            break
                        elif title.endswith('buffers clear.'):
                            found = 'clear'
                        if not found == False:
                            with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                settings = eval(file.read())
                            if settings[2][0]:
                                if msg.guild.get_role(settings[2][6]) or user.guild_permissions.administrator:
                                    e = reaction.emoji.encode('unicode-escape').decode('ASCII')
                                    if e == r'\u2705':
                                        try:
                                            await msg.remove_reaction('\u2705', client.user)
                                        except:
                                            pass
                                        else:
                                            if found == 'alert':
                                                await msg.delete()
                                            else:
                                                await msg.clear_reactions()
                                            exec(f'buffer_alert{msg.guild.id}.cancel()', globals())
                                            exec(f'del buffer_alert{msg.guild.id}', globals())
                                            ct = datetime.datetime.utcnow()
                                            with open(os.path.join(prefixDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                                prefix = file.read()
                                            with open(os.path.join(buffersDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                                text = file.read().split('\n')
                                                found = False
                                                if text == ['']:
                                                    text = [f'{user.id} 1']
                                                    score = '1'
                                                else:
                                                    for i in range(len(text)):
                                                        if text[i].startswith(str(user.id)):
                                                            found = True
                                                            score = str(int(text[i][19:])+1)
                                                            text[i] = text[i][:19] + score
                                                            break
                                                    if not found:
                                                        text.append(f'{user.id} 1')
                                                        score = '1'
                                                file.seek(0,0)
                                                file.write('\n'.join(text))
                                            with open(os.path.join(buffersLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                                text = file.read()
                                                file.seek(0,0)
                                                file.write(f":white_check_mark: **[{ct.strftime(dateformat)}]:** {user.mention}\n" + text)
                                            with open(os.path.join(skinsDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                                text = file.read().split('\n')
                                            found = False
                                            for i in text:
                                                if i.startswith(str(user.id)):
                                                    skin = f'https://minotar.net/avatar/{i[19:]}'
                                                    found = True
                                                    break
                                            if not found:
                                                skin = ''
                                            embed = discord.Embed(title = f':white_check_mark: **{user.display_name}** has marked buffers clear.', color = discord.Colour.green())
                                            embed.add_field(name = 'Checked by', value = user.mention, inline = True)
                                            embed.add_field(name = 'Score', value = score, inline = True)
                                            td = ct - datetime.datetime.strptime(settings[2][3], dateformat)
                                            td = datetime.timedelta(days = td.days, seconds = td.seconds)
                                            embed.add_field(name = 'Time Taken', value = str(td), inline = True)
                                            embed.add_field(name = 'Time Checked', value = ct.strftime(dateformat))
                                            embed.set_footer(text = user.display_name, icon_url = user.avatar_url)
                                            embed.set_thumbnail(url = skin)
                                            settings[2][3] = ct.strftime(dateformat)
                                            settings[2][4] = user.id
                                            with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                                file.write(str(settings))
                                            exec(create_buffer_code(msg.guild.id, settings), globals())
                                            msg = await msg.channel.send(embed = embed)
                                            await msg.add_reaction('\u2705')
                                            await msg.add_reaction('\U0001f4a3')
                                    elif e == r'\U0001f4a3':
                                        try:
                                            await msg.remove_reaction('\U0001f4a3', client.user)
                                        except:
                                            pass
                                        else:
                                            if settings[1][0]:
                                                if found == 'alert':
                                                    await msg.delete()
                                                else:
                                                    await msg.clear_reactions()
                                                ct = datetime.datetime.utcnow().strftime(dateformat)
                                                ch = client.get_channel(settings[1][5])
                                                exec(f'wall_alert{msg.guild.id}.cancel()', globals())
                                                exec(f'buffer_alert{msg.guild.id}.cancel()', globals())
                                                exec(f'del wall_alert{msg.guild.id}', globals())
                                                exec(f'del buffer_alert{msg.guild.id}', globals())
                                                messages = await ch.history(limit=30).flatten()
                                                for i in messages:
                                                    if i.author.id == client.user.id:
                                                        if len(i.embeds) == 1:
                                                            try:
                                                                if split_space(i.embeds[0].title) == 'Time to check walls!':
                                                                    await i.delete()
                                                                    break
                                                            except:
                                                                pass
                                                embed = discord.Embed(title = '', description = '```WeeWoo! We are being raided! Help!```', color = discord.Colour.red())
                                                embed.add_field(name = 'Triggered by', value = user.display_name)
                                                embed.add_field(name = 'Time', value = ct)
                                                embed.set_author(name = 'We are being raided! Help! Get online!', icon_url = 'https://www.logolynx.com/images/logolynx/6f/6f5bdc86a8c983a9a266765b10f1debd.png')
                                                embed.set_footer(text = 'stop reading this and GET ON!')
                                                embed.set_thumbnail(url = 'https://www.logolynx.com/images/logolynx/6f/6f5bdc86a8c983a9a266765b10f1debd.png')
                                                with open(os.path.join(wallsLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                                    text = file.read()
                                                    file.seek(0,0)
                                                    file.write(f':bomb: **[{ct}]:** {user.mention}\n{text}')
                                                with open(os.path.join(buffersLogsDir, str(msg.guild.id)+'.txt'), 'r+') as file:
                                                    text = file.read()
                                                    file.seek(0,0)
                                                    file.write(f':bomb: **[{ct}]:** {user.mention}\n{text}')
                                                settings[1][3] = ct
                                                settings[1][4] = msg.author.id
                                                with open(os.path.join(settingsDir, str(msg.guild.id)+'.txt'), 'w+') as file:
                                                    file.write(str(settings))
                                                exec(create_wall_code(msg.guild.id, settings), globals())
                                                exec(create_buffer_code(msg.guild.id, settings), globals())
                                                await ch.send(embed = embed)
                                                await ch.send(f'Weewoo! We are being raided! Get on! <@&{msg.guild.get_role(settings[1][6]).id}>\n'*3)
                                            else:
                                                with open(os.path.join(prefixDir, str(msg.guild.id)+'.txt'), 'r') as file:
                                                    prefix = file.read()
                                                embed = discord.Embed(title = ':gear: Settings - Walls', description = f':x: You cannot use that command because the __wall check__ module is `DISABLED`.\nTo enable the __wall check__ module, do `{prefix}settings walls on`', color = discord.Colour.blue())
                                                embed.set_footer(text = f'{user.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = user.avatar_url)
                                                await msg.channel.send(embed = embed)

@client.event
async def on_guild_channel_delete(ch):
    with open(os.path.join(settingsDir, str(ch.guild.id)+'.txt'), 'r') as file:
        settings = eval(file.read())
    if ch.id == settings[0][3]:
        if settings[0][0]:
            with open(os.path.join(prefixDir, str(ch.guild.id)+'.txt'), 'r') as file:
                prefix = file.read()
            found = False
            for i in ch.guild.text_channels:
                if i.name == 'value-added':
                    found = True
                    settings[0][3] = i.id
                    embed = discord.Embed(title = ':gear: Settings - Value Module', description = f'The previously set __value channel__ was deleted.\nTo overcome the issue, this channel has been automatically selected and will be used in the future. To change the value channel, do\n```{prefix}settings channel value <mention the channel>```', color = discord.Colour.blue())
                    embed.set_footer(text = f'{client.user.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                    await i.send(embed = embed)
                    break
            if not found:
                i = await ch.guild.create_text_channel('value-added')
                settings[0][3] = i.id
                embed = discord.Embed(title = ':gear: Settings - Value Module', description = f'The previously set __value channel__ was deleted.\nTo overcome the issue, this channel has been created and will be used in the future. To change the value channel, do\n```{prefix}settings channel value <mention the channel>```', color = discord.Colour.blue())
                embed.set_footer(text = f'{client.user.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                await i.send(embed = embed)
            with open(os.path.join(settingsDir, str(ch.guild.id)+'.txt'), 'w+') as file:
                file.write(str(settings))
        else:
            settings[0][3] = None
            with open(os.path.join(settingsDir, str(ch.guild.id)+'.txt'), 'w+') as file:
                file.write(str(settings))
    elif ch.id == settings[1][5]:
        if settings[1][0]:
            with open(os.path.join(prefixDir, str(ch.guild.id)+'.txt'), 'r') as file:
                prefix = file.read()
            found = False
            for i in ch.guild.text_channels:
                if i.name == 'wall-check':
                    found = True
                    settings[1][5] = i.id
                    embed = discord.Embed(title = ':gear: Settings - Walls Module', description = f'The previously set __walls channel__ was deleted.\nTo overcome the issue, this channel has been automatically selected and will be used in the future. To change the walls channel, do\n```{prefix}settings channel walls <mention the channel>```', color = discord.Colour.blue())
                    embed.set_footer(text = f'{client.user.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                    await i.send(embed = embed)
                    break
            if not found:
                i = await ch.guild.create_text_channel('wall-check')
                settings[1][5] = i.id
                embed = discord.Embed(title = ':gear: Settings - Walls Module', description = f'The previously set __walls channel__ was deleted.\nTo overcome the issue, this channel has been created and will be used in the future. To change the walls channel, do\n```{prefix}settings channel walls <mention the channel>```', color = discord.Colour.blue())
                embed.set_footer(text = f'{client.user.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                await i.send(embed = embed)
            with open(os.path.join(settingsDir, str(ch.guild.id)+'.txt'), 'w+') as file:
                file.write(str(settings))
        else:
            settings[1][5] = None
            with open(os.path.join(settingsDir, str(ch.guild.id)+'.txt'), 'w+') as file:
                file.write(str(settings))
    elif ch.id == settings[2][5]:
        if settings[2][0]:
            with open(os.path.join(prefixDir, str(ch.guild.id)+'.txt'), 'r') as file:
                prefix = file.read()
            found = False
            for i in ch.guild.text_channels:
                if i.name == 'buffer-check':
                    found = True
                    settings[2][5] = i.id
                    embed = discord.Embed(title = ':gear: Settings - Buffers Module', description = f'The previously set __buffers channel__ was deleted.\nTo overcome the issue, this channel has been automatically selected and will be used in the future. To change the buffers channel, do\n```{prefix}settings channel buffers <mention the channel>```', color = discord.Colour.blue())
                    embed.set_footer(text = f'{client.user.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                    await i.send(embed = embed)
                    break
            if not found:
                i = await ch.guild.create_text_channel('buffer-check')
                settings[2][5] = i.id
                embed = discord.Embed(title = ':gear: Settings - Buffers Module', description = f'The previously set __buffers channel__ was deleted.\nTo overcome the issue, this channel has been created and will be used in the future. To change the buffers channel, do\n```{prefix}settings channel buffers <mention the channel>```', color = discord.Colour.blue())
                embed.set_footer(text = f'{client.user.display_name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                await i.send(embed = embed)
            with open(os.path.join(settingsDir, str(ch.guild.id)+'.txt'), 'w+') as file:
                file.write(str(settings))
        else:
            settings[2][5] = None
            with open(os.path.join(settingsDir, str(ch.guild.id)+'.txt'), 'w+') as file:
                file.write(str(settings))


@client.event
async def on_guild_remove(a):

    os.remove(os.path.join(settingsDir, str(a.id)+'.txt'))
    try:
        exec(f'wall_alert{a.id}.cancel()', globals())
        exec(f'del wall_alert{a.id}', globals())
    except:
        pass
    try:
        exec(f'buffer_alert{a.id}.cancel()', globals())
        exec(f'del buffer_alert{a.id}', globals())
    except:
        pass
    print(f'\nRemoved from a guild: {a.id} - {a.id}\n')


@tasks.loop(hours = 23)
async def daily_report():
    ct = datetime.datetime.utcnow()
    td = datetime.datetime(ct.year, ct.month, ct.day+1, 0,0) - ct
    print(td.seconds)
    await asyncio.sleep(td.seconds)
    for a in client.guilds:
        try:
            perms = a.me.guild_permissions
            found = False
            if not perms.manage_roles:
                found = True
            elif not perms.manage_channels:
                found = True
            elif not perms.read_messages:
                found = True
            elif not perms.send_messages:
                found = True
            elif not perms.manage_messages:
                found = True
            elif not perms.embed_links:
                found = True
            elif not perms.read_message_history:
                found = True
            elif not perms.mention_everyone:
                found = True
            elif not perms.add_reactions:
                found = True
            if found:
                for i in a.text_channels:
                    if i.name =='value-added':
                        try:
                            embed = discord.Embed(title = ':gear: Not enough permissions.', description = 'The bot does not have the required permissions. Re-invite the bot using this [link](https://discordapp.com/api/oauth2/authorize?client_id=637575751583137822&permissions=268659792&scope=bot). If you are having problems, you can join the support [discord server](https://discord.gg/bnKE45S).', color = discord.Colour.blue())
                            await i.send(embed = embed)
                            break
                        except:
                            pass
            with open(os.path.join(settingsDir, str(a.id)+'.txt'), 'r') as file:
                settings = eval(file.read())
            if not settings[0][2] == None:
                if settings[0][0]:
                    ch = client.get_channel(settings[0][3])
                    perms = ch.permissions_for(a.me)
                    with open(os.path.join(todayDir, str(a.id)+'.txt'), 'r') as file:
                        text = file.read().split('\n')
                    if text == ['']:
                        if perms.send_messages:
                            embed = discord.Embed(title = 'Daily Progress Report', description = f"**Goal :** `{commas(str(settings[0][2]))}`\n\n**Value added today:** `0`\n\n*Stop slacking guys and get to work.*", color = discord.Colour.gold())
                            embed.set_footer(text = f'Daily score has been reset.\n{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                            await ch.send(embed = embed)
                    else:
                        text.sort(key = sortkey, reverse = True)
                        total = 0
                        for i in range(len(text)):
                            total += int(text[i][19:])
                            text[i] = f'**{i+1}.** <@!{text[i][:18]}> {commas(text[i][19:])}'
                        p = round(total/settings[0][2]*100, 3)
                        if total < 0:
                            message = "I don't even know how that's possible."
                        elif total == 0:
                            message = 'Stop slacking guys and get to work.'
                        elif p > 100:
                            message = "The daily goal was reached!"
                        elif p > 90:
                            message = 'Good job guys! We were so close.'
                        elif p > 75:
                            message = "Only if we had worked harder."
                        elif p//1 == 69:
                            message = "Nice."
                        elif p > 50:
                            message = "We were more than halfway through."
                        elif p > 25:
                            message = "Gotta work on our teamwork."
                        elif p > 0:
                            message = "We need to bump up these numbers."
                        text = '\n'.join(text)
                        if perms.send_messages:
                            embed = discord.Embed(title = 'Daily Progress Report', description = f"**Goal :** `{commas(str(settings[0][2]))}`\n\n**Value added till now :**\n`{commas(str(total))}` __{p}%__\n\n*\"{message}\"*\n\n**Top Contributers of the day - **\n{text}", color = discord.Colour.gold())
                            embed.set_footer(text = f'Daily score has been reset.\n{client.user.name} | {datetime.datetime.utcnow().strftime(dateformat)}', icon_url = client.user.avatar_url)
                            await ch.send(embed = embed)
                        with open(os.path.join(todayDir, str(a.id)+'.txt'), 'w+') as file:
                            pass
                    with open(os.path.join(valueLogsDir, str(a.id)+'.txt'), 'r+') as file:
                        text = file.read()
                        file.seek(0,0)
                        file.write(f":gear: **[{datetime.datetime.utcnow().strftime(dateformat)}]:** {a.me.mention} : reset daily score.\n{text}")
        except:
            pass

client.run(token)
