#!/bin/bash
set -e

WORKSHOP_DIR="$HOME/workshop_baremetal"
NO_OS_REPO="https://github.com/romandariana/no-OS.git"
NO_OS_BRANCH="workshop"
AI8X_REPO="https://github.com/analogdevicesinc/ai8x-synthesis.git"
MAX_SDK_ZIP="MAX78000SDK.zip"

sudo tee /etc/udev/rules.d/99-daplink.rules << 'EOF'
# DAPLink/CMSIS-DAP - USB interface
SUBSYSTEM=="usb", ATTR{idVendor}=="0d28", ATTR{idProduct}=="0204", MODE="0666"

# DAPLink/CMSIS-DAP - HID interface  
KERNEL=="hidraw*", ATTRS{idVendor}=="0d28", ATTRS{idProduct}=="0204", MODE="0666"
EOF

sudo udevadm control --reload-rules
sudo udevadm trigger

sudo usermod -a -G dialout,plugdev,tty $USER

sudo apt update
sudo apt install -y \
    gcc-arm-none-eabi \
    libusb-0.1-4 \
    libusb-1.0-0 \
    libusb-1.0-0-dev \
    libftdi-dev \
    libftdi1-dev \
    libgpiod2 \
    libhidapi-dev \
    libhidapi-libusb0 \
    picocom \
    python3-pygame

mkdir -p "$WORKSHOP_DIR"

if [ -d "$WORKSHOP_DIR/no-OS" ]; then
    echo "no-OS already exists, skipping"
else
    cd "$WORKSHOP_DIR"
    git clone -b "$NO_OS_BRANCH" "$NO_OS_REPO"
fi

if [ -d "$WORKSHOP_DIR/ai8x-synthesis" ]; then
    echo "ai8x-synthesis already exists, skipping"
else
    cd "$WORKSHOP_DIR"
    git clone "$AI8X_REPO"
fi

if [ -d "$WORKSHOP_DIR/MAX78000SDK" ]; then
    echo "MAX78000SDK already exists, skipping"
else
    cd "$WORKSHOP_DIR"
    wget https://swdownloads.analog.com/cse/kuiper/kuiperv2.0.0/university-workshops/"$MAX_SDK_ZIP"
    unzip "$MAX_SDK_ZIP"
    rm "$MAX_SDK_ZIP"
fi
