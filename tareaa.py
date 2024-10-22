import flet as ft

def main(page: ft.Page):

    page.window_width = 600
    page.window_height = 400 
    page.title = "Shopping List"
    
    # Encabezado y logo
    header_text = ft.Text("Lista de Compras", size=20, weight=ft.FontWeight.BOLD)
    logo = ft.Image(src="../recursos/img.png", width=150, height=150)
    
    header = ft.Row(
        [logo, header_text],
        alignment="center"
    )

    # Campo de entrada para nuevas tareas
    new_task = ft.TextField(hint_text="¿Qué hace falta?", width=150)

    # Función para añadir tarea
    def add_clicked(e):
        if new_task.value.strip():
            page.add(ft.Checkbox(label=new_task.value))  # Añade la tarea si hay contenido
            new_task.value = ""  # Limpia el campo de texto
            new_task.focus()
            new_task.update()

    # Contenido de la página
    page.add(
        header,
        ft.Divider(height=20),
        ft.Row([new_task, ft.ElevatedButton("Agregar", on_click=add_clicked)], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(main)

