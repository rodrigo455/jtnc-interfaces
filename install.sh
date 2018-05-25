#!/bin/bash

echo -e "\033[1mCertify that you have sudo privileges...\033[0m"

#Corba Modules must be in a safe order to satisfy dependency
read -r -d '' MODULES << EOM
JTRS
Packet
DevMsgCtl
Audio
Vocoder
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
	if [ -e "$OSSIEHOME/lib/${MODULE^^}Interfaces.jar" ]; then
		echo -e "\033[1mModule $MODULE already installed\033[0m"
	else
		echo "#############################################"
		echo -e "#   \033[1mBuild and Installing $MODULE Module\033[0m"
		echo "#############################################"
		cd $MODULE/ 

		echo -e "\033[1mConfigure...\033[0m"
		if ! ./reconf; then
			./reconf #try again
			wait
		fi
		if ! ./configure; then
			echo "Failed to configure $MODULE Module"
			exit 1
		fi

		#echo -e "\033[1mBuilding...\033[0m"
		#if ! make; then
		#	echo "Failed to build $MODULE Module"
		#	exit 1
		#fi

		echo -e "\033[1mBuilding and Installing...\033[0m"
		if ! sudo make install; then
			echo "Failed to install $MODULE Module"
			exit 1
		fi
	
		cd ..
	fi	
done

