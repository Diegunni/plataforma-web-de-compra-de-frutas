from fastapi import FastAPI

app = FastAPI(title="E-commerce de Frutas API")

frutas = []
carrito = []
pedidos = []

# -------- Subsistema Catalogo de Frutas --------

@app.get("/frutas")
def listar_frutas():
    return frutas

@app.post("/frutas")
def crear_fruta(fruta: dict):
    frutas.append(fruta)
    return fruta

@app.get("/frutas/{id}")
def obtener_fruta(id: int):
    for f in frutas:
        if f["id"] == id:
            return f
    return {"error": "Fruta no encontrada"}

@app.put("/frutas/{id}")
def actualizar_fruta(id: int, fruta: dict):
    for i in range(len(frutas)):
        if frutas[i]["id"] == id:
            frutas[i] = fruta
            return fruta
    return {"error": "Fruta no encontrada"}

@app.delete("/frutas/{id}")
def eliminar_fruta(id: int):
    for f in frutas:
        if f["id"] == id:
            frutas.remove(f)
            return {"mensaje": "Fruta eliminada"}
    return {"error": "Fruta no encontrada"}


# -------- Subsistema Carrito --------

@app.post("/carrito/agregar")
def agregar_carrito(fruta: dict):
    carrito.append(fruta)
    return {"mensaje": "Fruta agregada al carrito", "carrito": carrito}

@app.get("/carrito")
def ver_carrito():
    return carrito


# -------- Subsistema Pedidos --------

@app.post("/pedido")
def crear_pedido():
    pedido = {
        "id": len(pedidos) + 1,
        "productos": carrito.copy(),
        "estado": "creado"
    }
    pedidos.append(pedido)
    carrito.clear()
    return pedido

@app.get("/pedidos")
def listar_pedidos():
    return pedidos


# -------- Subsistema Pagos --------

@app.post("/pago/{pedido_id}")
def pagar_pedido(pedido_id: int):
    for p in pedidos:
        if p["id"] == pedido_id:
            p["estado"] = "pagado"
            return {"mensaje": "Pago realizado", "pedido": p}
    return {"error": "Pedido no encontrado"}
