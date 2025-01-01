# UniTEA

Minimal game engine to play games[^1] on your text editor.
[^1]: we call these games "text-edit adventures", or TEAs.

## Install

```sh
python3 -m venv venv
source venv/bin/activate
```
You may have to install per-game dependencies; related information will be shown if needed.

## Run

```sh
source venv/bin/activate
python3 unitea/unitea.py game.txt
```

Then open `game.txt` with our sample minimal editor (or your text editor) and follow instructions:
```sh
python3 unitea/unitea-editor.py game.txt
```

## Add Game

To add a new game 'MyGame':
```bash
python3 unitea/unitea.py --create mygame
```
