import sys
import os
import subprocess
from typing import List

def run_command(cmd: List[str], cwd: str = None) -> None:
    """Run a command and handle potential errors."""
    try:
        subprocess.run(cmd, cwd=cwd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {' '.join(cmd)}")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        raise

def generate_cfg(dot_dir: str, file_name: str) -> None:
    opt_cmd = ["opt", "-passes=dot-cfg", "-disable-output", file_name]
    print(f"Running opt_cmd: {' '.join(opt_cmd)}")
    run_command(opt_cmd, cwd=dot_dir)

    for dot_file in os.listdir(dot_dir):
        if dot_file.endswith(".dot"):
            png_file_name = dot_file.replace(".dot", ".png")
            dot_cmd = ["dot", "-Tpng", dot_file, "-o", png_file_name]
            print(f"Running dot_cmd: {' '.join(dot_cmd)}")
            run_command(dot_cmd, cwd=dot_dir)

def generate_ir(source_path: str, output_dir: str = "output") -> None:
    base_name = os.path.basename(source_path).replace(".c", "")
    optimization_levels = ["O1", "O2", "O3"]

    os.makedirs(output_dir, exist_ok=True)

    for opt_level in optimization_levels:
        opt_output_dir = os.path.join(output_dir, f"{base_name}_{opt_level}")
        os.makedirs(opt_output_dir, exist_ok=True)

        llvm_ir_file = os.path.join(opt_output_dir, f"{base_name}.ll")
        clang_cmd = [
            "clang", "-S", "-emit-llvm", f"-{opt_level}",
            source_path, "-o", llvm_ir_file
        ]

        print(f"Running: {' '.join(clang_cmd)}")
        run_command(clang_cmd)
        generate_cfg(opt_output_dir, f"{base_name}.ll")

def main() -> None:
    if len(sys.argv) != 2:
        print("Número incorreto de argumentos. Verifique se você incluiu o arquivo que deseja gerar cfgs")
        sys.exit(1)
    
    print("Nome do programa:", sys.argv[0])
    print("Caminho do código fonte C:", sys.argv[1])
    generate_ir(sys.argv[1])

if __name__ == "__main__":
    main()