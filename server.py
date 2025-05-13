import redis

# Configuración de Redis
redis_client = redis.Redis(host='https://distribuidos-server.onrender.com', port=6379, decode_responses=True)
pubsub = redis_client.pubsub()
pubsub.subscribe("acciones_jugadores")  # Escuchar acciones de los jugadores

# Procesar acciones y publicar estado del juego
def manejar_juego():
    print("[🔄] Servidor escuchando acciones...")
    for mensaje in pubsub.listen():
        if mensaje['type'] == 'message':
            print(f"[✔] Acción recibida: {mensaje['data']}")
            redis_client.publish("estado_juego", f"Estado actualizado -> {mensaje['data']}")

manejar_juego()
