from codeable_models import CClass, add_links, CBundle
from map_models.map_domain_model import api, message, operation, api_contract
from metamodels.guidance_metamodel import do_nothing_design_solution, decision, practice, add_decision_option_link, \
    add_stereotyped_link_with_how_tagged_value, force, negative, uses, positive, can_be_realized_with, extension, \
    consider_if_not_decided_yet, decide_for_some_instances_of, pattern, decide_for_all_instances_of, \
    very_negative, neutral, very_positive, can_use, enables, variant, is_a, includes, leads_to, realizes


def add_force_relations(force_relations_definition):
    for practice in force_relations_definition.keys():
        for force in force_relations_definition[practice]:
            stereotype = (force_relations_definition[practice])[force]
            add_links({practice: force}, role_name="forces", stereotype_instances=stereotype)


# patterns
api_catalog = CClass(pattern, "API Catalog")
data_catalog = CClass(pattern, "Data Product Catalog") #+ searchability, +discoverability, +centrally govern
single_data_landing_zone = CClass(pattern, "Single Infrastructure Provisioning and Data Product Developer Experience Plane")
multiple_data_landing_zones = CClass(pattern, "Source system- and consumer-aligned Infrastructure Provisioning and Data Product Developer Experience Planes")
cdc = CClass(pattern, "Change Data Capture")
hub_generic_special_data_landing_zones = CClass(pattern, "Hub-, generic-, and special Infrastructure Provisioning and Data Product Developer Experience Planes")
large_scale_enterprise = CClass(pattern, "Multiple Data Mesh Governance Planes")
functional_and_regionally_aligned_data_landing_zones = CClass(pattern, "Functional and Eegionally Infrastructure Provisioning and Data Product Developer Experience Planes")
register_derived_data_as_data_product = CClass(practice, "Registering the derived batch data set as a platform's own data product")
distributed_file_storage = CClass(pattern, " Distributed file storage")
elastic_performance_engine = CClass(pattern, 'Elastic Performance Engine')
query_engine = CClass(pattern, "Query Engine")
sql_endpoint = CClass(pattern, 'SQL Endpoint')
research_groups = CClass(pattern, "Research Groups")
unified_batch_stream_processing_service = CClass(pattern, 'Unified Batch Stream Processing Service')
integration_service = CClass(pattern, 'Integration Service')
workflow_automation_engine = CClass(pattern, 'Workflow Automation Engine')
polygot_storage_option = CClass(pattern, 'Polygot Storage Option')
schema_registry = CClass(pattern, 'Schema Registry')
VMs = CClass(pattern, 'VMs')
computing_engine = CClass(pattern, 'Computing Engine')
cataloging_function = CClass(pattern, 'Cataloging Function')
data_transformation_function = CClass(pattern, "Data Transformation Function")
data_integration_function = CClass(pattern, 'Data Integration Function')
business_glossary = CClass(pattern, 'Business Glossary')
data_observability = CClass(pattern, 'Data Observability')
experimental_platform = CClass(pattern, 'Experimental Platform')
other_platforms = CClass(practice, 'Custom Platforms')
devsecops_pipeline = CClass(pattern, 'DevSecOps Pipeline')
provide_standard_api_for_data_product_owners_to_get_schema_from = CClass(pattern, 'Provide standard API for Data Product Owners to get schema from')

