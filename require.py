import importlib
import sys

def _require(pkg, install):
    try:
        return importlib.import_module(pkg)
    except ImportError:
        sys.exit(f"Error: {pkg} is not installed. Please install it using '{install}' and try again.")

np = _require('numpy', 'pip install numpy')
pd = _require('pandas', 'pip install pandas')

