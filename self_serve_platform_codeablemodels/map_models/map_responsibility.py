from codeable_models import CClass, add_links, CBundle
from map_models.map_domain_model import api_endpoint, operation, api
from metamodels.guidance_metamodel import decision, category, pattern, add_decision_option_link, \
    category_decisions_relation, decide_for_some_instances_of, next_decision, is_a

responsibility_category = CClass(category, "Responsibility Category")

# base model
resource_role = CClass(pattern, "Resource Role")
operation_responsibility = CClass(pattern, "Operation Responsibility")
resource_operations = resource_role.association(operation_responsibility,
                                                "responsibility: [resource] 1 -> [operation] *")
api_roles = api.association(resource_role, "role: [api] 1 -> [role] *")

# patterns
processing_resource = CClass(pattern, "Processing Resource", superclasses=[resource_role])
information_holder_resource = CClass(pattern, "Information Holder Resource", superclasses=[resource_role])

computation_function = CClass(pattern, "Computation Function", superclasses=[operation_responsibility])
state_creation_operation = CClass(pattern, "State Creation Operation", superclasses=[operation_responsibility])
retrieval_operation = CClass(pattern, "Retrieval Operation", superclasses=[operation_responsibility])
state_transition_operation = CClass(pattern, "State Transition Operation", superclasses=[operation_responsibility])

master_data_holder = CClass(pattern, "Master Data Holder", superclasses=[resource_role])
operational_data_holder = CClass(pattern, "Operational Data Holder", superclasses=[resource_role])
reference_data_holder = CClass(pattern, "Reference Data Holder", superclasses=[resource_role])
data_transfer_resource = CClass(pattern, "Data Transfer Resource", superclasses=[resource_role])
link_lookup_resource = CClass(pattern, "Link Lookup Resource", superclasses=[resource_role])

# decisions
resource_role_decision = CClass(decision, "Architectural role of an API endpoint")
operation_responsibility_decision = CClass(decision, "Responsibility of an API operation")

# decision options architectural responsibility
add_decision_option_link(resource_role_decision, processing_resource,
                         "a resource whose primary function is to process incoming commands")
add_decision_option_link(resource_role_decision, information_holder_resource,
                         "a resource whose primary function is storage and retrieval of data or meta-data")

# decision options processing or transfer operation responsibility
add_decision_option_link(operation_responsibility_decision, computation_function,
                         "an operation that computes a result solely from the input " +
                         "and does not read or write server-side state")
add_decision_option_link(operation_responsibility_decision, state_creation_operation,
                         "an operation that creates states on an API endpoint and is in essence write-only")
add_decision_option_link(operation_responsibility_decision, retrieval_operation,
                         "a read-only operation that only finds and delivers data " +
                         "without allowing clients to change it")
add_decision_option_link(operation_responsibility_decision, state_transition_operation,
                         "an operation that performs one or more activities causing a server-side state change")
# decision contexts
add_links({resource_role_decision: api_endpoint}, role_name="context",
          stereotype_instances=decide_for_some_instances_of)
add_links({operation_responsibility_decision: operation}, role_name="context",
          stereotype_instances=decide_for_some_instances_of)

# next decision links
add_links({resource_role_decision: operation_responsibility_decision},
          role_name="next decision", stereotype_instances=next_decision)

# is-a links of information holder resource
add_links({information_holder_resource: [operational_data_holder]}, role_name="to", stereotype_instances=is_a,
          label="a resource that stores short-living, operational data")
add_links({information_holder_resource: [master_data_holder]}, role_name="to", stereotype_instances=is_a,
          label="a resource that stores long-living and frequently referenced, but still mutable data")
add_links({information_holder_resource: [reference_data_holder]}, role_name="to", stereotype_instances=is_a,
          label="a resource that stores long-living data that cannot be altered by clients")
add_links({information_holder_resource: [data_transfer_resource]}, role_name="to", stereotype_instances=is_a,
          label="a resource whose primary function is to offer a shared data exchange between other resources")
add_links({information_holder_resource: [link_lookup_resource]}, role_name="to", stereotype_instances=is_a,
          label="a resource whose primary function is supporting clients " +
                "that follow or dereference links to other resources")

# add decisions to category
add_links({resource_role_decision: responsibility_category}, association=category_decisions_relation)
add_links({operation_responsibility_decision: responsibility_category}, association=category_decisions_relation)

# bundles
base_model_elements = {resource_role, operation_responsibility, api}
all_decision_model_elements = list(
    set(responsibility_category.class_object.get_connected_elements()) - base_model_elements)

_all = CBundle("_all", elements=all_decision_model_elements)
responsibility_category_view = CBundle("responsibility_category",
                                       elements=[responsibility_category,
                                                 operation_responsibility_decision, resource_role_decision,
                                                 operation, api_endpoint])
architectural_role_view = CBundle("architectural_role_decision", elements=[
    resource_role_decision, processing_resource, information_holder_resource, responsibility_category])
information_holder_resource_view = CBundle("information_holder_resources", elements=[
    information_holder_resource, operational_data_holder, master_data_holder, reference_data_holder,
    data_transfer_resource, link_lookup_resource])
operation_responsibility_view = CBundle("operation_responsibility",
                                        elements=[operation_responsibility_decision,
                                                  computation_function,
                                                  state_creation_operation,
                                                  retrieval_operation,
                                                  state_transition_operation])

map_responsibility_views = [
    _all, {},
    responsibility_category_view, {},
    architectural_role_view, {},
    information_holder_resource_view, {},
    operation_responsibility_view, {}
]

responsibility_class_model_view = CBundle("responsibility_class_model", elements=list(base_model_elements))

map_responsibility_class_views = [
    responsibility_class_model_view, {}
]
