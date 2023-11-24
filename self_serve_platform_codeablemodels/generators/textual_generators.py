def _get_all_sub_classes_helper(cl, association, role_name, stereotype, visited=None):
    if visited is None:
        visited = set()
    result = []

    linked_classes = []
    links = cl.get_link_objects_for_association(association)
    for link in links:
        if stereotype in link.stereotype_instances:
            linked = link.source
            linked_role_name = association.source_role_name
            if link.source == cl:
                linked = link.target
                linked_role_name = association.role_name
            if linked_role_name == role_name:
                linked_classes.append(linked)

    for sc in linked_classes:
        if sc not in visited:
            visited.add(sc)
            result.append(sc)
            result += _get_all_sub_classes_helper(sc, association, role_name, stereotype, visited)
    return result

def get_names_list(obj_list):
    names = []
    for obj in obj_list:
        names.append(obj.name)
    return ', '.join(names)


def write_file(directory, file_name, text):
    file = open(directory + "/" + file_name, "a")
    file.write(text)
    file.close()


def get_color_coding_command(percentage):
    if percentage < 0.05:
        return "\\cll"
    if percentage < 0.10:
        return "\\cl"
    if percentage < 0.20:
        return "\\cml"
    if percentage < 0.35:
        return "\\cm"
    if percentage < 0.5:
        return "\\cmh"
    if percentage < 0.7:
        return "\\ch"
    return "\\chh"
