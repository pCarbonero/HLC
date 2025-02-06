import reflex as rx
from rxconfig import config
from ejercicio02.routes import Ruta
from ejercicio02.views.form.form import form



@rx.page(
    route = Ruta.INDEX.value,
    title = "Formulario de registro - Mi web"
)
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        rx.text("PAGINA FORMULARIO"),
        form(),
        align='center',
        spacing='3'
    )