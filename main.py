import tkinter as tk
import logic as lg
import assembler as assem
import vm as VM

# def change_pixel(x, y):
#     canvas.create_rectangle(x, y, x+1, y+1, fill="red")  # Change pixel color to red


# root = tk.Tk()
# canvas = tk.Canvas(root, width=512, height=256)
# canvas.pack()

# for x in range(256):
#     change_pixel(2*x, x)
#     pass

# # Start the main event loop
# root.mainloop()



cmp = lg.hack_computer()

VM_CODE = [
    "push constant 101", 
    "pop static 0",

    "push constant 1", 
    "pop static 1",

    "push constant 0",
    "pop static 2",

    "label loop", 

    "push static 2", 
    "push static 1", 
    "add", 
    "pop static 2",


    "push static 1", 
    "push constant 1",
    "add", 
    "pop static 1",

    "push static 1", 
    "push static 0",
    "lt", 
    "if-goto loop"
]
assembly_code = VM.convert_VM_code_to_assembly(VM_CODE)
cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))

cmp.do_n_operations(False, 9000)
cmp.show_data_memory(16, 20)









