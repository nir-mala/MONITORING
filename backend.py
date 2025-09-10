import asyncio
import aiohttp
import random
from datetime import datetime

# Konfigurasi Back4App
URL = "https://parseapi.back4app.com/classes/backend_trial"
HEADERS = {
    'X-Parse-Application-Id': 'EvdYX9DzGQFfIjgNHLKitEtnPrc6f0Ebo7QkpcoV',
    'X-Parse-REST-API-Key'  : 'I5p146Jcbyq1KKQZkLC4y1G4pY0De1RAR9rjUYVz',
    'Content-Type': 'application/json',
}

async def monitor_and_send():
    """Loop pengiriman data setiap detik."""
    async with aiohttp.ClientSession() as session:
        while True:
            now = datetime.now()
            sog_knot = round(random.uniform(0, 100), 2)
            sog_kmh = round(sog_knot * 1.852, 2)
            Lattitude = round(random.uniform(-90, 0), 1)
            Longitude = round(random.uniform(0, 180), 1)
            cog = round(random.uniform(0, 360), 2)
            Yaw = random.randint(0, 360) 
            x = random.randint(0, 2500)
            y = random.randint(0, 2500)

            data = {
                "Day": now.strftime("%a"),
                "Date": now.strftime("%Y/%m/%d"),
                "Time": now.strftime("%H:%M:%S"),
                "SOG_Knot": sog_knot,
                "SOG_kmperhours": sog_kmh,
                "COG": cog,
                "Yaw": Yaw,
                "Lattitude": Lattitude,
                "Longitude": Longitude,
                "Position_X": x,
                "Position_Y": y
            }

            await send_data(session, URL, HEADERS, data)
            await asyncio.sleep(1)

async def send_data(session, url, headers, data):
    """Mengirimkan data ke Back4App."""
    async with session.post(url, json=data, headers=headers) as response:
        if response.status == 201:
            print(f"Data berhasil dikirim: {data['Time']}")
        else:
            print(f"Error mengirim data: {response.status} - {await response.text()}")

# Jalankan program
asyncio.run(monitor_and_send())
