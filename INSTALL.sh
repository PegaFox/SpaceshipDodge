echo "Making game directory"
pip3 install pygame
mkdir ~/PegaFox
mkdir ~/PegaFox/applications
mkdir ~/PegaFox/applications/spaceship_dodge
echo "Setting up files"
sudo cp code/spaceship_dodge_launch.sh /usr/local/games
sudo cp code/assets/Ship_Idle.png /usr/share/pixmaps
cp -r code/assets ~/PegaFox/applications/spaceship_dodge
cp code/main.py ~/PegaFox/applications/spaceship_dodge
cp code/spaceshipDodge.desktop ~/Desktop
cp code/spaceshipDodge.desktop ~/.local/share/applications
mv code/UNINSTALL.sh .
mv INSTALL.sh code
echo "spaceship dodge has been installed"
