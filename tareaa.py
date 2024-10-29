import flet as ft

def main(page: ft.Page):
    
    page.window_width = 600
    page.window_height = 400 
    page.title = "Shopping List"
    
    # Encabezado y logo
    header_text = ft.Text("Listado", size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)
    header_welcome = ft.Text("Bienvenido!", size=15, text_align=ft.TextAlign.CENTER)
    logo = ft.Image(src="../recursos/img.png", width=125, height=125)
    
    header = ft.Column(
        [logo, header_text, header_welcome],
        alignment=ft.MainAxisAlignment.CENTER, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER 
    )
    # Hago este contenedor para centrar los elementos del header verticalemnte
    centered_header = ft.Container(
        content=header,
        alignment=ft.alignment.center  
    )
    # Campo de entrada para nuevas 
    new_task = ft.TextField(hint_text="¿Qué hace falta?", width=150)

    # Función para añadir tarea
    def add_clicked(e):        
        #Aca hago una validacion para que al darle agregar con el campo vacio no me guarde un str vacio
        if new_task.value.strip():
            task_label = new_task.value
            task_row = create_task_row(task_label)
            page.add(task_row)  # Añade la tarea si hay contenido
            new_task.value = ""  # Limpia el campo de texto para ingresar otro dato
            new_task.focus()
            new_task.update()

    # Funcion que 
    def create_task_row(task_label):
        task_row = ft.Row(
            [
                ft.Checkbox(label=task_label),
                ft.ElevatedButton("Editar", on_click=lambda e: edit_task(task_row)),
                ft.ElevatedButton("Borrar", on_click=lambda e: delete_task(task_row)),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        return task_row
    
    # Funcion que permite editar el registro
    
    def edit_task(task_row):
        
        task_checkbox = task_row.controls[0]
        new_label = task_checkbox.label
        new_task.value = new_label
        new_task.focus()
        
        page.controls.remove(task_row)
        page.update()
    
    # Pequeña funcion para eliminar un registro
    
    def delete_task(task_row):
        page.controls.remove(task_row)
        page.update()
        
    # Contenido de la página
    page.add(
        centered_header,
        ft.Divider(height=20),
        ft.Row([new_task, ft.ElevatedButton("Agregar", on_click=add_clicked)], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(main)
