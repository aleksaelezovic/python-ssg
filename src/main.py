import os
import shutil


def main():
    cp_files("./static", "./public")


def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:]
    raise Exception("no title in markdown")


def cp_files(src, dest):
    src = os.path.abspath(src)
    dest = os.path.abspath(dest)
    if not os.path.exists(src):
        raise Exception("source directory does not exist")
    shutil.rmtree(dest, ignore_errors=True)
    os.makedirs(dest, exist_ok=True)

    for d in os.listdir(src):
        if os.path.isfile(os.path.join(src, d)):
            shutil.copy(os.path.join(src, d), dest)
        else:
            cp_files(os.path.join(src, d), os.path.join(dest, d))


if __name__ == "__main__":
    main()
