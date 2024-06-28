import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import customtkinter
from customtkinter import CTk, CTkFrame, CTkEntry,  CTkButton
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np



# Colores
c_negro = '#010101'
c_morado = '#7f5af0'
c_verde = '#1ABC9C'
c_azul = '#76D7C4'
c_azul1 = '#2B7A78'
c_blanco = '#FFFFFF'
c_blanco1 = '#DEF2F1'

# Ventana principal
app = tk.Tk()
app.title("Como graficar vectores en dos y tres dimensiones")
app.geometry("500x500")

# Abrir Ventana secundaria (Vectores en R2)
def OpenNewWindow():
    nueva_ventana1 = tk.Toplevel(app)
    frame = tk.Frame(nueva_ventana1, background="#17252A")
    nueva_ventana1.geometry("800x600")
    nueva_ventana1.configure(background="#17252A")
    tk.Wm.wm_title(nueva_ventana1,"Graficas de vectores en R2")

    # Función Generar grafica R2
    def graficar_vector_r2(x, y):
        # Crear figura y canvas
        fig = Figure(figsize=(5, 5))
        canvas = FigureCanvasTkAgg(fig, master=nueva_ventana1)

        # Agregar eje
        ax = fig.add_subplot(111)

        # Dibujar vector
        ax.arrow(0, 0, x, y, head_width=0.3, head_length=0.5)

        # Mostrar canvas
        canvas.draw()
        canvas.get_tk_widget().pack()

    # Title
    title = tk.Label(frame, 
                      text="Graficas de vectores en R2",
                      bg="#17252A",
                      font=("courier", 18),
                      fg="white")
    # Definición
    definicion_r2 = """
    Representa una cantidad en un espacio bidimensional. Está compuesto por dos componentes, una para el eje horizontal (o eje x) y 
    otra para el eje vertical (o eje y).En términos más simples, un vector (x, y) indica un desplazamiento o cambio en dirección horizontal (x) 
    y vertical (y) desde un punto de referencia. Este tipo de vector es comúnmente utilizado en geometría analítica, física y otras áreas de las matemáticas 
    y las ciencias."""

    labelDef = tk.Label(frame, 
                      text=definicion_r2,
                      wraplength=600,
                      bg="#17252A",
                      font=("courier", 12),
                      fg="white")
    # Entrada para coordenada X
    labelX = tk.Label(frame, 
                      text="X:    ",
                      bg="#17252A",
                      font=("courier", 12),
                      fg="white")
    x_entry_r2 = tk.Entry(frame)
    
    # Entrada para coordenada Y
    labelY = tk.Label(frame, 
                      text="Y:    ",
                      bg="#17252A",
                      font=("courier", 12),
                      fg="white")
    y_entry_r2 = tk.Entry(frame)
    
    # Boton para graficar
    boton_r2 = CTkButton(frame, 
                        text="Graficar en R2",
                        text_color= c_negro,
                        border_width=2,
                        border_color= c_negro,
                        corner_radius=10,
                        hover_color= c_blanco1,
                        fg_color= c_azul,                           
                        command=lambda: graficar_vector_r2(float(x_entry_r2.get()), 
                                                            float(y_entry_r2.get()))
                        )


    # Etiquetas
    etiqueta_r2 = tk.Label(frame, 
                            text="Coordenadas en R2",
                            bg="#17252A",
                            font=("courier", 14),
                            fg="white"
                            )
    # Diseño
    title.grid(row=0, column=2, pady=10, columnspan=10)
    labelDef.grid(row=1, column=2, pady=10, columnspan=10)
    etiqueta_r2.grid(row=2, column=5, pady=10, columnspan=4)
    labelX.grid(row=3, column=5)
    x_entry_r2.grid(row=3, column=6, columnspan=2)
    labelY.grid(row=4, column=5)
    y_entry_r2.grid(row=4, column=6, columnspan=2)
    boton_r2.grid(row=5, column=5, pady=10, columnspan=4)
    
    frame.pack(expand=True)
# Boton para abrir ventana (Vectores en R2)
tk.Button(
    app,
    text="Vectores en R2",
    font=("courier", 14),
    bg="#17252A",
    fg="white",
    command=OpenNewWindow
).pack(
    fill=tk.BOTH,
    expand=True,
    side=tk.LEFT
)

