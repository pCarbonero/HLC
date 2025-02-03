import reflex as rx
from rxconfig import config
from ejercicio01.routes import *
from ejercicio01.Views.header.header import header


@rx.page(
    route = Ruta.INDEX.value,
    title = "Pagina principal"
)
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        header(),
        align='center',
        spacing='3'
    )