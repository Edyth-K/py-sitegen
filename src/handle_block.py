from blocktype import BlockType
import re

def markdown_to_blocks(text):
    new_list = []
    split = text.split("\n\n")
    for element in split:
        if len(element.strip()) != 0:
            new_list.append(element.strip())
    return new_list

def is_heading(block):
    matches = re.findall(r"^#{1,6} .+", block)
    return bool(matches)

def is_code(block):
    matches = re.findall(r"^```.+```$", block, re.DOTALL)
    return bool(matches)

def is_quote(block):
    matches = re.findall(r'^(>.*\n?)+$', block)
    return bool(matches)

def is_unordered_list(block):
    matches = re.findall(r'^(- .*\n?)+$', block)
    return bool(matches)

def is_ordered_list(block):
    lines = block.split('\n')
    for i in range(len(lines)):
        pre = f"{i+1}." 
        l_pre = len(pre)
        if pre != lines[i][:l_pre]:
            return False
    return True

def block_to_block_type(block):
    if is_heading(block): return BlockType.HEADING 
    if is_code(block): return BlockType.CODE 
    if is_quote(block): return BlockType.QUOTE
    if is_unordered_list(block): return BlockType.UNORDERED_LIST
    if is_ordered_list(block): return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
