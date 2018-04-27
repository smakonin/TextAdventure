#! /usr/bin/env python3
#
# TextAdventure.py -- Copyright (C) 2018 Cyan Makonin & Stephen Makonin
#

import sys, time, os, textwrap

class Command:
    def __init__(self, text, response, you_die=False):
        self.text = text
        self.response = response
        self.you_die = you_die

class Scene:
    def __init__(self, description='', picture='', commands=[], you_die=False, you_win=False, f=None):
        self.description = description
        self.picture = picture
        self.commands = commands
        self.you_die = you_die
        self.you_win = you_win
        self.f = f
        self.links = []

    def link(self, scenes):
        self.links = scenes

def output_char(char):
        sys.stdout.write(char)
        sys.stdout.flush()

        if char == '\n':
            time.sleep(0.2)
        else:
            time.sleep(0.05)

def output_text(text=''):
    if text == '':
        output_char('\n')
        return

    for line in textwrap.wrap(text, width=50):
        for c in line:
            output_char(c)
        output_char('\n')

def output_picture(picture):
    for line in picture.split('\n'):
        print(line)
        time.sleep(0.2)


titlepage = """

  .+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.
 (                                                                 )
  )                     Cyan's Text Adventure                     (
 (                                                                 )
  "+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"

                         ---///*****\\\\\---

    Story & programming (C) 2018 Cyan Makonin & Stephen Makonin
          Artwork (C) Joan G. Stark  (spunk1111@juno.com)

                         ---\\\\\*****///---

"""


castle = """
                       T~~
                       |
                      /"\\
              T~~     |'| T~~
          T~~ |    T~ WWWW|
          |  /"\   |  |  |/\T~~
         /"\ WWW  /"\ |' |WW|
        WWWWW/\| /   \|'/\|/"\\
        |   /__\/]WWW[\/__\WWWW
        |"  WWWW'|I_I|'WWWW'  |
        |   |' |/  -  \|' |'  |
        |'  |  |LI=H=LI|' |   |
        |   |' | |[_]| |  |'  |
        |   |  |_|###|_|  |   |
        '---'--'-/___\-'--'---'

"""

dragon = """
                     _ _
              _     //` `\\
          _,-"\%   // /``\`\\
     ~^~ >__^  |% // /  } `\`\\
            )  )%// / }  } }`\`\\
           /  (%/'/.\_/\_/\_/\`/
          (    '         `-._`
           \   ,     (  \   _`-.__.-;%>
          /_`\ \      `\ \." `-..-'`
         ``` /_/`"-=-'`/_/
            ```       ```

"""

mountains = """
                                  _
                        .-.      / \        _
            ^^         /   \    /^./\__   _/ \\
          _        .--'\/\_ \__/.      \ /    \  ^^  ___
         / \_    _/ ^      \/  __  :'   /\/\  /\  __/   \\
        /    \  /    .'   _/  /  \   ^ /    \/  \/ .`'\_/\\
       /\/\  /\/ :' __  ^/  ^/    `--./.'  ^  `-.\ _    _:\ _
      /    \/  \  _/  \-' __/.' ^ _   \_   .'\   _/ \ .  __/ \\
    /\  .-   `. \/     \ / -.   _/ \ -. `_/   \ /    `._/  ^  \\
   /  `-.__ ^   / .-'.--'    . /    `--./ .-'  `-.  `-. `.  -  `.
  /        `.  / /      `-.   /  .-'   / .   .'   \    \  \  .-  \\
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""

ocean = """
                         |
                     \       /
                       .-'-.
                  --  /     \  --
 `~~^~^~^~^~^~^~^~^~^-=======-~^~^~^~~^~^~^~^~^~^~^~`
 `~^_~^~^~-~^_~^~^_~-=========- -~^~^~^-~^~^_~^~^~^~`
 `~^~-~~^~^~-^~^_~^~~ -=====- ~^~^~-~^~_~^~^~~^~-~^~`
 `~-~^~-~^~~^~-~^~~-~^~^~-~^~~^-~^~^~^-~^~^~^~^~~^~-`

"""

tombstone = """
        _.---,._,'
       /' _.--.<
         /'     `'
       /' _.---._____
       \.'   ___, .-'`
           /'    \\              .
         /'       `-.          -|-
        |                       |
        |                   .-'~~~`-.
        |                 .'         `.
        |                 |  R  I  P  |
        |                 |           |
        |                 |           |
         \              \\\|           |//
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""

king = """
              _.+._
            (^\/^\/^)
             \@*@*@/
             {_____}
            ///\"\"\"\\\\\\
            (/6   6\)
             ||=^=||
             \\\\\\\\///
              \\\\///
               `)/
"""

sword = """
               ,
              (@|
 ,,           ,)|_____________________________________
//\\\\8@8@8@8@8@8 / _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \\
\\\\//8@8@8@8@8@8 \_____________________________________/
 ``           `)|
              (@|
               `
"""

road = """
               ,@@@@@@@,
       ,,,.   ,@@@@@@/@@,  .oo8888o.
    ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o
   ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'
   %&&%&%&/%&&%@@\@@/ /@@@88888\88888'
   %&&%/ %&%%&&@@\ V /@@' `88\8 `/88'
   `&%\ ` /%&'    |.|        \ '|8'
       |o|        | |         | |
       |.|        | |         | |
    \\\\/ ._\//_/__/  ,\_//__\\\\/.  \_//__/_
"""

