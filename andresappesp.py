import ctypes
import os
import time
import sys
from colorama import Fore, Style

# Función para mostrar el mensaje de bienvenida en colores del arcoíris
def rainbow_print(message):
    colores = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    for letra, color in zip(message, colores * (len(message) // len(colores) + 1)):
        print(color + letra, end='', flush=True)
        time.sleep(0.1)  # Pausa breve para efecto de animación
    print(Style.RESET_ALL)  # Reiniciar color después del mensaje
    
def animation_print(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)  # Pausa breve para efecto de animación
    print("\033[F", end="")  # Retrocede una línea para limpiar el mensaje animado

def animation_speed_print(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)  # Pausa breve para efecto de animación
    print("\033[F", end="")  # Retrocede una línea para limpiar el mensaje animado

# Borra la pantalla
os.system("cls")
    
# Función para mostrar la animación de carga
def loading_animation():
    print('Cargando', end='', flush=True)
    time.sleep(0.5)
    for _ in range(10):
        print('.', end='', flush=True)
        time.sleep(0.5)
    print()
    time.sleep(1.0)  # Espera adicional después de la animación
    rainbow_print('Carga Exitosa!')
    time.sleep(1.0)  # Espera adicional antes de salir

# Función principal del programa
def main():
    # Asigna el título a la ventana de la consola
    os.system("title Andres Apps")

    # Define la ruta del archivo de ícono (.ico)
    icon_path = "logo.ico"

    # Obtiene el identificador de la ventana de la consola
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()

    # Carga el ícono desde el archivo .ico
    icon = ctypes.windll.user32.LoadImageW(0, icon_path, 1, 0, 0, 0x00000010)

    # Establece el ícono de la ventana de la consola
    ctypes.windll.user32.SendMessageW(hwnd, 0x80, 0, icon)

    # Muestra la animación de carga
    loading_animation()

    # Borra la pantalla
    os.system("cls")

    # Solicita el nombre del usuario
    print('Por favor, introduce tu nombre:')
    nombre = input('> ')

    # Borra la pantalla
    os.system("cls")

    # Muestra el mensaje de bienvenida y otros detalles
    animation_print('¡Bienvenido a Andres Apps!')
    print('¡Bienvenido a Andres Apps!')
    print('Tu versión de la Aplicacion es Beta_Preview=1.0')
    print('')

    # Muestra las secciones del programa
    print('----------------------------------------------')
    print('                    Tienda                    ')
    print('----------------------------------------------')
    print('\033[31mNo Hay Niguna App En La Tienda (Coming Soon)\033[0m')
    print('')
    print('----------------------------------------------')
    print('                  Biblioteca                  ')
    print('----------------------------------------------')
    print('\033[92mPaint. Nada Mas\033[0m')
    print('\033[34mDile A El Discord Official de Andres Studios!\033[0m')
    print('\033[34mhttps://discord.gg/kujySff9\033[0m')
    print('')
    print('----------------------------------------------')
    print('                     Cmd                      ')
    print('----------------------------------------------')
    print('')

    while True:
        command = input('Andres Apps > ')
        if command.lower() == 'exit':
            print('Cerrando el proyecto...')
            exit()  # Sale del proyecto
        elif command.lower() == 'paint':
            print('Abriendo Paint...')
            os.system("start paint.py")
        elif command.lower() == 'reload':
            print('Reiniciando el proyecto...')
            os.system("start andresapp.py")  # Abre andresgames.py
            exit()  # Sale del proyecto actual
        elif command.lower() == 'temas > blanco':
            print('Se Ha Cambiado el Color')
            os.system("color 7")
        elif command.lower() == 'temas > gris':
            print('Se Ha Cambiado el Color')
            os.system("color 8")
        elif command.lower().startswith('pip install'):
            package_name = command.split(' ')[-1]  # Extrae el nombre del paquete de la última palabra
            print(f'Instalando el paquete {package_name}...')
            os.system(f"pip install {package_name}")
        elif command.lower().startswith('pip uninstall'):
            package_name = command.split(' ')[-1]  # Extrae el nombre del paquete de la última palabra
            print(f'Desinstalando el paquete {package_name}...')
            os.system(f"pip uninstall {package_name}")
        elif command.lower() == 'help':
            print('')
            print('Explorador de Comandos')
            print('Temas:temas > gris. temas > blanco')
            print('')

# Ejecuta la función principal
if __name__ == "__main__":
    main()
