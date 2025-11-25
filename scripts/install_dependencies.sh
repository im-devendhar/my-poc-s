
#!/bin/bash
set -e

# Change ownership so ubuntu user can write
sudo chown -R ubuntu:ubuntu /home/ubuntu/nodejs-app

# Navigate to app directory
cd /home/ubuntu/nodejs-app

# Install dependencies
npm install

