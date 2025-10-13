import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block) is not None:
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    is_quote = True
    for line in block.split("\n"):
        if not line.startswith(">"):
            is_quote = False
            break
    if is_quote:
        return BlockType.QUOTE
    is_ulist = True
    for line in block.split("\n"):
        if not line.startswith("- "):
            is_ulist = False
            break
    if is_ulist:
        return BlockType.ULIST
    is_olist = True
    i = 0
    for line in block.split("\n"):
        i = i + 1
        if not line.startswith(f"{i}. "):
            is_olist = False
            break
    if is_olist:
        return BlockType.OLIST
    return BlockType.PARAGRAPH


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks
