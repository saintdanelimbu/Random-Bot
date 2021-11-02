

import discord
import os
import time
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
import random
from random import randint
from dhooks import Webhook,Embed
import names


client = discord.Client()

client = commands.Bot(command_prefix = '-',case_insensitive=True) 

@client.event
async def on_ready():
    channel = client.get_channel(903690747197390888)
    await channel.send('Random Bot is UP!')
    print("bot online")
##GLOBE##
@client.command()
async def globe(ctx,howmany:int):
    def awitized():
      numbers=[]
      for i in range(0,howmany):
        globe = ['0905','0906','0915','0916','0917','0926','0927','0935','0936','0937','0945','0953','0954','0955','0956','0965','0966','0967','0975','0977','0978','0979','0994','0995','0996','0997'] 
        globenumber = random.choice(globe) 
        randomized = f"{globenumber}{random.randint(1000000,9999999)}"
        numbers.append(randomized)
      return '\n'.join(str(e) for e in numbers)
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed()   
    embed.title='GLOBE'
    embed.colour = discord.Color.teal()
    embed.description= awitized()
            
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/814869462188556339/903697451754590218/globe-removebg-preview.png') 
    embed.set_author(name='DNA Random Bot')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

##SMART##
@client.command()
async def smart(ctx,howmany:int):
    def awitized():
      numbers=[]
      for i in range(0,howmany):
        smart = ['0908','0918','0919','0920','0921','0928','0929','0939','0947','0949','0951','0961','0998','0999'] 
        smartnumber = random.choice(smart) 
        randomized = f"{smartnumber}{random.randint(1000000,9999999)}"
        numbers.append(randomized)
      return '\n'.join(str(e) for e in numbers)
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed()   
    embed.title='SMART'
    embed.colour = discord.Color.teal()
    embed.description= awitized()
            
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://download.logo.wine/logo/Smart_Communications/Smart_Communications-Logo.wine.png') 
    embed.set_author(name='DNA Random Bot')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

##SUN##
@client.command()
async def sun(ctx,howmany:int):
    def awitized():
      numbers=[]
      for i in range(0,howmany):
        sun = ['0922','0923','0924','0925','0931','0932','0933','0934','0940','0941','0942','0943','0973','0974']   
        sunnumber = random.choice(sun) 
        randomized = f"{sunnumber}{random.randint(1000000,9999999)}"
        numbers.append(randomized)
      return '\n'.join(str(e) for e in numbers)
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed()   
    embed.title='SUN'
    embed.colour = discord.Color.teal()
    embed.description= awitized()        
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://static.wikia.nocookie.net/logopedia/images/7/7c/Sun_Cellular_logo.svg/revision/latest/scale-to-width-down/250?cb=20130911111111') 
    embed.set_author(name='DNA Random Bot')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

##TNT##
@client.command()
async def tnt(ctx,howmany:int):
    def awitized():
      numbers=[]
      for i in range(0,howmany):
        tnt = ['0907','0909','0910','0912','0930','0938','0946','0948','0950']    
        tntnumber = random.choice(tnt) 
        randomized = f"{tntnumber}{random.randint(1000000,9999999)}"
        numbers.append(randomized)
      return '\n'.join(str(e) for e in numbers)
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed()   
    embed.title='TNT'
    embed.colour = discord.Color.teal()
    embed.description= awitized()        
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/3/36/TNT_%28cellular_service%29_logo.png') 
    embed.set_author(name='DNA Random Bot')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

##ADDRESS##
shit = open('words.txt').read().splitlines()
##NCR##
@client.command()
async def ncr(ctx,howmany:int):
    def awitized():
      address=[]
      for i in range(0,howmany):
        ncr = open('ncr.txt').read().splitlines()
        randomnumber = random.randint(1,999)
        randomshit = random.choice(shit)
        randomncr =random.choice(ncr)
        address.append(f"{str(randomnumber)} {randomshit} Street {randomncr}")
      return '\n'.join(str(e) for e in address)
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed()   
    embed.title='NATIONAL CAPITAL REGION (NCR)'
    embed.colour = discord.Color.teal()
    embed.description= awitized()        
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://wallpaperaccess.com/full/503514.jpg') 
    embed.set_author(name='DNA Random Bot')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

