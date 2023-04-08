"""
translator

Description:
"""
import alphabet
import pygame
import time
import wait



pygame.init()


dot = "."
dash = "__"



def translate(word):
    length = len(word)
    translated = ""
    n = 0
    while n < length:
        letter = word[n]
        added = alphabet.translate_one(letter)
        translated += added
        #translated += "|"
        #print(translated)
        n += 1
    return translated

x = 0

def play(word):
    length = len(word)
    x = 0
    for x in range(0, length):
        letter = word[x]
        music_channel = pygame.mixer.Channel(0)
        music_channels = pygame.mixer.Channel(1)
        if letter == "|":
            pygame.time.wait(400)
            #wait.wait()
            continue
            #input()
            #print(word)
        elif letter == ".":
            sound = pygame.mixer.Sound("morse_short.mp3")
            music_channel.play(sound)
            pygame.time.wait(400)
            #wait.wait()
            #time.sleep(2.5)
            #input()
            #print(word)
            #sound.play()
            x += 1
        elif letter == "-":
            sounds = pygame.mixer.Sound("morse_long.mp3")
            music_channels.play(sounds)
            pygame.time.wait(400)
            #wait.wait()
            #time.sleep(2.5)
            #input()
            #print(word)
            #sound.play()
            x += 1
        elif letter == "/":
            pygame.time.wait(800)
    

        
        
        
        
        


