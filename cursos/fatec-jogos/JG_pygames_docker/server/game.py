import os
import pygame
import numpy as np
import os
from aiortc import VideoStreamTrack
from av import VideoFrame

try:
    pygame.init()
    if not pygame.font.get_init():
        pygame.font.init()
except:
    pass

game_state = {"players": {}}

class GameStream(VideoStreamTrack):
    def __init__(self, client_id, nickname, color):
        super().__init__()
        self.client_id = client_id
        self.width, self.height = 640, 480
        self.screen = pygame.Surface((self.width, self.height))
        
        self.font = None
        try:
            font_path = os.path.join(os.path.dirname(__file__), "Roboto.ttf")
            if os.path.exists(font_path):
                self.font = pygame.font.Font(font_path, 18)
            else:
                self.font = pygame.font.SysFont(None, 24)
        except:
            print("⚠️ Erro ao carregar fontes. O jogo rodará sem nomes.")

        game_state["players"][client_id] = {
            "x": 320, "y": 240,
            "vx": 4, "vy": 3,
            "nickname": nickname,
            "color": color
        }

    async def recv(self):
        pts, time_base = await self.next_timestamp()
        self.screen.fill((20, 20, 20))

        for pid, p in list(game_state["players"].items()):
            p["x"] += p["vx"]
            p["y"] += p["vy"]

            if p["x"] < 15 or p["x"] > self.width - 15: p["vx"] *= -1
            if p["y"] < 15 or p["y"] > self.height - 15: p["vy"] *= -1

            color_rgb = self._get_color(p["color"])
            pygame.draw.circle(self.screen, color_rgb, (int(p["x"]), int(p["y"])), 12)
            
            if self.font:
                try:
                    txt = self.font.render(p["nickname"], True, (255, 255, 255))
                    rect = txt.get_rect(center=(int(p["x"]), int(p["y"]) - 30))
                    self.screen.blit(txt, rect)
                except: pass

        frame = np.array(pygame.surfarray.array3d(self.screen)).transpose([1, 0, 2])
        video_frame = VideoFrame.from_ndarray(frame, format="rgb24")
        video_frame.pts, video_frame.time_base = pts, time_base
        return video_frame

    def _get_color(self, name):
        colors = {"red": (255, 60, 60), "green": (60, 255, 60), "blue": (60, 60, 255)}
        return colors.get(name, (200, 200, 200))
