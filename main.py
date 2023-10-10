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
                    do Screen.drawPixel(32, 0);
                    do Screen.drawPixel(32, 1);
                    do Screen.drawPixel(32, 2);
                    do Screen.drawPixel(32, 3);
                    do Screen.drawPixel(32, 4);
                    do Screen.drawPixel(32, 5);
                    do Screen.drawPixel(32, 6);
                    do Screen.drawPixel(32, 7);
                    do Screen.drawPixel(32, 8);
                    do Screen.drawPixel(32, 9);
                    do Screen.drawPixel(32, 10);
                    do Screen.drawPixel(32, 11);
                    do Screen.drawPixel(32, 12);
                    do Screen.drawPixel(32, 13);
                    do Screen.drawPixel(32, 16);
                    do Screen.drawPixel(32, 17);
                    do Screen.drawPixel(32, 18);
                    do Screen.drawPixel(32, 19);


                    return 0;
                }
                
            }

        """
cmp = lg.hack_computer()

vm_code = sa.generate_vm_code_with_bootstrap(code)      
assembly_code = vm.convert_VM_code_to_assembly(vm_code)
cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))






def update_pixels():
    cmp.do_n_operations(False, 10000)
    pixels = cmp.get_data_memory(16384, 16384 + (32*256))
    index = 0
    for x in range(8192):
        for y in range(16):
            col = index
            row = int(x/32)
            
            if (pixels[x][y] == "1"):
                img.put("#deeb34", (col, row))
            else:
                img.put("#000000", (col,row))
            if (index == 511):
                index = 0
            else:
                index+=1

    
    
    window.after(1000, update_pixels)

window.after(1000, update_pixels)
window.mainloop()









# def check_speed():
#     start_time = time.time()
#     cmp.do_n_operations(False, 100000)

#     end_time = time.time()

#     elapsed_time = end_time - start_time

#     print(f"Elapsed time: {elapsed_time} seconds")


# check_speed()






