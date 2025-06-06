

def markdown_to_blocks(text):
    new_list = []
    split = text.split("\n\n")
    for element in split:
        if len(element.strip()) != 0:
            new_list.append(element.strip())
    return new_list
