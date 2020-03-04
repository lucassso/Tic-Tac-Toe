import time
import random
import os
import os
from random import shuffle
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

print('The board is a 3x3 area with nine spots, including: top-left, top-middle,  bottom-left, middle-right, et cetera. Swapping turns, try and use your pieces to make 3 in a row, either veritcally, horizontally, or diagonally. ')
time.sleep(1)
print("")
piece = input('Now, would player 1 like to be circles (O) or crosses (X)?\n')
piece = piece.lower().strip(" ")
pieces = ["crosses","circles"]

if piece == "crosses" or piece == "X" or piece == "cross" or piece == "x":
  piece = "cross"
  piece2 = "circle"
  print("")
  print("Okay, your piece will be crosses (X)\n")
  time.sleep(1)
elif piece == "circles" or piece == "O" or piece == "o" or piece == "0" or piece == "circle":
  piece = "circle"
  piece2 = "cross"
  print("")
  print("Okay, your piece will be circles (O)\n")
  time.sleep(1)
else:
  print("")
  piece1 = (random.choice(pieces))
  piece = piece1
  print("Thats not a suggested answer. We will decide for you. You will be...")
  time.sleep(2)
  print("%s!\n"%piece.title())
  if piece1 == "crosses":
    piece = "cross"
  elif piece1 == "circles":
    piece = "circle"
    
if piece == "circle":
  board_piece = "O"
  cpu_piece = "X"
  piece1 = 'circle'
elif piece == "circles":
  board_piece = "O"
  cpu_piece = "X"
elif piece == "cross":
  board_piece = "X"
  cpu_piece = "O"
elif piece == "crosses":
  board_piece = "X"
  cpu_piece = "O"

print("")


a1 = ' '
a2 = ' '
a3 = ' '
b1 = ' '
b2 = ' '
b3 = ' '
c1 = ' '
c2 = ' '
c3 = ' '
line1 = " "+a1+"|"+a2+"|"+a3 + "\n"
line1b = "--+-+--\n"
line2 = " "+b1+"|" + b2 + "|" + b3 + "\n"
line2b = "--+-+--\n"
line3 = " "+c1+"|" + c2 + "|" + c3 + '\n'
board = line1+line1b+line2+line2b+line3
print(board)
used_boxes = []
available_boxes = ["topleft", "topmiddle", "topright", "middleleft" , "middle", "middleright", "bottomleft", "bottommiddle", "bottomright"]

