0x00. AirBnB clone - The console
------------------------------------
This is the first step towards building our first
full web application: "the AirBnB clone"

the tasks to be performed are:
-------------------------------------------
-put in place a parent class (called BaseModel)
to take care of the initialization,
serialization and deserialization of our future
instances
-create a simple flow of serialization/deserialization:
Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB
(User, State, City, Place…) that inherit from BaseModel
-create the first abstracted storage engine of
the project:File storage.
-create all unittests to validate all our classes
and storage engine

command interpreter:
----------------------
A command interpreter to manipulate data without
a visual interface, like in a Shell
(perfect for development and debugging)

The console
------------------------------------------
-to create a data model
-manage (create, update, destroy, etc) objects via
a console / command interpreter
-store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage
system. This storage engine will give us
an abstraction between “My object” and
“How they are stored and persisted”
This abstraction will also allow you to
change the type of storage easily without updating
all of our codebase

How to start it
---------------------------------------------------
cmd: ./console
![console](https://i.imgur.com/Cacz3dg.png)
how to use it
------------------------


examples
------------------------------------------