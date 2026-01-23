# Tool Directory

This directory contains various Python scripts for network tools and utilities.

## Files

### network.py
A command-line tool for network operations. It supports the following commands:
- `ip`: Extract IP address from a hostname.
- `paths`: Scan for common paths on a given URL.
- `status_code`: Check if a URL is up (status code 200).

Usage: `python network.py <command>`

### script.py
A script that updates itself from a local server and greets the user by asking for their name. It uses the `rich` library for colored output.

### loc.py
A password checker script that fetches a list of passwords from a local URL (`http://localhost/cyber/password.txt`) and checks if the entered password matches any in the list.

### tempCodeRunnerFile.py
A temporary file, possibly used by VS Code for running code snippets.

## Subdirectory: tools/

Contains individual modules for the network tools:

- `extract_ip.py`: Function to extract IP from hostname.
- `scan_paths.py`: Function to scan common paths on a URL.
- `status_code.py`: Function to check URL status.

These are imported by `network.py`.