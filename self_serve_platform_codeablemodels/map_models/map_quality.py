from codeable_models import CClass, CBundle, add_links
from codeable_models.internal.commons import get_links
from map_models.map_domain_model import api, api_client, operation, message
from map_models.map_foundations import api_description
from map_models.map_responsibility import link_lookup_resource
from map_models.attic.map_structure_old_more_complex import atomic_parameter_list, parameter_tree, parameter_forest
from map_models.map_structure import link_element, data_element, metadata_element
from metamodels.domain_metamodel import and_combined_group
from metamodels.guidance_metamodel import (category, practice, pattern, decision, do_nothing_design_solution,
                                           variant, realizes, can_use, can_be_combined_with, uses, influences, includes,
                                           consider_if_not_decided_yet,
                                           decide_for_some_instances_of,
                                           add_stereotyped_link_with_how_tagged_value, add_decision_option_link,
                                           requires, optional_next)

# category
quality_category = CClass(category, "Quality Category")
endpoint_specific_qualities_category = CClass(category, "Endpoint-Specific Qualities")
quality_category.add_links(endpoint_specific_qualities_category, role_name="sub category")

# practices
authentication = CClass(practice, "Authentication")
authentication_protocol = CClass(practice, "Authentication Protocol")
authorization = CClass(practice, "Authorization")
authorization_protocol = CClass(practice, "Authorization Protocol")
protocol_level_error_codes = CClass(practice, "Protocol-Level Error Codes")

# patterns
api_key = CClass(pattern, "API Key")
conditional_request = CClass(pattern, "Conditional Request")
context_representation = CClass(pattern, "Context Representation")
error_reporting = CClass(pattern, "Error Reporting")
rate_limit = CClass(pattern, "Rate Limit")
request_bundle = CClass(pattern, "Request Bundle")
service_level_agreement = CClass(pattern, "Service Level Agreement")
rate_plan = CClass(pattern, "Rate Plan")
wish_list = CClass(pattern, "Wish List")
wish_template = CClass(pattern, "Wish Template")

embedded_entity = CClass(pattern, "Embedded Entity")
linked_information_holder = CClass(pattern, "Linked Information Holder")

# pattern variants and practices
api_key_combined_with_secret_key = CClass(pattern, "API Key Combined with Secret Key")

flat_rate_subscription = CClass(pattern, "Flat-rate Subscription")
usage_based_pricing = CClass(pattern, "Usage-based Pricing")
market_based_allocation = CClass(pattern, "Market-based Allocation")
freemium_model = CClass(pattern, "Freemium Model")

sla_only_for_internal_use = CClass(pattern, "SLA only for internal use")
sla_formally_specified_sl_os = CClass(pattern, "SLA with formally specified SLOs")
sla_informally_specified_sl_os = CClass(pattern, "SLA with informally specified SLOs")

# pattern dependencies

api_key.add_links(api_key_combined_with_secret_key, role_name="to", stereotype_instances=variant)
add_links({api_key: authentication, authentication_protocol: authentication}, role_name="to",
          stereotype_instances=realizes)

add_links({rate_limit: [authentication, service_level_agreement, context_representation],
           rate_plan: [rate_limit, authentication, service_level_agreement],
           api_description: service_level_agreement,
           service_level_agreement: authentication,
           wish_list: metadata_element}, role_name="to", stereotype_instances=can_use)

add_links({freemium_model: [flat_rate_subscription, usage_based_pricing, market_based_allocation, rate_plan]},
          role_name="from", stereotype_instances=can_be_combined_with)

add_stereotyped_link_with_how_tagged_value(wish_list, atomic_parameter_list, uses, "wish list structure")
add_stereotyped_link_with_how_tagged_value(wish_list, parameter_tree, can_use, "result data structure")
add_stereotyped_link_with_how_tagged_value(wish_list, parameter_forest, can_use, "result data structure")
add_stereotyped_link_with_how_tagged_value(wish_template, parameter_tree, can_use, "request/result data structure")
add_stereotyped_link_with_how_tagged_value(wish_template, parameter_forest, can_use, "request/result data structure")

add_links({conditional_request: [wish_list, wish_template],
           request_bundle: [wish_list, wish_template, conditional_request],
           error_reporting: protocol_level_error_codes},
          role_name="to", stereotype_instances=can_be_combined_with)

rate_limit.add_links([wish_list, wish_template, conditional_request, request_bundle],
                     role_name="from", stereotype_instances=influences)

