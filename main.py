# Cindy | 20 June 2022 | ICS2O Final Culminating Project

# Setting up replit
import play
import random

# sets the background black
play.set_backdrop('black')

# sets the starting lives left to 3
lives = 3

# sets starting "scene_id" to 1 (intro scene)
scene_id = 1 

# declares a variable in dictionary to include all of the other scenes
scenes = {}

# declares variables for each scene to be put into python dictionary
scene1 = {}
scene2 = {}
scene3 = {}
scene4 = {}
scene5 = {}
scene6 = {}
scene7 = {}
scene8 = {}
scene9 = {}
scene10 = {}
scene11 = {}
scene12 = {}
scene13 = {}
scene14 = {}
scene15 = {}
scene16 = {}
scene17 = {}
scene18 = {}
scene19 = {}

# Scene 1
## scene 1 background image of storms
scene1["background_scene"] = play.new_image(
      image = 'storm.png',
      x = 0, 
      y = 0, 
      size = 250,
    )
   
## scene 1 title (shadow)
scene1["text1_scene"] = play.new_text(
  words='WHAT A STORM!',    
  x = 5, 
  y = 175, 
  angle = 0, 
  font = None, 
  font_size = 100, 
  color = 'black', 
  transparency = 100
    )

## scene 1 title (white portion)
scene1["text2_scene"] = play.new_text(
  words='WHAT A STORM!',    
  x = 0, 
  y = 175, 
  angle = 0, 
  font = None, 
  font_size = 100, 
  color = 'white', 
  transparency = 100
    )

## scene 1 author's name
scene1["text3_scene"] = play.new_text(
  words='Written by Cindy Zhu',  
  x = 0, 
  y = -100, 
  angle = 0, 
  font = None, 
  font_size = 25, 
  color = 'white', 
  transparency = 100
    )

# Scene 2
## scene 2 background image of desert
scene2["background_scene"] = play.new_image(
  image = 'desert.png',
  x = 0, 
  y = 0, 
  size = 200,
  )

## scene 2 character on left
scene2["character"] = play.new_image(
  image= 'character.png', 
  x=-200, 
  y=-100, 
  angle=0, 
  size=25, 
  transparency=100
  )

## scene 2 text bubble
scene2["text_scene"] = play.new_image(
  image = 'text_scene2.png',
  x = 40,
  y = 100,
  size = 40,
  )

# Scene 3
## scene 3 background image of desert
scene3["background_scene"] = play.new_image(
  image = 'desert.png',
  x = 0, 
  y = 0, 
  size = 200,
  )

## scene 3 character on left
scene3["character"]= play.new_image(
  image= 'character.png', 
  x=-200, 
  y=-100, 
  angle=0, 
  size=25, 
  transparency=100
  )

## scene 3 text bubble
scene3["text_scene"] = play.new_image(
  image = 'text_scene3.png',
  x = 40,
  y = 100,
  size = 40,
  )

# Scene 4
## scene 4 background image of desert
scene4["background_scene"] = play.new_image(
  image = 'desert.png',
  x = 0, 
  y = 0, 
  size = 200,
  )

## scene 4 character on left
scene4["character"]= play.new_image(
  image= 'character.png', 
  x=-200, 
  y=-100, 
  angle=0, 
  size=25, 
  transparency=100
  )

## scene 4 text bubble
scene4["text_scene"] = play.new_image(
  image = 'text_scene4.png',
  x = 40,
  y = 100,
  size = 40,
  )

# Scene 5
## scene 5 background image of cave
scene5["background_scene"] = play.new_image(
  image = 'cave.jpg',
  x = 0, 
  y = 0, 
  size = 80,
  )

## scene 5 character on left
scene5["character"]= play.new_image(
  image= 'character.png', 
  x=-200, 
  y=-100, 
  angle=0, 
  size=25, 
  transparency=100
  )

