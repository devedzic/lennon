"""Project configuration settings (PROJECT_DIR, format strings, etc.)
"""

from pathlib import Path

PREFERRED_DATE_FORMAT = '%b %d, %Y'
PROJECT_DIR = Path(__file__).parent

# import os
#
# print(__file__)
# print(os.path.abspath(__file__))
# print(os.path.dirname(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# print()
#
# PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
# print(PROJECT_DIR)
# print(type(PROJECT_DIR))

# from pathlib import Path
#
# print(Path(__file__))
# print(Path(__file__).parent)
# print(Path.cwd())
# print()
#
# PROJECT_DIR = Path(__file__).parent
# print(PROJECT_DIR)
# print(type(PROJECT_DIR))
# print(type(PROJECT_DIR.parent))