add_links({linked_information_holder: link_element,
           link_lookup_resource: link_element},
          role_name="to", stereotype_instances=requires)

add_stereotyped_link_with_how_tagged_value(linked_information_holder, link_lookup_resource, can_use,
                                           "for providing an additional level of indirection to decouple " +
                                           "resource clients and providers")

# pattern variant links
add_links({rate_plan: [flat_rate_subscription, usage_based_pricing, market_based_allocation],
           service_level_agreement: [sla_only_for_internal_use, sla_formally_specified_sl_os,
                                     sla_informally_specified_sl_os]},
          role_name="to", stereotype_instances=variant)

# decisions

do_nothing = CClass(do_nothing_design_solution)
client_identification_and_authentication = CClass(decision, "Client Identification and Authentication")
client_identification_and_authentication.add_links(endpoint_specific_qualities_category)
client_identification_and_authentication_do_nothing_link = add_decision_option_link(
    client_identification_and_authentication,
    do_nothing, "no secure identification and authentication needed")
add_decision_option_link(client_identification_and_authentication, api_key,
                         "identification and authentication via shared secret")
add_decision_option_link(client_identification_and_authentication, api_key_combined_with_secret_key,
                         "identification and authentication via shared secret, secured with secret key")
add_decision_option_link(client_identification_and_authentication, authentication_protocol,
                         "identification and authentication via a dedicated protocol")
add_decision_option_link(client_identification_and_authentication, authorization_protocol,
                         "identification and authentication via a dedicated protocol")
authorization_protocol.add_links(authentication_protocol, role_name="to", stereotype_instances=includes)

explicit_specification_of_qualities = CClass(decision, "Explicit Specification of Quality Objectives and Penalties")
explicit_specification_of_qualities.add_links(endpoint_specific_qualities_category)
add_decision_option_link(explicit_specification_of_qualities, do_nothing, "no")
add_decision_option_link(explicit_specification_of_qualities, service_level_agreement, "yes")

metering_and_charging_for_api_consumption = CClass(decision, "Metering and Charging for API Consumption")
metering_and_charging_for_api_consumption.add_links(endpoint_specific_qualities_category)
add_decision_option_link(metering_and_charging_for_api_consumption, do_nothing, "no")
add_decision_option_link(metering_and_charging_for_api_consumption, rate_plan, "yes")

prevent_api_clients_from_excessive_usage = CClass(decision, "Prevent API Clients From Excessive API Usage")
prevent_api_clients_from_excessive_usage.add_links(endpoint_specific_qualities_category)
add_decision_option_link(prevent_api_clients_from_excessive_usage, do_nothing, "no")
add_decision_option_link(prevent_api_clients_from_excessive_usage, rate_limit, "yes")

add_links({explicit_specification_of_qualities: client_identification_and_authentication,
           metering_and_charging_for_api_consumption: client_identification_and_authentication,
           prevent_api_clients_from_excessive_usage: client_identification_and_authentication},
          role_name="next decision", stereotype_instances=consider_if_not_decided_yet)

avoid_unnecessary_data_transfer = CClass(decision, "Avoid Unnecessary Data Transfer")
avoid_unnecessary_data_transfer.add_links(quality_category)
add_decision_option_link(avoid_unnecessary_data_transfer, do_nothing, "no data transfer reduction possible or wanted")
add_decision_option_link(avoid_unnecessary_data_transfer, wish_list, "use simple list to provide the information")
add_decision_option_link(avoid_unnecessary_data_transfer, wish_template,
                         "use a structured template to provide the information")

add_decision_option_link(avoid_unnecessary_data_transfer, conditional_request,
                         "make data transfer dependent on a condition in the request")
add_decision_option_link(avoid_unnecessary_data_transfer, request_bundle,
                         "bundle multiple requests in a container message")

communicate_errors = CClass(decision, "Communicate Errors")
communicate_errors.add_links(endpoint_specific_qualities_category)
add_decision_option_link(communicate_errors, do_nothing, "provide not specific solution for communicating errors")
add_decision_option_link(communicate_errors, protocol_level_error_codes,
                         "communicate errors only using the application or transport protocol error codes")
add_decision_option_link(communicate_errors, error_reporting, "perform API-level error reporting")

reference_management_decision = CClass(decision, "Handling of Referenced Data")
reference_management_decision.add_links(quality_category)
add_decision_option_link(reference_management_decision, embedded_entity,
                         "referenced data is embedded in the message representation")
