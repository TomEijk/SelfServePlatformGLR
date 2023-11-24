from codeable_models import CClass, CBundle, add_links
from codeable_models.internal.commons import get_links
from map_models.map_domain_model import message
from metamodels.guidance_metamodel import (decision, category, pattern, variant,
                                           can_use, uses, optional_next, decide_for_all_instances_of,
                                           category_decisions_relation, do_nothing_design_solution,
                                           add_decision_option_link, add_stereotyped_link_with_how_tagged_value, option,
                                           is_a)

# categories
structural_representation_category = CClass(category, "Structural Representation Category")
structural_representation_category.add_links(message, stereotype_instances=decide_for_all_instances_of)

# patterns
atomic_parameter = CClass(pattern, "Atomic Parameter")
atomic_parameter_list = CClass(pattern, "Atomic Parameter List")
parameter_tree = CClass(pattern, "Parameter Tree")
parameter_forest = CClass(pattern, "Parameter Forest")

data_element = CClass(pattern, "Data Element")
id_element = CClass(pattern, "ID Element")
link_element = CClass(pattern, "Link Element")
metadata_element = CClass(pattern, "Metadata Element")

annotated_parameter_collection = CClass(pattern, "Annotated Parameter Collection")
pagination = CClass(pattern, "Pagination")
context_representation = CClass(pattern, "Context Representation")

# pattern variants
offset_based_pagination = CClass(pattern, "Offset-Based Pagination")
cursor_based_pagination = CClass(pattern, "Cursor-Based Pagination")
time_based_pagination = CClass(pattern, "Time-Based Pagination")

# do nothing solutions
do_nothing_pagination = CClass(do_nothing_design_solution)
do_nothing_annotated_parameter_collection = CClass(do_nothing_design_solution)
do_nothing_context_representation = CClass(do_nothing_design_solution)

# decisions
structure_of_parameter_representation_decision = CClass(decision, "Structure of Parameter Representation")
elements_stereotype_decision = \
    CClass(decision, "Meaning and Stereotypes of Message Elements")
annotated_parameter_collection_decision = CClass(decision, "Extension of Multiple Representation Elements " +
                                                 "with Additional Information Required")
context_representation_decision = CClass(decision, "Exchange of Context Information Required")
pagination_decision = CClass(decision, "Subset of High Number of Data Records with the Same Structure Required")

# add decisions to category
add_links({structure_of_parameter_representation_decision: structural_representation_category,
           elements_stereotype_decision: structural_representation_category,
           pagination_decision: structural_representation_category,
           annotated_parameter_collection_decision: structural_representation_category,
           context_representation_decision: structural_representation_category},
          association=category_decisions_relation)

# decisions option links
add_decision_option_link(structure_of_parameter_representation_decision, atomic_parameter, "scalar representation")
add_decision_option_link(structure_of_parameter_representation_decision, atomic_parameter_list, "list representation")
add_decision_option_link(structure_of_parameter_representation_decision, parameter_tree,
                         "complex representation with one root element")
add_decision_option_link(structure_of_parameter_representation_decision, parameter_forest,
                         "complex representation with multiple root elements")

add_decision_option_link(elements_stereotype_decision, data_element,
                         "a structured, data-only element")
add_decision_option_link(elements_stereotype_decision, id_element,
                         "an element containing a unique identifier")
add_decision_option_link(elements_stereotype_decision, link_element,
                         "an element containing a semantically typed hyperlink")
add_decision_option_link(elements_stereotype_decision, metadata_element,
                         "an element containing metadata annotating other elements")

add_decision_option_link(pagination_decision, pagination, "yes")
add_decision_option_link(pagination_decision, do_nothing_pagination, "no")

add_decision_option_link(annotated_parameter_collection_decision, annotated_parameter_collection, "yes")
add_decision_option_link(annotated_parameter_collection_decision, do_nothing_annotated_parameter_collection, "no")

add_decision_option_link(context_representation_decision, context_representation, "yes")
add_decision_option_link(context_representation_decision, do_nothing_context_representation, "no")

# next decision links
add_links({parameter_tree: pagination_decision,
           parameter_forest: pagination_decision,
           metadata_element: annotated_parameter_collection_decision},
          role_name="next decision", stereotype_instances=optional_next)

add_links({structure_of_parameter_representation_decision: [pagination_decision, elements_stereotype_decision],
           elements_stereotype_decision: [annotated_parameter_collection_decision]},
          role_name="next decision", stereotype_instances=optional_next)

