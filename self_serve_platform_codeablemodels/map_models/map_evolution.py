from codeable_models import CClass, add_links, CBundle
from map_models.map_domain_model import api_endpoint, operation, api
from map_models.map_foundations import api_description
from map_models.map_structure import metadata_element
from metamodels.guidance_metamodel import decision, category, pattern, add_decision_option_link, \
    category_decisions_relation, decide_for_some_instances_of, next_decision, is_a, do_nothing_design_solution, \
    optional_next, includes, add_stereotyped_link_with_how_tagged_value, uses, can_use, can_be_combined_with

evolution_category = CClass(category, "Evolution Category")

# patterns
version_identifier = CClass(pattern, "Version Identifier")
semantic_versioning = CClass(pattern, "Semantic Versioning")
two_in_production = CClass(pattern, "Two in Production")
limited_lifetime_guarantee = CClass(pattern, "Limited Lifetime Guarantee")
eternal_limited_lifetime_guarantee = CClass(pattern, "Eternal Lifetime Guarantee")
aggressive_obsolescence = CClass(pattern, "Aggressive Obsolescence")
experimental_preview = CClass(pattern, "Experimental Preview")

# decisions
version_identification_decision = CClass(decision, "Version identification")
version_introduction_and_decommissioning_decision = CClass(decision, "Version introduction and decommissioning")
experimental_preview_decision = CClass(decision, "Offering an experimental preview")

# decision options version_identification_decision
no_versioning = CClass(do_nothing_design_solution, "No Versioning Scheme Defined")
add_decision_option_link(version_identification_decision, no_versioning,
                         "no scheme for version identification and transmission defined")
add_decision_option_link(version_identification_decision, version_identifier,
                         "use an explicit version identification and transmission scheme")
add_decision_option_link(version_identification_decision, semantic_versioning,
                         "use well-known, structured version identifier")

# decision options version_introduction_and_decommissioning_decision
add_decision_option_link(version_introduction_and_decommissioning_decision, two_in_production,
                         "support two or more incompatible versions of the API in production at any time")
add_decision_option_link(version_introduction_and_decommissioning_decision, limited_lifetime_guarantee,
                         "support API versions for a predefined lifetime")
add_decision_option_link(version_introduction_and_decommissioning_decision, eternal_limited_lifetime_guarantee,
                         "support API versions forever")
add_decision_option_link(version_introduction_and_decommissioning_decision, aggressive_obsolescence,
                         "decommission API versions as early as possible")

# decision options version_introduction_and_decommissioning_decision
no_preview = CClass(do_nothing_design_solution, "No Experimental Preview")
add_decision_option_link(experimental_preview_decision, no_preview,
                         "do not offer API previews")
add_decision_option_link(experimental_preview_decision, experimental_preview,
                         "offer API previews")

add_links({version_identification_decision: api, version_introduction_and_decommissioning_decision: api,
           experimental_preview_decision: api}, role_name="context",
          stereotype_instances=decide_for_some_instances_of)

# next decision links
add_links({version_identification_decision: version_introduction_and_decommissioning_decision,
           version_introduction_and_decommissioning_decision: experimental_preview_decision},
          role_name="next decision", stereotype_instances=optional_next)

# pattern relations
add_links({semantic_versioning: [version_identifier]}, role_name="to", stereotype_instances=can_be_combined_with)
add_stereotyped_link_with_how_tagged_value(version_identifier, metadata_element, can_use,
                                           "used to transmit identifier in a message")
add_links({api_description: version_identifier}, role_name="to", stereotype_instances=includes)

# add decisions to category
add_links({version_identification_decision: evolution_category,
           version_introduction_and_decommissioning_decision: evolution_category,
           experimental_preview_decision: evolution_category},
          association=category_decisions_relation)

# bundles

all_decision_model_elements = \
    list(evolution_category.class_object.get_connected_elements(stop_elements_inclusive= \
                                                                    [api.class_object,
                                                                     metadata_element.class_object,
                                                                     api_description.class_object]))

_all = CBundle("_all", elements=all_decision_model_elements)
evolution_category_view = CBundle("evolution_category",
                                  elements=[evolution_category,
                                            version_identification_decision,
                                            version_introduction_and_decommissioning_decision,
                                            experimental_preview_decision, api])

version_identification_decision_view = CBundle("version_identification_decision", elements= \
    version_identification_decision.class_object.get_connected_elements(
        stop_elements_inclusive=[api.class_object, metadata_element.class_object, api_description.class_object],
        stop_elements_exclusive=[evolution_category.class_object,
                                 version_introduction_and_decommissioning_decision.class_object]
    ))
version_introduction_and_decommissioning_decision_view = \
    CBundle("version_introduction_and_decommissioning_decision", elements= \
        version_introduction_and_decommissioning_decision.class_object.get_connected_elements(
            stop_elements_inclusive=[api.class_object],
            stop_elements_exclusive=[
                evolution_category.class_object,
                version_identification_decision.class_object,
                experimental_preview_decision.class_object]
        ))
experimental_preview_decision_view = CBundle("experimental_preview_decision", elements= \
    experimental_preview_decision.class_object.get_connected_elements(
        stop_elements_inclusive=[api.class_object],
        stop_elements_exclusive=[
            evolution_category.class_object,
            version_introduction_and_decommissioning_decision.class_object]
    ))

map_evolution_views = [
    _all, {},
    evolution_category_view, {},
    version_identification_decision_view, {},
    version_introduction_and_decommissioning_decision_view, {},
    experimental_preview_decision_view, {}
]
