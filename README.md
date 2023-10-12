# xds_util - Helper script for XDS110 firmware update

## Usage

### Step 0

Clone this repository

### Step 1

First, you need to set a correct path to your ```xdsdfu```-tool to ```config.json```

This can be done by setting the value of string ```xdsfuPath``` in the config. The path string needs to end with "/" or "\\"

**Reminder**
Use /-characters in the path. If you really need to use "\\" remember to escape them (\\\\)

### Step 2

Connect the device and wait for your computer to recognize it (can take some time)

### Step 3

Run ```python xds_util.py <firmware alias>```

Firmware versions and aliases included:
|Firmware version|File|Alias|
|----------------|----|-----|
|3.0.0.16|firmware_3.0.0.16.bin|16|
|3.0.0.18|firmware_3.0.0.18.bin|18|
|3.0.0.20|firmware_3.0.0.20.bin|20|
|3.0.0.22|firmware_3.0.0.22.bin|22|

## Customization

You can edit the aliases and the files associated with them as you wish just by changing the ```config.json```. If you wish to add more firmware versions, just add them as key-value-pairs to config's ```firmwareBinaries```-object