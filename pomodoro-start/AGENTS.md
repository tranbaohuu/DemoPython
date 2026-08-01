# AGENTS.md — Pomodoro Timer Project Guide

## Project Overview
A beginner Python Pomodoro timer app built with **Tkinter**. The project is a single-file starter (`main.py`) with a tomato image asset (`tomato.png`). The structure follows a teaching/course pattern where logic sections are scaffolded via comment headers.

## Architecture & Structure
```
main.py        # All app logic: constants, timer, countdown, UI
tomato.png     # Tomato image displayed on the canvas (200×224 px)
```

### Section Layout (comment-delimited in `main.py`)
The file is intentionally divided into four named sections, in order:
1. **CONSTANTS** — Color hex codes, font name, and Pomodoro durations
2. **TIMER RESET** — Function to reset timer state and UI
3. **TIMER MECHANISM** — Pomodoro session logic (work → short break → long break cycling)
4. **COUNTDOWN MECHANISM** — Recursive countdown using `window.after()`
5. **UI SETUP** — `Tk` window, `Canvas` with tomato image, labels, and buttons

Do **not** reorganize these sections — they mirror a course scaffold structure.

## Key Constants (`main.py`)
```python
WORK_MIN = 25        # Work session length in minutes
SHORT_BREAK_MIN = 5  # Short break after each work session
LONG_BREAK_MIN = 20  # Long break after every 4th work session
FONT_NAME = "Courier"
YELLOW = "#f7f5dd"   # Window background color
```

## UI Conventions
- All UI is drawn on a `Canvas` (200×224), not with standard widget layout.
- Timer text is placed via `canvas.create_text(103, 130, ...)` — coordinates are fixed to align with `tomato.png`.
- Window padding: `padx=100, pady=50`.
- Colors reference the named constants (`PINK`, `RED`, `GREEN`, `YELLOW`) — do not use raw hex strings elsewhere.

## Running the App
```bash
python main.py
```
Requires Python 3 with Tkinter (bundled with standard macOS/Windows Python installs).  
No external dependencies or `requirements.txt`.

## Implementing Missing Features
The timer logic stubs are empty — expected implementations:
- **Countdown**: use `window.after(1000, callback)` for 1-second ticks; format time as `f"{minutes:02d}:{seconds:02d}"`.
- **Timer mechanism**: track session count to alternate work/break; update a label with session type using `PINK`/`RED`/`GREEN`.
- **Reset**: cancel pending `after` callbacks via `window.after_cancel(timer)`; clear checkmarks label.
- **Start/Reset buttons**: add below canvas using `Button` widget, no `pack` padding needed beyond defaults.

