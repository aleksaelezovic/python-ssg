import os
import shutil
import sys

from markdown_to_html_node import markdown_to_html_node


def main():
    basepath = sys.argv[1] if len(sys.argv) >= 2 else "/"
    cp_files("./static", "./docs")
    generate_pages("content", "template.html", "docs", basepath)


def generate_pages(content_dir_path, template_path, dest_dir_path, basepath):
    for d in os.listdir(content_dir_path):
        if os.path.isfile(os.path.join(content_dir_path, d)):
            if d.endswith(".md"):
                fname = d.rstrip(".md") + ".html"
                generate_page(os.path.join(content_dir_path, d), template_path, os.path.join(dest_dir_path, fname), basepath)
        else:
            generate_pages(os.path.join(content_dir_path, d), template_path, os.path.join(dest_dir_path, d), basepath)


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_doc = None
    with open(from_path) as f:
        from_doc = f.read()
    template_doc = None
    with open(template_path) as f:
        template_doc = f.read()
    title = extract_title(from_doc)
    content = markdown_to_html_node(from_doc).to_html()
    page = template_doc.replace("{{ Title }}", title).replace("{{ Content }}", content)
    page = page.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

    dest_path = os.path.abspath(dest_path)
    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w+") as f:
        f.write(page)


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