cave = """
           ___..-.
         ._/  __ \_`-.__
      ._/  .'/##\_ `-.  \--.
   ._/ - .-_/#####\  /-' `\_
 ./ / ._/ /###@@###\_  \._   `-
/  / /  _|###########\_`.  -' \\
'"''""''"" "'"''"'"'''" ''"'"''"'"''"
"""

jewel = """
                        '
               '                 '
       '         '      '      '        '
          '        \    '    /       '
              ' .   .-"```"-.  . '
                    \`-._.-`/
         - -  =      \\\\ | //      =  -  -
                    ' \\\\|// '
              . '      \|/     ' .
           .         '  `  '         .
        .          /    .    \           .
                 .      .      .
"""

def give_sword():
    scn_dragon.links[0] = scn_has_sword

cmd_walk_north = Command('walk north', 'You head North.')
cmd_walk_south = Command('walk south', 'You head South.')
cmd_walk_east = Command('walk east', 'You head East.')
cmd_walk_west = Command('walk west', 'You head West.')
cmd_enter_castle = Command('enter castle', 'Your walk over the drawbridge.')
cmd_kill_dragon = Command('kill dragon', 'You swing your sword.')
cmd_run_away = Command('run away', 'You quickly run away.')
cmd_drink_water = Command('drink water', 'You bend down and drink some of the ocean water.')
cmd_leave_castle = Command('leave castle', 'You turn and exit the castle.')
cmd_climb_mountain = Command('climb mountain', 'You start your climb.')
cmd_talk_to_king = Command('talk to king', 'You bow to the King.')

scn_road = Scene(
    description = 'You are at a cross roads.',
    commands = [cmd_walk_north, cmd_walk_south, cmd_walk_east, cmd_walk_west],
    picture = road
)

scn_castle = Scene(
    description = 'You stand at the foot of a huge castle.',
    commands = [cmd_enter_castle, cmd_walk_south],
    picture = castle
)

scn_ocean = Scene(
    description = 'You are blocked by the ocean!',
    commands = [cmd_drink_water, cmd_walk_north],
    picture = ocean
)

scn_dragon = Scene(
    description = 'A dragon attacks you!',
    commands = [cmd_kill_dragon, cmd_run_away],
    picture = dragon
)

scn_mountains = Scene(
    description = 'You are blocked by mountains!',
    commands = [cmd_climb_mountain, cmd_walk_east],
    picture = mountains
)

scn_throne_room = Scene(
    description = 'You enter the castle throne room. The King is seated on his throne.',
    commands = [cmd_talk_to_king, cmd_leave_castle],
    picture = king
)

scn_get_sword = Scene(
    description = 'The King says, "Rise my knight, I giviht thy my magic sword to slay the might dragon."',
    commands = [cmd_leave_castle],
    picture = sword,
    f = give_sword
)

scn_climbing_mountain = Scene(
    description = 'The mountains are too steep. You slip and fall.',
    you_die = True
)

scn_no_sword = Scene(
    description = 'Oh, wait... you do not have a sword! The dragon cooks you with fire and then eats you!',
    you_die = True
)

scn_drink_water = Scene(
    description = 'Cough! Cough! YUCK! The ocean water is too salty and tastes horrible! You collapse in pain.',
    you_die = True
)

scn_has_sword = Scene(
    description = 'As the dragon lunges at you, you peirce its scales as the sword sinks into the dragon\'s heart. The dragon is dead! You find a jewel that he was gaurding. You talk the jewel and now your are rich!',
    you_win = True
)

scn_road.link([scn_castle, scn_ocean, scn_dragon, scn_mountains])
scn_castle.link([scn_throne_room, scn_road])
scn_ocean.link([scn_drink_water, scn_road])
scn_dragon.link([scn_no_sword, scn_road])
scn_mountains.link([scn_climbing_mountain, scn_road])
scn_throne_room.link([scn_get_sword, scn_castle])
scn_get_sword.link([scn_castle])

os.system('clear')
output_picture(titlepage)
output_text('The story begins now...')
output_text()

scene = scn_road
huh = False
while True:
    if not huh:
        if scene.picture != '': output_picture(scene.picture)
        output_text(scene.description)
        if scene.f is not None: scene.f()

    if scene.you_die:
        output_picture(tombstone)
        output_text('YOUR DEAD, thanks for playing!!!')
        output_text()
        exit(0)

    if scene.you_win:
        output_picture(jewel)
        output_text('YOU WIN, thanks for playing!!!')
        output_text()
        exit(0)

    output_text('You can: ' + ', '.join([cmd.text for cmd in scene.commands]))
    output_text()
    player_says = input("? ")

    if player_says == 'quit':
        output_text()
        output_text('Bye, thanks for playing!!!')
        output_text()
        exit(0)

    huh = False
    for (i, cmd) in enumerate(scene.commands):
        if player_says == cmd.text:
            output_text('> ' + cmd.response)
            scene = scene.links[i]
            break
    else:
        output_text('> Huh? I don\'t understand!')
        output_text()
        huh = True
