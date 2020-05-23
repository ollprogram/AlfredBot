#-------------------------------------------------------------
#                   Python Alfred Bot
#-------------------------------------------------------------
#Auteurs:
#- Louka Placé -> à founit certaines commande du cobrabot
#- Olivier Palvadeau -> créateur du projet
#- Paul Coignac -> à founit certaines commande du cobrabot

#Version: 1.5
#prochain patch --> universalisation des commandes rainbow
#Description Globale:
#Ce programme fonctionne avec l'API discord pour python
#Le programme envoi des informations de script python au bot
#Le bot garde le code en mémoire
#Ce code permet donc de coder notre Bot Discord (Stephanie)

#Description du Bot:
    #Permet globalement, de attribuer des roles aux nouveaux
#arrivants

#-------------------------------------------------------------
#Importations de modules et packages:
#-------------------------------------------------------------
import discord
import asyncio
from random import *
import time
#-------------------------------------------------------------
#             Début du programme:
#-------------------------------------------------------------

bot = discord.Client() #l'objet bot correspond à CobraBot, il s'agit d'un client (utilisateur)
#id d'utilisateurs gérant le bot
Own1 = 233296342112403467 #Olivier
onoff = 0
#colors
rouge = discord.Colour.red()
rose = discord.Colour.magenta()
magenta = discord.Colour.dark_magenta()
violet = discord.Colour.dark_purple()
bleu = discord.Colour.dark_teal()
cyan = discord.Colour.teal()
turquoise = discord.Colour.blue()
vert = discord.Colour.dark_green()
lime = discord.Colour.green()
jaune = discord.Colour.gold()
orange = discord.Colour.dark_orange()
fire = discord.Colour.orange()
colorList = [rouge,rose,magenta,violet,bleu,cyan,turquoise,vert,lime,jaune,orange,fire]
    
    
#************************************************************************************************************************************************
#                                             Listes informations
#************************************************************************************************************************************************
def cleanList(liste):
    for index in range(len(liste)):                      #cette fonction permet d'effacer le \n pour chaque terme de la liste
        liste[index] = liste[index].replace("\n", "")
    return liste
def listType(liste, dataType):                           #cette fonction permet de changer le type de chaque terme de la liste
    if dataType == "int":
        for i in range(len(liste)):
            liste[i] = int(liste[i])
        return liste
    elif dataType == "str":
        for i in range(len(liste)):
            liste[i] = str(liste[i])
        return liste
S = open("Servers.txt","r")
Servers = S.readlines();                     #Liste qui contiendra les ID de serveurs
S.close()
Servers = cleanList(Servers)
Servers = listType(Servers, "int")           #la liste devient une liste d'entiers
print("Servers ID:", Servers)
SP = open("ServersPrefix.txt","r")
ServersPrefix = SP.readlines();              #liste qui contiendra les Prefixes de chaques serveurs
SP.close()                                   #il s'agit de la marque permettant au bot d'identifier qu'il s'agit du'une commande
ServersPrefix = cleanList(ServersPrefix) 
print("Prefixes:", ServersPrefix)
RC = open("rulesChannel.txt","r")
rulesChannel = RC.readlines();               #liste qui contiendra les différents salons
RC.close()
rulesChannel = cleanList(rulesChannel)
rulesChannel = listType(rulesChannel, "int") #la liste devient une liste d'entiers
print(rulesChannel)
R = open("Roles.txt", "r")
Roles = R.readlines();
R.close()
Roles = cleanList(Roles)
Roles = listType(Roles, "int")

#***************************************************************************************************************************************************


#************************************************************************************************************************************************
                                             #Connection au bot
#************************************************************************************************************************************************
@bot.event #Décorateur(la fonction ne peut pas fonctionner si il n'y a pas d'évenement)
async def on_ready():                               #Si le bot est prêt et connecté, la fonction est appelée
    print("Bot connecté:", bot.user.name)           #On affiche le nom du bot trouvé
    print("Bot id:", bot.user.id)                   #On affiche l'id du bot trouvé, si jamais il n'a pas un nom à jour
    botOwner1 = bot.get_user(Own1)       #Olivier #crée un objet de type user avec l'id du user
    #envoi un message aux gérants du bot
    await botOwner1.send("Le bot vient de démarrer!"); 
    await botOwner1.send(f"Serveurs connectés: {Servers}"); 
