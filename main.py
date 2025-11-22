import requests, random
from discord_webhook import DiscordWebhook, DiscordEmbed  # pip install discord_webhook
import os

print('''Bot Made & Coded by quehole''')
print("\x1b[32mhttps://youtube.com/@quehole\x1b[39m")
while True:
  ID = random.randint(10800000,
                      10960000)  # Start and stop IDs edit this if you want!
  webhook = DiscordWebhook(
      url=
      "your webhook here" # replace with your webhook URL
  )  # initates connection with discord_webhook module
  r = requests.get(
      f'https://groups.roblox.com/v1/groups/{ID}')  #sends requests using id
  json = r.json()  # json
  if 'owner' in r.text:  #checks if the group is valid to prevent key errors
    if json['owner'] == None and json[
        'publicEntryAllowed'] == True and 'isLocked' not in r.text:  # check if the group isnt locked and is open with no owner
      members = json['memberCount']  #members
      desc = json['description']  #obvious what this one is
      print(f"\x1b[42mhttps://www.roblox.com/groups/{ID}")
      print(r.text)
      embed = DiscordEmbed(title='New unclaimed Group',
                           color=242424)  # embed title
      embed.add_embed_field(name='ID', value=f'{ID}')  #Id to embed
      embed.add_embed_field(name='Description',
                            value=f'"{desc}"')  #description to embed
      embed.add_embed_field(name='Members',
                            value=f'{members}')  #adds members to embed
      embed.add_embed_field(name='Link',
                            value=f'https://www.roblox.com/groups/{ID}'
                            )  # im getting bored commenting
      embed.set_author(
          name='',
          icon_url=
          'https://images-ext-2.discordapp.net/external/ExvpqVgJoqrUwoORcZKxOTd50iE2vnNcwF9nlrU8Qms/%3Fsize%3D1024/https/cdn.discordapp.com/icons/799181637405376533/89565089064040e52100ba4aea324604.webp'
      )  #stuff
      embed.set_footer(
          text='GFind',
          icon_url=
          'https://images-ext-2.discordapp.net/external/ExvpqVgJoqrUwoORcZKxOTd50iE2vnNcwF9nlrU8Qms/%3Fsize%3D1024/https/cdn.discordapp.com/icons/799181637405376533/89565089064040e52100ba4aea324604.webp'
      )  # stuff
      embed.set_thumbnail(
          url=
          'https://images-ext-2.discordapp.net/external/ExvpqVgJoqrUwoORcZKxOTd50iE2vnNcwF9nlrU8Qms/%3Fsize%3D1024/https/cdn.discordapp.com/icons/799181637405376533/89565089064040e52100ba4aea324604.webp'
      )
      webhook.add_embed(embed)  #adds the embed to the response
      response = webhook.execute()  # sends to webhook
    else:
      print(f"\x1b[31mNothing found... {ID}")
  else:
    print(f"\x1b[31mNothing found... {ID}")