import reflex as rx
from rxconfig import config
from ejercicio01.routes import *

@rx.page(
    route = Ruta.BUSCADORES.value,
    title = "Buscadores"
)
def buscadores() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.text('BUSCADORES', font_size="40px", font_weight="bold", margin_top="20px", margin_bottom="20px", id="tituloBuscadores"),
            rx.list.unordered(
                rx.list.item(rx.link("Google", href="https://www.google.com", id="linkGoogle", is_external=True)),
                rx.list.item(rx.link("Bing", href="https://www.bing.com", id="linkBing", is_external=True)),
                rx.list.item(rx.link("Baidu", href="https://www.baidu.com", id="linkBaidu", is_external=True))
            ),
            rx.link("Volver", href="/", id="linkVolver")
        )
    )