# practices
data_discovery = CClass(practice, "Data Discovery")
build_deploy_monitor_dp_separated = CClass(practice, 'Separate build, deploy and monitor as three autonomous functions')
build_deploy_monitor_dp_unified = CClass(practice, 'Use build, deploy and monitor as interchangeable aspects in a single function')
data_security = CClass(practice, "Data Security")
data_profiling = CClass(practice, "Data Profiling")
data_access = CClass(practice, "Data Access")
data_lineage = CClass(practice, "Data Lineage")
networking = CClass(practice, "Interconnectivity")
data_quality_management = CClass(practice, 'Check on how well data contracts are respected')
cross_cutting_concerns = CClass(practice, 'Cross-cutting Concerns')
ci_cd_process = CClass(practice, 'CI/CD process')
runtime_observability = CClass(practice, 'Runtime Observability')
application_bootstraps = CClass(practice, 'Application Bootstraps')
self_serve_ui = CClass(practice, 'Self-Serve UI')
quality_management = CClass(practice, 'Quality Management')
log_management = CClass(practice, 'Log management')
mdm = CClass(practice, "Master Data Management")
ml_services = CClass(practice, "ML services")
data_lake_services = CClass(practice, "Data Lake Service")
VNetPeering = CClass(practice, "VNetPeering")
private_endpoints = CClass(practice, "Private Endpoints")
event_streaming_backbone = CClass(pattern, "Event Streaming Backbone")
lambda_architecture = CClass(pattern, "Lambda Architecture")
kappa_architecture = CClass(pattern, "Kappa Architecture")
data_source_ingestion = CClass(practice, "Data Source Ingestion")
access_control_management = CClass(practice, "Access control management")
manage_read_write_permissions = CClass(practice, "Manage read write functions")
policy_automation = CClass(practice, "Policy Automation")
managed_compute_infrastructure = CClass(practice, "Managed Compute Infrastructure") #+ abstract away, + elastic, + adapt to change
no_code_transformation = CClass(practice, "No-code transformation")
dependable_pipeline_management = CClass(practice, "Dependable pipeline management")
automated_issue_detection = CClass(practice, "Automated issue detection")
alerting = CClass(practice, "Alerting")
resolution = CClass(practice, "Resolution")
configure_depency = CClass(practice, "Configure pipelines for dependency management")
configure_thresholds = CClass(practice, "Configure pipelines for error tolerance thresholds")
configure_scheduling = CClass(practice, "Configure pipelines for scheduling")
data_transformation_orchestration = CClass(practice, "Data Transformation Orchestration")
manage_security_policies_of_dps = CClass(practice, "Manage security policies of DPs")
manage_emergent_graphs_of_dps = CClass(practice, "Manage emergent graphs of DPs")
discovery_and_explore_dps = CClass(practice, "Discovery and explore DPs")
declaratively_create_dp = CClass(practice, "Declaratively create DP")
read_dp = CClass(practice, "Read DP")
version_dp = CClass(practice, "Version DP")
secure_dp = CClass(practice, "Secure DP")
build_deploy_monitor_dp = CClass(practice, "Build, deploy, monitor DP")
separating_storage_and_compute = CClass(practice, 'Separating storage and compute') # + scalability, + autonomous
separating_compute_from_compute = CClass(practice, 'Separating compute from compute') # + scalability, + autonomous
restore_data_without_backups = CClass(practice, 'Ability to restore data and set back without having to take care of backups')
in_place_consumption = CClass(practice, 'In-place consumption') #- data movement, + global governance, + discrepancies, - costs, + up-to-date, + access control
scale_across_platforms_and_regions = CClass(practice, 'Ability to scale globally across platforms and regions')
metadata_management = CClass(practice, 'Metadata Management')
runtime_metadata = CClass(practice, 'Automatically make runtime data available')
compatible_metadata = CClass(practice, 'Automatically publish compatible metadata')
document_dp = CClass(practice, 'Establish Data Contract')
knowledge_graph = CClass(practice, 'Knowledge Graph')
central_search_function = CClass(practice, 'Central Search Function')
set_privacy_dp = CClass(practice, 'Set privacy DP')
elastic_performance_engine = CClass(pattern, 'Elastic Performance Engine')
infrastructure_as_code = CClass(practice, 'Infrastructure as Code')
visualization_function = CClass(practice, "Visualization Function")
software_as_a_service = CClass(practice, 'Software as a Service')
uptime_checks = CClass(practice, 'Uptime checks')
cost_management = CClass(practice, 'Cost Managment')
governed_mesh_topology = CClass(practice, "Governed Mesh Topology")
reporting_services = CClass(practice, "Reporting Services")
ml_platform = CClass(practice, "ML platform")
testing_dp = CClass(practice, "Testing DP for Deployment and Provisioning")
crud_operations = CClass(practice, "CRUD operations")
collaboration_function = CClass(practice, "Collaboration Function")
building_reports_dashboards = CClass(practice, "Building reports/dashboards")
building_pipeline_function = CClass(practice, "Building pipeline function")
data_governance_function = CClass(practice, "Data Governance function")
application_build_function = CClass(practice, "Application build function")
adding_data_set_function = CClass(practice, "Adding data set function")
query_recommendation_function = CClass(practice, "Query Recommendation Function")
export_data_set_function = CClass(practice, "Export data set function")
role_based_access_control = CClass(practice, "Role-based Access Control")
feedback_loop = CClass(pattern, 'Feedback Loop')
data_product_as_self_serve = CClass(pattern, 'Data Product as Self-Serve')
persona_to_tool_approach = CClass(practice, 'Persona to Tool approach')
change_management = CClass(practice, 'Change Management')
incremental = CClass(practice, 'Incremental')
full_refresh = CClass(practice, 'Full Refresh')
access_control = CClass(practice, 'Access controls')
visualize_schemas_contracts = CClass(practice, 'Visualize Schemas and Contracts')
alerting_and_monitoring = CClass(practice, 'Alerting and Monitoring')
visualize_access = CClass(practice, 'Visualize Data Access History')