add_decision_option_link(reference_management_decision, linked_information_holder,
                         "links are provided to look referenced data up with separate calls")
add_links({data_element: reference_management_decision},
          role_name="next decision", stereotype_instances=optional_next)

client_api_and_combined_group = CClass(and_combined_group)
client_api_and_combined_group.add_links([api_client, api], role_name="class")

add_links({endpoint_specific_qualities_category: client_api_and_combined_group}, role_name="context",
          stereotype_instances=decide_for_some_instances_of)
add_links({avoid_unnecessary_data_transfer: operation,
           reference_management_decision: message}, role_name="context",
          stereotype_instances=decide_for_some_instances_of)

# bundles

_all = CBundle("_all", elements=quality_category.class_object.get_connected_elements())

quality_category_view = CBundle("qualityCategory", elements=[quality_category, reference_management_decision,
                                                             message,
                                                             avoid_unnecessary_data_transfer,
                                                             operation, endpoint_specific_qualities_category,
                                                             explicit_specification_of_qualities,
                                                             metering_and_charging_for_api_consumption,
                                                             prevent_api_clients_from_excessive_usage,
                                                             client_identification_and_authentication,
                                                             communicate_errors, client_api_and_combined_group,
                                                             api_client, api])
api_key_view = CBundle("apiKey",
                       elements=[client_identification_and_authentication, api_key, api_key_combined_with_secret_key,
                                 authentication, do_nothing, authentication_protocol, authorization_protocol])
rate_limit_view = CBundle("rateLimit", elements=[prevent_api_clients_from_excessive_usage, rate_limit, authentication,
                                                 client_identification_and_authentication, do_nothing])
rate_plan_view = CBundle("ratePlan",
                         elements=[metering_and_charging_for_api_consumption, rate_plan, rate_limit, authentication,
                                   client_identification_and_authentication, do_nothing])
rate_plan_variants_view = CBundle("ratePlanVariants", elements=[rate_plan, flat_rate_subscription, usage_based_pricing,
                                                                market_based_allocation,
                                                                freemium_model])
sla_view = CBundle("sla", elements=[rate_limit, rate_plan, api_description, service_level_agreement,
                                    sla_formally_specified_sl_os,
                                    sla_informally_specified_sl_os, sla_only_for_internal_use, authentication,
                                    explicit_specification_of_qualities,
                                    client_identification_and_authentication, do_nothing])
error_reporting_view = CBundle("errorReporting",
                               elements=[communicate_errors, error_reporting, do_nothing, protocol_level_error_codes])
avoid_unnecessary_data_transfer_view = CBundle("avoidUnnecessaryDataTransfer",
                                               elements=[avoid_unnecessary_data_transfer, do_nothing,
                                                         wish_list, wish_template, conditional_request, request_bundle,
                                                         rate_limit])
avoid_unnecessary_data_transfer_combinations_view = CBundle("avoidUnnecessaryDataTransferCombinations",
                                                            elements=[request_bundle,
                                                                      conditional_request, wish_list, wish_template])

avoid_unnecessary_data_transfer_view_links = set(
    get_links([wish_list, wish_template, conditional_request, request_bundle]))
avoid_unnecessary_data_transfer_view_excluded_links = list(avoid_unnecessary_data_transfer_view_links -
                                                           set([link for link in
                                                                avoid_unnecessary_data_transfer_view_links if
                                                                link.source == avoid_unnecessary_data_transfer or
                                                                link.target == rate_limit]))

reference_management_view = CBundle("reference_management",
                                    elements=[reference_management_decision, embedded_entity, linked_information_holder,
                                              link_lookup_resource, link_element, data_element])

map_quality_views = [
    _all, {},
    quality_category_view, {},
    api_key_view, {},
    rate_limit_view, {"excluded_links": [client_identification_and_authentication_do_nothing_link]},
    rate_plan_view, {"excluded_links": [client_identification_and_authentication_do_nothing_link]},
    rate_plan_variants_view, {},
    sla_view, {"excluded_links": [client_identification_and_authentication_do_nothing_link] +
                                 [link for link in get_links([rate_limit, rate_plan]) if
                                  link.target != service_level_agreement]},
    error_reporting_view, {},
    avoid_unnecessary_data_transfer_view, {"excluded_links":
                                           avoid_unnecessary_data_transfer_view_excluded_links},
    avoid_unnecessary_data_transfer_combinations_view, {},
    reference_management_view, {}
]
