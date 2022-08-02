#Jeu du Tic Tac Toe

#importation des modules
import discord
from discord.ext import commands
import pygame
from game_1 import Game 

#definir le bot
bot = commands.Bot(command_prefix ="!", description = "Je suis un bot pour jouer a Tic Tac Toe !" )

@bot.command()
async def jouer(ctx):
    if __name__ == '__main__':
        pygame.init()
        game = Game()
        game.run()

bot.run("ODAwMzU5MzMwNjYxNzkzODEz.YAQ-tg.ACClFIeOlmtogZiwhqDb70j82Z4")