# forces
complexity = CClass(force, "Complexity")
data_quality = CClass(force, "Data Quality")
transparency = CClass(force, "Transparency")
latency = CClass(force, "Latency")
maintenance_needs = CClass(force, 'Maintenance Needs')
duplication = CClass(force, "Duplication")
ease_of_administration = CClass(force, 'Ease of Administration')
time_to_value = CClass(force, 'Time-to-Value')
agility = CClass(force, "Agility")
freshness = CClass(force, "Data Freshness")
interoperability = CClass(force, 'Interoperability')
decentralization = CClass(force, 'Decentralization')
compatibility = CClass(force, 'Compatability')
efficiency = CClass(force, 'Efficiency')
distinguish = CClass(force, "Distinguish")
domain_agnostic = CClass(force, "Domain-agnostic")
regional_legal = CClass(force, "Flexibility in regional or legal boundaries")
control_over_data = CClass(force, "Control over data")
redeliveries = CClass(force, "Redeliveries")
scalability = CClass(force, 'Scalability')
storage_function = CClass(practice, "Storage Function")
searchability = CClass(force, "Searchability")
discoverability = CClass(force, "Discoverability")
centrally_govern = CClass(practice, "Centrally govern data")
abstact_away_details = CClass(force, "Abstract away computational details")
elastic = CClass(force, "Elastic")
adapt_to_changing_volumes = CClass(force, "Adapt to changing volumes")
autonomous = CClass(force, 'Autonomous')
data_movement = CClass(force, 'Data movement')
global_governance = CClass(force, 'Global governance')
federated_analytics = CClass(force, 'Federated analytics')
delegated_ownership = CClass(force, 'Delegated ownership')
flexibility = CClass(force, 'Flexibility')
ad_hoc_exploration = CClass(force, 'Ad hoc exploration')
feature_engineering = CClass(force, 'Feature Engineering')
understandability = CClass(force, 'Understandability')
accessibility = CClass(force, 'Accessibility')
automation = CClass(force, 'Automation')
usability = CClass(force, 'Usability')
resource_deployment_process = CClass(force, 'Resource deployment process')
inconsistencies_between_deployed_resources_and_declared_code_in_source_control = CClass(force, 'Inconsistencies between deployed resources and declrared code in source control')
reduce_work_data_product_team = CClass(force, 'Reduce work done by data product team')
easily_replicable = CClass(force, 'Easily Replicable')
accuracy = CClass(force, 'Accuracy')
avoids_information_island = CClass(force, 'Avoids Information Island')
container_registry = CClass(force, 'Container Registry')
entry_barier = CClass(force, 'Entry Barrier')
security = CClass(force, 'Security')