# Abrir Ventana secundaria (Vectores en R3)
def OpenNewWindow1():
    nueva_ventana2 = tk.Toplevel(app)
    frame = tk.Frame(nueva_ventana2, background="#76D7C4")
    nueva_ventana2.geometry("1300x600")
    nueva_ventana2.configure(background="#76D7C4")
    tk.Wm.wm_title(nueva_ventana2,"Gráficas de vectores en R3")

    def graficar_vector_r3():
        # Obtiene los valores de los campos de entrada
        x = float(x_entry_r3.get())
        y = float(y_entry_r3.get())
        z = float(z_entry_r3.get())
       

        # Calcula los vértices del cubo
        vertices = np.array([[0, 0, 0],
                            [x, 0, 0],
                            [x, y, 0],
                            [0, y, 0],
                            [0, 0, z],
                            [x, 0, z],
                            [x, y, z],
                            [0, y, z]])
   

        # Índices para trazar las aristas del cubo
        edges = [[0, 1], [1, 2], [2, 3], [3, 0],
                [4, 5], [5, 6], [6, 7], [7, 4],
                [0, 4], [1, 5], [2, 6], [3, 7]]

        # Crea una figura y un eje 3D
        fig = plt.figure(figsize=(8, 6))  # Tamaño de la figura en pulgadas (ancho x alto)
        ax = fig.add_subplot(111, projection='3d')

        # Dibuja los vértices del cubo
        for i, vert in enumerate(vertices):
            if i == 0:  # Vértice en el origen (0, 0, 0)
                ax.scatter(vert[0], vert[1], vert[2], color='g', s=100) 
            else:
                ax.scatter(vert[0], vert[1], vert[2], color='r')


        # Dibuja las aristas del cubo
        for edge in edges:
            ax.plot3D(*zip(*vertices[edge]), linestyle='dotted', color='blue') 

        # Configura las etiquetas de los ejes
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
      

        # Dibuja el vector
        ax.quiver(0, 0, 0, x, y, z, color='red')
       

        # Ajusta los límites de los ejes para aumentar el zoom
        # Si X Y y Z son positivos
        if x > 0 and y > 0 and z > 0:
            
            ax.set_xlim([0, max(x, y, z)+2])  # Limites en el eje X
            ax.set_ylim([0, max(x, y, z)+2])  # Limites en el eje Y
            ax.set_zlim([0, max(x, y, z)+2])  # Limites en el eje Z

        # Si X y Y son positivos y Z negativo

        if x > 0 and y > 0 and z < 0:
            
            ax.set_xlim([0, max(x, y, z)+2])  # Limites en el eje X
            ax.set_ylim([0, max(x, y, z)+2])  # Limites en el eje Y
            ax.set_zlim([min(x, y, z)-2, 0])  # Limites en el eje Z

        # Si Z y Y son Negativos y X Positivos

        if x > 0 and y < 0 and z < 0:
            
            ax.set_xlim([0, max(x, y, z)+2])  # Limites en el eje X
            ax.set_ylim([min(x, y, z)-2,0])  # Limites en el eje Y
            ax.set_zlim([min(x, y, z)-2, 0])  # Limites en el eje Z
        
        # Si Z y Y son positivos y X negativo

        if x < 0 and y > 0 and z > 0:
            
            ax.set_xlim([min(x, y, z)-2, 0])  # Limites en el eje X
            ax.set_ylim([0, max(x, y, z)+2])  # Limites en el eje Y
            ax.set_zlim([0, max(x, y, z)+2])  # Limites en el eje Z

        # Si X y Z son Negativos y Y Positivo

        if x < 0 and y > 0 and z < 0:
            
            ax.set_xlim([min(x, y, z)-2, 0])  # Limites en el eje X
            ax.set_ylim([-10, max(x, y, z)+2])  # Limites en el eje Y
            ax.set_zlim([min(x, y, z)-2, 0])  # Limites en el eje Z

            # Si X y Y son negativos y Z Positivo

        if x < 0 and y < 0 and z > 0:
            
            ax.set_xlim([min(x, y, z)-2, 0])  # Limites en el eje X
            ax.set_ylim([min(x, y, z)-2, 0])  # Limites en el eje Y
            ax.set_zlim([0, max(x, y, z)+2])  # Limites en el eje Z

            # Si X y Z son positivos y Y negativo

        if x > 0 and y < 0 and z > 0:
            
            ax.set_xlim([0, max(x, y, z)+2])  # Limites en el eje X
            ax.set_ylim([min(x, y, z)-2, 0])  # Limites en el eje Y
            ax.set_zlim([0, max(x, y, z)+2])  # Limites en el eje Z

            # Si X,Y y Z son negativos

        if x < 0 and y < 0 and z < 0:
            
            ax.set_xlim([min(x, y, z)-10, 0])  # Limites en el eje X
            ax.set_ylim([min(x, y, z)-10, 0])  # Limites en el eje Y
            ax.set_zlim([min(x, y, z)-10, 0])  # Limites en el eje Z

        # Muestra la gráfica
        plt.show()

    # Definición
    title = tk.Label(frame, 
                      text="Gráficas de vectores en R3",
                      bg="#76D7C4",
                      font=("courier", 18),
                      fg="black")
    definicion_r3 = """
    En el espacio tridimensional (R³), un vector se puede representar gráficamente como una flecha que va desde el origen (0, 0, 0)hasta un punto (x, y, z), 
    donde las coordenadas representan las componentes del vector. La longitud de la flecha indica la magnitud del vector, y su dirección apunta hacia el punto final."""

    labelDef = tk.Label(frame, 
                      text=definicion_r3,
                      wraplength=600,
                      bg="#76D7C4",
                      font=("courier", 12),
                      fg="black")
    # Entrada para coordenadas en R3
    
    labelX = tk.Label(frame, 
                      text="X:    ",
                      bg="#76D7C4",
                      font=("courier", 12),
                      fg="black")
    x_entry_r3 = tk.Entry(frame)
    
    labelY = tk.Label(frame, 
                      text="Y:    ",
                      bg="#76D7C4",
                      font=("courier", 12),
                      fg="black")
    y_entry_r3 = tk.Entry(frame)
    labelZ = tk.Label(frame, 
                      text="Z:    ",
                      bg="#76D7C4",
                      font=("courier", 12),
                      fg="black")
    z_entry_r3 = tk.Entry(frame)

   

        
    # Boton para graficar
    boton_r3 = CTkButton(frame, 
                        text="Graficar en R3",
                        text_color= c_negro,
                        border_width=2,
                        border_color= c_negro,
                        corner_radius=10,
                        hover_color= c_blanco1,
                        fg_color= c_azul,                           
                        command=lambda: graficar_vector_r3()
                        )
    boton_r3Suma = CTkButton(frame, 
                        text="Suma de vectores en R3",
                        text_color= c_negro,
                        border_width=2,
                        border_color= c_negro,
                        corner_radius=10,
                        hover_color= c_blanco1,
                        fg_color= c_azul,                           
                        command=lambda: OpenNewWindow2()
                        )
    boton_r3Resta = CTkButton(frame, 
                        text="Resta de vectores en R3",
                        text_color= c_negro,
                        border_width=2,
                        border_color= c_negro,
                        corner_radius=10,
                        hover_color= c_blanco1,
                        fg_color= c_azul,                           
                        command=lambda: OpenNewWindow3()
                        )
                           
  


    # Etiquetas
    etiqueta_r3 = tk.Label(frame, 
                            text="Coordenadas en R3",
                            bg="#76D7C4",
                            font=("courier", 14),
                            fg="black"
                            )

    # Diseño
    title.grid(row=0, column=2, pady=10, columnspan=10)
    labelDef.grid(row=1, column=2, pady=10, columnspan=10)
 

    etiqueta_r3.grid(row=8, column=5, pady=10, columnspan=3)

    labelX.grid(row=9, column=5)
    x_entry_r3.grid(row=9, column=6, columnspan=2)
    labelY.grid(row=10, column=5)
    y_entry_r3.grid(row=10, column=6, columnspan=2)
    labelZ.grid(row=11, column=5)
    z_entry_r3.grid(row=11, column=6, columnspan=2)

    boton_r3.grid(row=12, column=5, pady=10, columnspan=3)
    boton_r3Suma.grid(row=13, column=5, pady=10, columnspan=3)
    boton_r3Resta.grid(row=14, column=5, pady=10, columnspan=3)
    
    frame.pack(expand=True)

