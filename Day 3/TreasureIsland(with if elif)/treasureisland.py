print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
while True:
  print("You are the first explorers to arrive at the island.You are at the starting point.")
  print("Enter choices with yes or no.")
  choice=input("There is a river in front of you do you want to swim?").lower()
  if choice=="yes":
    print('''
                                           ___.-----.______
                                   ___.-----'::::::::::::::::`---.___
                _.--._            (:::;,-----'~~~~~`----::::::::::.. `-.
   _          .'_---. `--.__       `~~'                 `~`--.:::::`..  `..
  ; `-.____.-' ' {0} ` `--._`---.____                         `:::::::: : ::
 :_^              ~   `--.___ `----.__`----.____                ~::::::.`;':
  :`--.__,-----.___(         `---.___ `---.___  `----.___         ~|;:,' : |
   `-.___,---.____     _,        ._  `----.____ `----.__ `-----.___;--'  ; :
                  `---' `.  `._    `))  ,  , , `----.____.----.____   --' :|
                        / `,--.\    `.` `  ` ` ,   ,  ,     _.--   `-----'|'
 _.~~~~~~._____    __./'_/'     :   .:----.___ ` ` ` ``  .-'      , ,  :::'
                 ///--\;  ____  :   :'    ____`---.___.--::     , ` ` ::'
                 `'           _.'   (    /______     (   `-._   `-._,-'
    ()  ()                 .-' __.-//     /_______---'       `-._   `.
  * *(o)'      ~~~        /////    `'       ~~~~~~      ~~ ______;   ::.
  `\ )( /*                `'`'                            /_______   _.'
    {()}      ,     ~~~                  ~~~~~~~~           /___.---'  --__
     !|       `                                              ~~~
  ~~~~~~~~
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 ''')
    print("You are eaten by an alligator. Game Over")
    break
  elif choice=="wait":
    print('''                                      # #  ( )
                                  ___#_#___|__
                              _  |____________|  _
                       _=====| | |            | | |==== _
                 =====| |.---------------------------. | |====
   <--------------------'   .  .  .  .  .  .  .  .   '--------------/
     \                                                             /
      \_______________________________________________WWS_________/
  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
   wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
      ''')
    print("A battleship has arrived to take you across the river.")
    choice=input("You see a cabin in the distance. Do you go to the cabin?").lower()
    if choice=="yes":
      print('''                         (   )
                          (    )
                           (    )
                          (    )
                            )  )
                           (  (                  /\
                            (_)                 /  \  /\
                    ________[_]________      /\/    \/  \
           /\      /\        ______    \    /   /\/\  /\/\
          /  \    //_\       \    /\    \  /\/\/    \/    \
   /\    / /\/\  //___\       \__/  \    \/
  /  \  /\/    \//_____\       \ |[]|     \
 /\/\/\/       //_______\       \|__|      \
/      \      /XXXXXXXXXX\                  \
        \    /_I_II  I__I_\__________________\
               I_I|  I__I_____[]_|_[]_____I
               I_II  I__I_____[]_|_[]_____I
               I II__I  I     XXXXXXX     I
            ~~~~~"   "~~~~~~~~~~~~~~~~~~~~~~~~''')
      print("You have arrived at the cabin.")
      choice=input("Enter the cabin?").lower()
      if choice=="yes":
        print('''                           /\
                                ( ;`~v/~~~ ;._
                             ,/'"/^) ' < o\  '".~'\\\--,
                           ,/",/W  u '`. ~  >,._..,   )'
                          ,/'  w  ,U^v  ;//^)/')/^\;~)'
                       ,/"'/   W` ^v  W |;         )/'
                     ;''  |  v' v`" W }  \\
                    "    .'\    v  `v/^W,) '\)\.)\/)
                             `\   ,/,)'   ')/^"-;'
                                  \
                                   '". _
                                        \'''''')   
        print("A werewolf was in the cabin. You got eaten. Game Over")
        break
      elif choice=="no":
        print("You see a castle ahead walk towards it?")
    elif choice=="no":
      print('''       ( )___( )
          /__oo   \
         ( \/     )
         | `=/    |
        /         \
       /  /    \   \
      /  (      \   \ 
     ( ,_/_      \   \
      \_ '=       \   )
        ""'       /  /
        ;        /  /'?
        :       (((( /
   ctr   `._   \  _ (
          __|   |  /_    
        ("__,.."'_._.)   
''')
      print("A bear comes and eats you. Game Over")
      break
    elif choice=="yes":
      print('''                                                    o         _ _ _ _ _
                                                _----|         I-I-I-I-I
                             _ _ _ _ _ _      o  ----|     o   \~~`~'~~/
                             ]-I-I-I-I-[ _----|      |_----|    |.    |
                             \~`\~~~/'~/  ----|     / \----|    |  /^\|
                              [*] ' __|       ^    / ^ \   ^    |_ |*||
                              |__    ,|      / \  /    `\ / \   |  ===|
                            __|  ___ ,|__   /    /=_=_=_=\   \  |,  __|
                            I_I__I_I__I_I  (====(_________)___|_|_____|___
                            \-\--|-|--/-/  |'    I~~[ ]~~I I_I__|IIII|_I_l
                             | [ ]    '|   | [~] |_`_~_ _[  \-\--|-|--/-/
                             |.   | |' |___|____`I_I_|_I_I___|---------|
                            / \| [] ~ .|_|-|_|-|-|_|-|_|-|_|-| []   [] |
                           <===>  |  ~.|-=-=-=-=-=-=-=-=-=-=-|~  |  ~ / \
                           | []|`   []~||.|.|.|.|.|.|.|.|.|.||-~   ~ <===>
   O O      o o            | []| ` |   |/////////I\\\\\\\\\\||__. ~| |[*]I
  O * O    o * o           <===> ~   ' ||||| |   |   | ||||.||  []  ~<===>
   O O      o o             \T/  |~|-- ||||| | O | O | ||||.|| . |'~  \T/
   \I        I/              |     ~.~_||||| |~~~|~~~| ||||.|| | ~   | |
____I/______\I____\/..___.../|' v . | .|||||/____|____\|||| /|. . | . .|\.\/_
''')
      choice=input("you have arrived at the castle. Do you enter?").lower()
      if choice=="yes":
        print("You have found one of the treasure chests. You win!")
        choice=input("Do you wish to end your adventure?").lower()
        if choice=="yes":
          print('''                                             __----~~~~~~~~~~~------___
                                   .  .   ~~//====......          __--~ ~~
                   -.            \_|//     |||\\  ~~~~~~::::... /~
                ___-==_       _-~ o  \/    |||  \\            _/~~-
        __---~~~.==~||\=_    -_--~/_-~|-   |\\   \\        _/~
    _-~~     .=~    |  \\-_    '-~7  /-   /  ||    \      /
  .~       .~       |   \\ -_    /  /-   /   ||      \   /
 /  ____  /         |     \\ ~-_/  /|- _/   .||       \ /
 |~~    ~~|--~~~~--_ \     ~    /\   /\   /\  =~~        .\
          '         ~-|    * \  ||   ||   || /)     __--~~
                      |-~~*   / ||   ||   ||   _-~
                          *  /  ||   ||   || /~
                         (* \ /--------------\ ~-
                         /// | * * ** * ** * *|  |
                             | - - -- - -- - -|\  |
                 /\          |                | ) \
                  \          |- - -  - -  - - | _--~|
                   \\        |                |//.-~~-\
                    \X__x___ ==================*
                     ~---,____--~~*''')
          print("You have got a treasure chest and leave, a dragon comes and destroys the castle.")
        elif choice=="no":
          continue
      elif choice=="no":
        print('''   / \
   / '.\
  /   '.\
 /     '.\   
 ~|~~~~~|~
 +|-===-|;-.
  |  |  |  `-
 _|--|--|_     
|--.....--|
|--.....--|
|--.....--| .''.
|--.....--| |~~|
 ~~-----~~   ~~
''')
        choice=input("You see a well in front of you after walking away from the castle. Enter the well?").lower()
        if choice=="yes":
          print(''',,
`""*$b..
     ""*$o.
         "$$o.
           "*$$o.
              "$$$o.
                "$$$$bo...       ..o:
                  "$$$$$$$$booocS$$$    ..    ,.
               ".    "*$$$$SP     V$o..o$$. .$$$b
                "$$o. .$$$$$o. ...A$$$$$$$$$$$$$$b
          ""bo.   "*$$$$$$$$$$$$$$$$$$$$P*$$$$$$$$:
             "$$.    V$$$$$$$$$P"**""*"'   VP  * "l
               "$$$o.4$$$$$$$$X
                "*$$$$$$$$$$$$$AoA$o..oooooo..           .b
                       .X$$$$$$$$$$$P""     ""*oo,,     ,$P
                      $$P""V$$$$$$$:    .        ""*****"
                    .*"    A$$$$$$$$o.4;      .
                         .oP""   "$$$$$$b.  .$;
                                  A$$$$$$$$$$P
                                  "  "$$$$$P"
                                      $$P*"
    mls                              .$"''')
          print("A dragon was in the well. You got eaten. Game over")
          break
        if choice=="no":
          print(''' / \          / \
 |~|          |~|
#"'"|'"'"'"'"|"'"|
#   |  _.._  |   |
#   |.'    `.|   |
#   |        |   |
#   |.   /~~/~~/~~/
#   | './  /  /  /
#   |  /--/--/--/|
#   | /  /  /  / |
#   |/--/--/--/  |
#   |========#   | lbm
''')
          print("You see a drawbridge in the distance. You walk towards it.")
          choice=input("do you cross the drawbridge?").lower()
          if choice=="yes":
            print("You found one of the treasure chests. You win!")
            choice=input("do you wish to end your adventure?").lower()
            if choice=="yes":
              break
            elif choice=="no":
              print("Please wait for next update to continue the journey")
              break
          if choice=="no":
            print("Your character got tired of walking your adventure is ending. To be continued...(till the next installment)")
            break