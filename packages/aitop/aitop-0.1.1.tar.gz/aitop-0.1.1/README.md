# AITop - AI-Focused System Monitor

[![PyPI version](https://badge.fury.io/py/aitop.svg)](https://badge.fury.io/py/aitop)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Copyright © 2024 Alexander Warth. All rights reserved.

Current version: 0.1.0

AITop is a powerful command-line system monitor specifically designed for monitoring AI/ML workloads across different GPU architectures. It provides real-time insights into GPU utilization, memory usage, AI-specific metrics, and system performance to help developers and researchers optimize their machine learning workflows.

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
  - Dynamic, color-coded displays
  - Real-time graphs and charts
  - Customizable views and layouts
  - Process-specific monitoring

- **Performance Optimized**
  - Efficient metric polling with minimal impact on GPU workloads
  - Low CPU and memory overhead for seamless real-time updates

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

   - **AMD GPUs**

     Install ROCm as per [ROCm Installation Guide](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html).

   - **Intel GPUs**

     Install Intel Compute Runtime or relevant OpenCL drivers.

## Quick Start

Launch AITop with the following command:

```bash
# Start AITop
aitop
```

## Usage

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

## Project Structure

```
aitop/
├── __init__.py
├── __main__.py
├── config/
│   ├── __init__.py
│   └── ai_process_patterns.json
├── core/
│   ├── __init__.py
│   ├── gpu/
│   │   ├── __init__.py
│   │   ├── amd.py
│   │   ├── base.py
│   │   ├── factory.py
│   │   ├── intel.py
│   │   └── nvidia.py
│   ├── process/
│   │   ├── __init__.py
│   │   └── monitor.py
│   └── system/
│       ├── __init__.py
│       ├── cpu.py
│       └── memory.py
├── ui/
│   ├── __init__.py
│   ├── display.py
│   └── components/
│       ├── __init__.py
│       ├── cpu_panel.py
│       ├── footer.py
│       ├── gpu_panel.py
│       ├── header.py
│       ├── memory_panel.py
│       ├── overview.py
│       ├── process_panel.py
│       └── tabs.py
├── setup.py
├── requirements.txt
├── project-structure.txt
├── LICENSE
├── .gitignore
└── aitop.egg-info/
```

## Development

### Setting Up the Development Environment

1. **Clone the Repository**

   ```bash
   git clone https://gitlab.com/CochainComplex/aitop.git
   cd aitop
   ```

2. **Create and Activate Virtual Environment**

   ```bash
   pyenv virtualenv 3.7.0 aitop
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

- **Python 3.7+**
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
