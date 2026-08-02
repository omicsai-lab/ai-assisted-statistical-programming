import subprocess
import sys
from pathlib import Path

scripts = [
    "ch07_data_structures.py",
    "ch08_import_inspect.py",
    "ch09_clean_recode.py",
    "ch10_descriptive_stats.py",
    "ch11_visualization.py",
    "ch12_basic_tests.py",
    "ch13_regression_models.py",
    "ch16_same_analysis.py",
]
root = Path(__file__).resolve().parent
for script in scripts:
    print("\n" + "=" * 72)
    print(f"Running {script}")
    print("=" * 72)
    subprocess.run([sys.executable, str(root / "scripts" / "python" / script)], cwd=root, check=True)
