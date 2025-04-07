import sys, subprocess, shutil, os

if len(sys.argv) != 3:
    print("Użycie: python run_simulation.py commands.json simulation_output.json")
    sys.exit(1)

input_json = sys.argv[1]
output_json = sys.argv[2]

subprocess.run(["python", "json_to_input.py", input_json], check = True)

subprocess.run(["./main.exe"], check=True)

subprocess.run(["python", "fix_output.py"], check=True)

os.replace("fixed_output.json", output_json)

print(f"✅ Symulacja zakończona. Wyjście zapisano do {output_json}")