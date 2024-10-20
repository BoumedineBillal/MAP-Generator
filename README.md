# Sokoban Map Generator

![Sokoban Map Generator](images/sokoban_gui.png)

## Description

This is a Python-based graphical user interface (GUI) application for creating and generating Sokoban game maps. The application allows users to design custom Sokoban levels using different elements like the player, walls, boxes, and targets, and then save these maps as text files.

The GUI is built using the `tkinter` library, and users can interactively design maps by clicking and dragging elements on the grid.

## Features

- **Grid Customization**: Define the number of rows, columns, and the cell size of the map grid.
- **Element Placement**: Place elements such as the Player, Walls, Boxes, and Targets on the grid via simple click or drag actions.
- **Save Map**: Save the created Sokoban map to a text file in a simple format for future use.

## Requirements

- Python 3.x
- `tkinter` library (included with most Python installations)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/sokoban-map-generator.git
    ```

2. Navigate to the project directory:
    ```bash
    cd sokoban-map-generator
    ```

3. Install any dependencies (if required):
    ```bash
    pip install tk
    ```

## How to Run

1. Open a terminal in the project directory.
2. Run the Python script:
    ```bash
    python sokoban_gui.py
    ```

3. The graphical interface will appear, allowing you to customize the grid size, place elements, and save the map.

## How to Use

1. **Customize Grid**:
   - Enter the number of rows and columns.
   - Adjust the cell size as needed.
   - Click "Apply Grid Size" to generate the grid.

2. **Place Elements**:
   - Select an element (Player, Wall, Box, etc.) via the radio buttons.
   - Click on a cell or drag the mouse over multiple cells to place elements.

3. **Save Map**:
   - Once done, click "Save Map" to export the map as a text file.

## Example

Here is an example of a generated Sokoban map saved as a text file:

```
OOOOOOOOOOOOOOOOOOOOOOOOO
O     R                 O
O           B          SO
 OO                OOOOOO
  O   B   B       O      
  O               O      
  O     B    S  S OOOOO  
 OO                    O 
 O                      O
 O       *              O
 OO                    OO
  OOOOOOO      S       O 
        OOO           OO 
          OOOOOOOOOOOOO  
```

## Screenshots

Here’s a screenshot of the application in action:

![Sokoban Screenshot](images/sokoban_screenshot.png)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
