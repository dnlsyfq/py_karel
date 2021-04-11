def main():
  move()
  while front_is_clear():
    if beepers_present():
      for i in range(10):
        pick_beeper()
    else:
      move()
