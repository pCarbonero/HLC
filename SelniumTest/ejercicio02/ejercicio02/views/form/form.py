import reflex as rx

def form() -> rx.Component:
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.hstack(
                rx.text("Nombre: "),
                    rx.input(
                        placeholder="Nombre",
                        type="text",
                        id="campoNombre",
                        max_length = 50
                    ),
                ),
            rx.hstack(
                rx.text("Apellidos: "),
                rx.input(
                    placeholder="Apellidos",
                    type="text",
                    id="campoApellidos",
                    max_length = 50
                ),
            ),
            rx.hstack(
                rx.text("Sexo: "),
                rx.radio(
                    ["Hombre", "Mujer"],
                    direction="row",
                    id="sexRadio"
                )
            ),
            rx.hstack(
                rx.text("Correo: "),
                rx.input(
                    placeholder="Correo Electrónico",
                    type="email",
                    id="mailInput"
                ),
            ),
            rx.hstack(
                rx.checkbox(default_checked=True, id="checkInformacion"),
                rx.text("Deseo recibir información sobre novedades y ofertas", id="textInformacion") 
            ),
            rx.hstack(
                rx.checkbox(id="checkCondiciones"),
                rx.text("Declaro haber leido y aceptar las condiciones generales del programa y la normativa sobre protección de datos", id="textCondiciones") 
            ),
            rx.button("Submit", type="submit"),
            ), 
            reset_on_submit=True,
       )       
    )