from pyodide.ffi import create_proxy
from pyscript import document


def greet(event):

    document.getElementById("output").innerHTML = "Hello, Comus Bala"


if document.getElementById("click_me").length > 0:
    proxy = create_proxy(greet)
    document.getElementById("click_me").addEventListener("click", proxy)


def add(a, b):
    return a + b
