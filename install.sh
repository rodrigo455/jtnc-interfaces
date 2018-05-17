#!/bin/bash

echo -e "\033[1mCertify that you have sudo privileges...\033[0m"

#Corba Modules must be in a safe order to satisfy dependency
read -r -d '' MODULES << EOM
JTRS
Packet
DevMsgCtl
Audio
DeviceIo
SerialPort
DevIOC
DevIOS
DevPK
DevPktSig
Ethernet
Gps
EOM

echo "$MODULES" | while read -r MODULE
do
	echo "#############################################"
	echo -e "#   \033[1mBuild and Installing $MODULE Module\033[0m"
	echo "#############################################"
	cd $MODULE/ 
	echo -e "\033[1mConfigure...\033[0m"
	./reconf
	./configure
	echo "\033[1mBuild and Install...\033[0m"
	if ! sudo make install; then
		echo "Failed to install $MODULE Module"
		exit 1
	fi
	
	wait
	cd ..

done