# decisions, options, and contexts

infra_provision_decision = CClass(decision, "Which architectural design elements should be offered by the Data Infrastructure Provisioning Plane?")
add_decision_option_link(infra_provision_decision, workflow_automation_engine,
                         "Implement a workflow automation engine")
add_decision_option_link(infra_provision_decision, access_control,
                         "Provide access controls")
add_decision_option_link(infra_provision_decision, networking,
                         "Enable networking")
add_decision_option_link(infra_provision_decision, data_transformation_orchestration,
                         "Include an orchestrator for the transformations")
add_decision_option_link(infra_provision_decision, VMs,
                         "Provision VMs")
add_decision_option_link(infra_provision_decision, container_registry,
                         "Provision a container registry")
add_decision_option_link(infra_provision_decision, data_source_ingestion,
                         "Provision the data source ingestion practices")
add_decision_option_link(infra_provision_decision, managed_compute_infrastructure,
                         "Provide a managed compute infrastructure")
add_decision_option_link(infra_provision_decision, polygot_storage_option,
                         "Enable a polygot storage option")
add_decision_option_link(infra_provision_decision, other_platforms,
                         "Create a customer platform")
add_force_relations({workflow_automation_engine: {ease_of_administration: very_positive,
                                                  discoverability: positive,
                                                  time_to_value: positive,
                                                  agility: very_positive,
                                                  maintenance_needs: negative,
                                                  control_over_data: negative},
                     access_control: {transparency: positive,
                                      security: very_positive,
                                      compatibility: positive,
                                      complexity: negative,
                                      maintenance_needs: very_negative},
                    networking: {interoperability: very_positive,
                                 agility: positive,
                                 efficiency: positive,
                                 complexity: negative,
                                 domain_agnostic: negative},
                    data_transformation_orchestration: {resource_deployment_process: positive,
                                                        efficiency: positive,
                                                        automation: positive,
                                                        latency: negative,
                                                        time_to_value: negative},
                     VMs: {scalability: positive,
                           elastic: positive,
                           complexity: negative,
                           time_to_value: negative},
                     data_source_ingestion: {freshness: very_positive,
                                             interoperability: positive,
                                             discoverability: positive,
                                             resource_deployment_process: negative,
                                             complexity: negative,
                                             time_to_value: negative},
                     managed_compute_infrastructure: {scalability: very_positive,
                                                      accessibility: positive,
                                                      global_governance: positive,
                                                      complexity: negative,
                                                      maintenance_needs: negative},
                     polygot_storage_option: {autonomous: very_positive,
                                              scalability: positive,
                                              adapt_to_changing_volumes: very_positive,
                                              data_movement: negative,
                                              complexity: negative},
                     other_platforms: {agility: positive,
                                       time_to_value: positive,
                                       compatibility: positive,
                                       complexity: negative,
                                       entry_barier: negative}
                     })

ml_other = \
    ml_platform.add_links(other_platforms, role_name="from", stereotype_instances=can_use)[0]
ex_other = \
    experimental_platform.add_links(other_platforms, role_name="from", stereotype_instances=can_use)[0]

elastic_compute = \
    elastic_performance_engine.add_links(managed_compute_infrastructure, role_name="from", stereotype_instances=can_use)[0]
query_compute = \
    query_engine.add_links(managed_compute_infrastructure, role_name="from", stereotype_instances=can_use)[0]
compute_compute = \
    separating_compute_from_compute.add_links(managed_compute_infrastructure, role_name="from", stereotype_instances=can_use)[0]
compute_storage = \
    separating_storage_and_compute.add_links(managed_compute_infrastructure, role_name="from", stereotype_instances=can_use)[0]

storage_compute = \
    separating_storage_and_compute.add_links(polygot_storage_option, role_name="from", stereotype_instances=can_use)[0]
storage_distributed = \
    distributed_file_storage.add_links(polygot_storage_option, role_name="from", stereotype_instances=uses)[0]

