from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
        else:
            text_nodes = []
            temp_words = []
            
            split_node = node.text.split(" ")
            
            for word in split_node:
                if word[0] == delimiter and word[-1] == delimiter:
                    if len(temp_words) > 0:
                        text_nodes.append(TextNode(" ".join(temp_words), text_type_text))
                        temp_words = []
                    text_nodes.append(TextNode(word[1:-1], text_type))
                elif word[0] == delimiter:
                    if len(temp_words) > 0:
                        text_nodes.append(TextNode(" ".join(temp_words), text_type_text))
                        temp_words = []
                    temp_words.append(word[1:])
                elif word[-1] == delimiter:
                    temp_words.append(word[:-1])
                    text_nodes.append(TextNode(" ".join(temp_words), text_type))
                    temp_words = []
                else:
                    temp_words.append(word)
            if len(temp_words) > 0:
                text_nodes.append(TextNode(" ".join(temp_words), text_type_text))
            
            if len(text_nodes) <= 2:
                raise ValueError("Invalid Markdown")
            
            new_nodes.extend(text_nodes)
    return new_nodes