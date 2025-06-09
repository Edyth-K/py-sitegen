from generate_page import generate_pages_recursive
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
    generate_public()
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)  

if __name__ == "__main__":
    main()