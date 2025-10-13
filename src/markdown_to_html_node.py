from textnode import TextNode, TextType
from htmlnode import ParentNode, LeafNode
from inline_markdown import text_to_textnodes
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType


def text_to_htmlnodes(text):
    textnodes = text_to_textnodes(text)
    return list(map(lambda x: x.to_html_node(), textnodes))


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.CODE:
                content = block.lstrip("```").rstrip("```").strip()
                code_node = TextNode(content, TextType.CODE)
                pre_node = ParentNode("pre", [code_node.to_html_node()])
                block_nodes.append(pre_node)
            case BlockType.PARAGRAPH:
                text = ""
                for line in block.split("\n"):
                    text += " " + line.strip()
                children = text_to_htmlnodes(text.strip())
                p_node = ParentNode("p", children)
                block_nodes.append(p_node)
            case BlockType.QUOTE:
                text = ""
                for line in block.split("\n"):
                    text += line.lstrip(">")
                children = text_to_htmlnodes(text.strip())
                bq_node = ParentNode("blockquote", children)
                block_nodes.append(bq_node)
            case BlockType.HEADING:
                i = 0
                for ch in block:
                    if ch != "#":
                        break
                    i += 1
                h_node = LeafNode(f"h{i}", block[i+1:])
                block_nodes.append(h_node)
            case BlockType.ULIST:
                lis = []
                for line in block.split("\n"):
                    text = line.lstrip("- ").strip()
                    li = ParentNode("li", text_to_htmlnodes(text))
                    lis.append(li)
                ul = ParentNode("ul", lis)
                block_nodes.append(ul)
            case BlockType.OLIST:
                lis = []
                i = 0
                for line in block.split("\n"):
                    i += 1
                    text = line.lstrip(f"{i}. ").strip()
                    li = ParentNode("li", text_to_htmlnodes(text))
                    lis.append(li)
                ol = ParentNode("ol", lis)
                block_nodes.append(ol)
    div_node = ParentNode("div", block_nodes)
    return div_node
