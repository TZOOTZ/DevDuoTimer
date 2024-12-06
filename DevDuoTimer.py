# Disclaimer (resumido):
# Esta app facilita el Pair Programming clásico,
# asignando y rotando roles (Driver/Navigator) a intervalos regulares
# para mantener a ambos desarrolladores involucrados.

import tkinter as tk
import time

class PairTimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("TZOOTZ RESEARCH - Pair Timer")
        self.master.geometry("800x600")
        self.master.resizable(False, False)
        self.master.configure(bg="black")

        # Colores y fuentes
        self.font = ("Consolas", 10)
        self.fg = "#00FF00"
        self.bg = "black"
        self.font_large = ("Consolas", 20, "bold")
        self.font_timer = ("Consolas", 30, "bold")
        self.font_brand = ("Consolas", 12)

        # Variables
        self.dev1_name = tk.StringVar()
        self.dev2_name = tk.StringVar()
        self.time_minutes = tk.IntVar(value=15)
        self.time_remaining = None
        self.running = False
        self.current_driver = None
        self.current_navigator = None

        self.create_widgets()

    def create_widgets(self):
        # Header con ASCII TZOOTZ RESEARCH
        header_frame = tk.Frame(self.master, bg=self.bg)
        header_frame.place(relx=0.5, rely=0.05, anchor="n")

        ascii_logo = [
            "████████╗████3██╗ ██████╗  ██4███╗ ████0███╗████®██╗",
            "T Z O O T Z    R E S E A R C H"
        ]

        for i, line in enumerate(ascii_logo):
            lbl = tk.Label(header_frame, text=line, bg=self.bg, fg=self.fg, font=self.font)
            lbl.pack()

        subtitle = tk.Label(header_frame, text="Code Synergie Timer v.1", bg=self.bg, fg=self.fg, font=self.font)
        subtitle.pack(pady=5)

        # Disclaimer resumido en la interfaz
        disclaimer = tk.Label(header_frame, text="Efficient Role Driver/Navigator Rotation for Pair Programming ", bg=self.bg, fg=self.fg, font=self.font)
        disclaimer.pack(pady=5)

        # Contenedor principal
        main_frame = tk.Frame(self.master, bg=self.bg)
        main_frame.place(relx=0.5, rely=0.3, anchor="n")

        # Formulario de nombres y tiempo
        form_frame = tk.Frame(main_frame, bg=self.bg)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Developer A:", bg=self.bg, fg=self.fg, font=self.font).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(form_frame, textvariable=self.dev1_name, bg=self.bg, fg=self.fg, font=self.font, insertbackground=self.fg).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Developer B:", bg=self.bg, fg=self.fg, font=self.font).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(form_frame, textvariable=self.dev2_name, bg=self.bg, fg=self.fg, font=self.font, insertbackground=self.fg).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Time (min):", bg=self.bg, fg=self.fg, font=self.font).grid(row=2, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(form_frame, textvariable=self.time_minutes, bg=self.bg, fg=self.fg, font=self.font, insertbackground=self.fg, width=5).grid(row=2, column=1, padx=5, pady=5)

        # Botones
        btn_frame = tk.Frame(main_frame, bg=self.bg)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Start", command=self.start_timer, bg=self.bg, fg=self.fg, font=self.font).grid(row=0,column=0, padx=10)
        tk.Button(btn_frame, text="Stop", command=self.stop_timer, bg=self.bg, fg=self.fg, font=self.font).grid(row=0,column=1, padx=10)
        tk.Button(btn_frame, text="Close", command=self.master.quit, bg=self.bg, fg=self.fg, font=self.font).grid(row=0,column=2, padx=10)

        # Role Display
        self.role_label = tk.Label(main_frame, text="", bg=self.bg, fg=self.fg, font=self.font_large)
        self.role_label.pack(pady=20)

        # Timer (rojo, grande)
        self.timer_label = tk.Label(main_frame, text="00:00", bg=self.bg, fg="red", font=self.font_timer)
        self.timer_label.pack(pady=10)

        # Footer Branding Legal
        footer_frame = tk.Frame(self.master, bg=self.bg)
        footer_frame.place(relx=0.5, rely=0.95, anchor="s")

        footer_text = "©2024 TZOOTZ RESEARCH | Internal Use Only | No cosmic anomalies guaranteed"
        tk.Label(footer_frame, text=footer_text, bg=self.bg, fg=self.fg, font=self.font_brand).pack()

    def start_timer(self):
        if not self.dev1_name.get() or not self.dev2_name.get():
            return
        if self.time_minutes.get() <= 0:
            return
        self.running = True
        if self.current_driver is None and self.current_navigator is None:
            self.current_driver = self.dev1_name.get()
            self.current_navigator = self.dev2_name.get()
        self.update_roles_display()
        self.reset_time()
        self.countdown()

    def stop_timer(self):
        self.running = False

    def reset_time(self):
        self.time_remaining = self.time_minutes.get() * 60

    def countdown(self):
        if not self.running:
            return
        if self.time_remaining <= 0:
            self.swap_roles()
            self.reset_time()
        else:
            self.time_remaining -= 1
        self.update_timer_display()
        self.master.after(1000, self.countdown)

    def update_roles_display(self):
        role_text = f"DRIVER: {self.current_driver}\nNAVIGATOR: {self.current_navigator}"
        self.role_label.config(text=role_text)

    def update_timer_display(self):
        mins = self.time_remaining // 60 if self.time_remaining else 0
        secs = self.time_remaining % 60 if self.time_remaining else 0
        self.timer_label.config(text=f"{mins:02}:{secs:02}")

    def swap_roles(self):
        d, n = self.current_navigator, self.current_driver
        self.current_driver, self.current_navigator = d, n
        self.update_roles_display()


if __name__ == "__main__":
    # Disclaimer resumido al inicio del código (comentario)
    # Esta app facilita Pair Programming rotando roles Driver/Navigator en intervalos definidos.
    root = tk.Tk()
    app = PairTimerApp(root)
    root.mainloop()
