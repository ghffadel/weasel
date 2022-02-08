from random import choice, randint
from string import ascii_uppercase
from tkinter import *
from tkinter import scrolledtext

PROBABILITY = 5
SIZE = 100

def initWindow (size):
  window = Tk()
  window.eval('tk::PlaceWindow . center')
  window.geometry(size)
  window.title('Weasel')

  return window

def generateCharacter ():
  return choice(ascii_uppercase + ' ')

def generateString (length):
  return ''.join([generateCharacter() for i in range(length)])

def compareStrings (string, target):
  return sum(int(string[i] == target[i]) for i in range(len(string)))

def modifiedString (string):
  string = list(string)

  for i in range(len(string)):
    if randint(1, 100) <= PROBABILITY:
      string[i] = generateCharacter()

  return ''.join(string)

def weasel (target):
  generation = 1
  found = False
  string = generateString(len(target))
  window = initWindow('350x250')
  textArea = scrolledtext.ScrolledText(window, width = 30, height = 13, font = ('Arial', 10, 'normal'))

  while not found:
    strings = list()
    scores = list()
    maxScore = (0, 0)

    for i in range(SIZE):
      strings.append(modifiedString(string))
      scores.append(compareStrings(strings[i], target))

      if scores[i] > maxScore[1]:
        maxScore = (i, scores[i])

    found = maxScore[1] == len(target)
    string = strings[maxScore[0]]

    textArea.insert(INSERT, 'Generation %d:\nString: %s\nScore: %d\n\n' % (generation, string, maxScore[1]))

    generation += 1
  
  textArea.configure(state = 'disabled')
  textArea.grid(column = 0, padx = 60, pady = 15)

  window.mainloop()

window = initWindow('350x250')

targetVar = StringVar()
targetLabel = Label(window, text = 'Insert the target string', font = ('Arial', 10, 'bold'))
targetEntry = Entry(window, textvariable = targetVar, font = ('Arial', 10, 'normal'))

confirmButton = Button(window, text = 'Confirm', font = ('Arial', 10, 'bold'), 
command = lambda: [window.destroy(), weasel(targetVar.get().upper())])

targetLabel.grid(row = 0, column = 0, padx = 100, pady = 40)
targetEntry.grid(row = 1, column = 0, padx = 100)
confirmButton.grid(row = 2, column = 0, padx = 100, pady = 20)

window.mainloop()