import re
from typing import List, Tuple
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

"""
    This function needs to conver a str to a list of text notes

    For Example: This is text with a **bolded** word

    Should become: 
    [
        TextNode("This is text with a ", "text"),
        TextNode("bolded", "bold"),
        TextNode(" word", "text"),
    ]

    TO DO: include functionality for nested inline elements
    Markdown parsers often support the nesting of inline elements. 
    For example, you can have a bold word inside of italics: This is an *italic and **bold** word*.
"""

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text: str) -> List[Tuple[str,...]]:
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches



def extract_markdown_links(text: str) -> List[Tuple[str,...]]:
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches
