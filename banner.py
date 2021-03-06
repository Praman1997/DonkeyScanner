#!/usr/bin/python
# -*- coding: utf-8 -*-
# DonkeyScan banners


#---------------------------------------------------------------------------#
# This file is part of DonkeyScan.                                          #
# DonkeyScan is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU General Public License as published by      #
# the Free Software Foundation, either version 3 of the License, or         #
# (at your option) any later version.                                       #
#                                                                           #
# DonkeyScan is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
# GNU General Public License for more details.                              #
#                                                                           #
# You should have received a copy of the GNU General Public License         #
# along with DonkeyScan.  If not, see <http://www.gnu.org/licenses/>.       #
#                                                                           #
#---------------------------------------------------------------------------#


import random

header1 = """
                                                                                                                
                                                                                                                
    ,---,                                ,-.                      .--.--.                                       
  .'  .' `\                          ,--/ /|                     /  /    '.                                     
,---.'     \    ,---.        ,---, ,--. :/ |                    |  :  /`. /                              ,---,  
|   |  .`\  |  '   ,'\   ,-+-. /  |:  : ' /                     ;  |  |--`                           ,-+-. /  | 
:   : |  '  | /   /   | ,--.'|'   ||  '  /      ,---.       .--,|  :  ;_       ,---.     ,--.--.    ,--.'|'   | 
|   ' '  ;  :.   ; ,. :|   |  ,"' |'  |  :     /     \    /_ ./| \  \    `.   /     \   /       \  |   |  ,"' | 
'   | ;  .  |'   | |: :|   | /  | ||  |   \   /    /  |, ' , ' :  `----.   \ /    / '  .--.  .-. | |   | /  | | 
|   | :  |  ''   | .; :|   | |  | |'  : |. \ .    ' / /___/ \: |  __ \  \  |.    ' /    \__\/: . . |   | |  | | 
'   : | /  ; |   :    ||   | |  |/ |  | ' \ \'   ;   /|.  \  ' | /  /`--'  /'   ; :__   ," .--.; | |   | |  |/  
|   | '` ,/   \   \  / |   | |--'  '  : |--' '   |  / | \  ;   :'--'.     / '   | '.'| /  /  ,.  | |   | |--'   
;   :  .'      `----'  |   |/      ;  |,'    |   :    |  \  \  ;  `--'---'  |   :    :;  :   .'   \|   |/       
|   ,.'                '---'       '--'       \   \  /    :  \  \            \   \  / |  ,     .-./'---'        
'---'                                          `----'      \  ' ;             `----'   `--`---'                 
                                                            `--`                                               
"""

header2 = """
 ______   _______  _        _        _______           _______  _______  _______  _       
(  __  \ (  ___  )( (    /|| \    /\(  ____ \|\     /|(  ____ \(  ____ \(  ___  )( (    /|
| (  \  )| (   ) ||  \  ( ||  \  / /| (    \/( \   / )| (    \/| (    \/| (   ) ||  \  ( |
| |   ) || |   | ||   \ | ||  (_/ / | (__     \ (_) / | (_____ | |      | (___) ||   \ | |
| |   | || |   | || (\ \) ||   _ (  |  __)     \   /  (_____  )| |      |  ___  || (\ \) |
| |   ) || |   | || | \   ||  ( \ \ | (         ) (         ) || |      | (   ) || | \   |
| (__/  )| (___) || )  \  ||  /  \ \| (____/\   | |   /\____) || (____/\| )   ( || )  \  |
(______/ (_______)|/    )_)|_/    \/(_______/   \_/   \_______)(_______/|/     \||/    )_)
                                                                                          
"""

header3 = """
 _______   ______   .__   __.  __  ___  ___________    ____  _______.  ______     ___      .__   __. 
|       \ /  __  \  |  \ |  | |  |/  / |   ____\   \  /   / /       | /      |   /   \     |  \ |  | 
|  .--.  |  |  |  | |   \|  | |  '  /  |  |__   \   \/   / |   (----`|  ,----'  /  ^  \    |   \|  | 
|  |  |  |  |  |  | |  . `  | |    <   |   __|   \_    _/   \   \    |  |      /  /_\  \   |  . `  | 
|  '--'  |  `--'  | |  |\   | |  .  \  |  |____    |  | .----)   |   |  `----./  _____  \  |  |\   | 
|_______/ \______/  |__| \__| |__|\__\ |_______|   |__| |_______/     \______/__/     \__\ |__| \__| 
                                                                                                     
"""

