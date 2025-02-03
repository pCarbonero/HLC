import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.text('Enlaces favoritos', font_size="40px", font_weight="bold", margin_top="20px", margin_bottom="20px", id="enlacesFav"),

            rx.list.unordered(
                rx.list.item(rx.link("Buscadores", href="/buscadores", id="linkBuscadores")),
                rx.list.item(rx.link("Redes Sociales", href="/redessociales", id="linkRrss"))
            )
        )
    )