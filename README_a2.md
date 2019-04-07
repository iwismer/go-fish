# Go Fish

Isaac Wismer  
wismeri@uoguelph.ca  
0959337  
CIS*4450 W19  

A simple game of go fish written in python using PyQt5.

## File Structure

### Folders

**go_fish:** All the classes related to the game of go fish
**ui:** The files that contain the UI design. These can be opened with Qt5 Designer  
**uml:** The UML diagram in XMI and PDF format. Umbrello was used to create the diagram

### Files

#### root

**main_window.py:** This is the main GUI for the game.  
**main.py:** This is the main class that runs the whole program, and represents the interface between the GUI and the game.  
**save_broken.gofish:** A save file that will cause an error when loaded
**save_working_3.gofish:** A save file that has 3 bots
**setup_dialog.py:** This is the setup window for the game.  

#### go_fish

**card.py:** The card related classes (Suit, CardValue, Card)  
**deck.py:** The deck related classes (Deck [abstract], PokerDeck)  
**game.py:** The Game [abstract] class  
**go_fish.py:** The GoFish class, a subclass of Game  
**hand.py:** The Hand class  
**player.py:** The Player [abstract], HumanPlayer and BotPlayer classes  

#### ui

**output_frame:** A frame that is used to show the output of each bot. These are dynamically places on the GUI depending on how many bots are playing.
**pairs_frame:** A frame that is used to show the score and pairs for each player. These are dynamically places on the GUI depending on how many bots are playing.
**Ui_dialog.py:** The GUI class generated by pyuic for the game over/error dialog  
**Ui_go_fish.py:** The GUI class for the main window of the game. Generated by pyuic.  
**Ui_setup.py:** The GUI class for the setup window. Generated by pyuic.  


## Building & Running

This project requires Python 3.7 (it may work on Python 3.6 but I have not tested that) and and for the module PyQt5 to be installed through pip (or python-pyqt5 through your package manager). It does not run on the SOCS server as it only has Python 3.5.3  
This program has a GUI written in Qt, and does not have a CLI implementation.

### Virtual Environment

From within the project folder:

```sh
python3.7 -m venv venv
source venv/bin/activate
pip3.7 install pyqt5
python3.7 main.py
```

### Native

Generally PyQt5 is installed with the command `pip3.7 install pyqt5`  
To run, use the command: `python3.7 main.py`  

## Using the program

The window shown when the program starts allows you to choose the number of bots you wish to play against, their difficulty, and set their and your names. You can also open an existing game from this window.  
The game begins when you press "Play Go Fish". First, all players put down any pairs that they have in their hands.  
It is always the human player's turn first. Select a card from your hand that you would like to ask for a match for using the radio buttons on the left. Then push a the button for the bot you would like to ask for if they have a card of the same number.  
See the output on the right for the outcome of the ask. If the bot did not have a matching card, you will automatically go fish, and each bot will take their turn. It will then be your turn again. If you did get a match, you will get to go again.  
All bot actions are automatic using my advanced (totally not RNG) AI. You can see the outcome from their turns in their respective output boxes.  
A game can be saved at any time using the "Save Game" option in the File menu. The same goes for the "Open Game" option in the same menu for opening an old game.

To demonstrate the portable object, I have added a "Print Hand to JSON" menu item, which will print your player's hand to STDOUT.

There are also keyboard shortcuts in the main window:
- Ctrl+O = Open Game
- Ctrl+S = Save Game
- Ctrl+N = New game
- Ctrl+Q = Quit

## User Stories

1. As a user I want to be able to save my current game, then reopen it and start where I left off later on if I don't have enough time to finish the game
2. As a user I want to be able to select the number of bots I will to play against as this will make the game more interesting
3. As a user I want to be able to rename my player and the bots to make the game more personalized
4. As a user I want to be able to select the level of bot difficulty so I can tune the game to my skills

## Tips

If you can't figure out my code, take a look at the UML diagram. It can be very helpful with figuring out how the classes interact

If you have a hard time reading the tables or titles, render the markdown, and the tables will be formatted nicely

## Learning Outcomes

### Demonstrate best practices for OO development in the language of your choice

#### Good encapsulation -> Using properties and "private" functions and variables

Many instance methods and variables within the classes are hidden. Generally speaking, if it doesn't make sense for the variable to be changed by the user, then it's not public. A good example of this is the deck class, We want to keep the deck private, but still allow things like drawing cards, so we make the variables private, but create public methods to do specific actions.