header4 = """
▓█████▄  ▒█████   ███▄    █  ██ ▄█▀▓█████▓██   ██▓  ██████  ▄████▄   ▄▄▄       ███▄    █ 
▒██▀ ██▌▒██▒  ██▒ ██ ▀█   █  ██▄█▒ ▓█   ▀ ▒██  ██▒▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █ 
░██   █▌▒██░  ██▒▓██  ▀█ ██▒▓███▄░ ▒███    ▒██ ██░░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒
░▓█▄   ▌▒██   ██░▓██▒  ▐▌██▒▓██ █▄ ▒▓█  ▄  ░ ▐██▓░  ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒
░▒████▓ ░ ████▓▒░▒██░   ▓██░▒██▒ █▄░▒████▒ ░ ██▒▓░▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░
 ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░  ██▒▒▒ ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
 ░ ▒  ▒   ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░▒ ▒░ ░ ░  ░▓██ ░▒░ ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░
 ░ ░  ░ ░ ░ ░ ▒     ░   ░ ░ ░ ░░ ░    ░   ▒ ▒ ░░  ░  ░  ░  ░          ░   ▒      ░   ░ ░ 
   ░        ░ ░           ░ ░  ░      ░  ░░ ░           ░  ░ ░            ░  ░         ░ 
 ░                                        ░ ░              ░                             


"""

header5 = """
████████▄   ▄██████▄  ███▄▄▄▄      ▄█   ▄█▄    ▄████████ ▄██   ▄      ▄████████  ▄████████    ▄████████ ███▄▄▄▄   
███   ▀███ ███    ███ ███▀▀▀██▄   ███ ▄███▀   ███    ███ ███   ██▄   ███    ███ ███    ███   ███    ███ ███▀▀▀██▄ 
███    ███ ███    ███ ███   ███   ███▐██▀     ███    █▀  ███▄▄▄███   ███    █▀  ███    █▀    ███    ███ ███   ███ 
███    ███ ███    ███ ███   ███  ▄█████▀     ▄███▄▄▄     ▀▀▀▀▀▀███   ███        ███          ███    ███ ███   ███ 
███    ███ ███    ███ ███   ███ ▀▀█████▄    ▀▀███▀▀▀     ▄██   ███ ▀███████████ ███        ▀███████████ ███   ███ 
███    ███ ███    ███ ███   ███   ███▐██▄     ███    █▄  ███   ███          ███ ███    █▄    ███    ███ ███   ███ 
███   ▄███ ███    ███ ███   ███   ███ ▀███▄   ███    ███ ███   ███    ▄█    ███ ███    ███   ███    ███ ███   ███ 
████████▀   ▀██████▀   ▀█   █▀    ███   ▀█▀   ██████████  ▀█████▀   ▄████████▀  ████████▀    ███    █▀   ▀█   █▀  
                                  ▀                                                                               

"""

header6 = """
8888888b.                    888                         .d8888b.                             
888  "Y88b                   888                        d88P  Y88b                            
888    888                   888                        Y88b.                                 
888    888  .d88b.  88888b.  888  888  .d88b.  888  888  "Y888b.    .d8888b  8888b.  88888b.  
888    888 d88""88b 888 "88b 888 .88P d8P  Y8b 888  888     "Y88b. d88P"        "88b 888 "88b 
888    888 888  888 888  888 888888K  88888888 888  888       "888 888      .d888888 888  888 
888  .d88P Y88..88P 888  888 888 "88b Y8b.     Y88b 888 Y88b  d88P Y88b.    888  888 888  888 
8888888P"   "Y88P"  888  888 888  888  "Y8888   "Y88888  "Y8888P"   "Y8888P "Y888888 888  888 
                                                    888                                       
                                               Y8b d88P                                       
                                                "Y88P"                                        
"""

def xe_header():
    headers = [header1, header2, header3, header4, header5, header6]
    return random.choice(headers)