## scene 5 text bubble
scene5["text_scene"] = play.new_image(
  image = 'text_scene5.png',
  x = 40,
  y = 100,
  size = 40,
  )

# Scene 6 death scene
## scene 6 death text scene
scene6["background_scene"] = play.new_image(
  image = 'text_scene6.png',
  x = 0, 
  y = 50, 
  size = 60,
  )

# Scene 7
## scene 7 background image of desert bridge
scene7["background_scene"] = play.new_image(
    image = 'bridge.png',
    x = 0, 
    y = 0, 
    size = 80,
    )

## scene 7 character on left
scene7["character"]= play.new_image(
  image= 'character.png', 
  x=-200, 
  y=-100, 
  angle=0, 
  size=25, 
  transparency=100
  )

## scene 7 text bubble
scene7["text_scene"] = play.new_image(
  image = 'text_scene7.png',
  x = 40,
  y = 100,
  size = 40,
  )

# Scene 8
## scene 8 background image of desert bridge
scene8["background_scene"] = play.new_image(
  image = 'bridge.png',
  x = 0, 
  y = 0, 
  size = 80,
  )

## scene 8 character on left
scene8["character"]= play.new_image(
  image= 'character.png', 
  x=-200, 
  y=-100, 
  angle=0, 
  size=25, 
  transparency=100
  )

## scene 8 text bubble
scene8["text_scene"] = play.new_image(
  image = 'text_scene8.png',
  x = 40,
  y = 100,
  size = 40,
  )

# Scene 9
## scene 9 background image of desert bridge
scene9["background_scene"] = play.new_image(
  image = 'bridge.png',
  x = 0, 
  y = 0, 
  size = 80,
  )

## scene 9 character on left
scene9["character"]= play.new_image(
  image= 'character.png', 
  x=-250, 
  y=-100, 
  angle=0, 
  size=25, 
  transparency=100
  )

## scene 9 text bubble
scene9["text_scene"] = play.new_image(
  image = 'text_scene9.png',
  x = -40,
  y = 100,
  size = 40,
  )

## scene 9 (angry) troll character on right
scene9["troll"] = play.new_image(
  image= 'troll.png', 
  x=200, 
  y=0, 
  angle=0, 
  size=60, 
  transparency=100
  )

# Scene 10
## scene 10 background image of desert bridge
scene10["background_scene"] = play.new_image(
  image = 'bridge.png',
  x = 0, 
  y = 0, 
  size = 80,
  )

## scene 10 character on left
scene10["character"]= play.new_image(
  image= 'character.png', 
  x=-250, 
  y=-100, 
  angle=0, 
  size=25, 
  transparency=100
  )

## scene 10 text bubble
scene10["text_scene"] = play.new_image(
  image = 'text_scene10.png',
  x = -50,
  y = 100,
  size = 40,
  )

## scene 10 (angry) troll character on right
scene10["troll"] = play.new_image(
  image= 'troll.png', 
  x=200, 
  y=-20, 
  angle=0, 
  size=60, 
  transparency=100
  )

# Scene 11
## scene 11 background image of desert bridge
scene11["background_scene"] = play.new_image(
  image = 'bridge.png',
  x = 0, 
  y = 0, 
  size = 80,
  )

## scene 11 character on left
scene11["character"] = play.new_image(
  image= 'character.png', 
  x=-250, 
  y=-100, 
  angle=0, 
  size=25, 
  transparency=100
  )

## scene 11 text bubble
scene11["text_scene"] = play.new_image(
  image = 'text_scene11.png',
  x = -50,
  y = 100,
  size = 40,
  )

## scene 11 (angry) troll character on right
scene11["troll"] = play.new_image(
  image= 'troll.png', 
  x=200, 
  y=-20, 
  angle=0, 
  size=60, 
  transparency=100
  )

# declaring a variable to count whether the character won or not 
## (0 equals troll won, 1 equal character won, default is that the troll won)
character_win = 0