## CORDILLERA ADMINISTRATIVE REGION ##
@client.command()
async def cordillera(ctx,howmany:int):
    def awitized():
      address=[]
      for i in range(0,howmany):
        cordillera = open('cordillera.txt').read().splitlines()
        randomnumber = random.randint(1,999)
        randomshit = random.choice(shit)
        randomcordillera =random.choice(cordillera)
        address.append(f"{str(randomnumber)} {randomshit} Street {randomcordillera}")
      return '\n'.join(str(e) for e in address)
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed()   
    embed.title='CORDILLERA ADMINISTRATIVE REGION'
    embed.colour = discord.Color.teal()
    embed.description= awitized()        
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://wallpaperaccess.com/full/503514.jpg') 
    embed.set_author(name='DNA Random Bot')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

## REGION 1 (ILOCOS REGION)##
@client.command()
async def ilocosregion(ctx,howmany:int):
    def awitized():
      address=[]
      for i in range(0,howmany):
        region1 = open('region1.txt').read().splitlines()
        randomnumber = random.randint(1,999)
        randomshit = random.choice(shit)
        randomregion1 =random.choice(region1)
        address.append(f"{str(randomnumber)} {randomshit} Street {randomregion1}")
      return '\n'.join(str(e) for e in address)
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed()   
    embed.title='REGION 1 (ILOCOS REGION)'
    embed.colour = discord.Color.teal()
    embed.description= awitized()        
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://wallpaperaccess.com/full/503514.jpg') 
    embed.set_author(name='DNA Random Bot')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

## REGION 2 (CAGAYAN REGION)##
@client.command()
async def cagayanregion(ctx,howmany:int):
    def awitized():
      address=[]
      for i in range(0,howmany):
        region2 = open('region2.txt').read().splitlines()
        randomnumber = random.randint(1,999)
        randomshit = random.choice(shit)
        randomregion2 =random.choice(region2)
        address.append(f"{str(randomnumber)} {randomshit} Street {randomregion2}")
      return '\n'.join(str(e) for e in address)
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed()   
    embed.title='REGION 2 (CAGAYAN REGION)'
    embed.colour = discord.Color.teal()
    embed.description= awitized()        
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://wallpaperaccess.com/full/503514.jpg') 
    embed.set_author(name='DNA Random Bot')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

## REGION 3 (CENTRAL LUZON)##
@client.command()
async def centralluzon(ctx,howmany:int):
    def awitized():
      address=[]
      for i in range(0,howmany):
        region3 = open('region3.txt').read().splitlines()
        randomnumber = random.randint(1,999)
        randomshit = random.choice(shit)
        randomregion3 =random.choice(region3)
        address.append(f"{str(randomnumber)} {randomshit} Street {randomregion3}")
      return '\n'.join(str(e) for e in address)
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed()   
    embed.title='REGION 3 (CENTRAL LUZON)'
    embed.colour = discord.Color.teal()
    embed.description= awitized()        
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://wallpaperaccess.com/full/503514.jpg') 
    embed.set_author(name='DNA Random Bot')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

## REGION 4 (CALABARZON)##
@client.command()
async def calabarzon(ctx,howmany:int):
    def awitized():
      address=[]
      for i in range(0,howmany):
        calabarzon = open('calabarzon.txt').read().splitlines()
        randomnumber = random.randint(1,999)
        randomshit = random.choice(shit)
        randomcalabarzon =random.choice(calabarzon)
        address.append(f"{str(randomnumber)} {randomshit} Street {randomcalabarzon}")
      return '\n'.join(str(e) for e in address)
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed()   
    embed.title='REGION 4 (CALABARZON)'
    embed.colour = discord.Color.teal()
    embed.description= awitized()        
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://wallpaperaccess.com/full/503514.jpg') 
    embed.set_author(name='DNA Random Bot')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

## REGION 4 (MIMAROPA)##
@client.command()
async def mimaropa(ctx,howmany:int):
    def awitized():
      address=[]
      for i in range(0,howmany):
        mimaropa = open('mimaropa.txt').read().splitlines()
        randomnumber = random.randint(1,999)
        randomshit = random.choice(shit)
        randommimaropa =random.choice(mimaropa)
        address.append(f"{str(randomnumber)} {randomshit} Street {randommimaropa}")
      return '\n'.join(str(e) for e in address)
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed()   
    embed.title='REGION 4 (MIMAROPA)'
    embed.colour = discord.Color.teal()
    embed.description= awitized()        
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://wallpaperaccess.com/full/503514.jpg') 
    embed.set_author(name='DNA Random Bot')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

