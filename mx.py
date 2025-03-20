import asyncio
import websockets
import json
import time  # Importation du module time pour mesurer le temps

# URL du WebSocket pour BTC/USDT sur Binance
url = "wss://stream.binance.com:9443/ws/btcusdt@trade"

# Fonction pour recevoir les données en temps réel
async def get_btc_price():
    async with websockets.connect(url) as websocket:
        print("✅ Connexion WebSocket établie, réception des données...")
        
        # Boucle infinie pour recevoir les messages en temps réel
        while True:
            # Enregistrer le temps avant la réception du message
            start_time = time.time()  # Temps de début en secondes
            
            # Recevoir un message du WebSocket
            message = await websocket.recv()
            
            # Enregistrer le temps après réception du message
            end_time = time.time()  # Temps de fin en secondes
            
            # Calculer le temps écoulé en millisecondes
            elapsed_time_ms = (end_time - start_time) * 1000  # Conversion en millisecondes
            
            data = json.loads(message)
            
            # Extraire le prix du message reçu
            price = data['p']
            timestamp = data['T']
            
            # Affichage du temps mis pour recevoir la réponse
            print(f"⏰ Timestamp: {timestamp}, 📈 Prix BTC/USDT: {price}, ⏳ Temps de réponse: {elapsed_time_ms:.2f} ms")

# Démarrer l'event loop
asyncio.get_event_loop().run_until_complete(get_btc_price())
