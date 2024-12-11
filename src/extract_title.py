from markdown_to_blocks import markdown_to_blocks

def extract_title(markdown):
    if markdown == "":
        raise Exception("Empty String")
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            parts = block.split("# ")
            title = parts[1].strip()
            return title
    raise Exception("No Title Found")