## REGION 5 (BICOL REGION)##
@client.command()
async def bicolregion(ctx,howmany:int):
    def awitized():
      address=[]
      for i in range(0,howmany):
        region5 = open('region5.txt').read().splitlines()
        randomnumber = random.randint(1,999)
        randomshit = random.choice(shit)
        randomregion5 =random.choice(region5)
        address.append(f"{str(randomnumber)} {randomshit} Street {randomregion5}")
      return '\n'.join(str(e) for e in address)
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed()   
    embed.title='REGION 5 (BICOL REGION)'
    embed.colour = discord.Color.teal()
    embed.description= awitized()        
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://wallpaperaccess.com/full/503514.jpg') 
    embed.set_author(name='DNA Random Bot')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

## REGION 6 (WESTERN VISAYAS)##
@client.command()
async def westernvisayas(ctx,howmany:int):
    def awitized():
      address=[]
      for i in range(0,howmany):
        region6 = open('region6.txt').read().splitlines()
        randomnumber = random.randint(1,999)
        randomshit = random.choice(shit)
        randomregion6 =random.choice(region6)
        address.append(f"{str(randomnumber)} {randomshit} Street {randomregion6}")
      return '\n'.join(str(e) for e in address)
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed()   
    embed.title='REGION 6 (WESTERN VISAYAS)'
    embed.colour = discord.Color.teal()
    embed.description= awitized()        
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://wallpaperaccess.com/full/503514.jpg') 
    embed.set_author(name='DNA Random Bot')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

## REGION 7 (CENTRAL VISAYAS)##
@client.command()
async def centralvisayas(ctx,howmany:int):
    def awitized():
      address=[]
      for i in range(0,howmany):
        region7 = open('region7.txt').read().splitlines()
        randomnumber = random.randint(1,999)
        randomshit = random.choice(shit)
        randomregion7 =random.choice(region7)
        address.append(f"{str(randomnumber)} {randomshit} Street {randomregion7}")
      return '\n'.join(str(e) for e in address)
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed()   
    embed.title='REGION 7 (CENTRAL VISAYAS)'
    embed.colour = discord.Color.teal()
    embed.description= awitized()        
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://wallpaperaccess.com/full/503514.jpg') 
    embed.set_author(name='DNA Random Bot')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

## REGION 8 (EASTERN VISAYAS)##
@client.command()
async def easternvisayas(ctx,howmany:int):
    def awitized():
      address=[]
      for i in range(0,howmany):
        region8 = open('region8.txt').read().splitlines()
        randomnumber = random.randint(1,999)
        randomshit = random.choice(shit)
        randomregion8 =random.choice(region8)
        address.append(f"{str(randomnumber)} {randomshit} Street {randomregion8}")
      return '\n'.join(str(e) for e in address)
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed()   
    embed.title='REGION 8 (EASTERN VISAYAS)'
    embed.colour = discord.Color.teal()
    embed.description= awitized()        
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://wallpaperaccess.com/full/503514.jpg') 
    embed.set_author(name='DNA Random Bot')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

## REGION 9 (ZAMBOANGA PENINSULA)##
@client.command()
async def zamboanga(ctx,howmany:int):
    def awitized():
      address=[]
      for i in range(0,howmany):
        region9 = open('region9.txt').read().splitlines()
        randomnumber = random.randint(1,999)
        randomshit = random.choice(shit)
        randomregion9 =random.choice(region9)
        address.append(f"{str(randomnumber)} {randomshit} Street {randomregion9}")
      return '\n'.join(str(e) for e in address)
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed()   
    embed.title='REGION 9 (ZAMBOANGA PENINSULA)'
    embed.colour = discord.Color.teal()
    embed.description= awitized()        
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://wallpaperaccess.com/full/503514.jpg') 
    embed.set_author(name='DNA Random Bot')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

