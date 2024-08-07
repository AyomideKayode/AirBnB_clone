# 0x00. AirBnB clone - The console

![Air-BnB-Project](./technicals/HBNB.png)

## [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=500&size=28&pause=1000&repeat=false&width=435&lines=Table+of+Contents%3A)](https://git.io/typing-svg)

- [Project Description](#project-description)
- [Description of the command interpreter](#description-of-the-command-interpreter)
- [How to start it, How to use it](#how-to-start-it-how-to-use-it)
- [Contributors](#contributors)
- [Usage](#usage)

<!-- ubuntu -->
<a href="https://ubuntu.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A" alt="Suite CRM"></a> 
<!-- python-->
<a href="https://www.python.org" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Python&color=FFD43B&logo=python&logoColor=3776AB&labelColor=2F333A" alt="python"></a> </a>
<!-- vim -->
<a href="https://www.vim.org/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Vim&color=019733&logo=Vim&logoColor=019733&labelColor=2F333A" alt="Suite CRM"></a>
<!-- vs code -->
<a href="https://code.visualstudio.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Visual%20Studio%20Code&color=5C2D91&logo=Visual%20Studio%20Code&logoColor=5C2D91&labelColor=2F333A" alt="Suite CRM"></a>
<!-- git -->
<a href="https://git-scm.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Git&color=F05032&logo=Git&logoColor=F05032&labelColor=2F333A" alt="git distributed version control system"></a>
<!-- github -->
<a href="https://github.com" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="Github"></a>

## Project Description

This is the first step towards building a full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration

Each task is linked and will help you to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

## Description of the command interpreter

- Its exactly the same as the shell but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

  - Create a new object (ex: a new User or a new Place)
  - Retrieve an object from a file, a database etc
  - Do operations on objects (count, compute stats, etc)
  - Update attributes of an object
  - Destroy an object

## How to start it, How to use it

- **Execution**
  - Your shell should work like this in interactive mode:

```sh
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
Amenity    City  Place   State  all    create   help  show
BaseModel  EOF   Review  User   count  destroy  quit  update

(hbnb)
(hbnb)
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project(simple shell) in C)

```sh
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
Amenity    City  Place   State  all    create   help  show
BaseModel  EOF   Review  User   count  destroy  quit  update
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

All tests should also pass in non-interactive mode:

```bash
echo "python3 -m unittest discover tests" | bash
```

## Usage

- Start the console in interactive mode:

```bash
$ ./console.py
(hbnb)
```

- Use help to see the available commands:

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

- Quit the console:

```bash
(hbnb) quit
$
```

## Contributors

- The following people contributed to this repository.
  - Ayomide Kayode
  - Ifeoluwa Hughes
