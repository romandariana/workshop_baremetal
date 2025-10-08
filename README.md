# MAX78000 Bare-Metal Workshop

Embedded software workshop using the no-OS framework on MAX78000FTHR. Learn UART/SPI communication, sensor interfacing, and real-time data processing.

## Prerequisites

### Hardware

- MAX78000FTHR development board
- USB-C cable (data-capable)
- ADXL355 accelerometer + 6 wires (for Examples 2-4)

### Software

- Linux (Ubuntu 20.04+, Debian 11+, or Raspberry Pi OS)
- ~2GB free disk space
- Internet connection

**Note:** macOS/Windows users need WSL2 or Linux VM.

## Quick Setup

```bash
cd ~/workshop_baremetal
chmod +x setup.sh
./setup.sh
```

**What it does:**

- ✅ Configures USB permissions for the programmer
- ✅ Installs ARM cross-compiler and tools
- ✅ Clones no-OS framework and ai8x-synthesis
- ✅ Installs serial communication tools

**Important:** Log out and back in after setup (required for USB permissions).

## Understanding the Framework

The no-OS framework separates hardware from application logic:

```text
┌────────────────────────────┐
│  Your Application Code     │  ← Examples live here
├────────────────────────────┤
│  Common Configuration      │  ← Shared peripheral setup
├────────────────────────────┤
│  Platform Layer (Maxim)    │  ← MAX78000-specific code
├────────────────────────────┤
│  no-OS Drivers (HAL)       │  ← UART, SPI, GPIO APIs
└────────────────────────────┘
```

**Benefits:**

- Same example code works on different MCUs
- Change pins without touching application code
- Clear separation of concerns

## Workspace Structure

After setup, your workspace looks like:

```text
~/workshop_baremetal/
├── setup.sh              # Setup script
├── ai8x-synthesis/       # OpenOCD (ARM64 support)
├── MAX78000SDK/          # Workshop SDK package
│   └── Libraries/        # ← MAXIM_LIBRARIES points here
└── no-OS/
    └── projects/
        └── workshop/     # ← Your working directory
```

## Platform Notes

### x86_64 (Desktop)

Everything works out of the box.

### ARM64 (Raspberry Pi)

The setup script automatically:

- Installs system ARM toolchain (SDK toolchain is x86-only)
- Clones ai8x-synthesis for ARM64-compatible OpenOCD
- Build system auto-detects and uses it

No manual configuration needed.

## Next Steps

✅ **Setup complete!** Navigate to the project directory:

```bash
cd ~/workshop_baremetal/no-OS/projects/workshop
```

📖 **Read the project README** for build commands and hardware setup.

📚 **Start the workshop:** Open `HANDS_ON.md` for step-by-step instructions.

## Troubleshooting Setup

### "arm-none-eabi-gcc: command not found"

```bash
sudo apt install gcc-arm-none-eabi
```

### "Permission denied" on USB/serial

```bash
# Verify groups (should see 'dialout' and 'plugdev')
groups

# If missing, log out and log back in
```

### Build fails with "MAXIM_LIBRARIES not set"

```bash
export MAXIM_LIBRARIES=$HOME/workshop_baremetal/MAX78000SDK/Libraries
export PLATFORM=maxim
export TARGET=max78000
```

### Flash fails: "unable to find CMSIS-DAP device"

- Check USB cable (must support data)
- Try different USB port
- Press reset button on board
- On Raspberry Pi: verify ai8x-synthesis is in ~/workshop_baremetal/

## Workshop Examples

| Example | Description | Hardware |
|---------|-------------|----------|
| 1 | UART Hello World | Board only |
| 2 | SPI sensor communication | + ADXL355 |
| 3 | Fixed-point math | + ADXL355 |
| 4 | IIO streaming | + ADXL355 |

## Resources

- **no-OS Documentation:** <https://analogdevicesinc.github.io/no-OS/>
- **MAX78000 Info:** <https://www.analog.com/max78000>
- **ADXL355 Datasheet:** <https://www.analog.com/adxl355>