# Boton para abrir ventana (Vectores en R3)
tk.Button(
    app,
    text="Vectores en R3",
    font=("courier", 14),
    bg="#76D7C4",
    fg="black",
    command=OpenNewWindow1
).pack(
    fill=tk.BOTH,
    expand=True,
    side=tk.LEFT
)

# R3SUMA
def OpenNewWindow2():
    
    nueva_ventana2 = tk.Toplevel(app)
    frame = tk.Frame(nueva_ventana2, background="#76D7C4")
    nueva_ventana2.geometry("1300x600")
    nueva_ventana2.configure(background="#76D7C4")
    tk.Wm.wm_title(nueva_ventana2,"Gráficas de vectores en R3")

    # Define una función local para graficar el vector
    def graficar_vector_r3():
        # Obtiene los valores de los campos de entrada
        x1 = float(x1_entry_r3.get())
        y1 = float(y1_entry_r3.get())
        z1 = float(z1_entry_r3.get())
        x2 = float(x2_entry_r3.get())
        y2 = float(y2_entry_r3.get())
        z2 = float(z2_entry_r3.get())

        # Calcula la suma de los vectores
        x_suma = x1 + x2
        y_suma = y1 + y2
        z_suma = z1 + z2

        # Calcula los vértices del primer cubo
        vertices1 = np.array([[0, 0, 0],
                            [x1, 0, 0],
                            [x1, y1, 0],
                            [0, y1, 0],
                            [0, 0, z1],
                            [x1, 0, z1],
                            [x1, y1, z1],
                            [0, y1, z1]])

        # Calcula los vértices del segundo cubo
        vertices2 = np.array([[0, 0, 0],
                            [x2, 0, 0],
                            [x2, y2, 0],
                            [0, y2, 0],
                            [0, 0, z2],
                            [x2, 0, z2],
                            [x2, y2, z2],
                            [0, y2, z2]])
        vertices3 = np.array([[0, 0, 0],
                            [x_suma, 0, 0],
                            [x_suma, y_suma, 0],
                            [0, y_suma, 0],
                            [0, 0, z_suma],
                            [x_suma, 0, z_suma],
                            [x_suma, y_suma, z_suma],
                            [0, y_suma, z_suma]])

        # Índices para trazar las aristas de ambos cubos
        edges = [[0, 1], [1, 2], [2, 3], [3, 0],
                [4, 5], [5, 6], [6, 7], [7, 4],
                [0, 4], [1, 5], [2, 6], [3, 7]]

        # Crea una figura y un eje 3D
        fig = plt.figure(figsize=(8, 6))  # Tamaño de la figura en pulgadas (ancho x alto)
        ax = fig.add_subplot(111, projection='3d')

        # Dibuja los vértices del primer cubo
        for i, vert in enumerate(vertices1):
            if i == 0:  # Vértice en el origen (0, 0, 0)
                ax.scatter(vert[0], vert[1], vert[2], color='g', s=100) 
            else:
                ax.scatter(vert[0], vert[1], vert[2], color='r')

        # Dibuja los vértices del segundo cubo
        for i, vert in enumerate(vertices2):
            if i == 0:  # Vértice en el origen (0, 0, 0)
                ax.scatter(vert[0], vert[1], vert[2], color='g', s=100) 
            else:
                ax.scatter(vert[0], vert[1], vert[2], color='b')

        for i, vert in enumerate(vertices3):
            if i == 0:  # Vértice en el origen (0, 0, 0)
                ax.scatter(vert[0], vert[1], vert[2], color='g', s=100) 
            else:
                ax.scatter(vert[0], vert[1], vert[2], color='b')

        # Dibuja las aristas de ambos cubos
        for edge in edges:
            ax.plot3D(*zip(*vertices1[edge]), linestyle='dotted', color='r')
            ax.plot3D(*zip(*vertices2[edge]), linestyle='dotted', color='b')
            ax.plot3D(*zip(*vertices3[edge]), linestyle='dotted', color='yellow')

            # Dibuja el vector
        ax.quiver(0, 0, 0, x1, y1, z1, color='red')
        ax.quiver(0, 0, 0, x2, y2, z2, color='blue')
        ax.quiver(0, 0, 0, x_suma, y_suma, z_suma, color='gray')

        min_x = min(0, x1, x2, x_suma)
        max_x = max(0, x1, x2, x_suma)
        min_y = min(0, y1, y2, y_suma)
        max_y = max(0, y1, y2, y_suma)
        min_z = min(0, z1, z2, z_suma)
        max_z = max(0, z1, z2, z_suma)

        ax.quiver(0, 0, 0, x_suma, y_suma, z_suma, color='b', label='Suma')
        ax.quiver(0, 0, 0, x1, y1, z1, color='r', label='Vector 1')
        ax.quiver(0, 0, 0, x2, y2, z2, color='g', label='Vector 2')
        ax.set_xlim([min_x, max_x])
        ax.set_ylim([min_y, max_y])
        ax.set_zlim([min_z, max_z])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.legend()

        # Muestra la gráfica
        plt.show()

    # Definición
    title = tk.Label(frame, 
                        text="Suma de vectores en R3",
                        bg="#76D7C4",
                        font=("courier", 18),
                        fg="black")
    definicion_r3 = """
    La suma de dos vectores es una operación en la que se combinan las componentes de ambos vectores para obtener un nuevo vector. 
    Esto se realiza sumando las componentes correspondientes de los vectores. Es decir (X+X),(Y+Y),(Z+Z)
    """

    labelDef = tk.Label(frame, 
                        text=definicion_r3,
                        wraplength=600,
                        bg="#76D7C4",
                        font=("courier", 12),
                        fg="black")

    # Entrada para coordenadas en R3 del primer vector
    labelX1 = tk.Label(frame, 
                        text="X:    ",
                        bg="#76D7C4",
                        font=("courier", 12),
                        fg="black")
    x1_entry_r3 = tk.Entry(frame)
    
    labelY1 = tk.Label(frame, 
                        text="Y:    ",
                        bg="#76D7C4",
                        font=("courier", 12),
                        fg="black")
    y1_entry_r3 = tk.Entry(frame)
    labelZ1 = tk.Label(frame, 
                        text="Z:    ",
                        bg="#76D7C4",
                        font=("courier", 12),
                        fg="black")
    z1_entry_r3 = tk.Entry(frame)

    # Entrada para coordenadas en R3 del segundo vector
    labelX2 = tk.Label(frame, 
                        text="X:    ",
                        bg="#76D7C4",
                        font=("courier", 12),
                        fg="black")
    x2_entry_r3 = tk.Entry(frame)
    
    labelY2 = tk.Label(frame, 
                        text="Y:    ",
                        bg="#76D7C4",
                        font=("courier", 12),
                        fg="black")
    y2_entry_r3 = tk.Entry(frame)
    labelZ2 = tk.Label(frame, 
                        text="Z:    ",
                        bg="#76D7C4",
                        font=("courier", 12),
                        fg="black")
    z2_entry_r3 = tk.Entry(frame)

    
    # Boton para graficar
    boton_r3 = CTkButton(frame, 
                        text="Graficar en R3",
                        text_color= c_negro,
                        border_width=2,
                        border_color= c_negro,
                        corner_radius=10,
                        hover_color= c_blanco1,
                        fg_color= c_azul,                           
                        command=lambda: graficar_vector_r3()
                        )


    # Etiquetas
    etiqueta_vector1 = tk.Label(frame, 
                            text="Coordenadas del primer vector         ",
                            bg="#76D7C4",
                            font=("courier", 14),
                            fg="black"
                            )
    etiqueta_vector2 = tk.Label(frame, 
                        text="Coordenadas del segundo vector",
                        bg="#76D7C4",
                        font=("courier", 14),
                        fg="black"
                        )

    # Diseño
    title.grid(row=0, column=2, pady=10, columnspan=10)
    labelDef.grid(row=1, column=2, pady=10, columnspan=10)
    etiqueta_vector1.grid(row=8, column=2, pady=10, columnspan=3)
    etiqueta_vector2.grid(row=8, column=5, pady=10, columnspan=3)

    labelX1.grid(row=9, column=2)
    x1_entry_r3.grid(row=9, column=2, columnspan=3)
    labelY1.grid(row=10, column=2)
    y1_entry_r3.grid(row=10, column=2, columnspan=3)
    labelZ1.grid(row=11, column=2)
    z1_entry_r3.grid(row=11, column=2, columnspan=3)

    labelX2.grid(row=9, column=5)
    x2_entry_r3.grid(row=9, column=5, columnspan=3)
    labelY2.grid(row=10, column=5)
    y2_entry_r3.grid(row=10, column=5, columnspan=3)
    labelZ2.grid(row=11, column=5)
    z2_entry_r3.grid(row=11, column=5, columnspan=3)
    
    boton_r3.grid(row=15, column=3, pady=10, columnspan=3)
    
    frame.pack(expand=True)