#Fin de la connection au bot
#************************************************************************************************************************************************
    
    
#***************************************************************************************************************************************************
#                                                   Commandes dans le chat
#                                              et reconnaissance des serveurs
#***************************************************************************************************************************************************
@bot.event
async def on_message(message):          #La fonction est appelée si le bot lit un message dans le chat
    #On utilise les listes en global
    global ServersPrefix
    global Roles
    global Servers
    global rulesChannel
    global Serv
    global onoff
    global colorList
    if message.author == bot.user:      #Si l'auteur du message est le bot, ne fait rien.
        return
        #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        #Reconnaissance du serveur:
    if message.content:                 #Si le bot détecte un message autre que le sien
        Serv = [message.guild.id];      #liste contenant l'id du serveur ou a été reçu le message
        ServPrefix = "";#Variable de type string qui contiendra un préfix temporaire
        
        #Si le serveur n'est pas dans la base de données(liste Serveurs):
        if Serv[0] not in Servers: 
            Servers = Servers + Serv                               #On concatène (on ajoute un terme dans la liste) (On rajoute une Id de serveur)
            ServPrefix = "!";                                      #Le préfixe temporaire prend cette valeur
            ServersPrefix = ServersPrefix + list(ServPrefix)       #On concatène (on ajoute un terme dans la liste) (on rajoute un préfixe dans la liste)
            ServRulesChannel="0";                                  #On définit un salon ? si le serveur n'est pas dans la base de donnée
            ServRole = [0];
            rulesChannel=rulesChannel + list(ServRulesChannel)
            Roles = Roles + ServRole
        
        #Sinon (si le serveur est dans la base de données(liste Serveurs):
        else: 
            for s in range(0,len(Servers)):
                if Servers[s] == Serv[0]:
                    ServPrefix = ServersPrefix[s]        #Le préfixe temporaire prend la valeur du préfixe du serveur correspondant
                    ServRulesChannel = rulesChannel[s]
        #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                    
        #Commande test:
        #Le bot envoi un message test
        if message.content == f"{ServPrefix}test" or message.content == f"{ServPrefix}Test" or message.content == f"{ServPrefix}TEST":
            await message.channel.send(f"Bonjour à toi {message.author.mention}!! Je fonctionne très bien!")# le bot envoi un message dans le canal où il a lu la commande
        
        #Commande CobraBot:
        #Le bot explique ce pour quoi il a été créé
        if message.content == f"{ServPrefix}Alfred" or message.content == f"{ServPrefix}alfred" or message.content == f"{ServPrefix}ALFRED":
            await message.channel.send(f"Bonjour {message.author.mention} , je suis un robot qui a pour rôle de vous servir, c'est grâce à moi que les rôles sont atribués immédiatement aux arrivants, et que certains rôles sont multicolores")# le bot envoi un message dans le canal où il a lu la commande
        
        #Commande rules:
        if message.content == f"{ServPrefix}rules" :
            ServRulesChannel = message.channel.id            #récupère l'id du salon
            for s in range(0,len(Servers)):
                if Servers[s] == Serv[0]:
                    rulesChannel[s] = ServRulesChannel
            await message.channel.send("Ce salon est maintenant le salon règlement")

        #Commande prefix:
        #Le bot change le prefixe du serveur correspondant dans la base de données(liste ServersPrefix)
        if message.content.startswith(f"{ServPrefix}prefix "):
            newprefix = message.content;                   #On reprend le message entier de l'utilisateur
            #On enlève des éléments au message
            newprefix = newprefix.replace(f"{ServPrefix}prefix","")
            newprefix = newprefix.replace(" ", "")
            #il ne reste plus que le préfixe dans la variable
            for s in range(0,len(Servers)):
                if Servers[s] == Serv[0]:
                    ServersPrefix[s] = newprefix           #Le préfixe correspondant au serveur dans la base de donnée est remplacé par le nouveau
            await message.channel.send(f"Le prefix a été remplacé par '{newprefix}'")      # Le bot envoi un message
            #************************************************************************************
        
        #commande role:
        if message.content.startswith(f"{ServPrefix}role "):
            t=0 #markeur 0 déjà un role 1 pas de role
            for s in range(0,len(Servers)):
                if Servers[s] == Serv[0]:
                    roleId = Roles[s]
                    role = message.guild.get_role(roleId)
                if roleId == 0:
                    role = message.guild.default_role.id
                    t = 1
            RoleName = message.content
            RoleName = RoleName.replace(f"{ServPrefix}role","")
            RoleName = RoleName.replace(" ", "") #message traité (il ne rest plus que le nom)
            if t == 1: #si il n'y a pas de rôle, on en crée un
                newrole = await message.guild.create_role(name = RoleName, permissions = discord.Permissions(0));
                for s in range(0,len(Servers)):
                    if Servers[s] == Serv[0]:
                        Roles[s] = newrole.id
                await message.channel.send(f"J'ai créé un nouveau role d'arrivées intitulé '{RoleName}'")
            elif t == 0: #si il y a déjà un rôle, on modifie son nom
                lastn = role.name
                await role.edit(name = RoleName)
                await message.channel.send(f"J'ai changé le nom du role d'arrivées intitulé '{lastn}' par '{RoleName}'")
        
        if message.content == f"{ServPrefix}rolesinfo":
            print("in")
            allRoles = message.guild.roles
            allRNames = [""]*len(allRoles)
            for r in range(len(allRoles)):
                allRNames[r] = allRoles[r].name
            await message.channel.send(f"```|Roles info|```")
            for n in range(1,len(allRNames)):
                await message.channel.send(f"```[{allRNames[n]}]```")
                allMemb = allRoles[n].members
                for m in range(len(allMemb)):
                    await message.channel.send(f"```- {allMemb[m].name}```")
            print("worked")
           
        #cette commande n'est pas dite multiServeur
        if message.guild.id == 693203113665888347:
            if message.content == f"{ServPrefix}rainbowOn":
                onoff = 1
                await message.channel.send(f"```EVENT: APP ON.```")
            if message.content == f"{ServPrefix}rainbowOff":
                onoff = 0
                await message.channel.send(f"```EVENT: APP OFF and reseted.```")
            if message.content.startswith(f"{ServPrefix}rainbow "):
                allRoles = message.guild.roles
                index = len(allRoles)
                print(index)
                allRolesID = [0]*index
                print(len(allRoles)); print(len(allRolesID));
                for r in range(len(allRoles)):
                    allRolesID[r] = allRoles[r].id
                RoleID = message.content
                RoleID = RoleID.replace(f"{ServPrefix}rainbow ","")
                RoleID = RoleID.replace("<@&", "")
                RoleID = RoleID.replace(">", "")
                try:
                    RoleID = int(RoleID)
                    if RoleID in allRolesID:
                        await message.channel.send(f"```EVENT: role with id '{RoleID}' found.```")
                        if onoff == 0:
                            await message.channel.send(f"```OOPS: first you need to make it on with ({ServPrefix}rainbowOn).```")
                        else:
                            await message.channel.send(f"```EVENT: Animation started```")
                            objRole = message.guild.get_role(RoleID)
                            k = 0
                            c = colorList[0]
                            norep = colorList[0]
                            while onoff == 1:
                                shuffle(colorList)
                                c = colorList[0]
                                while c == norep:
                                    shuffle(colorList)
                                    c = colorList[0]
                                norep = colorList[0]
                                await objRole.edit(colour = colorList[0])
                                if k == 0:
                                    await message.channel.send(f"```EVENT: Something worked```")
                                    k = 1
                                time.sleep(2)
                            await message.channel.send(f"```EVENT: Loop correctly ended```")
                    else:
                        await message.channel.send(f"```ERROR: no role with id '{RoleID}'.```")
                        return
                except ValueError:
                    await message.channel.send(f"```ERROR: invalid id '{RoleID}', this is not a role id.```")
                except discord.errors.Forbidden:
                    await message.channel.send(f"```ERROR: 403 Forbidden (error code: 50013): Missing Permissions```")
        
        if message.content.startswith(f"{ServPrefix}tryColorPerm "):
                allRoles = message.guild.roles
                index = len(allRoles)
                print(index)
                allRolesID = [0]*index
                print(len(allRoles)); print(len(allRolesID));
                for r in range(len(allRoles)):
                    allRolesID[r] = allRoles[r].id
                RoleID = message.content
                RoleID = RoleID.replace(f"{ServPrefix}tryColorPerm ","")
                RoleID = RoleID.replace("<@&", "")
                RoleID = RoleID.replace(">", "")
                try:
                    RoleID = int(RoleID)
                    objRole = message.guild.get_role(RoleID)
                    await objRole.edit(colour = colorList[0])
                except discord.errors.Forbidden:
                    await message.channel.send(f"```ERROR: 403 Forbidden (error code: 50013): Missing Permissions```")
                except ValueError:
                    await message.channel.send(f"```ERROR: invalid id '{RoleID}', this is not a role id.```")
                    
        #écriture dans les fichiers:
        S = open("Servers.txt", "w")
        for ligne in Servers:
            S.write(str(ligne)+"\n")
        S.close()
        SP = open("ServersPrefix.txt", "w")
        for ligne in ServersPrefix:
            SP.write(str(ligne)+"\n")
        SP.close()
        RC = open("rulesChannel.txt", "w")
        for ligne in rulesChannel:
            RC.write(str(ligne)+"\n")
        RC.close()
        R = open("Roles.txt", "w")
        for ligne in Roles:
            R.write(str(ligne)+"\n")
        R.close()
        
        

    
        
