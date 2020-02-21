0x00. AirBnB clone - The console
------------------------------------
This is the first step towards building our first
full web application: "the AirBnB clone"

The tasks to be performed are:
-------------------------------------------
- Put in place a parent class (called BaseModel)
to take care of the initialization,
serialization and deserialization of our future
instances
- Create a simple flow of serialization/deserialization:
Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB
(User, State, City, Place…) that inherit from BaseModel
- Create the first abstracted storage engine of
the project:File storage.
- Create all unittests to validate all our classes
and storage engine

Command interpreter:
----------------------
A command interpreter to manipulate data without
a visual interface, like in a Shell
(perfect for development and debugging)

The console
------------------------------------------
- Create a data model.
- Manage (create, update, destroy, etc) objects via
a console / command interpreter.
- Store and persist objects to a file (JSON file)
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

#### Create Command

```sh
(hbnb) create <Model_name>
```

#### Update Command

```sh
(hbnb) update <Model_name> <id> <attribute name> <value>
```

#### Show Command

```sh
(hbnb) (hbnb) show <Model_name> <id>
```

#### Create Command

```sh
(hbnb) update <Model_name> <id> <attribute name> <value>
```

#### Create Command

```sh
(hbnb) update <Model_name> <id> <attribute name> <value>
```

#### Create Command

```sh
(hbnb) update <Model_name> <id> <attribute name> <value>
```

#### Create Command

```sh
(hbnb) update <Model_name> <id> <attribute name> <value>
```


examples
------------------------------------------