## REGION 10 (NORTHERN MINDANAO)##
@client.command()
async def northernmindanao(ctx,howmany:int):
    def awitized():
      address=[]
      for i in range(0,howmany):
        region10 = open('region10.txt').read().splitlines()
        randomnumber = random.randint(1,999)
        randomshit = random.choice(shit)
        randomregion10 =random.choice(region10)
        address.append(f"{str(randomnumber)} {randomshit} Street {randomregion10}")
      return '\n'.join(str(e) for e in address)
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed()   
    embed.title='REGION 10 (NORTHERN MINDANAO)'
    embed.colour = discord.Color.teal()
    embed.description= awitized()        
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://wallpaperaccess.com/full/503514.jpg') 
    embed.set_author(name='DNA Random Bot')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

## REGION 11 (DAVAO REGION)##
@client.command()
async def davaoregion(ctx,howmany:int):
    def awitized():
      address=[]
      for i in range(0,howmany):
        region11 = open('region11.txt').read().splitlines()
        randomnumber = random.randint(1,999)
        randomshit = random.choice(shit)
        randomregion11 =random.choice(region11)
        address.append(f"{str(randomnumber)} {randomshit} Street {randomregion11}")
      return '\n'.join(str(e) for e in address)
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed()   
    embed.title='REGION 11 (DAVAO REGION)'
    embed.colour = discord.Color.teal()
    embed.description= awitized()        
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://wallpaperaccess.com/full/503514.jpg') 
    embed.set_author(name='DNA Random Bot')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

## REGION 12 (Soccsksargen)##
@client.command()
async def region12(ctx,howmany:int):
    def awitized():
      address=[]
      for i in range(0,howmany):
        region12 = open('region12.txt').read().splitlines()
        randomnumber = random.randint(1,999)
        randomshit = random.choice(shit)
        randomregion12 =random.choice(region12)
        address.append(f"{str(randomnumber)} {randomshit} Street {randomregion12}")
      return '\n'.join(str(e) for e in address)
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed()   
    embed.title='REGION 12 (Soccsksargen)'
    embed.colour = discord.Color.teal()
    embed.description= awitized()        
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://wallpaperaccess.com/full/503514.jpg') 
    embed.set_author(name='DNA Random Bot')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

## REGION 13 (CARAGA)##
@client.command()
async def caraga(ctx,howmany:int):
    def awitized():
      address=[]
      for i in range(0,howmany):
        region13 = open('region13.txt').read().splitlines()
        randomnumber = random.randint(1,999)
        randomshit = random.choice(shit)
        randomregion13 =random.choice(region13)
        address.append(f"{str(randomnumber)} {randomshit} Street {randomregion13}")
      return '\n'.join(str(e) for e in address)
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed()   
    embed.title='REGION 13 (CARAGA)'
    embed.colour = discord.Color.teal()
    embed.description= awitized()        
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://wallpaperaccess.com/full/503514.jpg') 
    embed.set_author(name='DNA Random Bot')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

##RANDOM NAME##

## FIRSTNAME##
@client.command()
async def firstname(ctx,howmany:int):
    def awitized():
      name=[]
      for i in range(0,howmany):
        awit = names.get_first_name()
        name.append(awit)
      return '\n'.join(str(e) for e in name)
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed()   
    embed.title='FIRST NAME'
    embed.colour = discord.Color.teal()
    embed.description= awitized()        
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/814869462188556339/904842661318520882/MALEFEMALE-removebg-preview.png') 
    embed.set_author(name='DNA Random Bot')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

## FIRSTNAME MALE##
@client.command()
async def firstname_male(ctx,howmany:int):
    def awitized():
      name=[]
      for i in range(0,howmany):
        awit = names.get_first_name(gender='male')
        name.append(awit)
      return '\n'.join(str(e) for e in name)
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed()   
    embed.title='FIRST NAME (MALE)'
    embed.colour = discord.Color.teal()
    embed.description= awitized()        
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Mars-male-symbol-pseudo-3D-blue.svg/1200px-Mars-male-symbol-pseudo-3D-blue.svg.png') 
    embed.set_author(name='DNA Random Bot')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

