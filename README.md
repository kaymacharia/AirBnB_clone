AIRBNB PROJECT - THE CONSOLE
The first part of the project that aims at creating a fully working website.
The project clones the airbnb.com website.
The Console creates a command interpreter
to manipulate data without a visual interface.
It is just like Shell. It is perfect for development and debugging.
The Console will:
	create your data model
	manage(create, update, destroy, etc) objects via a console
	/ command interpreter
	store and persist objects to a file(JSON file)

The first piece is to manipulate a powerful storage system.
This storage engine will give us an abstraction between “My object” and
“How they are stored and persisted”.
This means: from your console code(the command interpreter itself) and from
the front-end and RestAPI you will build later,
you won’t have to pay attention(take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage
easily without updating all of your codebase.
