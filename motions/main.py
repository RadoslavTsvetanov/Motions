import tkinter as tk

def create_dot_window(x, y):
    # Create a Tkinter window without borders
    dot_window = tk.Tk()
    dot_window.overrideredirect(True)
    dot_window.attributes("-topmost", True)
    dot_window.geometry(f"+{x}+{y}")

    # Create a canvas to draw on
    canvas = tk.Canvas(dot_window, bg="black", highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    # Draw a red dot at the center of the canvas
    dot_size = 10
    canvas.create_oval(canvas.winfo_reqwidth() // 2 - dot_size // 2, 
                       canvas.winfo_reqheight() // 2 - dot_size // 2,
                       canvas.winfo_reqwidth() // 2 + dot_size // 2, 
                       canvas.winfo_reqheight() // 2 + dot_size // 2,
                       fill="red")

# Define coordinates for the dot windows
dot_window_coordinates = [
    (100, 100),
    (200, 200),
    (300, 300)
]

# Function to create dot windows one by one with a delay
def create_dot_windows_slowly(coordinates, index):
    if index < len(coordinates):
        x, y = coordinates[index]
        create_dot_window(x, y)
        # Schedule the next dot window creation after 1000 milliseconds (1 second)
        root.after(1000, create_dot_windows_slowly, coordinates, index + 1)

# Create the root Tkinter window
root = tk.Tk()

# Start creating dot windows with a delay
create_dot_windows_slowly(dot_window_coordinates, 0)

# Run the Tkinter event loop
root.mainloop()