+------------+-------+------------------------------------------------------------------------------------+
| File       | Line  | Description                                                                        |
| :--------- | :---: | :--------------------------------------------------------------------------------- |
| player.py  | 39,48 | Using properties for a getter and setter on a private variable                     |
+------------+-------+------------------------------------------------------------------------------------+
| card.py    |  63   | Using a property to allow getting, but not setting the name value                  |
+------------+-------+------------------------------------------------------------------------------------+
| go_fish.py |  52   | protecting a method from outside calling by prepending the name with an underscore |
+------------+-------+------------------------------------------------------------------------------------+
| go_fish.py |  203  | making a method public by not adding an underscore to the beginning of the name    |
+------------+-------+------------------------------------------------------------------------------------+

#### High cohesion and Low Coupling -> MVC used for GUI, code split into modules

For this assignment I rewrote the front end of my application, to better decouple it from the game object. While the front end is not general enough to work with any game, it does not interact directly with the game except to read its state to update the interface. This was accomplished by adding a controller (GoFishGame in main.py:23) between the model(GoFish in go_fish.py:19) and view (MainWindow in main_window.py:23). This allows the objects to be less coupled to each other.

+---------+-------+---------------------------------------------------------------------------------------------------+
| File    | Line  | Description                                                                                       |
| :------ | :---: | :------------------------------------------------------------------------------------------------ |
| main.py |  23   | The controller that was added to reduce coupling between the GUI and game                         |
+---------+-------+---------------------------------------------------------------------------------------------------+
| main.py | 17-20 | Main imports from 3 different local modules: the root (the folder that main is in, go_fish, which |
|         |       | contains all the go fish related classes, and ui, which has most of the GUI classes.)             |
+---------+-------+---------------------------------------------------------------------------------------------------+

#### Good code style -> Following PEP8, type hinting

Throughout my code I adhere to Python style guides (as much as possible). This is accomplished through the use of an auto formatter.
As well, I use type hinting to enhance the readability and understandability of my code through the annotations of parameters and return values of functions.

+------------+-------+----------------------------------------------------------------------------------------+
| File       | Line  | Description                                                                            |
| :--------- | :---: | :------------------------------------------------------------------------------------- |
| go_fish.py |  73   | Type hinting a function to help a reader better understand what it does, if also has a |
|            |       | docstring to explain the purpose if each argument                                      |
+------------+-------+----------------------------------------------------------------------------------------+
| main.py    |  117  | Another example of type hinting and a docstring                                        |
+------------+-------+----------------------------------------------------------------------------------------+

For more examples, look at almost any  public function in the program, and it will be annotated with a docstring and have type hinting

#### Override built in class functions (__str__)

Python has built in functions for classes that can be overridden, for example to print to a string, for equality or to allow access by index.

+-----------+-------+---------------------------------------------------------------------------------+
| File      | Line  | Description                                                                     |
| :-------- | :---: | :------------------------------------------------------------------------------ |
| card.py   |  39   | function to output a CardValue to a string (allows use of the str() function)   |
+-----------+-------+---------------------------------------------------------------------------------+
| card.py   |  96   | function to output a Card to a string (allows use of the str() function)        |
+-----------+-------+---------------------------------------------------------------------------------+
| card.py   |  42   | function compare 2 CardValues against each other using =                        |
+-----------+-------+---------------------------------------------------------------------------------+
| hand.py   |  23   | function to output a Hand to a string (allows use of the str() function)        |
+-----------+-------+---------------------------------------------------------------------------------+
| player.py |  31   | function to output a Player to a string (allows use of the str() function)      |
+-----------+-------+---------------------------------------------------------------------------------+
| player.py |  31   | function to output a HumanPlayer to a string (allows use of the str() function) |
+-----------+-------+---------------------------------------------------------------------------------+
| player.py |  31   | function to output a BotPlayer to a string (allows use of the str() function)   |
+-----------+-------+---------------------------------------------------------------------------------+

### Utilize persistence effectively to realize a user story that could not be realized without persistence

I used persistence to allow a user to save and open games. To do this, I use the built in pickle module which exports an object to a binary file, and allows that object to be read back into an object.

