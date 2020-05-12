
# Defines the RPI variable which is needed by rc-switch/RCSwitch.h
CXXFLAGS=-DRPI

all: switchctl

switchctl: /home/pi/433Utils/rc-switch/RCSwitch.o switchctl.o
	$(CXX) $(CXXFLAGS) $(LDFLAGS) $+ -o $@ -lwiringPi -lwiringPiDev -lcrypt
	

clean:
	$(RM) *.o send codesend servo RFSniffer

