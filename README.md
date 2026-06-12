# Contact Book CLI

A command-line contact management app built with Python. Store, search, and manage contacts with persistent JSON storage so your data is saved between sessions.

## Features

- Add contacts with name, phone number, email, and category (friends, family, work)
- View all contacts in a formatted display
- Search contacts by name, email, or category with partial matching
- Delete contacts by name
- Persistent storage — contacts are saved to JSON and loaded automatically on startup

## How to Run

Make sure you have Python 3 installed, then:

```bash
python3 main.py
```

## Project Structure

contact-book/
main.py        — Entry point, menu loop, user interaction
models.py      — Contact and ContactBook classes
storage.py     — JSON save and load functions
data.json      — Auto-generated data file

## Built With

- Python 3
- Dataclasses for structured data
- JSON for persistent storage
- No external libraries

## What I Learned

This was my second Python project, building on the finance tracker. Key things I learned:

- Object-oriented programming with classes, composition, and dataclasses
- Separating code into multiple files (models, storage, main)
- Converting between objects and dictionaries for JSON serialization
- Loading saved data back into class instances on startup
- Project structure and imports