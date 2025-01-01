import json
import os
import sys
from jupyter_client.kernelspec import install_kernel_spec

def install_kernel():
    kernel_name = "jupyter_native_kernel"
    kernel_spec = {
        "argv": [sys.executable, "-m", "jupyter_native_kernel", "-f", "{connection_file}"],
        "display_name": "Native",
        "language": "native",
    }

    kernel_dir = os.path.join(os.path.dirname(__file__), 'kernelspec')
    os.makedirs(kernel_dir, exist_ok=True)

    with open(os.path.join(kernel_dir, 'kernel.json'), 'w') as f:
        json.dump(kernel_spec, f, indent=2)

    install_kernel_spec(kernel_dir, kernel_name, user=True)
    print(f"Installed Jupyter kernel '{kernel_name}'.")

if __name__ == "__main__":
    install_kernel()
