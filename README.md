# IP Grabber Proof of Concept 

## Description

The IP Grabber is a Proof of Concept (PoC) tool that can obtain information of a machine connected to the internet. This tool is written in Python and uses several libraries and APIs to gather information such as Country, Region, City, Latitude, Longitude, ISP, Organization, AS, MAC, HWID, and PC-User name.

This tool essentially collects all available information about a device's connection to the internet. Although it can also get the MAC address and HWID, this is commented out in the default version of the script.

Please remember that this project is simply a PoC and should _not_ be used maliciously. Its intended use is for preventative measures and learning about information that is readily available on the internet. Irresponsible use could lead to legal consequences.

## Features

- Fetches IP, Country, Region, City, Latitude, Longitude, ISP, Organization, AS, MAC, HWID, and PC-User name
- Sends the collected information to a specified webhook
- Returns execution time
- Returns start time

## Note

The MAC, HWID, and PC-USER are commented out in the default version of the script. It is included for educational purposes only