# Scene 12 Victory Scene
## scene 12 background image of desert city
scene12["background_scene"] = play.new_image(
  image = 'city.jpg',
  x = 0, 
  y = 20, 
  size = 100,
  )

## scene 12 character on left
scene12["character"] = play.new_image(
  image= 'character.png', 
  x=-200, 
  y=-100, 
  angle=0, 
  size=25, 
  transparency=100
  )

## scene 12 text bubble
scene12["text_scene"] = play.new_image(
  image = 'text_scene12.png',
  x = 40,
  y = 100,
  size = 40,
  )

# Scene 13 death scene
## scene 13 background death text
scene13["background_scene"] = play.new_image(
  image = 'text_scene13.png',
  x = 0, 
  y = 50, 
  size = 70,
  )

# Scene 14
## scene 14 background image of desert
scene14["background_scene"] = play.new_image(
  image = 'desert.png',
  x = 0, 
  y = 0, 
  size = 200,
  )

## scene 14 character on left
scene14["character"]= play.new_image(
  image= 'character.png', 
  x=-200, 
  y=-100, 
  angle=0, 
  size=25, 
  transparency=100
  )

## scene 14 text bubble
scene14["text_scene"] = play.new_image(
  image = 'text_scene14.png',
  x = 40,
  y = 100,
  size = 40,
  )

# Scene 15
## scene 15 background image of cave
scene15["background_scene"] = play.new_image(
  image = 'cave.jpg',
  x = 0, 
  y = 0, 
  size = 80,
  )

## scene 15 character on left
scene15["character"]= play.new_image(
  image= 'character.png', 
  x=-200, 
  y=-100, 
  angle=0, 
  size=25, 
  transparency=100
  )

## scene 15 text bubble
scene15["text_scene"] = play.new_image(
  image = 'text_scene15.png',
  x = 40,
  y = 100,
  size = 40,
  )

# Scene 16
## scene 16 background image of a cave inside 
scene16["background_scene"] = play.new_image(
  image = 'insideCave.jpg',
  x = 0, 
  y = 40, 
  size = 80,
  )

## scene 16 character on left
scene16["character"]= play.new_image(
  image= 'character.png', 
  x=-200, 
  y=-100, 
  angle=0, 
  size=25, 
  transparency=100
  )

## scene 16 text bubble
scene16["text_scene"] = play.new_image(
  image = 'text_scene16.png',
  x = 40,
  y = 100,
  size = 40,
  )

## scene 16 lion on right
scene16["lion"] = play.new_image(
  image= 'lion.png', 
  x=200, 
  y=-100, 
  angle=0, 
  size=50, 
  transparency=100
  )

# Scene 17 death scene
## scene 17 background death text
scene17["background_scene"] = play.new_image(
  image = 'text_scene17.png',
  x = 0, 
  y = 50, 
  size = 70,
  )

# Scene 18
## scene 18 background image of cave inside
scene18["background_scene"] = play.new_image(
  image = 'insideCave.jpg',
  x = 0, 
  y = 40, 
  size = 80,
  )

## scene 18 character on left
scene18["character"]= play.new_image(
  image= 'character.png', 
  x=-200, 
  y=-100, 
  angle=0, 
  size=25, 
  transparency=100
  )

## scene 18 text bubble
scene18["text_scene"] = play.new_image(
  image = 'text_scene18.png',
  x = 40,
  y = 100,
  size = 40,
  )

# Scene 19
## scene 19 background image of cave inside
scene19["background_scene"] = play.new_image(
  image = 'insideCave.jpg',
  x = 0, 
  y = 40, 
  size = 80,
  )

## scene 19 character on left
scene19["character"]= play.new_image(
  image= 'character.png', 
  x=-200, 
  y=-100, 
  angle=0, 
  size=25, 
  transparency=100
  )

## scene 19 text bubble
scene19["text_scene"] = play.new_image(
  image = 'text_scene19.png',
  x = 40,
  y = 100,
  size = 40,
  )