#await nous permet d'appeler la fonction de l'API discord étant donné que nous sommes dans une fonction async
#Fin messages
   
#************************************************************************************************************************************************

#************************************************************************************************************************************************
#                                             Lorsque un membre rejoins le serveur
#************************************************************************************************************************************************
@bot.event
async def on_member_join(member):          #La fonction est appelée si quelqu'un rejoint le serveur
    global Roles
    Serv = [member.guild.id]
    for s in range(0,len(Servers)):
        if Servers[s] == Serv[0]:
            roleId = Roles[s]                 
            if roleId == 0:
                roleId = member.guild.default_role.id
                role = member.guild.default_role
            else:
                role = member.guild.get_role(roleId)
                
    await member.add_roles(role)
        
    await member.send("Bonjour à toi " + member.mention + " et bienvenu sur le serveur " + member.guild.name )           #Envoie un message de bienvenu au membre qui rejoint
    for s in range(0,len(Servers)):
        if Servers[s] == Serv[0]:
            channelId = rulesChannel[s]                 #On récupère le salon de règle correspondant au serveur -> temporairement
            channel = bot.get_channel(channelId)        #on crée un objet du type channel avel l'id du salon
    if channelId != 0:                                        #'?' est le symbole définit si il n'y a pas de salon règle définit
        await member.send(f"Veuillez lire le salon {channel.mention}.")             #envoie du message dans le channel d'arrivée qui le System Channel
    R = open("Roles.txt", "w")
    for ligne in Roles:
        R.write(str(ligne)+"\n")
    R.close()
#*************************************************************************************************************************************************

#*************************************************************************************************************************************************
#                                                  Lorsque un membre quitte le serveur
#*************************************************************************************************************************************************
@bot.event
async def on_member_remove(member):                                              #La fonction est appelée si quelqu'un quitte le serveur
    await member.send("Reviens  quand tu veux " + member.mention + "sur" + member.guild.name )                                                           #envoie du message dans le channel d'arrivée qui le System Channel
#*************************************************************************************************************************************************

#*************************************************************************************************************************************************
    #Lorsque une quelqu'un ajoute cobrabot à son serveur
#*************************************************************************************************************************************************

@bot.event
async def on_guild_join(guild):
    await guild.system_channel.send("Bonjour à vous! Merci d'avoir choisi le Bot Stephanie!!!")

#*************************************************************************************************************************************************




#Doit être utilisé en dernier
bot.run("")
#On met en ligne le bot à partir de son Token (dispo sur le site développeur de discord)