win_combos = [[a1,a2,a3], [b1,b2,b3], [c1,c2,c3], [a1,b1,c1], [a2,b2,c2], [a3,b3,c3], [a1,b2,c3], [a3,b2,c1]]
win = False
moves = 0
while win == False:
  move = input('Where would you like to place your %s, player 1?\n'%piece).replace(" ","").lower().replace("-","")
  print("")
  if move in used_boxes:
    print('That place is occupied.')
    time.sleep(1)
    while move not in available_boxes:
      move = input('Where would you like to place your %s, player 1?\n'%piece)
      move = move.strip('').lower().replace('-', '')
      print("")
      if move in used_boxes:
        print('That place is occupied.\n')
        time.sleep(1)
      elif move == 'middle':
        b2 = board_piece
        line2 = " " + b1 + "|" + b2 + "|" + b3 + "\n"
      elif move == "topleft":
        a1 = board_piece
        line1 = " " + a1 + "|" + a2 + "|"+a3 + "\n"
      elif move == "topmiddle":
        a2 = board_piece
        line1 = " " + a1 + "|" + a2 + "|" + a3 + "\n"
      elif move == "topright":
        a3 = board_piece
        line1 = " " + a1 + "|" + a2 + "|" + a3 + "\n"
      elif move == "middleleft":
        b1 = board_piece
        line2 = " "+b1+"|"+b2+"|"+b3 + "\n"
      elif move == "middleright":
        b3 = board_piece
        line2 = " "+b1+"|"+b2+"|"+b3 + "\n"
      elif move == "bottomleft":
        c1 = board_piece
        line3 = " "+c1+"|"+c2+"|" + c3 + "\n"
      elif move == "bottommiddle":
        c2 = board_piece
        line3 = " "+c1+"|" + c2+"|"+c3 + "\n"
      elif move == "bottomright":
        c3 = board_piece
        line3 = " "+c1+"|"+c2+"|"+c3 + "\n"
      else:
        print("That's not a space on the board. Try again.\n")
        time.sleep(1)
  elif move == 'middle':
    b2 = board_piece
    line2 = " " + b1 + "|" + b2 + "|" + b3 + "\n"
  elif move == "topleft":
    a1 = board_piece
    line1 = " " + a1 + "|" + a2 + "|"+a3 + "\n"
  elif move == "topmiddle":
    a2 = board_piece
    line1 = " " + a1 + "|" + a2 + "|" + a3 + "\n"
  elif move == "topright":
    a3 = board_piece
    line1 = " " + a1 + "|" + a2 + "|" + a3 + "\n"
  elif move == "middleleft":
    b1 = board_piece
    line2 = " "+b1+"|"+b2+"|"+b3 + "\n"
  elif move == "middleright":
    b3 = board_piece
    line2 = " "+b1+"|"+b2+"|"+b3 + "\n"
  elif move == "bottomleft":
    c1 = board_piece
    line3 = " "+c1+"|"+c2+"|" + c3 + "\n"
  elif move == "bottommiddle":
    c2 = board_piece
    line3 = " "+c1+"|" + c2+"|"+c3 + "\n"
  elif move == "bottomright":
    c3 = board_piece
    line3 = " "+c1+"|"+c2+"|"+c3 + "\n"
  else:
    print('That piece is not on the board. Try again.\n')
    while move not in available_boxes:
      move = input('Where would you like to place your %s, player 1?\n'%piece)
      move = move.replace(' ', '').lower().replace('-', '')
      print("")
      if move in used_boxes:
        print('That place is occupied.')
        time.sleep(1)
      elif move == 'middle':
        b2 = board_piece
        line2 = " " + b1 + "|" + b2 + "|" + b3 + "\n"
      elif move == "topleft":
        a1 = board_piece
        line1 = " " + a1 + "|" + a2 + "|"+a3 + "\n"
      elif move == "topmiddle":
        a2 = board_piece
        line1 = " " + a1 + "|" + a2 + "|" + a3 + "\n"
      elif move == "topright":
        a3 = board_piece
        line1 = " " + a1 + "|" + a2 + "|" + a3 + "\n"
      elif move == "middleleft":
        b1 = board_piece
        line2 = " "+b1+"|"+b2+"|"+b3 + "\n"
      elif move == "middleright":
        b3 = board_piece
        line2 = " "+b1+"|"+b2+"|"+b3 + "\n"
      elif move == "bottomleft":
        c1 = board_piece
        line3 = " "+c1+"|"+c2+"|" + c3 + "\n"
      elif move == "bottommiddle":
        c2 = board_piece
        line3 = " "+c1+"|" + c2+"|"+c3 + "\n"
      elif move == "bottomright":
        c3 = board_piece
        line3 = " "+c1+"|"+c2+"|"+c3 + "\n"
  available_boxes.remove(move)
  used_boxes.append(move)
  board = line1+line1b+line2+line2b+line3
  cls()
  print(board)
  move = input('Where would you like to place your %s, player 2?\n'%piece + "You can place it in: " + ", ".join(available_boxes) + '\n').strip().lower().replace("-","")
  print("")
  if move in used_boxes:
    print('That place is occupied.')
    time.sleep(1)
    while move not in available_boxes:
      move = input('Where would you like to place your %s, player 2?\n'%piece + "You can place it in: " + ", ".join(available_boxes) + '\n').strip().lower().replace("-","")
      print("")
      if move in used_boxes:
        print('That place is occupied.\n')
        time.sleep(1)
      elif move == 'middle':
        b2 = cpu_piece
        line2 = " " + b1 + "|" + b2 + "|" + b3 + "\n"
      elif move == "topleft":
        a1 = cpu_piece
        line1 = " " + a1 + "|" + a2 + "|"+a3 + "\n"
      elif move == "topmiddle":
        a2 = cpu_piece
        line1 = " " + a1 + "|" + a2 + "|" + a3 + "\n"
      elif move == "topright":
        a3 = cpu_piece
        line1 = " " + a1 + "|" + a2 + "|" + a3 + "\n"
      elif move == "middleleft":
        b1 = cpu_piece
        line2 = " "+b1+"|"+b2+"|"+b3 + "\n"
      elif move == "middleright":
        b3 = cpu_piece
        line2 = " "+b1+"|"+b2+"|"+b3 + "\n"
      elif move == "bottomleft":
        c1 = cpu_piece
        line3 = " "+c1+"|"+c2+"|" + c3 + "\n"
      elif move == "bottommiddle":
        c2 = cpu_piece
        line3 = " "+c1+"|" + c2+"|"+c3 + "\n"
      elif move == "bottomright":
        c3 = cpu_piece
        line3 = " "+c1+"|"+c2+"|"+c3 + "\n"
      else:
        print("That's not a space on the board. Try again.\n")
        time.sleep(1)
      if move == 'middle':
        b2 = cpu_piece
        line2 = " " + b1 + "|" + b2 + "|" + b3 + "\n"
      elif move == "topleft":
        a1 = cpu_piece
        line1 = " " + a1 + "|" + a2 + "|"+a3 + "\n"
      elif move == "topmiddle":
        a2 = cpu_piece
        line1 = " " + a1 + "|" + a2 + "|" + a3 + "\n"
      elif move == "topright":
        a3 = cpu_piece
        line1 = " " + a1 + "|" + a2 + "|" + a3 + "\n"
      elif move == "middleleft":
        b1 = cpu_piece
        line2 = " "+b1+"|"+b2+"|"+b3 + "\n"
      elif move == "middleright":
        b3 = cpu_piece
        line2 = " "+b1+"|"+b2+"|"+b3 + "\n"
      elif move == "bottomleft":
        c1 = cpu_piece
    line3 = " "+c1+"|"+c2+"|" + c3 + "\n"
  elif move == "bottommiddle":
    c2 = cpu_piece
    line3 = " "+c1+"|" + c2+"|"+c3 + "\n"
  elif move == "bottomright":
    c3 = cpu_piece
    line3 = " "+c1+"|"+c2+"|"+c3 + "\n"
  else:
    print('That piece is not on the board. Try again.\n')
    while move not in available_boxes:
      move = input('Where would you like to place your %s, player 2?\n'%piece2 + "You can place it in: " + ", ".join(available_boxes) + '\n').strip().lower().replace("-","")
      print("")
      if move in used_boxes:
        print('That place is occupied.')
        time.sleep(1)
      elif move == 'middle':
        b2 = board_piece
        line2 = " " + b1 + "|" + b2 + "|" + b3 + "\n"
      elif move == "topleft":
        a1 = board_piece
        line1 = " " + a1 + "|" + a2 + "|"+a3 + "\n"
      elif move == "topmiddle":
        a2 = board_piece
        line1 = " " + a1 + "|" + a2 + "|" + a3 + "\n"
      elif move == "topright":
        a3 = board_piece
        line1 = " " + a1 + "|" + a2 + "|" + a3 + "\n"
      elif move == "middleleft":
        b1 = board_piece
        line2 = " "+b1+"|"+b2+"|"+b3 + "\n"
      elif move == "middleright":
        b3 = board_piece
        line2 = " "+b1+"|"+b2+"|"+b3 + "\n"
      elif move == "bottomleft":
        c1 = board_piece
        line3 = " "+c1+"|"+c2+"|" + c3 + "\n"
      elif move == "bottommiddle":
        c2 = board_piece
        line3 = " "+c1+"|" + c2+"|"+c3 + "\n"
      elif move == "bottomright":
        c3 = board_piece
        line3 = " "+c1+"|"+c2+"|"+c3 + "\n"

  available_boxes.remove(move)
  used_boxes.append(move)
  board = line1+line1b+line2+line2b+line3
 
