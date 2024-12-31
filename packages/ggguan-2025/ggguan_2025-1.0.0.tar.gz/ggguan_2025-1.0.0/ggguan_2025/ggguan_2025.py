import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
from datetime import datetime, timedelta
import random


# 创建主窗口
class NewYearApp:
    def __init__(self, root):
        self.root = root
        self.root.title("2025 New Year Visualization")

        # 创建倒计时标签
        self.countdown_label = tk.Label(root, text="", font=("Helvetica", 24))
        self.countdown_label.pack(pady=20)

        # 创建烟花按钮
        self.fireworks_button = tk.Button(root, text="Show Fireworks", command=self.show_fireworks)
        self.fireworks_button.pack(pady=10)

        # 初始化倒计时
        self.target_date = datetime(2025, 1, 1, 0, 0, 0)
        self.update_countdown()

    def update_countdown(self):
        now = datetime.now()
        delta = self.target_date - now
        if delta.total_seconds() > 0:
            days, seconds = delta.days, delta.seconds
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60
            countdown_text = f"Time to 2025: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
        else:
            countdown_text = "Happy New Year 2025!"

        self.countdown_label.config(text=countdown_text)
        self.root.after(1000, self.update_countdown)

    def show_fireworks(self):
        fig, ax = plt.subplots()
        ax.axis("off")

        def update(frame):
            ax.clear()
            ax.axis("off")
            for _ in range(20):
                x = random.uniform(-1, 1)
                y = random.uniform(-1, 1)
                size = random.uniform(50, 300)
                color = random.choice(["red", "yellow", "blue", "green", "purple", "orange"])
                ax.scatter(x, y, s=size, c=color, alpha=0.6)

        ani = animation.FuncAnimation(fig, update, frames=30, interval=200, repeat=False)
        plt.show()


# 运行应用
if __name__ == "__main__":
    root = tk.Tk()
    app = NewYearApp(root)
    root.mainloop()
