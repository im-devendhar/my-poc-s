
#!/bin/bash
cd /home/ubuntu/nodejs-app

# Kill any existing Node.js process
pkill -f "node app.js" || true

# Start the app
nohup node app.js > app.log 2>&1 &