net_pipeline = \
    dependable_pipeline_management.add_links(data_transformation_orchestration, role_name="from", stereotype_instances=can_use)[0]
net_depency = \
    configure_depency.add_links(data_transformation_orchestration, role_name="from", stereotype_instances=uses)[0]
net_thresholds = \
    configure_thresholds.add_links(data_transformation_orchestration, role_name="from", stereotype_instances=uses)[0]
net_scheduling = \
    configure_scheduling.add_links(data_transformation_orchestration, role_name="from", stereotype_instances=uses)[0]

no_code_self = \
    no_code_transformation.add_links(declaratively_create_dp, role_name="from", stereotype_instances=uses)[0]

data_product_developer_decision = CClass(decision, "What elements should be considered when designing a Data Product Developer Experience Plane?")
add_decision_option_link(data_product_developer_decision, build_deploy_monitor_dp,
                         "Provision a build, deploy, monitor interface")
add_decision_option_link(data_product_developer_decision, version_dp,
                         "Provision a versioning interface")
add_decision_option_link(data_product_developer_decision, secure_dp,
                         "Provision a security interface")
add_decision_option_link(data_product_developer_decision, read_dp,
                         "Provision a read interface")
add_decision_option_link(data_product_developer_decision, document_dp,
                         "Provision a document interface")
add_decision_option_link(data_product_developer_decision, declaratively_create_dp,
                         "Provision a declaratively create interface")
add_decision_option_link(data_product_developer_decision, testing_dp,
                         "Provision a testing interface")
add_decision_option_link(data_product_developer_decision, feedback_loop,
                         "Provision a Feedback Loop interface")
add_decision_option_link(data_product_developer_decision, crud_operations,
                         "Provision a CRUD interface")
add_force_relations({build_deploy_monitor_dp: {maintenance_needs: positive,
                                                  scalability: positive,
                                                  time_to_value: positive,
                                                transparency: positive},
                    version_dp: {federated_analytics: positive,
                                 reduce_work_data_product_team: positive,
                                 easily_replicable: positive,
                                 control_over_data: negative},
                     secure_dp: {security: positive,
                                 control_over_data: positive,
                                 entry_barier: negative,
                                 usability: negative},
                     feedback_loop: {usability: positive,
                                     understandability: positive,
                                     discoverability: positive,
                                     accuracy: negative,
                                     agility: negative},
                     read_dp: {discoverability: positive,
                               searchability: positive,
                               abstact_away_details: positive},
                    document_dp: {global_governance: very_positive,
                                  discoverability: positive,
                                  searchability: positive,
                                  inconsistencies_between_deployed_resources_and_declared_code_in_source_control: negative,
                                  maintenance_needs: negative,
                                  redeliveries: negative},
                     declaratively_create_dp: {scalability: positive,
                                               duplication: positive,
                                               automation: positive,
                                               reduce_work_data_product_team: negative},
                     testing_dp: {discoverability: positive,
                                  maintenance_needs: positive,
                                  accuracy: positive,
                                  time_to_value: negative},
                     crud_operations: {abstact_away_details: positive,
                                       reduce_work_data_product_team: positive}
                     })

issue_monitor = \
    automated_issue_detection.add_links(build_deploy_monitor_dp, role_name="from", stereotype_instances=uses)[0]
uptime_build = \
    uptime_checks.add_links(build_deploy_monitor_dp, role_name="from", stereotype_instances=uses)[0]
sep_build = \
    build_deploy_monitor_dp_separated.add_links(build_deploy_monitor_dp, role_name="from", stereotype_instances=can_be_realized_with)[0]
uni_build = \
    build_deploy_monitor_dp_unified.add_links(build_deploy_monitor_dp, role_name="from", stereotype_instances=can_be_realized_with)[0]

ci_uni = \
    ci_cd_process.add_links(build_deploy_monitor_dp_unified, role_name="from", stereotype_instances=uses)[0]

decl_infa = \
    infrastructure_as_code.add_links(declaratively_create_dp, role_name="from", stereotype_instances=uses)[0]

