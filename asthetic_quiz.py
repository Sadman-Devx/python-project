import tkinter as tk
from tkinter import font
import random

class AestheticQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Quiz Time ✨")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        
        # Dark aesthetic color palettes
        self.themes = {
            "midnight": {
                "bg": "#0D1117", "card": "#161B22", "accent": "#58A6FF",
                "text": "#E6EDF3", "correct": "#238636", "wrong": "#DA3633",
                "button": "#1F6FEB", "button_hover": "#388BFD", "glow": "#58A6FF"
            },
            "purple_haze": {
                "bg": "#13111C", "card": "#1E1B2E", "accent": "#A855F7",
                "text": "#E9E4F0", "correct": "#22C55E", "wrong": "#EF4444",
                "button": "#9333EA", "button_hover": "#A855F7", "glow": "#C084FC"
            },
            "cyber_pink": {
                "bg": "#170D14", "card": "#231A20", "accent": "#FF2E97",
                "text": "#FFE4F1", "correct": "#00FF88", "wrong": "#FF4757",
                "button": "#FF0080", "button_hover": "#FF2E97", "glow": "#FF79C6"
            },
            "ocean_depth": {
                "bg": "#0A1628", "card": "#112240", "accent": "#64FFDA",
                "text": "#CCD6F6", "correct": "#64FFDA", "wrong": "#FF6B6B",
                "button": "#0EA5E9", "button_hover": "#38BDF8", "glow": "#64FFDA"
            },
            "aurora": {
                "bg": "#0F0F1A", "card": "#1A1A2E", "accent": "#00D9FF",
                "text": "#EAEAEA", "correct": "#00FF87", "wrong": "#FF5757",
                "button": "#6C63FF", "button_hover": "#8B83FF", "glow": "#00D9FF"
            },
            "blood_moon": {
                "bg": "#1A0A0A", "card": "#2D1515", "accent": "#FF4444",
                "text": "#FFDDDD", "correct": "#44FF88", "wrong": "#FF4444",
                "button": "#CC0000", "button_hover": "#FF2222", "glow": "#FF6666"
            }
        }
        
        self.current_theme = "midnight"
        self.colors = self.themes[self.current_theme]
        
        self.quiz_data = [
            {
                "question": "What is the capital of France?",
                "options": ["London", "Berlin", "Paris", "Madrid"],
                "answer": 2
            },
            {
                "question": "What is 2 + 2?",
                "options": ["3", "4", "5", "6"],
                "answer": 1
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Earth", "Mars", "Jupiter", "Saturn"],
                "answer": 2
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "options": ["Charles Dickens", "Shakespeare", "Mark Twain", "Jane Austen"],
                "answer": 1
            },
            {
                "question": "What is the boiling point of water in Celsius?",
                "options": ["90°C", "100°C", "110°C", "120°C"],
                "answer": 1
            }
        ]
        
        self.current_question = 0
        self.score = 0
        self.selected_option = None
        self.option_buttons = []
        self.floating_elements = []
        self.glow_items = []
        
        self.setup_ui()
        self.create_floating_elements()
        self.animate_floating()
        self.show_welcome_screen()
    
    def setup_ui(self):
        self.root.configure(bg=self.colors["bg"])
        
        # Main canvas for animations
        self.canvas = tk.Canvas(
            self.root, width=600, height=700,
            bg=self.colors["bg"], highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True)
        
        # Container frame on canvas
        self.container = tk.Frame(self.canvas, bg=self.colors["bg"])
        self.canvas.create_window(300, 350, window=self.container)
    
    def create_floating_elements(self):
        # Clear existing elements
        for elem in self.floating_elements:
            self.canvas.delete(elem["id"])
        self.floating_elements = []
        
        symbols = ["✦", "✧", "⋆", "˚", "°", "•", "◦", "○", "◯", "✴", "✳", "❋"]
        for _ in range(25):
            x = random.randint(20, 580)
            y = random.randint(20, 680)
            symbol = random.choice(symbols)
            size = random.randint(8, 18)
            speed = random.uniform(0.2, 0.8)
            direction = random.choice([-1, 1])
            alpha = random.choice(["", ""])  # Simulated transparency via color
            element = self.canvas.create_text(
                x, y, text=symbol, font=("Arial", size),
                fill=self.colors["accent"]
            )
            self.floating_elements.append({
                "id": element, "speed": speed, "direction": direction,
                "base_x": x, "offset": 0, "y_speed": random.uniform(0.1, 0.4)
            })
    
    def animate_floating(self):
        for elem in self.floating_elements:
            # Horizontal sway
            elem["offset"] += elem["speed"] * elem["direction"]
            if abs(elem["offset"]) > 25:
                elem["direction"] *= -1
            
            coords = self.canvas.coords(elem["id"])
            if coords:
                new_x = elem["base_x"] + elem["offset"]
                new_y = coords[1] - elem["y_speed"]
                
                if new_y < -20:
                    new_y = 720
                    elem["base_x"] = random.randint(20, 580)
                    new_x = elem["base_x"]
                
                self.canvas.coords(elem["id"], new_x, new_y)
        
        self.root.after(50, self.animate_floating)
    
    def clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()
        self.option_buttons = []
    
    def show_welcome_screen(self):
        self.clear_container()
        
        # Glowing title effect
        title_frame = tk.Frame(self.container, bg=self.colors["bg"])
        title_frame.pack(pady=(50, 10))
        
        # Shadow/glow text
        title_shadow = tk.Label(
            title_frame, text="✦ Quiz Time ✦",
            font=("Helvetica", 38, "bold"), bg=self.colors["bg"],
            fg=self.colors["glow"]
        )
        title_shadow.place(x=2, y=2)
        
        title = tk.Label(
            title_frame, text="✦ Quiz Time ✦",
            font=("Helvetica", 38, "bold"), bg=self.colors["bg"],
            fg=self.colors["text"]
        )
        title.pack()
        self.pulse_animation(title, title_shadow)
        
        subtitle = tk.Label(
            self.container, text="~ Test your knowledge ~",
            font=("Helvetica", 13), bg=self.colors["bg"],
            fg=self.colors["accent"]
        )
        subtitle.pack(pady=(5, 40))
        
        # Theme selector
        theme_frame = tk.Frame(self.container, bg=self.colors["bg"])
        theme_frame.pack(pady=20)
        
        tk.Label(
            theme_frame, text="⟡ Choose your aesthetic ⟡",
            font=("Helvetica", 11), bg=self.colors["bg"],
            fg=self.colors["text"]
        ).pack(pady=(0, 15))
        
        theme_buttons_frame = tk.Frame(theme_frame, bg=self.colors["bg"])
        theme_buttons_frame.pack()
        
        theme_icons = {
            "midnight": ("🌙", "Midnight"),
            "purple_haze": ("🔮", "Purple"),
            "cyber_pink": ("💗", "Cyber"),
            "ocean_depth": ("🌊", "Ocean"),
            "aurora": ("🌌", "Aurora"),
            "blood_moon": ("🩸", "Blood")
        }
        
        row1 = tk.Frame(theme_buttons_frame, bg=self.colors["bg"])
        row1.pack(pady=5)
        row2 = tk.Frame(theme_buttons_frame, bg=self.colors["bg"])
        row2.pack(pady=5)
        
        for i, (theme_name, (icon, label)) in enumerate(theme_icons.items()):
            parent = row1 if i < 3 else row2
            btn_frame = tk.Frame(parent, bg=self.colors["bg"])
            btn_frame.pack(side="left", padx=8)
            
            btn = tk.Button(
                btn_frame, text=icon, font=("Arial", 22),
                width=2, height=1, bd=0, cursor="hand2",
                bg=self.themes[theme_name]["card"],
                fg="white",
                activebackground=self.themes[theme_name]["accent"],
                command=lambda t=theme_name: self.change_theme(t)
            )
            btn.pack()
            
            lbl = tk.Label(
                btn_frame, text=label, font=("Helvetica", 8),
                bg=self.colors["bg"], fg=self.colors["accent"]
            )
            lbl.pack(pady=(2, 0))
            
            self.add_hover_effect(btn, self.themes[theme_name]["card"], 
                                  self.themes[theme_name]["accent"])
        
        # Start button with glow effect
        start_frame = tk.Frame(self.container, bg=self.colors["bg"])
        start_frame.pack(pady=40)
        
        start_btn = tk.Button(
            start_frame, text="⟡  Begin Quest  ⟡",
            font=("Helvetica", 16, "bold"), bg=self.colors["button"],
            fg="white", padx=35, pady=12, bd=0, cursor="hand2",
            activebackground=self.colors["button_hover"],
            activeforeground="white", command=self.start_quiz
        )
        start_btn.pack()
        self.add_hover_effect(start_btn, self.colors["button"], self.colors["button_hover"])
        self.glow_button(start_btn)
    
    def glow_button(self, button, intensity=0, direction=1):
        if not button.winfo_exists():
            return
        # Simulated glow pulsing
        self.root.after(100, lambda: self.glow_button(button, intensity, direction))
    
    def change_theme(self, theme_name):
        self.current_theme = theme_name
        self.colors = self.themes[theme_name]
        self.root.configure(bg=self.colors["bg"])
        self.canvas.configure(bg=self.colors["bg"])
        self.container.configure(bg=self.colors["bg"])
        
        # Update floating elements color
        for elem in self.floating_elements:
            self.canvas.itemconfig(elem["id"], fill=self.colors["accent"])
        
        self.show_welcome_screen()
    
    def pulse_animation(self, widget, shadow=None, growing=True, size=38):
        if not widget.winfo_exists():
            return
        
        if growing:
            size += 1
            if size >= 42:
                growing = False
        else:
            size -= 1
            if size <= 38:
                growing = True
        
        widget.configure(font=("Helvetica", size, "bold"))
        if shadow and shadow.winfo_exists():
            shadow.configure(font=("Helvetica", size, "bold"))
        
        self.root.after(120, lambda: self.pulse_animation(widget, shadow, growing, size))
    
    def add_hover_effect(self, button, normal_color, hover_color):
        def on_enter(e):
            button.configure(bg=hover_color)
        def on_leave(e):
            button.configure(bg=normal_color)
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
    
    def start_quiz(self):
        self.current_question = 0
        self.score = 0
        self.show_question()
    
    def show_question(self):
        self.clear_container()
        self.selected_option = None
        
        q = self.quiz_data[self.current_question]
        
        # Progress bar with glow
        progress_frame = tk.Frame(self.container, bg=self.colors["bg"])
        progress_frame.pack(fill="x", pady=(30, 10), padx=30)
        
        progress_bg = tk.Frame(progress_frame, bg=self.colors["card"], height=6)
        progress_bg.pack(fill="x")
        
        progress_pct = (self.current_question) / len(self.quiz_data)
        if progress_pct > 0:
            progress_fill = tk.Frame(progress_bg, bg=self.colors["accent"], height=6)
            progress_fill.place(x=0, y=0, relwidth=progress_pct)
        
        # Question counter
        counter = tk.Label(
            self.container,
            text=f"Question {self.current_question + 1} of {len(self.quiz_data)}",
            font=("Helvetica", 11), bg=self.colors["bg"], fg=self.colors["accent"]
        )
        counter.pack(pady=(10, 20))
        
        # Question card with border glow effect
        card_border = tk.Frame(self.container, bg=self.colors["accent"], padx=2, pady=2)
        card_border.pack(fill="x", padx=25, pady=10)
        
        card = tk.Frame(card_border, bg=self.colors["card"], padx=30, pady=25)
        card.pack(fill="both")
        
        question_label = tk.Label(
            card, text=q["question"], font=("Helvetica", 17),
            bg=self.colors["card"], fg=self.colors["text"],
            wraplength=450, justify="center"
        )
        question_label.pack()
        
        # Options
        options_frame = tk.Frame(self.container, bg=self.colors["bg"])
        options_frame.pack(pady=25)
        
        for i, option in enumerate(q["options"]):
            btn = tk.Button(
                options_frame, text=f"  {option}  ", font=("Helvetica", 13),
                width=28, pady=12, bd=0, cursor="hand2",
                bg=self.colors["card"], fg=self.colors["text"],
                activebackground=self.colors["accent"],
                activeforeground=self.colors["bg"],
                command=lambda idx=i: self.select_option(idx)
            )
            btn.pack(pady=8)
            self.option_buttons.append(btn)
            self.add_hover_effect(btn, self.colors["card"], self.colors["accent"])
            
            # Fade-in animation
            self.root.after(i * 150, lambda b=btn: self.fade_in(b))
        
        # Submit button
        self.submit_btn = tk.Button(
            self.container, text="✦  Submit  ✦", font=("Helvetica", 14, "bold"),
            bg=self.colors["button"], fg="white", padx=30, pady=10,
            bd=0, cursor="hand2", state="disabled",
            activebackground=self.colors["button_hover"],
            command=self.check_answer
        )
        self.submit_btn.pack(pady=20)
        
        # Score display
        score_label = tk.Label(
            self.container, text=f"✧ Score: {self.score} ✧",
            font=("Helvetica", 13), bg=self.colors["bg"], fg=self.colors["accent"]
        )
        score_label.pack()
    
    def fade_in(self, widget):
        if widget.winfo_exists():
            widget.configure(state="normal")
    
    def select_option(self, index):
        self.selected_option = index
        
        for i, btn in enumerate(self.option_buttons):
            if i == index:
                btn.configure(bg=self.colors["accent"], fg=self.colors["bg"])
            else:
                btn.configure(bg=self.colors["card"], fg=self.colors["text"])
        
        self.submit_btn.configure(state="normal")
        self.add_hover_effect(self.submit_btn, self.colors["button"], self.colors["button_hover"])
    
    def check_answer(self):
        q = self.quiz_data[self.current_question]
        correct = self.selected_option == q["answer"]
        
        # Disable all buttons
        for btn in self.option_buttons:
            btn.configure(state="disabled", cursor="")
        
        if correct:
            self.score += 1
            self.option_buttons[self.selected_option].configure(
                bg=self.colors["correct"], fg="white"
            )
            self.show_feedback("✦ Correct! ✦", True)
        else:
            self.option_buttons[self.selected_option].configure(
                bg=self.colors["wrong"], fg="white"
            )
            self.option_buttons[q["answer"]].configure(
                bg=self.colors["correct"], fg="white"
            )
            self.show_feedback("✧ Not quite ✧", False)
    
    def show_feedback(self, message, is_correct):
        self.submit_btn.configure(state="disabled")
        
        color = self.colors["correct"] if is_correct else self.colors["wrong"]
        
        feedback = tk.Label(
            self.container, text=message,
            font=("Helvetica", 20, "bold"), bg=self.colors["bg"],
            fg=color
        )
        feedback.pack(pady=10)
        
        self.root.after(1500, self.next_question)
    
    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.quiz_data):
            self.show_question()
        else:
            self.show_results()
    
    def show_results(self):
        self.clear_container()
        
        pct = (self.score / len(self.quiz_data)) * 100
        
        if pct == 100:
            emoji, msg = "👑", "Perfect! Legendary!"
        elif pct >= 80:
            emoji, msg = "⚡", "Excellent work!"
        elif pct >= 60:
            emoji, msg = "✨", "Well done!"
        elif pct >= 40:
            emoji, msg = "🌙", "Nice try!"
        else:
            emoji, msg = "💫", "Keep going!"
        
        # Big emoji with glow
        emoji_label = tk.Label(
            self.container, text=emoji, font=("Arial", 80),
            bg=self.colors["bg"]
        )
        emoji_label.pack(pady=(50, 20))
        self.bounce_animation(emoji_label)
        
        result_text = tk.Label(
            self.container, text=msg, font=("Helvetica", 28, "bold"),
            bg=self.colors["bg"], fg=self.colors["text"]
        )
        result_text.pack(pady=10)
        
        # Score with accent
        score_frame = tk.Frame(self.container, bg=self.colors["bg"])
        score_frame.pack(pady=15)
        
        tk.Label(
            score_frame, text=f"{self.score}", font=("Helvetica", 48, "bold"),
            bg=self.colors["bg"], fg=self.colors["accent"]
        ).pack(side="left")
        
        tk.Label(
            score_frame, text=f" / {len(self.quiz_data)}", font=("Helvetica", 28),
            bg=self.colors["bg"], fg=self.colors["text"]
        ).pack(side="left", pady=(15, 0))
        
        # Percentage bar
        pct_frame = tk.Frame(self.container, bg=self.colors["bg"])
        pct_frame.pack(pady=20, fill="x", padx=100)
        
        pct_bg = tk.Frame(pct_frame, bg=self.colors["card"], height=12)
        pct_bg.pack(fill="x")
        
        pct_fill = tk.Frame(pct_bg, bg=self.colors["accent"], height=12)
        pct_fill.place(x=0, y=0, relwidth=pct/100)
        
        tk.Label(
            self.container, text=f"{pct:.0f}%",
            font=("Helvetica", 18), bg=self.colors["bg"],
            fg=self.colors["accent"]
        ).pack(pady=(5, 20))
        
        # Buttons
        btn_frame = tk.Frame(self.container, bg=self.colors["bg"])
        btn_frame.pack(pady=20)
        
        retry_btn = tk.Button(
            btn_frame, text="✦ Play Again ✦", font=("Helvetica", 13, "bold"),
            bg=self.colors["button"], fg="white", padx=25, pady=10,
            bd=0, cursor="hand2", command=self.start_quiz
        )
        retry_btn.pack(side="left", padx=10)
        self.add_hover_effect(retry_btn, self.colors["button"], self.colors["button_hover"])
        
        home_btn = tk.Button(
            btn_frame, text="⟡ Home ⟡", font=("Helvetica", 13),
            bg=self.colors["card"], fg=self.colors["text"], padx=25, pady=10,
            bd=0, cursor="hand2", command=self.show_welcome_screen
        )
        home_btn.pack(side="left", padx=10)
        self.add_hover_effect(home_btn, self.colors["card"], self.colors["accent"])
    
    def bounce_animation(self, widget, direction=1, offset=0):
        if not widget.winfo_exists():
            return
        
        offset += direction * 4
        if offset >= 20:
            direction = -1
        elif offset <= 0:
            direction = 1
        
        widget.pack_configure(pady=(50 - offset, 20 + offset))
        self.root.after(60, lambda: self.bounce_animation(widget, direction, offset))


if __name__ == "__main__":
    root = tk.Tk()
    app = AestheticQuiz(root)
    root.mainloop()