#!/bin/bash

# Kill any old ngrok processes
pkill -f ngrok > /dev/null 2>&1

echo "Starting FastAPI..."
python run.py &
SERVER_PID=$!
sleep 1

echo "Starting ngrok..."
ngrok http 8000 > /dev/null &
NGROK_PID=$!
sleep 2

NGROK_URL=$(curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url')
echo "ngrok is live at: $NGROK_URL"

wait $SERVER_PID
echo "Shutting down ngrok..."
kill $NGROK_PID
