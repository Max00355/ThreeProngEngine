About
=====


3ProngEngine is a graphical game engine created to make 2D game development in Python easier, and with less programming.

The engine was made specifically for 3 Prong Productions, my game development "company"

The engine includes collision detection, a 2D edit view, and multiple built in object modules such as:

* Basic player module
* Basic enemy module (they just walk back and forth at a set distance)
* Game inanimate objects (such as craits, or objects that can be pushed by the character)


The engine is extendable so creating your own game objects, such as "smarter" enemies, can be as easy as defining a JSON file and writing some Python.


Why?
====

Developing a game in the early stage is a gruling task. It is not fun. The actual task of creating game logic, and the "fun stuff" comes much later in the development of a game. I found that I have repeated code a lot from other projects for the collision detection and character/object movement. I wanted to remove this step all together so that a develper could jump right into the game development stage of game making. The fun part. Developing games, especially in Python, should be fun, so that's my goal.


I also wanted to make a framework that would compile to an EXE, via PyInstaller, painlessly.
