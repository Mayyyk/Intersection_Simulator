import sys
import subprocess
import os

if len(sys.argv) < 3:
    print("Użycie: python run_simulation.py commands.json output.json [--deterministic]")
    sys.exit(1)

input_json = sys.argv[1]
output_json = sys.argv[2]
deterministic = "--deterministic" in sys.argv

# 1. Wygeneruj input.txt
json_input_cmd = ["python", "json_to_input.py", input_json]
if deterministic:
    json_input_cmd.append("--deterministic") # Tryb testów

subprocess.run(json_input_cmd, check=True)

print("🔧 Kompilowanie main.c...")
subprocess.run(["gcc", "main.c", "-o", "main.exe"], check=True)

# 2. Uruchom program w C
subprocess.run(["./main.exe"], check=True)

# 3. Napraw output.json → fixed_output.json
subprocess.run(["python", "fix_output.py"], check=True)

# 4. Przenieś poprawiony plik do finalnej nazwy
os.replace("fixed_output.json", output_json)

print(f"✅ Gotowe! Wynik zapisano jako: {output_json}")
