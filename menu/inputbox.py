# by Timothy Downs, inputbox written for my map editor

# This program needs a little cleaning up
# It ignores the shift key
# And, for reasons of my own, this program converts "-" to "_"

# A program to get user input, allowing backspace etc
# shown in a box in the middle of the screen
# Called by:
# import inputbox
# answer = inputbox.ask(screen, "Your name")
#
# Only near the center of the screen is blitted to

import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *

def get_key():
  while True:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font('menu/data/coders_crux/coders_crux.ttf', 36)
  pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 2),
                    (screen.get_height() / 2),
                    500,30), 0)
  pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2),
                    (screen.get_height() / 2),
                    504,34), 1)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2), (screen.get_height() / 2)+8))
  pygame.display.flip()

def ask(screen, question, atual=None, b=True):
	pygame.font.init()
	if atual != None:
		current_string = atual
	else:
		current_string = ""
	display_box(screen, question + ": " + string.join(current_string,""))
	while 1:
		inkey = get_key()
		if inkey == K_BACKSPACE:
			current_string = current_string[0:-1]
		elif inkey == K_RETURN:
			if not b and current_string not in ['easy', 'medium', 'hard']:
				continue
			else:
				screen.fill((0,0,0))
				break
		elif inkey <= 127:
			if (len(current_string) < 17 and b == True) or (len(current_string) < 6 and b == False):
				current_string+=chr(inkey)
		display_box(screen, question + ": " + string.join(current_string,""))
	return string.join(current_string,"")

def main():
  screen = pygame.display.set_mode((320,240))
  print ask(screen, "Name") + " was entered"

if __name__ == '__main__': main()
