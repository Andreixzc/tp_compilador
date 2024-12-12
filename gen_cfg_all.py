import sys
import os
import subprocess
import glob
from typing import List

def run_command(cmd: List[str], cwd: str = None) -> subprocess.CompletedProcess:
    """Run a command and return the result."""
    try:
        return subprocess.run(cmd, check=True, capture_output=True, text=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {' '.join(cmd)}")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        raise

def generate_cfg(source_file: str, output_dir: str):
    base_name = os.path.basename(source_file).replace(".c", "")
    optimization_levels = ["O0", "O1", "O2", "O3"]

    for opt_level in optimization_levels:
        opt_output_dir = os.path.join(output_dir, f"{base_name}_{opt_level}")
        os.makedirs(opt_output_dir, exist_ok=True)

        # Generate LLVM IR
        ll_file = os.path.join(opt_output_dir, f"{base_name}.ll")
        clang_cmd = [
            "clang", "-S", "-emit-llvm", f"-{opt_level}",
            "-fno-discard-value-names", "-Xclang", "-disable-O0-optnone",
            source_file, "-o", ll_file
        ]
        print(f"Generating LLVM IR: {' '.join(clang_cmd)}")
        run_command(clang_cmd)

        if not os.path.exists(ll_file):
            print(f"Error: {ll_file} was not created.")
            continue

        # Generate dot files
        opt_cmd = ["opt", "-passes=dot-cfg", "-disable-output", ll_file]
        print(f"Generating dot files: {' '.join(opt_cmd)}")
        run_command(opt_cmd, cwd=opt_output_dir)

        # Convert dot files to PNG
        print(f"Searching for dot files in: {opt_output_dir}")
        dot_files = glob.glob(os.path.join(opt_output_dir, ".*dot"))
        if not dot_files:
            print(f"No dot files found in {opt_output_dir}")
            continue

        print(f"Found {len(dot_files)} dot files")
        for dot_file in dot_files:
            png_file = dot_file.replace(".dot", ".png").lstrip(".")
            dot_cmd = ["dot", "-Tpng", dot_file, "-o", png_file]
            print(f"Converting to PNG: {' '.join(dot_cmd)}")
            try:
                run_command(dot_cmd)
                print(f"Conversion successful: {png_file}")
            except Exception as e:
                print(f"Unexpected error during PNG conversion: {e}")

def process_directory(directory: str, output_base_dir: str):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.c'):
                source_file = os.path.abspath(os.path.join(root, file))
                relative_path = os.path.relpath(root, directory)
                output_dir = os.path.abspath(os.path.join(output_base_dir, relative_path))
                print(f"Processing file: {source_file}")
                generate_cfg(source_file, output_dir)

def main():
    if len(sys.argv) != 2:
        print("Usage: python App.py <path_to_src_directory>")
        sys.exit(1)

    src_directory = os.path.abspath(sys.argv[1])
    output_directory = os.path.abspath("output")
    os.makedirs(output_directory, exist_ok=True)

    process_directory(src_directory, output_directory)

if __name__ == "__main__":
    main()