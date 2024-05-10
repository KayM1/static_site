from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

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

# def split_nodes_delimiter(old_nodes, delimiter, text_type):
#     new_list = []
#     text_string = old_nodes[0].text
#     if text_type == text_type_bold and delimiter == "**":
#         if "**" in text_string:
#             start_bold = text_string.find("**")
#             end_bold = text_string.rfind("**")
#             if start_bold != -1 and end_bold != -1 and start_bold < end_bold:
#                 before_bold = text_string[:start_bold]
#                 bold_text = text_string[start_bold+2:end_bold]
#                 after_bold = text_string[end_bold+2:]

#                 new_list.append(TextNode(before_bold, text_type_text))
#                 new_list.append(TextNode(bold_text, text_type_bold))
#                 new_list.append(TextNode(after_bold, text_type_text))

#                 return new_list
            
#     elif text_type == text_type_italic and delimiter == "*":
#         if "*" in text_string:
#             start_ital = text_string.find("*")
#             end_ital = text_string.rfind("*")
#             if start_ital != -1 and end_ital != -1 and start_ital < end_ital:
#                 before_ital = text_string[:start_ital]
#                 ital_text = text_string[start_ital+1:end_ital]
#                 after_ital = text_string[end_ital+1:]

#                 new_list.append(TextNode(before_ital, text_type_text))
#                 new_list.append(TextNode(ital_text, text_type_italic))
#                 new_list.append(TextNode(after_ital, text_type_text))

#                 return new_list
#     elif text_type == text_type_code and delimiter == "`":
#         if "`" in text_string:
#             start_code = text_string.find("`")
#             end_code = text_string.rfind("`")
#             if start_code != -1 and end_code != -1 and start_code < end_code:
#                 before_code = text_string[:start_code]
#                 code_text = text_string[start_code+1:end_code]
#                 after_code = text_string[end_code+1:]

#                 new_list.append(TextNode(before_code, text_type_text))
#                 new_list.append(TextNode(code_text, text_type_code))
#                 new_list.append(TextNode(after_code, text_type_text))

#                 return new_list
#     else:
#         new_list.extend(old_nodes)


# testing
# print("--- test begins here ---")
# node = TextNode("This is a line with a `bold text` piece of mark up", text_type_text)
# new_nodes = split_nodes_delimiter([node], "`", text_type_code)

# print(f"--- test_result: {new_nodes} ---")