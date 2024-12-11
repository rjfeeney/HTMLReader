
def block_to_block_type(block):
    lines = block.split("\n")
    if block.startswith("#"):
        return "Heading"
    elif block.startswith("```"):
        return "Code"
    elif block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return "Paragraph"
        return "Quote"
    elif block.startswith(("*", "-")) and not block.startswith("**"):
        return "Unordered List"
    elif block.startswith("1. "):
        counter = 1
        for line in lines:
            if not line.startswith(f"{counter}. "):
                return "Paragraph"
            counter += 1
        return "Ordered List"
    else:
        return "Paragraph"