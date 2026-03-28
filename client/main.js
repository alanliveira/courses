// ── session ID ─────────────────────────────────────────────────────────────
const sessionID = Math.random().toString(36).substring(2, 8).toUpperCase();
document.getElementById("sessionID").textContent = sessionID;

// ── DOM refs ───────────────────────────────────────────────────────────────
const videoEl  = document.getElementById("video");
const nickEl   = document.getElementById("nick");
const colorEl  = document.getElementById("color");
const startBtn = document.getElementById("startBtn");
const listBtn  = document.getElementById("listBtn");
const userList = document.getElementById("userList");
const loader   = document.getElementById("loader");

// ── WebRTC state ───────────────────────────────────────────────────────────
let pc = null;

// ── start / reconnect ──────────────────────────────────────────────────────
async function start() {
  loader.classList.remove("hidden");

  if (pc) pc.close();

  pc = new RTCPeerConnection({
    iceServers: [{ urls: "stun:stun.l.google.com:19302" }],
  });

  pc.ontrack = ({ streams: [stream] }) => {
    videoEl.srcObject = stream;
  };

  // Esconde o loader assim que o primeiro frame do stream chegar
  videoEl.onplaying = () => loader.classList.add("hidden");

  pc.addTransceiver("video", { direction: "recvonly" });

  const offer = await pc.createOffer();
  await pc.setLocalDescription(offer);

  const res = await fetch("/offer", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      sdp: pc.localDescription.sdp,
      type: pc.localDescription.type,
      client_id: sessionID,
      nickname: nickEl.value.trim() || "Player",
      color: colorEl.value,
    }),
  });

  const answer = await res.json();
  await pc.setRemoteDescription(new RTCSessionDescription(answer));
}

startBtn.addEventListener("click", start);

// ── player list toggle ─────────────────────────────────────────────────────
listBtn.addEventListener("click", async () => {
  const isVisible = !userList.classList.contains("hidden");

  if (isVisible) {
    userList.classList.add("hidden");
    listBtn.textContent = "Mostrar Jogadores Online";
    return;
  }

  const res = await fetch("/players");
  const players = await res.json();

  userList.innerHTML = `<h3>Online:</h3>${players.map(playerCard).join("")}`;
  userList.classList.remove("hidden");
  listBtn.textContent = "Ocultar Jogadores Online";
});

// ── helpers ────────────────────────────────────────────────────────────────
function playerCard({ nickname, client_id, color }) {
  return `
    <div class="user-item">
      <div class="dot" style="background:${escapeHtml(color)}"></div>
      <div class="user-info">
        <strong>${escapeHtml(nickname)}</strong>
        <span class="user-id">ID: ${escapeHtml(client_id)}</span>
      </div>
    </div>`;
}

function escapeHtml(str) {
  return String(str).replace(/[&<>"']/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c])
  );
}
