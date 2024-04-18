import tkinter as tk
from tkinter import ttk, filedialog, colorchooser
from PIL import Image, ImageGrab
import time
import threading

# Variables globales
current_color = "black"
current_mode = "pencil"
shape_start = None

def open_paint():
    def change_color(new_color):
        global current_color
        current_color = new_color

    def change_mode(new_mode):
        global current_mode
        current_mode = new_mode

    def paint(event):
        brush_size = int(brush_size_slider.get())
        if current_mode == "pencil":
            x1, y1 = (event.x - brush_size), (event.y - brush_size)
            x2, y2 = (event.x + brush_size), (event.y + brush_size)
            canvas.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color, width=brush_size * 2)
        elif current_mode == "erase":
            x1, y1 = (event.x - brush_size * 2), (event.y - brush_size * 2)
            x2, y2 = (event.x + brush_size * 2), (event.y + brush_size * 2)
            canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="white")
        elif current_mode == "fill":
            canvas.create_rectangle(0, 0, canvas.winfo_width(), canvas.winfo_height(), fill=current_color)
        elif current_mode == "fill_eraser":
            canvas.delete("all")  # Borrar todo el lienzo
        elif current_mode == "original_brush":
            x1, y1 = (event.x - brush_size), (event.y - brush_size)
            x2, y2 = (event.x + brush_size), (event.y + brush_size)
            canvas.create_rectangle(x1, y1, x2, y2, fill=current_color, outline=current_color)
        elif current_mode == "marker":
            x1, y1 = (event.x - brush_size * 2), (event.y - brush_size * 2)
            x2, y2 = (event.x + brush_size * 2), (event.y + brush_size * 2)
            canvas.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color, width=brush_size)
        elif current_mode == "oil_brush":
            x1, y1 = (event.x - brush_size), (event.y - brush_size)
            x2, y2 = (event.x + brush_size), (event.y + brush_size)
            canvas.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color, width=brush_size * 4)
        elif current_mode == "natural_pencil":
            x1, y1 = (event.x - brush_size), (event.y - brush_size)
            x2, y2 = (event.x + brush_size), (event.y + brush_size)
            canvas.create_line(x1, y1, x2, y2, fill=current_color, width=brush_size)

    def save_project():
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
        if file_path:
            x = paint_window.winfo_rootx() + canvas.winfo_x()
            y = paint_window.winfo_rooty() + canvas.winfo_y()
            x1 = x + canvas.winfo_width()
            y1 = y + canvas.winfo_height()
            ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)

    def choose_custom_color():
        selected_color = colorchooser.askcolor(title="Choose Color")[1]
        if selected_color:
            change_color(selected_color)

    paint_window = tk.Tk()  # Cambiado de Toplevel a Tk
    paint_window.title("Paint")
    paint_window.geometry("400x400")

    # Establecer el icono de la ventana principal
    icon_image = tk.PhotoImage(file="paint.png")  # Ruta de tu archivo de icono
    paint_window.iconphoto(True, icon_image)

    canvas_frame = ttk.Frame(paint_window)
    canvas_frame.pack(fill=tk.BOTH, expand=tk.YES)

    canvas = tk.Canvas(canvas_frame, bg="white")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

    vscrollbar = ttk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=canvas.yview)
    vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.config(yscrollcommand=vscrollbar.set)

    hscrollbar = ttk.Scrollbar(paint_window, orient=tk.HORIZONTAL, command=canvas.xview)
    hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
    canvas.config(xscrollcommand=hscrollbar.set)

    canvas.bind("<B1-Motion>", paint)

    brush_size_slider = ttk.Scale(paint_window, from_=1, to=60, orient=tk.HORIZONTAL)
    brush_size_slider.set(5)  # Tamaño de pincel predeterminado
    brush_size_slider.pack(side=tk.BOTTOM, fill=tk.X)

    brush_size_entry = ttk.Entry(paint_window)
    brush_size_entry.pack(side=tk.BOTTOM, fill=tk.X)
    brush_size_entry.insert(tk.END, "5")  # Valor predeterminado

    def update_brush_size(event):
        try:
            size = int(brush_size_entry.get())
            if 1 <= size <= 20:
                brush_size_slider.set(size)
            else:
                brush_size_entry.delete(0, tk.END)
                brush_size_entry.insert(tk.END, str(brush_size_slider.get()))
        except ValueError:
            brush_size_entry.delete(0, tk.END)
            brush_size_entry.insert(tk.END, str(brush_size_slider.get()))

    brush_size_entry.bind("<Return>", update_brush_size)

    # Paleta de colores
    colors = ["black", "red", "blue", "green", "yellow", "orange", "purple", "custom"]
    color_buttons_frame = ttk.Frame(paint_window)
    color_buttons_frame.pack(side=tk.BOTTOM, fill=tk.X)

    for color in colors:
        if color == "custom":
            color_button = ttk.Button(color_buttons_frame, text="Custom", command=choose_custom_color)
        else:
            color_button = ttk.Button(color_buttons_frame, text=color.capitalize(), command=lambda c=color: change_color(c))
        color_button.pack(side=tk.LEFT, padx=5, pady=5)

    # Herramientas
    tools = ["pencil", "fill", "erase", "fill_eraser", "original_brush", "marker", "oil_brush", "natural_pencil"]
    tool_buttons_frame = ttk.Frame(paint_window)
    tool_buttons_frame.pack(side=tk.BOTTOM, fill=tk.X)

    for tool in tools:
        tool_button = ttk.Button(tool_buttons_frame, text=tool.replace("_", " ").capitalize(), command=lambda t=tool: change_mode(t))
        tool_button.pack(side=tk.LEFT, padx=5, pady=5)

    # Menú
    menubar = tk.Menu(paint_window)
    paint_window.config(menu=menubar)

    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Save Project", command=save_project)

    paint_window.mainloop()  # Agregado para iniciar el bucle principal

open_paint()
