ignore the readme its not that important, its just a backup for the start code for getting a virtual screen when running on codespaces 

########################################################################









#!/usr/bin/env bash
set -e

# --- Remove broken Yarn repo so apt works ---
if [ -f /etc/apt/sources.list.d/yarn.list ]; then
    echo "⚠️ Removing broken Yarn repo..."
    sudo rm /etc/apt/sources.list.d/yarn.list
fi

# --- Function to free a port if already in use ---
free_port() {
    local PORT=$1
    if lsof -i TCP:$PORT -sTCP:LISTEN >/dev/null 2>&1; then
        echo "🛑 Port $PORT is in use — killing process..."
        lsof -ti TCP:$PORT -sTCP:LISTEN | xargs kill -9
        echo "✅ Port $PORT is now free."
    else
        echo "🟢 Port $PORT is already free."
    fi
}

echo "🔍 STEP 1: Checking and cleaning ports..."
free_port 5900
free_port 6080

echo "🧹 STEP 1.5: Killing leftover GUI processes..."
pkill Xvfb || true
pkill fluxbox || true
pkill x11vnc || true
pkill websockify || true

rm -f /tmp/.X1-lock
rm -f /tmp/.X11-unix/X1

echo "📦 STEP 2: Installing GUI dependencies..."
sudo apt-get update -y
sudo apt-get install -y xvfb x11vnc fluxbox websockify novnc

echo "🖥️ STEP 3: Starting virtual display server (Xvfb)..."
Xvfb :1 -screen 0 800x600x24 &
export DISPLAY=:1
sleep 2

echo "🪟 STEP 4: Launching window manager (Fluxbox)..."
fluxbox &

echo "🔐 STEP 5: Starting VNC server on port 5900..."
x11vnc -display :1 -nopw -forever -shared -rfbport 5900 &

echo "🌐 STEP 6: Starting noVNC on port 6080..."
webroot="/usr/share/novnc"
[ -d "$webroot" ] || webroot="/usr/lib/novnc"
websockify --web=$webroot 6080 localhost:5900 &

echo ""
echo "🎉 STEP 7: GUI environment is ready!"
echo "➡️ Open the Ports tab, set port 6080 to Public, then click the link."
