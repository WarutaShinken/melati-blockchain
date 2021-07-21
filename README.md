# Melati-blockchain

![Alt text](https://pbs.twimg.com/profile_banners/1414817722559467521/1626153982/1080x360)

# The main network is running!!

discord https://discord.gg/VDGmfmwPsX

twitter https://twitter.com/MelatiNetwork

# How to instal on ubuntu/debian
sudo apt-get update

sudo apt-get upgrade -y

# Install Git
sudo apt install git -y

# Checkout the source and install
git clone https://github.com/Melati-Network/Melati-blockchain.git -b latest --recurse-submodules

cd melati-blockchain

sh install.sh

. ./activate

# The GUI requires you have Ubuntu Desktop or a similar windowing system installed.
# You can not install and run the GUI as root

sh install-gui.sh

cd melati-blockchain-gui

npm run electron &

