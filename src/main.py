from textnode import TextType, TextNode
from generate_page import generate_page
import shutil
import os

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def generate_public():
    src_path = "static/"
    dst_path = "public/"
    if (os.path.exists(dst_path)):
        shutil.rmtree(dst_path)
    shutil.copytree(src_path, dst_path)


def main():
    print("Hello World.")
    generate_public()
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )

if __name__ == "__main__":
    main()