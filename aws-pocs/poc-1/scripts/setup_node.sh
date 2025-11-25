
#!/bin/bash
set -e

# Update package index
sudo apt-get update -y

# Install Node.js 16.x from NodeSource (you can change to 18.x or 20.x)
curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -

# Install Node.js and npm
sudo apt-get install -y nodejs

