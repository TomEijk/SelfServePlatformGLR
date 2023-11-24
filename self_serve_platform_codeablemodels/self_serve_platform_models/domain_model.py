from codeable_models import CClass, CBundle
from map_models.map_domain_model import api
from metamodels.domain_metamodel import domain_metaclass, and_combined_group

domain_model = CClass(domain_metaclass, "Domain Model")
model_element = CClass(domain_metaclass, "Domain Model Element")
domain_model.association(model_element, "elements: [model] * -> [elements] *")

model_element_group = CClass(domain_metaclass, "Model Element Group", superclasses=model_element)
model_element_group.association(model_element, "members: [group] * -> [members] *")

shared_kernel = CClass(domain_metaclass, "Shared Kernel", superclasses=model_element_group)
bounded_context = CClass(domain_metaclass, "Bounded Context", superclasses=model_element_group)
identified_interface_elements = CClass(domain_metaclass, "Identified Interface Elements",
                                       superclasses=model_element_group)

entity = CClass(domain_metaclass, "Entity", superclasses=model_element)
value_object = CClass(domain_metaclass, "Value Object", superclasses=model_element)
service = CClass(domain_metaclass, "Service", superclasses=model_element)
aggregate = CClass(domain_metaclass, "Aggregate", superclasses=model_element_group)
repository = CClass(domain_metaclass, "Repository", superclasses=model_element)
layer = CClass(domain_metaclass, "Layer", superclasses=model_element_group)

domain_model_element_link = CClass(domain_metaclass, "Link", superclasses=model_element_group)
model_element.association(domain_model_element_link, "links from: [from] * -> [link] 1")
domain_model_element_link.association(model_element, "links to: [link] 1 -> [to] *")

domain_model_and_api = CClass(and_combined_group, "Domain Model and API")
domain_model_and_api.add_links([domain_model, api], role_name="class")

# View
ddd_domain_model = CBundle("ddd_domain_model", elements=domain_model.get_connected_elements())

domain_model_views = [
    ddd_domain_model, {}
]
