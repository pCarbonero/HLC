"""Welcome to Reflex! This file outlines the steps to create a basic app."""


import reflex as rx

from ejercicio01.Pages.index import index
from ejercicio01.Pages.buscadores import buscadores
from ejercicio01.Pages.redesSociales import redesSociales
from rxconfig import config


class State(rx.State):
    """The app state."""

    ...



app = rx.App()
app.add_page(index)
app.add_page(buscadores)
app.add_page(redesSociales)
app._compile()
