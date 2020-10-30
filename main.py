# i don't know what i am doing, but i hope it works anyway


from os import system # so that i can clear the screen when i update the UI
import sys, time
from random import randint


# might be the plr_ variable assignment list
plr_money = 0 #        used to buy upgrades
plr_currentammo = 10 # ammo in reserve
plr_clipsize = 5 #     most ammo you can have in your gun
plr_loadedammo = 5 #   current amount of ammo in your gun
plr_target="nothing in particular" # default enemy
plr_health = 150 #                   your health
plr_attack = 5 #                     your damage amount

#bad_ (enemy, hence bad) variables
bad_health = 225 #        enemy health
bad_attack_max = 8 #      the most possible damage dealt
bad_attack_min = 2 #      the least possible damage dealt



#game_ variables
game_output = "" # used to print a message
game_moneygain_min = 3 # most possible money gained
game_moneygain_max = 6 # least possible money gained
sv_cheats = False #      cheats on?


# this is used in a subroutine for reloading
var_reloadamount = 0 # leave this alone, as it is used to keep track of the reloading process



# clear the game UI
def ui_clr():
  system("clear")




# player functions
def plr_canshoot(): # is the gun out of bullets?
  if plr_loadedammo < 1:
    return False
  else:
    return True



def plr_buyhealth(): # buy health
  global game_output
  global plr_money
  if plr_money < 10:
    game_output = "  You do not have enough money."
  else:
    global plr_health
    game_output = "  You purchase your life back."
    plr_money -= 10
    plr_health += 12



def plr_buybighealth(): # buy even more health
  global game_output
  global plr_money
  if plr_money < 25:
    game_output = "  You do not have enough money."
  else:
    global plr_health
    game_output = "  You purchase your life back."
    plr_money -= 25
    plr_health += 25



def plr_buygun(): # gives 10 more reserve shots, more damage, and 1 extra bullet in your gun
  global game_output
  global plr_money # gotta avoid those 'UnboundLocalError' monsters by using 'global' keyword
  if plr_money < 20:
    game_output = "  You do not have enough money to upgrade."
  else:
    global plr_attack
    global plr_clipsize
    global plr_currentammo
    global plr_loadedammo
    game_output = "  You purchase a new gun with more ammo, 10 more bullets extra, and more damage."
    plr_money -= 20
    plr_attack += 2
    plr_clipsize += 1
    plr_loadedammo = plr_clipsize
    plr_currentammo += 10



def plr_shootgun(target="nothing in particular", dev=False): #make the gun shoot and lose a bullet
  global game_output
  if plr_canshoot():
    global plr_money
    plr_money += randint(game_moneygain_min, game_moneygain_max) # gain more money after the shot
    global bad_health
    global plr_loadedammo # to ward off the fire-breathing monster 'UnboundLocalError'
    plr_loadedammo = plr_loadedammo - 1 
    game_output = "\033[2;37;40m BANG! You fire off a shot at " + target + "."
    bad_health -= plr_attack
    debug_showgundata(dev)
  else:
    game_output = "\033[2;37;40m CLICK! Your gun is empty. You need to reload it."



def plr_reloadgun(dev=False): # get more bullets into your gun
  global plr_currentammo # this gets rid of the 'UnboundLocalError' error
  global plr_loadedammo #  this too
  global game_output #     in fact any 'global' keyword used right wards off 'UnboundLocalError' errors
  if plr_loadedammo > plr_clipsize - 1:
    print("Your gun is already full.")
    return
  if plr_currentammo < 1:
    print("You are out of ammo. You need to buy more.")
  var_reloadamount = plr_clipsize - plr_loadedammo # how much bullet to get
  if dev: # just for debug purposes
    print("  var_reloadamount (plr_reloadgun):" + str(var_reloadamount))
  plr_currentammo -= var_reloadamount # takes away bullets from reserve
  plr_loadedammo += var_reloadamount # gives you your ammo back into the gun
  plr_loadedammo = abs(plr_loadedammo)
  debug_showgundata(dev)
  game_output = " You reload your gun, and ready yourself to shoot."



# debug_ subroutines are located below
def debug_showgundata(debuggingOn=False): # this is for debugging. it dumps the gun ammo variables to the UI
  if debuggingOn:
    print("  debug_showgundata (output):")
    print(" plr_currentammo:" + str(plr_currentammo) + "\n plr_clipsize:" + str(plr_clipsize) + "\n plr_loadedammo:" + str(plr_loadedammo))
  else:
    pass



# yes and no, for easier reading
yes = True
no = False
theWorldHasNotEndedYet = True # why not



# the epic mainloop
plr_target = "Evil Monster"
game_output = " You are approached by a(n) " + plr_target + "."
print("\033[2;37;40m")
firstTime = True # so that you do not get attacked immediately

while theWorldHasNotEndedYet: # start mainloop
  if plr_health < 1: # you have zero or less health
    ui_clr()
    print("\033[2;37;40m                                   GAME OVER! YOU LOSE!                                   ")
    exit()
  elif bad_health < 1: # they have zero or less health
    ui_clr()
    print("\033[2;37;40m                                    GAME OVER! YOU WIN!                                   ")
    exit()
  if not firstTime: ui_clr()
  if not firstTime: print()
  if not firstTime: print("\033[2;37;40m                   " + str(plr_currentammo) + "  🔫 " + str(plr_loadedammo) + "/" + str(plr_clipsize) + " | Health: | " + str(plr_health) + "  | " + plr_target + " Health: | " + str(bad_health) + "  | 💰 " + str(plr_money))
  if not firstTime: print("\033[2;37;40m                           " + game_output)
  if not firstTime: print()
  if not firstTime: time.sleep(2)
  if not firstTime: game_output = " SWING! The " + plr_target + " swings at you."
  if not firstTime: plr_health -= randint(bad_attack_min, bad_attack_max)
  firstTime = False
  ui_clr()
  print()
  print("\033[2;37;40m                   " + str(plr_currentammo) + "  🔫 " + str(plr_loadedammo) + "/" + str(plr_clipsize) + " | Health: | " + str(plr_health) + "  | " + plr_target + " Health: | " + str(bad_health) + "  | 💰 " + str(plr_money))
  print("\033[2;37;40m                           " + game_output)
  print()
  print("\033[2;37;40m                          ( COMMANDS: shoot, reload, upgrade/buy[20$], heal[10$], healbig[25$] )")
  action = input("                      >")
  if action == "shoot":
    plr_shootgun(plr_target)
  elif action == "reload":
    plr_reloadgun()
  elif (action == "upgrade") or (action == "buy"):
    plr_buygun()
  elif action == "heal":
    plr_buyhealth()
  elif action == "healbig":
    plr_buybighealth()
  elif action == "sv_cheats 1":
    sv_cheats = True
    game_output = "sv_cheats ON"
  elif action == "sv_cheats 0":
    sv_cheats = False
    game_output = "sv_cheats OFF"
  elif action == "sv_cheats":
    game_output = str(sv_cheats)

  #needs cheats on
  elif action == "debug_givemoney":
    if sv_cheats: plr_money += 50
    else: game_output = "cheats are not availiable without sv_cheats on"
  elif action == "debug_healthup":
    if sv_cheats: plr_health += 100
    else: game_output = "cheats are not availiable without sv_cheats on"
  elif action == "debug_showgundata":
    if sv_cheats: debug_showgundata(yes)
    else: game_output = "cheats are not availiable without sv_cheats on"
  else: # if the input is not valid, then it ignores it and continues the game
    game_output = " Uhhh... You hesitate for a moment."