# next button on right to switch scenes that do not include choices
next_btn = play.new_image(
  image = 'next.png',
  x = 300,
  y = -100,
  size = 20,
  transparency = 100
  )

# declaration of which scenes to include a "next button"
scene1["next"] = next_btn
scene2["next"] = next_btn
scene3["next"] = next_btn
scene8["next"] = next_btn
scene11["next"] = next_btn
scene18["next"] = next_btn
scene19["next"] = next_btn

# choice 1 on bottom to allow user to switch scenes based on option 1
choice1 = play.new_image(
  image = 'choice1.png',
  x = -100,
  y = -130,
  size = 25,
  transparency = 100
  )

# choice 2 on bottom to allow user to switch scenes based on option 2
choice2 = play.new_image(
  image = 'choice2.png',
  x = 30,
  y = -130,
  size = 27,
  transparency = 100
  )

# choice 3 on bottom to allow user to switch scenes based on option 3
choice3 = play.new_image(
  image = 'choice3.png',
  x = 160,
  y = -130,
  size = 22,
  transparency = 100
  )

# declaration of which scenes to include the choice buttons
## choices 1, 2, 3 for scene 4
scene4["choice1"] = choice1
scene4["choice2"] = choice2
scene4["choice3"] = choice3

## choices 1 and 2 for scene 5
scene5["choice1"] = choice1
scene5["choice2"] = choice2

## choices 1 and 2 for scene 7
scene7["choice1"] = choice1
scene7["choice2"] = choice2

## choices 1, 2, 3 for scene 9
scene9["choice1"] = choice1
scene9["choice2"] = choice2
scene9["choice3"] = choice3

## choices 1 and 2 for scene 10
scene10["choice1"] = choice1
scene10["choice2"] = choice2

## choices 1, 2, 3 for scene 14
scene14["choice1"] = choice1
scene14["choice2"] = choice2
scene14["choice3"] = choice3

## choices 1, 2, 3 for scene 15
scene15["choice1"] = choice1
scene15["choice2"] = choice2
scene15["choice3"] = choice3

## choices 1 and 2 for scene 16
scene16["choice1"] = choice1
scene16["choice2"] = choice2

# restart button for whenever character hits a "death scene" (maximum restarts = 3, each restart costs 1 life)
restart = play.new_image(
  image = 'restart.jpg',
  x = 30,
  y = -130,
  size = 27,
  transparency = 100
  )

# declaration of which scenes to include the restart buttons
scene6["restart"] = restart
scene13["restart"] = restart
scene17["restart"] = restart

# Lives Left
## outputs a black box underneath the text
lives_left_box = play.new_box(
  color = "black",
  x = -275, 
  y = 250, 
  width = 140, 
  height = 27, 
)

# declaration of which scenes to include the lives left box
scene1["lives_left_box"] = lives_left_box
scene2["lives_left_box"] = lives_left_box
scene3["lives_left_box"] = lives_left_box
scene4["lives_left_box"] = lives_left_box
scene5["lives_left_box"] = lives_left_box
scene6["lives_left_box"] = lives_left_box
scene7["lives_left_box"] = lives_left_box
scene8["lives_left_box"] = lives_left_box
scene9["lives_left_box"] = lives_left_box
scene10["lives_left_box"] = lives_left_box
scene11["lives_left_box"] = lives_left_box
scene12["lives_left_box"] = lives_left_box
scene13["lives_left_box"] = lives_left_box
scene14["lives_left_box"] = lives_left_box
scene15["lives_left_box"] = lives_left_box
scene16["lives_left_box"] = lives_left_box
scene17["lives_left_box"] = lives_left_box
scene18["lives_left_box"] = lives_left_box
scene19["lives_left_box"] = lives_left_box

## outputs lives left counter on the top left corner of the screen 
lives_left = play.new_text(
  words = 'Lives left: ' + str(lives),
  x = -273, 
  y = 250, 
  angle = 0, 
  font = None, 
  font_size = 30, 
  color = 'lightBlue', 
  transparency = 100
  )

