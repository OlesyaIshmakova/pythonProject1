xread.py
Bulldins.
import os.path
FILES_DIR = os.path.dirname(＿file＿)
dej get_path(filename: str): return os.path.join(FILES_DIR, filename)
TXT_FILE_PATH get_path(filename "poem.txt")
CSV_FILE_PATH = get_path(filename="users.csv")
JSON_FILE_PATH = get_path(filename="users.json")
JPEG_FILE_PATH = get_path(Iilename="python.jpeg")