# pattern links
add_links(
    {atomic_parameter_list: atomic_parameter,
     parameter_tree: atomic_parameter, parameter_forest: [parameter_forest, atomic_parameter,
                                                          parameter_tree,
                                                          atomic_parameter_list]},
    role_name="to", stereotype_instances=uses)
add_stereotyped_link_with_how_tagged_value(atomic_parameter_list, parameter_tree, can_use,
                                           "as wrapper structure for transport")
add_stereotyped_link_with_how_tagged_value(pagination, parameter_tree, can_use, "for output pages")
add_stereotyped_link_with_how_tagged_value(pagination, parameter_forest, can_use, "for output pages")
add_stereotyped_link_with_how_tagged_value(pagination, atomic_parameter_list, can_use, "for input query parameters")

add_links({metadata_element: data_element,
           id_element: data_element,
           link_element: id_element},
          role_name="to", stereotype_instances=is_a)

# pattern variant links
add_links({pagination: [offset_based_pagination, cursor_based_pagination, time_based_pagination]},
          role_name="to", stereotype_instances=variant)

# bundles
_all = CBundle("_all", elements=structural_representation_category.class_object.get_connected_elements())

pagination_decision_view = CBundle("pagination_decision",
                                   elements=[pagination_decision, pagination,
                                             offset_based_pagination, cursor_based_pagination,
                                             time_based_pagination, do_nothing_pagination,
                                             parameter_tree, parameter_forest])
pagination_dependencies_view = CBundle("pagination_dependencies",
                                       elements=[parameter_tree, parameter_forest, pagination,
                                                 atomic_parameter_list])

structural_representation_category_view = CBundle("structural_representation_category",
                                                  elements=[structural_representation_category,
                                                            structure_of_parameter_representation_decision,
                                                            elements_stereotype_decision,
                                                            annotated_parameter_collection_decision,
                                                            context_representation_decision,
                                                            pagination_decision,
                                                            message])
structure_of_parameter_representation_decision_view = CBundle("structure_of_parameter_representation_decision",
                                                              elements=[structure_of_parameter_representation_decision,
                                                                        atomic_parameter,
                                                                        atomic_parameter_list,
                                                                        parameter_tree, parameter_forest])
structure_of_parameter_representation_dependency_view = CBundle("structure_of_parameter_representation_dependencies",
                                                                elements=[parameter_forest, atomic_parameter_list,
                                                                          atomic_parameter, parameter_tree])

# structure_of_parameter_representation_dependency_view = CBundle("structure_of_parameter_representation_dependencies",
#                                                                 elements=[structure_of_parameter_representation,
#                                                                           atomic_parameter,
#                                                                           atomic_parameter_list,
#                                                                           parameter_tree, parameter_forest])
element_stereotypes_view = CBundle("elements_stereotypes",
                                   elements=[elements_stereotype_decision, data_element, id_element, link_element,
                                             metadata_element])

context_representation_view = CBundle("context_representation",
                                      elements=[context_representation_decision, context_representation,
                                                do_nothing_context_representation])

annotated_parameter_collection_view = CBundle("annotated_parameter_collection",
                                              elements=[annotated_parameter_collection_decision,
                                                        annotated_parameter_collection,
                                                        do_nothing_annotated_parameter_collection,
                                                        metadata_element])

pagination_dependencies_view_excludes = [link for link in
                                         get_links([parameter_tree, parameter_forest, atomic_parameter_list])
                                         if link.source != pagination]
pagination_decision_view_excludes = [link for link in get_links([parameter_tree, parameter_forest]) if
                                     link.target != pagination_decision]
structure_of_parameter_representation_excludes_for_dependencies_only = [link for link in get_links(
    [structure_of_parameter_representation_decision]) if option in link.stereotype_instances]
structure_of_parameter_representation_excludes_for_decision_only = [link for link in get_links(
    [atomic_parameter, atomic_parameter_list, parameter_tree, parameter_forest])
                                                                    if option not in link.stereotype_instances]

map_structure_views = [
    _all, {},
    element_stereotypes_view, {},
    # pagination_view, {"excluded_links": pagination_view_excludes},
    pagination_decision_view, {"excluded_links": pagination_decision_view_excludes},
    pagination_dependencies_view, {"excluded_links": pagination_dependencies_view_excludes},
    # parameter_patterns_view, {},
    structural_representation_category_view, {},
    structure_of_parameter_representation_dependency_view, {},
    structure_of_parameter_representation_decision_view, {
        "excluded_links": structure_of_parameter_representation_excludes_for_decision_only},
    context_representation_view, {},
    annotated_parameter_collection_view, {}]
