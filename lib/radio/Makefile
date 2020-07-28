
# Defines the RPI variable which is needed by rc-switch/RCSwitch.h
CXXFLAGS=-DRPI

build/switchctl: /home/pi/433Utils/rc-switch/RCSwitch.o src/switchctl.o
	$(CXX) $(CXXFLAGS) $(LDFLAGS) $+ -o $@ -lwiringPi -lwiringPiDev -lcrypt
	
clean:
	$(RM) src/*.o build/switchctl
