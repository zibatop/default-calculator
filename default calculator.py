import tkinter as tk
def calculate():
    try:
        result = eval(entry.get())
        result_label.config(text=f"Ответ: {result}")
    except:
        result_label.config(text="Ошибка")
window = tk.Tk()
window.title("Калькулятор")
window.geometry("500x300")

entry = tk.Entry(window, font=("Arial", 16))
entry.pack(pady=20)

button = tk.Button(window, text="Посчитать", command=calculate)
button.pack()

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=20)

window.mainloop()