privacy_secure = \
    set_privacy_dp.add_links(secure_dp, role_name="from", stereotype_instances=uses)[0]
devops_secure = \
    devsecops_pipeline.add_links(secure_dp, role_name="from", stereotype_instances=uses)[0]
pol_sec = \
    policy_automation.add_links(secure_dp, role_name="from", stereotype_instances=can_use)[0]

incremetnal_test = \
    incremental.add_links(testing_dp, role_name="from", stereotype_instances=uses)[0]
full_test = \
    full_refresh.add_links(testing_dp, role_name="from", stereotype_instances=uses)[0]

sql_read = \
    sql_endpoint.add_links(read_dp, role_name="from", stereotype_instances=can_use)[0]
inplace_consumption_read = \
    in_place_consumption.add_links(read_dp, role_name="from", stereotype_instances=can_use)[0]

version_ability = \
    restore_data_without_backups.add_links(version_dp, role_name="from", stereotype_instances=enables)[0]

mesh_decision = CClass(decision, "What capabilities are accessible more conveniently on a Data Mesh Supervision Plane?")
add_decision_option_link(mesh_decision, schema_registry,
                         "Keep track of the different schemas")
add_decision_option_link(mesh_decision, api_catalog,
                         "Keep track of the different APIs")
add_decision_option_link(mesh_decision, data_observability,
                         "Monitor your data")
add_decision_option_link(mesh_decision, metadata_management,
                         "Focus on metadata management")
add_force_relations({schema_registry: {automation: positive,
                                       interoperability: positive,
                                       delegated_ownership: positive,
                                       complexity: negative,
                                       maintenance_needs: negative},
                     api_catalog: {searchability: positive,
                                   discoverability: positive,
                                   usability: very_positive,
                                   maintenance_needs: negative,
                                   resource_deployment_process: negative},
                     data_observability: {data_quality: very_positive,
                                          freshness: positive,
                                          accuracy: positive,
                                          transparency: very_positive,
                                          maintenance_needs: negative,
                                          time_to_value: negative},
                     metadata_management: {ad_hoc_exploration: very_positive,
                                           discoverability: very_positive,
                                           searchability: very_positive,
                                           accessibility: positive,
                                           delegated_ownership: positive,
                                           feature_engineering: positive,
                                           maintenance_needs: negative}
                     })

schem_api = \
    provide_standard_api_for_data_product_owners_to_get_schema_from.add_links(schema_registry, role_name="from", stereotype_instances=uses)[0]

met_dat = \
    data_catalog.add_links(metadata_management, role_name="from", stereotype_instances=uses)[0]
manage_know = \
    knowledge_graph.add_links(metadata_management, role_name="from", stereotype_instances=uses)[0]
know_manage = \
    manage_emergent_graphs_of_dps.add_links(knowledge_graph, role_name="from", stereotype_instances=uses)[0]
manage_dat = \
    manage_emergent_graphs_of_dps.add_links(data_catalog, role_name="from", stereotype_instances=uses)[0]
discover_cat = \
    discovery_and_explore_dps.add_links(data_catalog, role_name="from", stereotype_instances=uses)[0]
business_cat = \
    business_glossary.add_links(data_catalog, role_name="from", stereotype_instances=uses)[0]

quality_ob = \
    data_quality_management.add_links(data_observability, role_name="from", stereotype_instances=can_use)[0]
obser_alert = \
    alerting.add_links(data_observability, role_name="from", stereotype_instances=can_use)[0]
obser_log = \
    log_management.add_links(data_observability, role_name="from", stereotype_instances=can_use)[0]

# ** self_serve_decision **

self_serve_decision = CClass(decision, "What elements should be included in the user interface (UI) of a self-serve platform?")
add_decision_option_link(self_serve_decision, cataloging_function,
                         "Provide a cataloging function")
add_decision_option_link(self_serve_decision, data_transformation_function,
                         "Provide a pipeline building function")
