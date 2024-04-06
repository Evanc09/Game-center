def main():
    import tkinter as tk
    from tkinter import Button
    import sys  
    
    
    try:
        from utils2 import main, TWO_player_Free_play, lives
    except ImportError as ie:
        print(f"Could not import(E: {ie})")
        sys.exit()
    root = tk.Tk()
    def destroy(root2):
            root.destroy()
    b1=Button(text="normal", command=lambda:[destroy(root), main(lives)])
    testButton = Button(text="Free Play", command=lambda:[destroy(root),TWO_player_Free_play.Free_play() ])
    testButton.pack()
    b1.pack()
    root.mainloop()
    
