# _TeamGen_ – Universal Party Generator

A tool for generating a random, progression-viable party of six (or fewer) Pokémon for use in a Pokémon playthrough. 
Pokémon availability and game progression are respected in the final output. Customization options are 
available to curate the output further.

## Table of contents
1. [Introduction](#introduction)
2. [Currently supported games](#currently-supported-games)
3. [Installation](#installation)
4. [Usage](#usage)
5. [License](#license)

## Introduction
_TeamGen_ generates a prescribed party for use in a playthrough — to introduce an element of 
challenge or simply for team inspiration. 
This tool is **universal** in the sense that it maintains compatibility with _most_ generations of Pokémon, 
but also with romhacks that might contain the following (as long as the relevant game data files are added):
- New Pokémon
- New locations 
- Changes to existing game data (evolution methods, etc.)

## Currently supported games
- **Vanilla**
  - Pokémon Red
  - Pokémon Blue
- **Romhacks**
  - [Pokémon Solus RGB](https://github.com/Dechrissen/poke-solus-rgb)

## Installation

**Option 1** (Recommended): Linux / macOS

Prerequisites:
- Python 3.10+
- pip
- (Optional) venv

Steps:
- Clone this repository
- `cd teamgen`
- (Optional) Create a virtual environment first for less headache (`python -m venv .venv` then
`source .venv/bin/activate`)
- Install dependencies (`pip install -r requirements.txt`)
- Run with `python main.py`

**Option 2**: Windows – Prebuilt executable

- Download the latest .exe from [Releases](https://github.com/Dechrissen/teamgen/releases/latest)
- Run it directly

## Usage

TODO

## License

_TeamGen_ is licensed under the MIT License. See the `LICENSE` file for full details.
