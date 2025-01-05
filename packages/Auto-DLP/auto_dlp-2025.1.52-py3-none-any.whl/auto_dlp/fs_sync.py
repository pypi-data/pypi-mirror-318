import os.path as path
import shutil
from pathlib import Path


def sync(src: Path, dest: Path, check_modification_date=True):
    if not src.exists():
        print(f"Deleting {dest}")

    if src.is_dir():
        if dest.exists() and not dest.is_dir():
            print(f"Deleting {dest}")

        dest.mkdir(parents=True, exist_ok=True)

        for item in dest.iterdir():
            sub_path = item.relative_to(dest)
            sync(src / sub_path, dest / sub_path, check_modification_date=check_modification_date)

        for item in src.iterdir():
            sub_path = item.relative_to(src)
            sync(src / sub_path, dest / sub_path, check_modification_date=check_modification_date)
        return

    if not dest.exists():
        # dest.touch(exist_ok=True)
        dest_mod = -1
    elif dest.is_dir():
        print(f"Deleting {dest}")
        # dest.touch(exist_ok=True)
        dest_mod = -1
    else:
        dest_mod = path.getmtime(dest)


    src_mod = path.getmtime(src)

    if src_mod <= dest_mod:
        return

    shutil.copy2(src, dest)
