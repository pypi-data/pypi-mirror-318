# Kelian

Kelian is a Python library that provides a collection of useful and commonly used code snippets to speed up development and avoid reinventing the wheel. It includes utility functions, common algorithms, data manipulations, and more, designed to simplify your workflow and increase productivity.

## Installation

You can install the Kelian library via pip:

```bash
pip install kelian
```

## Examples

- [Average Time](./examples/average_time.md)
- [Encryption](./examples/encryption.md)
- [Loading Bar](./examples/loading_bar.md)
- [System](./examples/system.md)
- [Utilities](./examples/utilities.md)

## Functions

### Time Tracking

Utility to measure and average time intervals for various operations.

- `AverageTime`: Class
    - `start`: Starts a timer for a specific ID.
    - `loop`: Records both start and end times for a specific ID.
    - `stop`: Stops a timer for a specific ID.
    - `get_average`: Retrieves the average elapsed time for a specific ID or all IDs.
    - `__str__`, `__repr__`: Returns the average elapsed time(s) as a formatted string.

*([see examples of use](./examples/average_time.md))*

### Encryption

Simple functions to encrypt and decrypt data using predefined mappings or lists.

- `alpha2dict`: Maps alphabets to a dictionary for encryption.
- `list2dict`: Converts a list to a dictionary.
- `encrypt`: Encrypts a given text using predefined mappings.
- `decrypt`: Decrypts a given encrypted text.
- `encrypt_by_list`: Encrypts text based on a custom list.
- `decrypt_by_list`: Decrypts text based on a custom list.

*([see examples of use](./examples/encryption.md))*

### Loading Bar

- `ProgressBar`: Class
    - `format`: Change pattern of progress bar.
    - `update`: Increment the progress by one.
    - `display`: Return the progress bar updated or not, depending on the given parameter.
    - `__str__`, `__repr__`: Return the progress bar updated.

*([see examples of use](./examples/loading_bar.md))*

### System

Retrieve detailed information about your computer's hardware, including processor, motherboard, GPU, RAM, and more.

- `get_processor_details`: Returns details about the CPU.
- `get_motherboard_details`: Returns details about the motherboard.
- `get_gpu_details`: Returns details about the GPU.
- `get_monitor_details`: Returns details about the monitor.
- `get_cd_drive_details`: Returns details about the CD drive.
- `get_mouse_details`: Returns details about the mouse.
- `get_speaker_details`: Returns details about the speakers.
- `get_keyboard_details`: Returns details about the keyboard.
- `get_hard_disk_details`: Returns details about the hard disk.
- `get_ram_details`: Returns details about the RAM.

*([see examples of use](./examples/system.md))*

### Utility

Helper functions like hashing utilities for common tasks.

- `string2hash`: Converts a string to its sha256 hashed value.
- `fix_encoding`: Corrects common encoding issues in a text.
- `multi_replace`: Replaces multiple substrings in a text with specified values.
- `multi_replace_by_one`: Replaces multiple substrings in a text with a single specified value.
- `while_replace`: Replaces a substring in a text repeatedly until it no longer exists.

*([see examples of use](./examples/utilities.md))*

## License

This project is licensed under the MIT License. See the <a href="./LICENSE.txt">LICENSE</a> file for more details.