# R3RESTA
def OpenNewWindow3():
    
    nueva_ventana3 = tk.Toplevel(app)
    frame = tk.Frame(nueva_ventana3, background="#76D7C4")
    nueva_ventana3.geometry("1300x600")
    nueva_ventana3.configure(background="#76D7C4")
    tk.Wm.wm_title(nueva_ventana3,"Resta de vectores en R3")

    # Define una función local para graficar el vector
    def graficar_vector_r3():
        # Obtiene los valores de los campos de entrada
        x1 = float(x1_entry_r3.get())
        y1 = float(y1_entry_r3.get())
        z1 = float(z1_entry_r3.get())
        x2 = float(x2_entry_r3.get())
        y2 = float(y2_entry_r3.get())
        z2 = float(z2_entry_r3.get())

        # Calcula la suma de los vectores
        x_resta = x1 - x2
        y_resta = y1 - y2
        z_resta = z1 - z2

        # Calcula los vértices del primer cubo
        vertices1 = np.array([[0, 0, 0],
                            [x1, 0, 0],
                            [x1, y1, 0],
                            [0, y1, 0],
                            [0, 0, z1],
                            [x1, 0, z1],
                            [x1, y1, z1],
                            [0, y1, z1]])

        # Calcula los vértices del segundo cubo
        vertices2 = np.array([[0, 0, 0],
                            [x2, 0, 0],
                            [x2, y2, 0],
                            [0, y2, 0],
                            [0, 0, z2],
                            [x2, 0, z2],
                            [x2, y2, z2],
                            [0, y2, z2]])
        vertices3 = np.array([[0, 0, 0],
                            [x_resta, 0, 0],
                            [x_resta, y_resta, 0],
                            [0, y_resta, 0],
                            [0, 0, z_resta],
                            [x_resta, 0, z_resta],
                            [x_resta, y_resta, z_resta],
                            [0, y_resta, z_resta]])

        # Índices para trazar las aristas de ambos cubos
        edges = [[0, 1], [1, 2], [2, 3], [3, 0],
                [4, 5], [5, 6], [6, 7], [7, 4],
                [0, 4], [1, 5], [2, 6], [3, 7]]

        # Crea una figura y un eje 3D
        fig = plt.figure(figsize=(8, 6))  # Tamaño de la figura en pulgadas (ancho x alto)
        ax = fig.add_subplot(111, projection='3d')

        # Dibuja los vértices del primer cubo
        for i, vert in enumerate(vertices1):
            if i == 0:  # Vértice en el origen (0, 0, 0)
                ax.scatter(vert[0], vert[1], vert[2], color='g', s=100) 
            else:
                ax.scatter(vert[0], vert[1], vert[2], color='r')

        # Dibuja los vértices del segundo cubo
        for i, vert in enumerate(vertices2):
            if i == 0:  # Vértice en el origen (0, 0, 0)
                ax.scatter(vert[0], vert[1], vert[2], color='g', s=100) 
            else:
                ax.scatter(vert[0], vert[1], vert[2], color='b')

        for i, vert in enumerate(vertices3):
            if i == 0:  # Vértice en el origen (0, 0, 0)
                ax.scatter(vert[0], vert[1], vert[2], color='g', s=100) 
            else:
                ax.scatter(vert[0], vert[1], vert[2], color='b')

        # Dibuja las aristas de ambos cubos
        for edge in edges:
            ax.plot3D(*zip(*vertices1[edge]), linestyle='dotted', color='r')
            ax.plot3D(*zip(*vertices2[edge]), linestyle='dotted', color='b')
            ax.plot3D(*zip(*vertices3[edge]), linestyle='dotted', color='yellow')

            # Dibuja el vector
        ax.quiver(0, 0, 0, x1, y1, z1, color='red')
        ax.quiver(0, 0, 0, x2, y2, z2, color='blue')
        ax.quiver(0, 0, 0, x_resta, y_resta, z_resta, color='gray')

        min_x = min(0, x1, x2, x_resta)
        max_x = max(0, x1, x2, x_resta)
        min_y = min(0, y1, y2, y_resta)
        max_y = max(0, y1, y2, y_resta)
        min_z = min(0, z1, z2, z_resta)
        max_z = max(0, z1, z2, z_resta)

        ax.quiver(0, 0, 0, x_resta, y_resta, z_resta, color='b', label='Suma')
        ax.quiver(0, 0, 0, x1, y1, z1, color='r', label='Vector 1')
        ax.quiver(0, 0, 0, x2, y2, z2, color='g', label='Vector 2')
        ax.set_xlim([min_x, max_x])
        ax.set_ylim([min_y, max_y])
        ax.set_zlim([min_z, max_z])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.legend()

        # Muestra la gráfica
        plt.show()

    # Definición
    title = tk.Label(frame, 
                        text="Resta de vectores en R3",
                        bg="#76D7C4",
                        font=("courier", 18),
                        fg="black")
    definicion_r3 = """
    La resta de dos vectores es una operación en la que se combinan las componentes de ambos vectores para obtener un nuevo vector. 
    Esto se realiza restando los componentes correspondientes de los vectores. Es decir (X-X),(Y-Y),(Z-Z)"""

    labelDef = tk.Label(frame, 
                        text=definicion_r3,
                        wraplength=600,
                        bg="#76D7C4",
                        font=("courier", 12),
                        fg="black")

    # Entrada para coordenadas en R3 del primer vector
    labelX1 = tk.Label(frame, 
                        text="X:    ",
                        bg="#76D7C4",
                        font=("courier", 12),
                        fg="black")
    x1_entry_r3 = tk.Entry(frame)
    
    labelY1 = tk.Label(frame, 
                        text="Y:    ",
                        bg="#76D7C4",
                        font=("courier", 12),
                        fg="black")
    y1_entry_r3 = tk.Entry(frame)
    labelZ1 = tk.Label(frame, 
                        text="Z:    ",
                        bg="#76D7C4",
                        font=("courier", 12),
                        fg="black")
    z1_entry_r3 = tk.Entry(frame)

    # Entrada para coordenadas en R3 del segundo vector
    labelX2 = tk.Label(frame, 
                        text="X:    ",
                        bg="#76D7C4",
                        font=("courier", 12),
                        fg="black")
    x2_entry_r3 = tk.Entry(frame)
    
    labelY2 = tk.Label(frame, 
                        text="Y:    ",
                        bg="#76D7C4",
                        font=("courier", 12),
                        fg="black")
    y2_entry_r3 = tk.Entry(frame)
    labelZ2 = tk.Label(frame, 
                        text="Z:    ",
                        bg="#76D7C4",
                        font=("courier", 12),
                        fg="black")
    z2_entry_r3 = tk.Entry(frame)

    
    # Boton para graficar
    boton_r3 = CTkButton(frame, 
                        text="Graficar en R3",
                        text_color= c_negro,
                        border_width=2,
                        border_color= c_negro,
                        corner_radius=10,
                        hover_color= c_blanco1,
                        fg_color= c_azul,                           
                        command=lambda: graficar_vector_r3()
                        )


    etiqueta_vector1 = tk.Label(frame, 
                            text="Coordenadas del primer vector         ",
                            bg="#76D7C4",
                            font=("courier", 14),
                            fg="black"
                            )
    etiqueta_vector2 = tk.Label(frame, 
                        text="Coordenadas del segundo vector",
                        bg="#76D7C4",
                        font=("courier", 14),
                        fg="black"
                        )

    # Diseño
    title.grid(row=0, column=2, pady=10, columnspan=10)
    labelDef.grid(row=1, column=2, pady=10, columnspan=10)
    etiqueta_vector1.grid(row=8, column=2, pady=10, columnspan=3)
    etiqueta_vector2.grid(row=8, column=5, pady=10, columnspan=3)

    labelX1.grid(row=9, column=2)
    x1_entry_r3.grid(row=9, column=2, columnspan=3)
    labelY1.grid(row=10, column=2)
    y1_entry_r3.grid(row=10, column=2, columnspan=3)
    labelZ1.grid(row=11, column=2)
    z1_entry_r3.grid(row=11, column=2, columnspan=3)

    labelX2.grid(row=9, column=5)
    x2_entry_r3.grid(row=9, column=5, columnspan=3)
    labelY2.grid(row=10, column=5)
    y2_entry_r3.grid(row=10, column=5, columnspan=3)
    labelZ2.grid(row=11, column=5)
    z2_entry_r3.grid(row=11, column=5, columnspan=3)
    boton_r3.grid(row=15, column=3, pady=10, columnspan=3)
    
    frame.pack(expand=True)

app.mainloop()