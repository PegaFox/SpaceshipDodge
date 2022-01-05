echo "removing game files"
sudo rm /usr/local/games/spaceship_dodge_launch.sh
sudo rm /usr/share/pixmaps/Ship_Idle.png
rm -r ~/PegaFox/applications/spaceship_dodge
rm ~/Desktop/spaceshipDodge.desktop
rm ~/.local/share/applications/spaceshipDodge.desktop
mv code/INSTALL.sh .
mv UNINSTALL.sh code
echo "spaceship dodge has been uninstalled"
