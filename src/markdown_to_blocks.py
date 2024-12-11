
def markdown_to_blocks(markdown):
    if isinstance(markdown, str):
        new_strings = markdown.split("\n\n")
        stripped_strings = [new_string.strip() for new_string in new_strings]
        nonempty_strings = [stripped_string for stripped_string in stripped_strings if stripped_string != ""]
        return nonempty_strings
    else:
        raise TypeError("Invalid input type")