add_decision_option_link(self_serve_decision, role_based_access_control,
                         "Functionalities showed to the users are based on its role")
add_decision_option_link(self_serve_decision, data_governance_function,
                         "Provide a data governance function")
add_decision_option_link(self_serve_decision, application_build_function,
                         "Provide an application build function")
add_decision_option_link(self_serve_decision, query_recommendation_function,
                         "Provide a query recommendation function")
add_force_relations({cataloging_function: {discoverability: very_positive,
                                       searchability: very_positive,
                                       usability: positive,
                                       understandability: positive,
                                       duplication: positive,
                                       resource_deployment_process: negative,
                                       complexity: negative,
                                       maintenance_needs: negative},
                     data_transformation_function: {flexibility: very_positive,
                                                    feature_engineering: positive,
                                                    inconsistencies_between_deployed_resources_and_declared_code_in_source_control: negative,
                                                    maintenance_needs: negative},
                     role_based_access_control: {delegated_ownership: positive,
                                                 control_over_data: positive,
                                                 accessibility: positive,
                                                 transparency: very_positive,
                                                 security: positive,
                                                 agility: negative,
                                                 efficiency: negative},
                     data_governance_function: {transparency: positive,
                                                security: very_positive,
                                                control_over_data: very_positive,
                                                global_governance: positive,
                                                decentralization: negative,
                                                flexibility: negative},
                     application_build_function: {automation: positive,
                                                  agility: positive,
                                                  time_to_value: positive,
                                                  complexity: negative,
                                                  global_governance: negative},
                     query_recommendation_function: {searchability: positive,
                                                     discoverability: positive,
                                                     ad_hoc_exploration: positive,
                                                     usability: very_positive,
                                                     flexibility: negative,
                                                     transparency: negative}
                     })
profile_catalog = \
    data_profiling.add_links(cataloging_function, role_name="from", stereotype_instances=enables)[0]
lineage_catalog = \
    data_lineage.add_links(cataloging_function, role_name="from", stereotype_instances=enables)[0]

pipe_trans = \
    building_pipeline_function.add_links(data_transformation_function, role_name="from", stereotype_instances=enables)[0]
line_trans = \
    data_lineage.add_links(data_transformation_function, role_name="from", stereotype_instances=enables)[0]

sec_gov = \
    data_security.add_links(data_governance_function, role_name="from", stereotype_instances=enables)[0]
col_gov = \
    collaboration_function.add_links(data_governance_function, role_name="from", stereotype_instances=can_be_realized_with)[0]
access_gov = \
    visualize_access.add_links(data_governance_function, role_name="from", stereotype_instances=enables)[0]
vis_schem = \
    visualize_schemas_contracts.add_links(data_governance_function, role_name="from", stereotype_instances=enables)[0]
alert_monitor = \
    alerting_and_monitoring.add_links(data_governance_function, role_name="from", stereotype_instances=enables)[0]

# ** mapping_decision **

mapping_decision = CClass(decision, " How to align a self-serve platform and its components with data mesh?")
add_decision_option_link(mapping_decision, single_data_landing_zone,
                         "Use a single infrastructure provisioning plane")
add_decision_option_link(mapping_decision, multiple_data_landing_zones,
                         "Use source system- and consumer-aligned infrastructure provisioning planes")
add_decision_option_link(mapping_decision, hub_generic_special_data_landing_zones,
                         "Use hub-, generic-, special infrastructure provisioning plane")
add_decision_option_link(mapping_decision, functional_and_regionally_aligned_data_landing_zones,
                         "Use functional and regionally aligned infrastructure provisioning plane")
add_decision_option_link(mapping_decision, large_scale_enterprise,
                         "Use different data mesh supervision planes")
