from codeable_models import CClass, CBundle
from metamodels.domain_metamodel import domain_metaclass

api = CClass(domain_metaclass, "API")
communication_participant = CClass(domain_metaclass, "Communication Participant")
api_client = CClass(domain_metaclass, "API Client", superclasses=communication_participant)
api_provider = CClass(domain_metaclass, "API Provider", superclasses=communication_participant)
api_provider.association(api, "exposes: [providers] * -> [apis] *")
api_client.association(api, "uses: [clients] * -> [apis] *")

api_endpoint = CClass(domain_metaclass, "API Endpoint")
api.association(api_endpoint, "has: [api] 1 -> [apiEndpoints] *")
communication_participant.association(api_endpoint, "uses: [participants] * -> [apiEndpoints] *")

operation = CClass(domain_metaclass, "Operation", attributes={"ID": ""})
api.association(operation, "has: [api] 1 -> [operations] *")

conversation = CClass(domain_metaclass, "Conversation")
call = CClass(domain_metaclass, "Call", superclasses=conversation)
event = CClass(domain_metaclass, "Event", superclasses=conversation)
callback = CClass(domain_metaclass, "Callback", superclasses=conversation)

operation.association(conversation, "invoked by: [operation] 1 -> [conversations] *")

message = CClass(domain_metaclass, "Message")
conversation.association(message, "uses: [conversations] * -> [messages]*")

address = CClass(domain_metaclass, "Address")
message.association(address, "contains to address: [message] 1 -> [to address] 0..1")
message.association(address, "contains from address: [message] 1 -> [to address] 0..1")
api_endpoint.association(address, "has: [endpoint] 1 -> [to address] 1")

representation = CClass(domain_metaclass, "Representation")
message.association(representation, "has: [message] 1 -> [representations] *")

parameter = CClass(domain_metaclass, "Parameter")
representation.association(parameter, "describes: [representations] * -> [parameters] *")

api_contract = CClass(domain_metaclass, "API Contract")
api_contract.association(operation, "describes: [contract] 1 -> [operations] *")
api_contract.association(api_endpoint, "describes: [contract] 1 -> [endpoints] *")
api.association(api_contract, "[api] 1 <*>- [contract] 1")
communication_participant.association(api_contract, "agrees on: [participants] * ->[contracts] *")

# bundles

_all = CBundle("_all", elements=api.get_connected_elements())
api_contract_view = CBundle("apiContract", elements=[communication_participant, api_contract, operation, api_endpoint])
communication_participant_view = CBundle("communicationParticipant",
                                         elements=[communication_participant, api_client, api_provider, api,
                                                   api_endpoint, address])
conversation_view = CBundle("conversation", elements=[conversation, call, event, callback, message])
message_view = CBundle("message", elements=[message, representation, parameter, address, api_endpoint])
operation_view = CBundle("operation", elements=[operation, api, conversation, message])
eplop19_view = CBundle("eplop19",
                       elements=[communication_participant, api_contract, operation, api_endpoint, api_client,
                                 api_provider, api, address, conversation, message])

map_domain_model_views = [_all, {},
                          api_contract_view, {},
                          communication_participant_view, {},
                          conversation_view, {},
                          message_view, {},
                          operation_view, {},
                          eplop19_view, {}]
