import subprocess
import torch_directml

device = torch_directml.device()
print("🟢 DirectML device :", device)

powershell_path = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"

try:
    result = subprocess.check_output([
        powershell_path,
        "-Command",
        "Get-CimInstance Win32_VideoController | Select-Object -ExpandProperty Name"
    ])
    gpu_names = result.decode().strip().split("\n")
    gpu_names = [name.strip() for name in gpu_names if name.strip()]  # Nettoyer les lignes vides
    print("🎮 GPU(s) détecté(s) :")
    for name in gpu_names:
        print("   🔹", name)
except Exception as e:
    print("❌ Impossible de détecter le nom du GPU :", e)