add_force_relations({multiple_data_landing_zones: {automation: positive,
                                                   resource_deployment_process: positive,
                                                   efficiency: positive,
                                                   agility: positive,
                                                   latency: negative,
                                                   freshness: negative},
                     hub_generic_special_data_landing_zones: {agility: positive,
                                                              flexibility: positive,
                                                              adapt_to_changing_volumes: positive,
                                                              autonomous: positive,
                                                              interoperability: negative,
                                                              avoids_information_island: negative,
                                                              discoverability: negative},
                     functional_and_regionally_aligned_data_landing_zones: {federated_analytics: positive,
                                                                            flexibility: positive,
                                                                            delegated_ownership: negative,
                                                                            agility: negative},
                     large_scale_enterprise: {scalability: positive,
                                              decentralization: positive,
                                              global_governance: positive,
                                              delegated_ownership: positive,
                                              agility: negative,
                                              time_to_value: negative}
                     })

multiple_persona = \
    persona_to_tool_approach.add_links(multiple_data_landing_zones, role_name="from", stereotype_instances=can_be_realized_with)[0]

cdc_multiple = \
    cdc.add_links(multiple_data_landing_zones, role_name="from", stereotype_instances=uses)[0]
data_lake_multiple = \
    data_lake_services.add_links(multiple_data_landing_zones, role_name="from", stereotype_instances=uses)[0]
ml_multiple = \
    ml_services.add_links(multiple_data_landing_zones, role_name="from", stereotype_instances=uses)[0]
reporting_multiple = \
    reporting_services.add_links(multiple_data_landing_zones, role_name="from", stereotype_instances=uses)[0]

governed_hub = \
    governed_mesh_topology.add_links(hub_generic_special_data_landing_zones, role_name="from", stereotype_instances=uses)[0]

private_func = \
    private_endpoints.add_links(functional_and_regionally_aligned_data_landing_zones, role_name="from", stereotype_instances=uses)[0]
VNet_funct = \
    VNetPeering.add_links(functional_and_regionally_aligned_data_landing_zones, role_name="from", stereotype_instances=uses)[0]

# decision links
add_links({mesh_decision: [self_serve_decision],
           infra_provision_decision: [self_serve_decision],
           data_product_developer_decision: [self_serve_decision],
           self_serve_decision: [mapping_decision]},
          role_name="next decision", stereotype_instances=consider_if_not_decided_yet)

# decision views
forces_class_objects = [f.class_object for f in force.all_classes]

_all = CBundle("_all", elements=infra_provision_decision.class_object.get_connected_elements())
inter_decision_links_view = CBundle("inter_decision_links",
                                    elements=[mapping_decision, infra_provision_decision, data_product_developer_decision, mesh_decision, self_serve_decision])

infra_provision_decision_view = CBundle("infra_provision_decision",
                                    elements=infra_provision_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            mapping_decision.class_object,
                                            data_product_developer_decision.class_object,
                                            mesh_decision.class_object,
                                            self_serve_decision.class_object,
                                        ]))

data_product_developer_decision_view = CBundle("data_product_developer_decision",
                                    elements=data_product_developer_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            mapping_decision.class_object,
                                            infra_provision_decision.class_object,
                                            mesh_decision.class_object,
                                            self_serve_decision.class_object,
                                        ]))

mesh_decision_view = CBundle("mesh_decision",
                                    elements=mesh_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            mapping_decision.class_object,
                                            infra_provision_decision.class_object,
                                            data_product_developer_decision.class_object,
                                            self_serve_decision.class_object
                                        ]))

self_serve_decision_view = CBundle("self_serve_decision",
                                    elements=self_serve_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            mapping_decision.class_object,
                                            infra_provision_decision.class_object,
                                            data_product_developer_decision.class_object,
                                            mesh_decision.class_object
                                        ]))

mapping_decision_view = CBundle("mapping_decision",
                                    elements=mapping_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            infra_provision_decision.class_object,
                                            data_product_developer_decision.class_object,
                                            mesh_decision.class_object,
                                            self_serve_decision.class_object,
                                        ]))


self_serve_platform_views = [
    _all, {},
    inter_decision_links_view, {},
    infra_provision_decision_view, {},
    data_product_developer_decision_view, {},
    mesh_decision_view, {},
    mapping_decision_view, {},
    self_serve_decision_view, {}
]


