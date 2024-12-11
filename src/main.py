import os
from copy_to_public import copy_to_public
from generate_page import generate_pages_recursive, reset_public

def main():
    static_path = "/home/rboot/site_gen/static"
    public_path = "/home/rboot/site_gen/public"
    content_path = "/home/rboot/site_gen/content"
    template_file = "/home/rboot/site_gen/template.html"
    
    reset_public()
    
    if os.path.exists(static_path):
        copy_to_public(static_path, public_path)
    else:
        print(f"Static path {static_path} does not exist")

    if os.path.exists(content_path):
        if os.path.exists(template_file):
            generate_pages_recursive(content_path, template_file, public_path)
        else:
            print(f"Template file {template_file} does not exist")
    else:
        print(f"Content path {content_path} does not exist")

if __name__ == "__main__":
    main()
