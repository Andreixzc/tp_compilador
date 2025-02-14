# Control Flow Graph (CFG) Generator

This project generates Control Flow Graphs (CFGs) for C programs at different optimization levels using LLVM.

## Versions Used

- **Operating System:** Ubuntu 24.04.1 LTS  
- **Clang:** Ubuntu clang version 18.1.3 (1ubuntu1)  
- **LLVM:** Ubuntu LLVM version 18.1.3  
- **Python:** 3.12.3  

## Dependency Installation

To install the required dependencies, run the following commands:

```bash
sudo apt update
sudo apt install clang llvm python3 graphviz
```

Verify the installations with:

```bash
clang --version
llvm-config --version
python3 --version
dot -V
```

## How to Run

### For a specific program:

Use the `gen_cfg.py` script:

```bash
python3 gen_cfg.py <path_to_file.c>
```

Example:

```bash
python3 gen_cfg.py Test.c
```

### For all algorithms in the `src` folder:

Use the `gen_cfg_all.py` script:

```bash
python3 gen_cfg_all.py src
```

This script will process all `.c` files found in the `src` folder and its subdirectories.

## Project Structure

- `gen_cfg.py`: Generates a CFG for a specific C program  
- `gen_cfg_all.py`: Generates CFGs for all algorithms in the `src` folder  
- `src/`: Directory containing the C source files to be processed  

## Output

The generated CFGs will be saved in the `output/` folder in PNG format, organized by source file and optimization level.

## Additional Notes

- Ensure that all C files in the `src` folder compile correctly before running the scripts  
- The generated optimization levels are O0, O1, O2, and O3  
