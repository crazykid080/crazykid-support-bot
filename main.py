import nextcord as discord
from nextcord import Interaction, SlashOption
import nextcord.utils as ncutils
from nextcord.ext.commands import check, group, Bot

if __name__ == "__main__":
	### SETUP ###
	invitelink = "Nothing yet"
	intents = discord.Intents.default()
	client = Bot(intents=intents)

### CHECKS ###
def isOwner(id):
	return id == 341928732602269698

### MESSAGE HELPERS ###
async def sendinteract(interaction, msg, delete_after=None, ephemeral=False):
	if(delete_after == None):
		return await interaction.response.send_message(msg, ephemeral=ephemeral)
	else:
		return await interaction.response.send_message(msg, delete_after=delete_after, ephemeral=ephemeral)