+---------+-------+-----------------------------------------------------------------------------------------------+
| File    | Line  | Description                                                                                   |
| :------ | :---: | :-------------------------------------------------------------------------------------------- |
| main.py |  59   | In this function I use the file name that is provided by the file_name parameter and save the |
|         |       | object to a binary file                                                                       |
+---------+-------+-----------------------------------------------------------------------------------------------+
| main.py |  70   | In this function I use the file name that is provided by the file_name parameter and read the |
|         |       | binary file into the game variable, then set up the opened game for the player                |
+---------+-------+-----------------------------------------------------------------------------------------------+

### Facilitate the addition of portability to your program via the definition and creation of portable objects

To make each of the objects portable, I added 2 methods to each: `json_dict` and `json_str`. These methods are used to export the object to JSON.  
`json_dict` exports the object's important instance variables to a dictionary that can be directly dumped into JSON. This method is called by `json_str`, but also by other objects that are composed of that object when they are being dumped.  
`json_str` calls `json_dict`, but then dumps that dict to JSON and returns that string.
These are JSON to facilitate future creation of a web version, to allow multiple people to play against each other over a network. Since JSON is ubiquitous for use in REST APIs on a network, I chose JSON over XML.

+-----------+-------+--------------------------------------------------------------------------------------------+
| File      | Line  | Description                                                                                |
| :-------- | :---: | :----------------------------------------------------------------------------------------- |
| card.py   |  70   | `json_dict` method for a CardValue                                                         |
+-----------+-------+--------------------------------------------------------------------------------------------+
| card.py   |  78   | `json_str` method for a CardValue                                                          |
+-----------+-------+--------------------------------------------------------------------------------------------+
| card.py   |  155  | `json_dict` method for a Card, calls the same method for CardValue                         |
+-----------+-------+--------------------------------------------------------------------------------------------+
| card.py   |  166  | `json_str` method for a Card                                                               |
+-----------+-------+--------------------------------------------------------------------------------------------+
| deck.py   |  84   | `json_dict` method for a Deck, calls the same method for Card                              |
+-----------+-------+--------------------------------------------------------------------------------------------+
| deck.py   |  101  | `json_str` method for a Deck                                                               |
+-----------+-------+--------------------------------------------------------------------------------------------+
| game.py   |  81   | `json_dict` method for a Game, calls the same method for Deck, HumanPlayer, BotPlayer      |
+-----------+-------+--------------------------------------------------------------------------------------------+
| game.py   |  99   | `json_str` method for a Game                                                               |
+-----------+-------+--------------------------------------------------------------------------------------------+
| hand.py   |  100  | `json_dict` method for a Hand, calls the same method for Card                              |
+-----------+-------+--------------------------------------------------------------------------------------------+
| hand.py   |  113  | `json_str` method for a Hand                                                               |
+-----------+-------+--------------------------------------------------------------------------------------------+
| player.py |  170  | `json_dict` method for a Player, calls the same method for Card and Hand                   |
+-----------+-------+--------------------------------------------------------------------------------------------+
| player.py |  186  | `json_str` method for a Player                                                             |
+-----------+-------+--------------------------------------------------------------------------------------------+
| player.py |  210  | `json_dict` method for a HumanPlayer, simply renames the object from player to humanPlayer |
+-----------+-------+--------------------------------------------------------------------------------------------+
| player.py |  221  | `json_str` method for a HumanPlayer                                                        |
+-----------+-------+--------------------------------------------------------------------------------------------+
| player.py |  255  | `json_dict` method for a HumanPlayer, simply renames the object from player to             |
|           |       | botPlayer and adds bot_difficulty                                                          |
+-----------+-------+--------------------------------------------------------------------------------------------+
| player.py |  267  | `json_str` method for a BotPlayer                                                          |
+-----------+-------+--------------------------------------------------------------------------------------------+

## Assumptions & Limitations

- The number of players cannot be changed
- The player always goes first
- Not all errors are handled with saving and opening a game
- If there is a tie, the game over dialog will not reflect that

## Next Steps & Possible Improvements

- Find a way to make Game more generic while allowing for different actions during a turn
- Implement more deck and game subclasses
- Improve the usability of the GUI
- Change the turn functions in GoFish to action functions
- Allow multiple human players
  - Hot seat game
  - network game

## Change log

- Rewrite the front end so that the project properly implements MVC
  - Make all the windows their own classes
  - pass functions for even handlers
- Make the window more dynamic to allow for different numbers of players
- Add a setup screen
- Add saving and opening games
- Remove some bugs from the game play