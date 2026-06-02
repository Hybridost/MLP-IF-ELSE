from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field, ValidationError
from typing import Dict
from datetime import datetime
import json
import pathlib

app = FastAPI()
html_path = pathlib.Path(__file__).parent / "templates"

class ChatMessage(BaseModel):
    type: str = "message"
    text: str = Field(..., min_length=1, max_length=200) # Валидация длины

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, username: str):
        await websocket.accept()
        self.active_connections[username] = websocket
        await self.broadcast_system(f"{username} joined")

    def disconnect(self, username: str):
        if username in self.active_connections:
            del self.active_connections[username]

    async def send_personal(self, message: dict, username: str):
        if username in self.active_connections:
            await self.active_connections[username].send_json(message)

    async def broadcast(self, message: dict, exclude: str = None):
        for user, connection in self.active_connections.items():
            if user != exclude:
                await connection.send_json(message)
                
    async def broadcast_system(self, text: str):
        sys_msg = {
            "type": "system", "text": text,
            "online": len(self.active_connections),
            "ts": datetime.now().isoformat()
        }
        await self.broadcast(sys_msg)

manager = ConnectionManager()

@app.get("/")
async def get():
    html = (html_path / "chat.html").read_text(encoding="utf-8")
    return HTMLResponse(content=html, status_code=200)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, username: str = Query(...)):
    if not username or username.strip() == "":
        await websocket.close(code=1008)
        return
        
    await manager.connect(websocket, username)
    try:
        while True:
            data = await websocket.receive_text()
            try:
                msg_data = json.loads(data)
                msg = ChatMessage(**msg_data) # Валидация Pydantic
                
                # Обработка приватных сообщений
                if msg.text.startswith("/w "):
                    parts = msg.text.split(" ", 2)
                    if len(parts) >= 3:
                        target_user, private_text = parts[1], parts[2]
                        priv_msg = {"type": "private", "from": username, "to": target_user, "text": private_text, "ts": datetime.now().isoformat()}
                        if target_user in manager.active_connections:
                            await manager.send_personal(priv_msg, target_user)
                            await manager.send_personal(priv_msg, username)
                        else:
                            await manager.send_personal({"type": "error", "detail": f"User {target_user} not found"}, username)
                    else:
                        await manager.send_personal({"type": "error", "detail": "Format: /w username text"}, username)
                else:
                    # Публичное сообщение
                    out_msg = {"type": "message", "user": username, "text": msg.text, "ts": datetime.now().isoformat()}
                    await manager.broadcast(out_msg)
                    
            except ValidationError:
                await websocket.send_json({"type": "error", "detail": "Message is empty or >200 chars"})
            except json.JSONDecodeError:
                await websocket.send_json({"type": "error", "detail": "Invalid JSON"})
                
    except WebSocketDisconnect:
        manager.disconnect(username)
        await manager.broadcast_system(f"{username} left")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)