# declaration of which scenes to include the lives left text
scene1["lives_left"] = lives_left
scene2["lives_left"] = lives_left
scene3["lives_left"] = lives_left
scene4["lives_left"] = lives_left
scene5["lives_left"] = lives_left
scene6["lives_left"] = lives_left
scene7["lives_left"] = lives_left
scene8["lives_left"] = lives_left
scene9["lives_left"] = lives_left
scene10["lives_left"] = lives_left
scene11["lives_left"] = lives_left
scene12["lives_left"] = lives_left
scene13["lives_left"] = lives_left
scene14["lives_left"] = lives_left
scene15["lives_left"] = lives_left
scene16["lives_left"] = lives_left
scene17["lives_left"] = lives_left
scene18["lives_left"] = lives_left
scene19["lives_left"] = lives_left

# adding each scene into the dictionary scenes
scenes[1] = scene1
scenes[2] = scene2
scenes[3] = scene3
scenes[4] = scene4
scenes[5] = scene5
scenes[6] = scene6
scenes[7] = scene7
scenes[8] = scene8
scenes[9] = scene9
scenes[10] = scene10
scenes[11] = scene11
scenes[12] = scene12
scenes[13] = scene13
scenes[14] = scene14
scenes[15] = scene15
scenes[16] = scene16
scenes[17] = scene17
scenes[18] = scene18
scenes[19] = scene19

# show each of the scenes based on the scene id that is requested in the dictionary using the "keys" function
def show_scene(id):
  for i in scenes[id].keys():
    scenes[id][i].show()

# hide each of the scenes whenever not in use in the dictionary using the "keys" function
def hide_scene(id):
  for i in scenes[id].keys():
    scenes[id][i].hide()

# calling upon the function variable "hide_scene" to hide scenes
for k in scenes.keys():
  hide_scene(k)

# Next Button
## defining what happens when the "next button" is clicked
@next_btn.when_clicked
def next_function():
  global scene_id ## allows the variable "scene_id" to be used in this function
  
  hide_scene(scene_id) ## hides the scene with the next button

  ## start of if/elif statements for which scene to switch to depending on the current scene
  if scene_id == 18:
    scene_id = 8 
  elif scene_id == 19:
    scene_id = 8
  elif scene_id == 11: ## changes the scene for the dice roll depending on the result of the dice roll
    if character_win == 1: 
      scene_id = 12 ## victory scene if dice roll won
    elif character_win == 0:
      scene_id = 13 ## death scene if dice roll lost
  else:
    scene_id = scene_id + 1 
    
  show_scene(scene_id) ## shows the new scene after the scene ("scene_id") gets switched

show_scene(scene_id) # this is needed in order to show the starting screen with "WHAT A STORM!"

# Choice 1
## defining what happens when the "choice 1 button" is clicked
@choice1.when_clicked
def next_function():
  global scene_id ## allows the variable "scene_id" to be used in this definition
  
  hide_scene(scene_id) ## hides the current scene with the choice 1 button

  ## start of if/elif statements for which scene to switch to depending on the current scene
  if scene_id == 4:
    scene_id = 5
  elif scene_id == 5:
    scene_id = 6
  elif scene_id == 7:
    scene_id = 15
  elif scene_id == 14:
    scene_id = 15
  elif scene_id == 15:
    scene_id = 17
  elif scene_id == 16:
    scene_id = 19
  elif scene_id == 9:
    scene_id = 10
  elif scene_id == 10:
    scene_id = 11 ## switches the scene to scene 11

    global character_win ## allows the variable "character_win" to be used within this function
    
    ## declaring a variable to later output the result of the game
    text_result = "That was..."

    ## declares variable for the character's dice
    character_dice = random.randint(1, 6)

    ## outputting on the scene what the character rolled
    scene11["text1_scene11"] = play.new_text(
      words='You rolled ' + str(character_dice) + '!',  
      x = 0, 
      y = -100, 
      angle = 0, 
      font = None, 
      font_size = 25, 
      color = 'white', 
      transparency = 100
      )

    ## beginning of if/elif/else statements to declare whether the dice was even or odd
    if character_dice == 2:
      text_result += " even! You won!"
      character_win += 1
    elif character_dice == 4:
      text_result += " even! You won!"
      character_win += 1
    elif character_dice == 6:
      text_result += " even! You won!"
      character_win += 1
    else:
      text_result += " odd... uh oh..."

    ## outputting the final text result depending on the dice roll
    scene11["text2_scene11"] = play.new_text(
      words = text_result, 
      x = 0, 
      y = -150, 
      angle = 0, 
      font = None, 
      font_size = 25, 
      color = 'white', 
      transparency = 100
    )
  show_scene(scene_id) ## shows the new scene after the scene ("scene_id") gets switched