## FIRSTNAME FEMALE##
@client.command()
async def firstname_female(ctx,howmany:int):
    def awitized():
      name=[]
      for i in range(0,howmany):
        awit = names.get_first_name(gender='female')
        name.append(awit)
      return '\n'.join(str(e) for e in name)
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed()   
    embed.title='FIRST NAME (FEMALE)'
    embed.colour = discord.Color.teal()
    embed.description= awitized()        
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Venus-female-symbol-pseudo-3D-pink.svg/1200px-Venus-female-symbol-pseudo-3D-pink.svg.png') 
    embed.set_author(name='DNA Random Bot')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)
lastname = open('lastname.txt').read().splitlines()
## FULLNAME##
@client.command()
async def fullname(ctx,howmany:int):
    def awitized():
      name=[]
      for i in range(0,howmany):
        randomlastname = random.choice(lastname)
        awit = f"{names.get_first_name()} {randomlastname}"
        name.append(awit)
      return '\n'.join(str(e) for e in name)
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed()   
    embed.title='FULL NAME'
    embed.colour = discord.Color.teal()
    embed.description= awitized()        
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/814869462188556339/904842661318520882/MALEFEMALE-removebg-preview.png') 
    embed.set_author(name='DNA Random Bot')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

## FULLNAME MALE##
@client.command()
async def fullname_male(ctx,howmany:int):
    def awitized():
      name=[]
      for i in range(0,howmany):
        randomlastname = random.choice(lastname)
        awit = f"{names.get_first_name(gender='male')} {randomlastname}"
        name.append(awit)
      return '\n'.join(str(e) for e in name)
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed()   
    embed.title='FULL NAME (MALE)'
    embed.colour = discord.Color.teal()
    embed.description= awitized()        
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Mars-male-symbol-pseudo-3D-blue.svg/1200px-Mars-male-symbol-pseudo-3D-blue.svg.png') 
    embed.set_author(name='DNA Random Bot')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

## FULLNAME FEMALE##
@client.command()
async def fullname_female(ctx,howmany:int):
    def awitized():
      name=[]
      for i in range(0,howmany):
        randomlastname = random.choice(lastname)
        awit = f"{names.get_first_name(gender='female')} {randomlastname}"
        name.append(awit)
      return '\n'.join(str(e) for e in name)
    hook = Webhook('https://discord.com/api/webhooks/890607746481782815/HHIIWq6PrYTmkfGX-buMS92CGXDfZoek-2JvyfU2kFywge5jW3OcblFar6qMjTNNhD6g')   
    embed = discord.Embed()   
    embed.title='FULL NAME (FEMALE)'
    embed.colour = discord.Color.teal()
    embed.description= awitized()        
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Venus-female-symbol-pseudo-3D-pink.svg/1200px-Venus-female-symbol-pseudo-3D-pink.svg.png') 
    embed.set_author(name='DNA Random Bot')  
    await ctx.send(embed=embed)
    hook.send(embed=embed)

##HELP##
client.remove_command('help')
@client.command(pass_context=True)
async def help(ctx):
  author = ctx.message.author
  embed = discord.Embed(
    description="""**RANDOM PHONE NUMBERS:**
  -globe (value) 
  -smart (value) 
  -sun (value) 
  -tnt (value) 
  
  **RANDOM ADDRESS:**
  -ncr (value) 
  -cordillera (value) 
  -ilocosregion (value) 
  -cagayanregion (value) 
  -centralluzon (value) 
  -calabarzon (value) 
  -bicolregion (value) 
  -westernvisayas (value) 
  -centralvisayas (value) 
  -easternvisayas (value) 
  -zamboanga (value) 
  -northernmindanao(value) 
  -davaoregion (value) 
  -region12 (value) 
  -caraga (value) 
  
  **RANDOM NAME:**
  -firstname (value) 
  -firstname_male (value) 
  -firstname_female (value) 
  -fullname (value) 
  -fullname_male (value) 
  -fullname_female (value) """
  )
  embed.colour = discord.Color.teal()
  embed.title='DNA HELP'
  embed.set_thumbnail(url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
  
  embed.set_footer(text='Powered by DNA Solutions',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
  
  await author.send(embed=embed)
  await ctx.send("Look at your DM's!")

client.run("OTA0ODIzNTQxMzk5MTU4Nzk0.YYBIlw.xZ64Eu9IVMdsRsDk6z6LZ2nH5yM")