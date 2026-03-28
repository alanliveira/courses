import os
import logging
from aiohttp import web
from aiortc import RTCPeerConnection, RTCSessionDescription, RTCConfiguration, RTCIceServer
from game import GameStream, game_state

logging.basicConfig(level=logging.INFO)
ROOT = os.path.dirname(__file__)
CLIENT_DIR = os.path.join(ROOT, "..", "client")
pcs = set()

async def index(request):
    path = os.path.join(CLIENT_DIR, "index.html")
    with open(path, "r") as f:
        return web.Response(content_type="text/html", text=f.read())

async def get_players(request):
    """Retorna lista de jogadores com Nick e ID"""
    players_list = [
        {"client_id": pid, "nickname": p["nickname"], "color": p["color"]}
        for pid, p in game_state["players"].items()
    ]
    return web.json_response(players_list)

async def offer(request):
    params = await request.json()
    client_id = params.get("client_id")
    nickname = params.get("nickname", "Player")
    color = params.get("color", "red")

    if client_id in game_state["players"]:
        del game_state["players"][client_id]

    offer = RTCSessionDescription(sdp=params["sdp"], type=params["type"])
    pc = RTCPeerConnection(configuration=RTCConfiguration(
        iceServers=[RTCIceServer(urls=["stun:stun.l.google.com:19302"])]
    ))
    pcs.add(pc)

    @pc.on("connectionstatechange")
    async def on_connectionstatechange():
        if pc.connectionState in ["closed", "failed", "disconnected"]:
            if client_id in game_state["players"]:
                del game_state["players"][client_id]
            await pc.close()
            pcs.discard(pc)

    pc.addTrack(GameStream(client_id, nickname, color))
    await pc.setRemoteDescription(offer)
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)

    return web.json_response({"sdp": pc.localDescription.sdp, "type": pc.localDescription.type})

app = web.Application()
app.router.add_get("/", index)
app.router.add_get("/players", get_players)
app.router.add_post("/offer", offer)

# Serve static client assets (style.css, main.js)
app.router.add_static("/client", CLIENT_DIR)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=8080)
