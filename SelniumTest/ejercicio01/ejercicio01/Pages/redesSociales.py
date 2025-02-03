import reflex as rx
from rxconfig import config
from ejercicio01.routes import *

@rx.page(
    route = Ruta.RRSS.value,
    title = "Redes Sociales"
)
def redesSociales() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.text('REDES SOCIALES', font_size="40px", font_weight="bold", margin_top="20px", margin_bottom="20px"),
            rx.list.unordered(
                rx.list.item(rx.link("Instagram", href="https://www.instagram.com", id="ig", is_external=True)),
                rx.list.item(rx.link("TikTok", href="https://www.tiktok.com", id="tiktok", is_external=True)),
                rx.list.item(rx.link("Facebook", href="https://www.facebook.com", id="fb", is_external=True))
            ),
            rx.link("Volver", href="/", id="linkVolverRs")      
        )
    )