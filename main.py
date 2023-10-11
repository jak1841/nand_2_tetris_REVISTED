import logic as lg

import assembler as assem
import vm 
import syntax_analayzer as sa



import time
from random import randint

from tkinter import Tk, Canvas, PhotoImage

WIDTH, HEIGHT = 512, 256

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
canvas.pack()
img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")


code = """
            class Main {
                static int ram, ram1, ram2, ram3;
                function void main() {
                    do Main.draw_cross();
                    return 0;
                }

                function void draw_cross() {
                    
                    do Screen.drawRectangle(0, 128-16, 511, 128+16);
                    do Screen.drawRectangle(256-16, 0, 256+16, 255);

                    return 0;
                }
                
            }

        """
cmp = lg.hack_computer()

vm_code = sa.generate_vm_code_with_bootstrap(code)      
assembly_code = vm.convert_VM_code_to_assembly(vm_code)
cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))






def update_pixels():
    cmp.do_n_operations(False, 300000)
    pixels = cmp.get_data_memory(16384, 16384 + (32*256))
    index = 0
    for x in range(8192):
        for y in range(16):
            reverse_index = 15 - y
            col = index
            row = int(x/32)
            
            if (pixels[x][reverse_index] == "1"):
                img.put("#deeb34", (col, row))
            else:
                img.put("#000000", (col,row))
            if (index == 511):
                index = 0
            else:
                index+=1

    
    
    window.after(100, update_pixels)

window.after(100, update_pixels)
window.mainloop()









# def check_speed():
#     start_time = time.time()
#     cmp.do_n_operations(False, 100000)

#     end_time = time.time()

#     elapsed_time = end_time - start_time

#     print(f"Elapsed time: {elapsed_time} seconds")


# check_speed()






