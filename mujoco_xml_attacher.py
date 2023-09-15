import xml.etree.ElementTree as ET

def find_body(root, body_name):
    # Iterate over all 'body' elements in the document
    for body in root.iter('body'):
        if body.get('name') == body_name:
            print(ET.tostring(body, encoding='unicode'))
            return body
    raise Exception('Body with name {} not found'.format(body_name))

def include_included_files(root):
    """
    copy in all included files into the same tree
    """
    pass

def compile_defaults(root):
    """
    compile all default values into the tree, so that the defaults can be removed
    """
    pass

parent_tree = ET.parse('humanoid.xml')
child_tree = ET.parse('human_hand.xml')

parent_root = parent_tree.getroot()
child_root = child_tree.getroot()

find_body(parent_root, 'hand_right')