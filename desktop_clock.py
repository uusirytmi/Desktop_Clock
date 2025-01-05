import tkinter as tk
from datetime import datetime

class SimpleDesktopClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('シンプルデスクトップ時計')
        self.root.geometry('300x150+500+300')
        self.root.attributes('-topmost', True)

        self.label = tk.Label(
            self.root,
            font=('Arial', 40),
            background='black',
            foreground='white'
        )
        self.label.pack(fill='both', expand=True)

        self.update_time()

    def update_time(self):
        current_time = datetime.now().strftime('%H:%M:%S')
        self.label.config(text=current_time)
        self.label.after(1000, self.update_time)

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    clock = SimpleDesktopClock()
    clock.run()
