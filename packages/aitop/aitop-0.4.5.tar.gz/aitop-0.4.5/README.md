# AITop - AI-Focused System Monitor

[![PyPI version](https://badge.fury.io/py/aitop.svg)](https://badge.fury.io/py/aitop)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Copyright © 2024 Alexander Warth. All rights reserved.

Current version: 0.4.5

AITop is a powerful command-line system monitor specifically designed for monitoring AI/ML workloads across different GPU architectures. It provides real-time insights into GPU utilization, memory usage, AI-specific metrics, and system performance to help developers and researchers optimize their machine learning workflows.

> **Beta Phase Notice**: AITop has now entered beta phase (v0.3.0), indicating that the core functionality is complete and stable. While the software is feature-complete and suitable for general use, you may still encounter minor bugs or areas needing refinement. We encourage users to report any issues or suggestions through our issue tracker.

## Features

- **Real-time GPU Monitoring**
  - Utilization metrics (compute, memory)
  - Memory usage and allocation
  - Temperature and power consumption
  - Fan speed and thermal performance

- **AI Workload Focus**
  - Detection of AI/ML processes
  - Tensor core utilization tracking
  - Framework-specific metrics (e.g., CUDA, ROCm, OpenCL)
  - Inference and training performance statistics

- **Multi-Vendor Support**
  - NVIDIA GPUs (via NVML)
  - AMD GPUs (via ROCm)
  - Intel GPUs (via OpenCL)

- **Customizability**
  - Configure displayed metrics
  - Customize refresh rates
  - Choose different output views (compact, detailed, graphical)

- **Interactive UI**
  - Dynamic, color-coded displays with advanced color management
  - True color support for modern terminals
  - Intelligent color fallback for basic terminals
  - Real-time graphs and charts
  - Customizable views and layouts
  - Process-specific monitoring

- **Performance Optimized**
  - Efficient metric polling with minimal impact on GPU workloads
  - Low CPU and memory overhead for seamless real-time updates
  - Smart color caching for optimal rendering performance

## Installation

### Quick Install (Recommended)

Install AITop directly from PyPI:

```bash
pip install aitop
```

For development features, install with extra dependencies:

```bash
pip install aitop[dev]
```

### From Source

1. **Clone the Repository**

   ```bash
   git clone https://gitlab.com/CochainComplex/aitop.git
   cd aitop
   ```

2. **Set Up a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -e ".[dev]"
   ```

### GPU Dependencies

   - **NVIDIA GPUs**

     Ensure NVIDIA drivers are installed and NVML is accessible.
     Tested with NVIDIA-SMI version 565.57.01.

   - **AMD GPUs**

     Install ROCm as per [ROCm Installation Guide](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html).
     Tested with:
     - ROCm 6.3
     - rocm-smi 3.0.0

   - **Intel GPUs**

     Install Intel Compute Runtime or relevant OpenCL drivers.
     Note: Intel GPU support is currently in testing phase with limited functionality.

## Quick Start

Launch AITop with the following command:

```bash
# Start AITop
aitop

# Enable debug logging
aitop --debug
```

## Usage

### Theme Configuration

AITop includes a theme system that automatically adapts to your terminal environment:

- **Automatic Detection**: Automatically selects appropriate theme based on:
  - Terminal type (VSCode, iTerm, Terminator, etc.)
  - Color support capabilities
  - Background color settings

- **Manual Override**: Set preferred theme using environment variable:
  ```bash
  # Enable 256-color support (required for some terminals)
  export TERM=xterm-256color
  
  # Set theme before running aitop
  export AITOP_THEME=default
  aitop
  ```

- **Available Themes**:
  - `default`: Standard theme based on htop colors
  - `monokai_pro`: Modern dark theme with vibrant, carefully balanced colors
  - `nord`: Arctic-inspired color palette optimized for eye comfort
  - `solarized_dark`: Scientifically designed for optimal readability
  - `material_ocean`: Modern theme based on Material Design principles
  - `stealth_steel`: Sleek gray-based palette with subtle color accents
  - `forest_sanctuary`: Nature-inspired palette with rich greens and earthen tones
  - `cyberpunk_neon`: Futuristic neon color scheme with vibrant accents

Each theme is carefully crafted for specific use cases:
- `monokai_pro`: Features a vibrant yet balanced color scheme with distinctive progress bars (▰▱)
- `nord`: Offers a cool, arctic-inspired palette that reduces eye strain with elegant progress bars (━─)
- `solarized_dark`: Uses scientifically optimized colors for maximum readability with classic block indicators (■□)
- `material_ocean`: Implements Material Design principles with circular progress indicators (●○)
- `stealth_steel`: Provides a professional, minimalist look with half-block indicators (▀░)
- `forest_sanctuary`: Delivers a natural, calming experience with bold block indicators (▮▯)
- `cyberpunk_neon`: Features a high-contrast neon palette with classic block indicators (█░)

### Color Support

AITop now features advanced color management:
- Automatic detection of terminal color capabilities
- True color support (16 million colors) for modern terminals
- Intelligent fallback for terminals with limited color support
- Color caching for optimal performance
- Smooth color approximation when exact colors aren't available

### Debug Mode

AITop supports a debug mode that can be enabled with the `--debug` flag. When enabled:
- Creates a detailed log file `aitop.log` in the current directory
- Logs comprehensive debug information including:
  - Application initialization and shutdown
  - Data collection events
  - UI rendering updates
  - Error traces and exceptions
  - System state changes
  - Theme detection and color setup
- Useful for troubleshooting issues or development


AITop provides an interactive interface with the following controls:

- **Navigation**
  - **Left/Right Arrow Keys**: Switch between tabs
  - **Up/Down Arrow Keys**: Scroll through the process list

- **Process Sorting**
  - **'c'**: Sort by CPU usage
  - **'m'**: Sort by memory usage
  - **'h'**: Toggle sort order (ascending/descending)

- **General**
  - **'q'**: Quit application

### Interface Tabs

- **Overview**: System-wide metrics including CPU, memory, and overall GPU usage.
- **AI Processes**: Lists detected AI/ML processes with detailed metrics.
- **GPU**: Detailed GPU metrics per vendor, including utilization, temperature, and power consumption.
- **Memory**: System memory statistics and usage.
- **CPU**: CPU usage and performance statistics.

For detailed project structure and component documentation, see [STRUCTURE.md](STRUCTURE.md).

## Development

### Setting Up the Development Environment

1. **Clone the Repository**

   ```bash
   git clone https://gitlab.com/CochainComplex/aitop.git
   cd aitop
   ```

2. **Create and Activate Virtual Environment**

   ```bash
   pyenv virtualenv 3.10.0 aitop
   pyenv activate aitop
   ```

3. **Install Development Dependencies**

   ```bash
   pip install -e ".[dev]"
   ```

### Running Tests

Execute the test suite using:

```bash
pytest
```

### Code Formatting

Ensure code consistency with the following tools:

- **Black**

  ```bash
  black .
  ```

- **isort**

  ```bash
  isort .
  ```

## Requirements

- **Python 3.9+**
- **NVIDIA Drivers** (for NVIDIA GPU support)
- **ROCm** (for AMD GPU support)
- **Intel Compute Runtime** (for Intel GPU support)

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. **Fork the Repository**
2. **Create Your Feature Branch**

   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m 'Add some AmazingFeature'
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/AmazingFeature
   ```

5. **Open a Pull Request**

   Discuss your changes and get feedback before merging.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Alexander Warth

## Legal Disclaimer

AITop is an independent project and is not affiliated with, endorsed by, or sponsored by NVIDIA Corporation, Advanced Micro Devices, Inc. (AMD), or Intel Corporation. All product names, logos, brands, trademarks, and registered trademarks mentioned in this project are the property of their respective owners.

- NVIDIA®, CUDA®, and NVML™ are trademarks and/or registered trademarks of NVIDIA Corporation.
- AMD® and ROCm™ are trademarks and/or registered trademarks of Advanced Micro Devices, Inc.
- Intel® is a trademark and/or registered trademark of Intel Corporation.

The use of these trademarks is for identification purposes only and does not imply any endorsement by the trademark holders. AITop provides monitoring capabilities for GPU hardware but makes no guarantees about the accuracy, reliability, or completeness of the information provided. Use at your own risk.

## Acknowledgments

Special thanks to:
- The open-source community
- All contributors and users of AITop
