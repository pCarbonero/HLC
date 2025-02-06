import reflex as rx

def form() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.hstack(
                rx.text("Nombre: "),
                rx.input(
                    placeholder="Nombre",
                    type="text",
                    id="campoNombre"
                ),
            ),
            rx.hstack(
                rx.text("Apellidos: "),
                rx.input(
                    placeholder="Apellidos",
                    type="text",
                    id="campoApellidos"
                ),
            ),
            rx.hstack(
                rx.text("Sexo: "),
                rx.radio(
                    ["Hombre", "Mujer"],
                    direction="row",
                    id="sexRadio"
                )
            )
        )
    )