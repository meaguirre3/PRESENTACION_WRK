"""Presentación local con cinco demostraciones del notebook."""
import argparse
import base64
import contextlib
import io
import json
import re
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Lock

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

CARPETA = Path(__file__).resolve().parent
CALCULO = Lock()
SECCIONES = ("0.6", "0.7", "0.8", "0.9", "1.1")


def bloque(documento, etiqueta):
    patron = r"^```\{python\}\n#\| label: " + re.escape(etiqueta) + r"\n(.*?)^```\s*$"
    return re.search(patron, documento, re.M | re.S).group(1)


def ejecutar(seccion):
    documento = (CARPETA / "presentacion.qmd").read_text(encoding="utf-8")
    entorno = {}
    salida = io.StringIO()
    graficas = []
    try:
        with contextlib.redirect_stdout(salida), plt.ioff():
            exec(bloque(documento, "base-notebook"), entorno)
            exec(bloque(documento, "nb-" + seccion.replace(".", "-")), entorno)
            for numero in plt.get_fignums():
                png = io.BytesIO()
                plt.figure(numero).savefig(png, format="png", bbox_inches="tight")
                graficas.append(base64.b64encode(png.getvalue()).decode("ascii"))
    finally:
        plt.close("all")
    return {"texto": salida.getvalue(), "graficas": graficas}


class Presentacion(BaseHTTPRequestHandler):
    def responder(self, estado, tipo, contenido):
        self.send_response(estado)
        self.send_header("Content-Type", tipo)
        self.send_header("Content-Length", str(len(contenido)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(contenido)

    def do_GET(self):
        if self.path in ("/", "/presentacion.html"):
            self.responder(200, "text/html; charset=utf-8",
                           (CARPETA / "presentacion.html").read_bytes())
        else:
            self.send_error(404)

    def do_POST(self):
        puerto = self.server.server_port
        origen = f"http://127.0.0.1:{puerto}"
        if self.headers.get("Origin") != origen or self.headers.get("Host") != f"127.0.0.1:{puerto}":
            return self.send_error(403)
        seccion = self.path.removeprefix("/ejecutar/")
        if self.path != "/ejecutar/" + seccion or seccion not in SECCIONES:
            return self.send_error(404)
        try:
            with CALCULO:
                datos = ejecutar(seccion)
        except Exception as error:
            self.responder(500, "application/json", json.dumps({"error": str(error)}).encode())
        else:
            self.responder(200, "application/json", json.dumps(datos).encode())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sin-navegador", action="store_true")
    opciones = parser.parse_args()
    with ThreadingHTTPServer(("127.0.0.1", 0), Presentacion) as servidor:
        url = f"http://127.0.0.1:{servidor.server_port}/"
        print(f"Presentación en {url}\nMantén abierta esta ventana. Pulsa Ctrl+C para terminar.", flush=True)
        if not opciones.sin_navegador:
            webbrowser.open(url)
        try:
            servidor.serve_forever()
        except KeyboardInterrupt:
            pass
