import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# Constants representing Sokoban elements with their associated colors
ELEMENTS = {
    'Player': ('R', 'blue'),
    'Wall': ('O', 'gray'),
    'Empty': (' ', 'white'),
    'Box': ('B', 'brown'),
    'Target': ('S', 'green'),
    'Player on Target': ('.', 'lightblue'),
    'Box on Target': ('*', 'purple')
}

class SokobanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sokoban Map Generator")

        # Applying a modern theme
        self.style = ttk.Style()
        self.style.theme_use("clam")  # You can change this to 'alt', 'default', or other themes

        # Custom style for ttk buttons
        self.style.configure("TButton", font=("Arial", 10), padding=6)
        self.style.configure("TLabel", font=("Arial", 10), padding=6)
        self.style.configure("TRadiobutton", font=("Arial", 10))
        
        self.selected_element = tk.StringVar(value='Empty')  # Default selected element
        self.cell_size = 40  # Default cell size
        self.grid_frame = None
        self.cells = []

        # UI Elements
        self.create_widgets()
        self.create_grid(5, 5)  # Initial grid size

    def create_widgets(self):
        # Frame for grid size, cell size, and buttons
        control_frame = ttk.Frame(self.root, padding="10 10 10 10")
        control_frame.pack(side=tk.TOP, padx=10, pady=5)

        # Grid size input
        ttk.Label(control_frame, text="Rows:").pack(side=tk.LEFT)
        self.row_entry = ttk.Entry(control_frame, width=3)
        self.row_entry.pack(side=tk.LEFT)
        self.row_entry.insert(0, "5")  # Default rows

        ttk.Label(control_frame, text="Cols:").pack(side=tk.LEFT)
        self.col_entry = ttk.Entry(control_frame, width=3)
        self.col_entry.pack(side=tk.LEFT)
        self.col_entry.insert(0, "5")  # Default columns

        # Cell size input
        ttk.Label(control_frame, text="Cell Size:").pack(side=tk.LEFT)
        self.size_entry = ttk.Entry(control_frame, width=3)
        self.size_entry.pack(side=tk.LEFT)
        self.size_entry.insert(0, "40")  # Default cell size

        # Button to apply the grid size change
        apply_button = ttk.Button(control_frame, text="Apply Grid Size", command=self.apply_grid_size)
        apply_button.pack(side=tk.LEFT, padx=(10, 0))

        # Frame for selecting elements
        element_frame = ttk.Frame(self.root, padding="10 10 10 10")
        element_frame.pack(side=tk.TOP)

        # Radio buttons for selecting elements
        for name in ELEMENTS:
            button = ttk.Radiobutton(element_frame, text=name, variable=self.selected_element, value=name)
            button.pack(side=tk.LEFT, padx=5)

        # Save button
        save_button = ttk.Button(self.root, text="Save Map", command=self.save_map)
        save_button.pack(side=tk.BOTTOM, pady=10)

    def create_grid(self, rows, cols):
        """ Create a grid of buttons based on the number of rows and columns. """
        if self.grid_frame:
            self.grid_frame.destroy()  # Remove the old grid

        self.grid_frame = ttk.Frame(self.root, padding="10 10 10 10")
        self.grid_frame.pack()

        self.cells = []
        for row in range(rows):
            row_cells = []
            for col in range(cols):
                button = tk.Button(self.grid_frame, bg=ELEMENTS['Empty'][1], width=self.cell_size // 10, height=self.cell_size // 20, relief=tk.FLAT)
                button.grid(row=row, column=col, padx=2, pady=2)

                # Assign row and column as attributes
                button.location = (row, col)

                # Bind mouse events for click and drag
                button.bind("<Button-1>", self.on_button_click)  # Click to start placing
                button.bind("<B1-Motion>", self.on_drag)  # Drag to place
                button.bind("<Enter>", self.on_hover)  # Hover for dragging placement

                row_cells.append(button)
            self.cells.append(row_cells)

    def apply_grid_size(self):
        """ Apply the grid size and cell size from the user input. """
        try:
            rows = int(self.row_entry.get())
            cols = int(self.col_entry.get())
            self.cell_size = int(self.size_entry.get())
        except ValueError:
            print("Invalid input. Please enter valid integers.")
            return

        self.create_grid(rows, cols)

    def on_button_click(self, event):
        """ Handle the initial click to place an element. """
        button = event.widget
        self.place_element(button)

    def on_drag(self, event):
        """ Handle dragging to place the selected element in cells. """
        widget = event.widget.winfo_containing(event.x_root, event.y_root)
        if isinstance(widget, tk.Button):
            self.place_element(widget)

    def on_hover(self, event):
        """ Handle hovering over a button to place an element while dragging. """
        if event.state & 0x0100:  # Check if left mouse button is pressed
            self.place_element(event.widget)

    def place_element(self, button):
        """ Place the selected element in the specified button. """
        selected = self.selected_element.get()
        button['text'] = ELEMENTS[selected][0]
        button['bg'] = ELEMENTS[selected][1]

    def save_map(self):
        """ Save the game map to a text file. """
        game_map = ""
        for row_cells in self.cells:
            line = "".join([cell['text'] if cell['text'] != '' else ' ' for cell in row_cells])
            game_map += line + "\n"

        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as f:
                f.write(game_map)
            print("Map saved to:", file_path)

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = SokobanGUI(root)
    root.mainloop()