# Choice 2
## defining what happens when the "choice 2 button" is clicked
@choice2.when_clicked
def next_function():
  global scene_id ## allows the variable "scene_id" to be used in this definition
  
  hide_scene(scene_id) ## hides the current scene with the choice 2 button

  ## start of if/elif statements for which scene to switch to depending on the current scene
  if scene_id == 4:
    scene_id = 7
  elif scene_id == 5:
    scene_id = 8
  elif scene_id == 7:
    scene_id = 8
  elif scene_id == 14:
    scene_id = 16
  elif scene_id == 15:
    scene_id = 16
  elif scene_id == 16:
    scene_id = 17
  elif scene_id == 9:
    scene_id = 13
  elif scene_id == 10:
    scene_id = 13
    
  show_scene(scene_id) ## shows the new scene after the scene ("scene_id") gets switched

# Choice 3
## defining what happens when the "choice 3 button" is clicked
@choice3.when_clicked
def next_function():
  global scene_id ## allows the variable "scene_id" to be used in this definition
  
  hide_scene(scene_id) ## hides the current scene with the choice 3 button

  ## start of if/elif statements for which scene to switch to depending on the current scene
  if scene_id == 4:
    scene_id = 14
  elif scene_id == 14:
    scene_id = 17
  elif scene_id == 15:
    scene_id = 18
  elif scene_id == 9:
    scene_id = 13
    
  show_scene(scene_id) ## shows the new scene after the scene ("scene_id") gets switched

# Restart
## defining what happens when the "restart button" is clicked
@restart.when_clicked
def next_function():
  ## allows the variables "scene_id" and "lives" to be used within this function
  global scene_id
  global lives
  
  hide_scene(scene_id) ## hides the current scene with the restart button
  
  scene_id = 1 ## resets the scene to the first intro scene with "What a storm!"
  lives -= 1 ## subtracts 1 life from the number of lives
  
  show_scene(scene_id) ## shows the new scene after the scene ("scene_id") gets switched

  ## outputs a black box underneath the text
  lives_left_box = play.new_box(
    color = "black",
    x = -275, 
    y = 250, 
    width = 140, 
    height = 27, 
  )
  ## outputs lives left counter on the top left corner of the screen 
  lives_left = play.new_text(
    words = 'Lives left: ' + str(lives),
    x = -273, 
    y = 250, 
    angle = 0, 
    font = None, 
    font_size = 30, 
    color = 'lightBlue', 
    transparency = 100
    )

  # if statement for what happens when character has 0 lives left
  if lives == 0:
    # sets a black box
    black = play.new_circle(
      color = "black",
      x = 0,
      y = 0,
      radius = 500,
      )
    
    # fail death text
    ouch = play.new_text(
      words = "FAIL! YOU DIED (FOREVER)!!! AHHHHH!!!",
      font_size = 50,
      x = 0,
      y = 30,
      color = 'red',
      transparency = 100
    )

play.start_program() # allows Python Play to actually start the program