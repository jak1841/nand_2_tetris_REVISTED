import tkinter as tk


def change_pixel(x, y):
    
    canvas.create_rectangle(x, y, x+1, y+1, fill="red")  # Change pixel color to red

root = tk.Tk()
canvas = tk.Canvas(root, width=512, height=256)
canvas.pack()

for x in range(256):
    change_pixel(2*x, x)
    pass

# Start the main event loop
root.mainloop()



