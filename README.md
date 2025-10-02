# Typing Speed Test

A GUI application to test and improve typing speed built with Python's Tkinter library.

## Features

- **Real-time typing analysis** with live WPM and accuracy tracking
- **Visual feedback** with color-coded correct/incorrect characters
- **Detailed statistics** including keystrokes, backspaces, and accuracy
- **Multiple test passages** with random selection
- **60-second timed tests** with countdown timer

## Showcase

**Main UI**

<img width="792" height="624" alt="typingtestui" src="https://github.com/user-attachments/assets/d1cfd7e4-d1ad-4fde-8151-1a544f4f89ef" />

**During Test UI**

<img width="797" height="628" alt="duringtypingtestui" src="https://github.com/user-attachments/assets/80d9162c-cfa6-4c0c-a00b-bc96e241951c" />

**Results UI**

<img width="396" height="375" alt="typingtestresultsui" src="https://github.com/user-attachments/assets/bd2bf7d0-c3c6-4599-93c1-c4dc99bdcc89" />




## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd typing_speed_test
```

2. Run the application:
```bash
python src/main.py
```

## Usage

1. Click **Start Test** to begin a typing challenge
2. Type the displayed passage in the text area
3. Watch your real-time WPM and accuracy stats
4. Complete the passage or wait for the timer to finish
5. View detailed results in the popup summary
6. Use **Reset** to clear and **Change Passage** for variety

## Project Structure

```
src/
├── main.py          # Application entry point
├── ui.py            # GUI components and layout
├── controller.py    # Event handling and coordination
├── logic.py         # Core typing test logic and calculations
├── passages.py      # Test passage management
└── config.py        # UI styling and configuration
```

## Requirements

- Python 3.x
- Tkinter (included with Python)

## License

MIT License - see LICENSE file for details
