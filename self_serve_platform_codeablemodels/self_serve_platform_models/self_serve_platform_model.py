from codeable_models import CClass, add_links, CBundle
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
federated_query_engine = CClass(pattern, "Federated Query Engine")
stream_batch_data_connectors = CClass(pattern, "Stream/Batch Data Connectors") 
batch_stream_data_processors = CClass(pattern, "Batch Stream Data Processors")
bi_tools = CClass(pattern, "BI Tools")
polygot_data_storage = CClass(pattern, "Polygot DAta Storage")
event_stream_platform = CClass(pattern, "Event Stream Platform")
schema_registry = CClass(pattern, "Schema Registry")
model_store = CClass(pattern, "Model Store")
metadata_store = CClass(practice, "Metadata Store")
bi_tool_connectors = CClass(pattern, "BI Tool Connectors")
legacy_and_operational_system_connectors = CClass(pattern, 'Legacy and Operational System Connectors')
connector_repository = CClass(pattern, "Connector Repository")
pipeline_orchestrator = CClass(pattern, 'Pipeline Orchestrator')
pipeline_workflow = CClass(pattern, "Pipeline/Workflow")
external_dsl = CClass(pattern, 'External DSL')
embedded_dsl = CClass(pattern, 'Embedded DSL')
low_no_code_programming_model = CClass(pattern, 'Low/no Code Programming Model')
pipeline_connectors = CClass(pattern, 'Pipeline Connectors')
data_pipeline = CClass(pattern, 'Data Pipeline')
ml_pipeline = CClass(pattern, 'ML Pipeline')
template_repository = CClass(pattern, 'Template Repository')
cataloging_product_assets = CClass(pattern, 'Cataloging Product Assets')
api_catalog = CClass(pattern, 'API Catalog')
data_catalog = CClass(pattern, 'Data Catalog')
pull_model = CClass(pattern, 'Pull Model')
push_model = CClass(pattern, 'Push Model')
policy_as_code = CClass(pattern, 'Policy-as-Code')
authoring_tools = CClass(pattern, 'Authoring Tools')
policy_engines = CClass(pattern, 'Policy Engines')
data_quality_checkers = CClass(pattern, 'Data Quality Checkers')
access_and_identity_manager = CClass(pattern, 'Access and Identity Manager')
privacy_enhancing_technologies = CClass(pattern, 'Privacy-Enhancing Technologies (PET)')
networking = CClass(pattern, 'Networking')
compute = CClass(pattern, 'Compute')
container_orchestrators = CClass(pattern, 'Container Orchestrators')
container_registry = CClass(pattern, 'Container Registry')
containers = CClass(pattern, 'Containers')
auto_scaling = CClass(pattern, 'Auto-scaling')
iac = CClass(pattern, 'IaC')
iac_based_orchestrators = CClass(pattern, 'IaC based Orchestrators')
vpc = CClass(pattern, 'VPC')
multi_tenancy = CClass(pattern, 'Multi-tenancy')
vms = CClass(pattern, 'VMs')
faas = CClass(pattern, 'FaaS')
faas_orchestrators = CClass(pattern, 'FaaS Orchestrators')
ci_cd_pipeline = CClass(pattern, 'CI-CD Pipeline')
ci_cd_platform = CClass(pattern, 'CI-CD Platform')
version_control_system = CClass(pattern, 'Version Control System')
library = CClass(pattern, 'Library')
cli = CClass(pattern, 'CLI')
web_ui = CClass(pattern, 'Web UI')
web_api = CClass(pattern, 'Web API')
low_level_catalog_apis = CClass(pattern, 'Low-level Catalog APIs')
data_product_contract = CClass(pattern, 'Data Product Contract')
metric_calculation_pipeline = CClass(pattern, 'Metric Calculation Pipeline')
data_product_code_repository = CClass(pattern, 'Data Product Code Repository')
push_pull_notfication = CClass(pattern, 'Push/pull Notification')
global_data_lineage_graphs = CClass(pattern, 'Global Data Lineage Graphs')
alerts = CClass(pattern, 'Alerts')
high_level_policy_enforcement_api = CClass(pattern, 'High-level Policy Enforcement API')
data_mesh_graphs = CClass(pattern, 'Data Mesh Graphs')

# practices
ingesting_data_from_various_sources = CClass(practice, "Ingesting Data from Various Sources")
sending_data_to_various_sinks = CClass(practice, 'Sending Data to Various Sinks')
transforming_data = CClass(practice, 'Transforming Data')
storing_various_data = CClass(practice, "Storing Various Data")
storing_other_various_assets = CClass(practice, "Storing Other Various Assets")
how_to_support_orchestration_of_complex_data_transformations = CClass(practice, "ADD 1.1: How to support orchestration of complex data transformations?")
how_to_support_generalists_as_well_data_engineers_in_product_teams_in_writing_data_transformations = CClass(practice, "ADD 1.2: How to support generalists as well data engineers in product teams in writing data transformations?")
how_to_support_customization_and_reuse_of_pipelines = CClass(practice, "ADD 1.3: How to support customization and reuse of pipelines?")
pipeline_templates = CClass(practice, 'Pipeline Templates')
monitoring_infrastructure_resources = CClass(practice, 'Monitoring Infrastructure Resources, Product Components and Assets')
defining_and_enforcing_of_governance_policies = CClass(practice, 'Defining and Enforcing of Governance Policies')
resource_usage_and_cost_management = CClass(practice, 'Resource Usage and Cost Management')
alert_generation = CClass(practice, 'Alert Generation')
log_management = CClass(practice, 'Log Management')
how_to_publish_assets_information = CClass(practice, 'How to publish assets information?')
how_to_catalog_various_assets = CClass(practice, 'How to catalog various assets?')
how_to_propagate_the_changes_to_the_status_of_assets = CClass(practice, 'How to propagate the changes to the status of assets?')
what_deployment_options_should_be_supported = CClass(practice, "What deployment options should be supported?")
how_should_resources_be_provisioned_and_managed = CClass(practice, 'How should resources be provisioned and managed?')
how_should_resources_be_shared_among_domain_terms_while_ensuring_workload_isolation = CClass(practice, 'How should resources be shared among domain terms while ensuring workload isolation?')
build_scripts_and_ui = CClass(practice, 'Build Scripts and UI')
how_to_automate_building_delivery_and_deployment_of_product_and_platform_components = CClass(practice, 'How to automate building, delivery, and deployment of product and platform components?')
what_should_be_the_form_of_the_apis_of_the_infrastructure_utility_plane = CClass(practice, 'What should be the form of the APIs of the infrastructure utility plane?')
should_a_platform_component_be_built_or_bought = CClass(practice, 'Should a component be built or bought?')
how_should_the_features_and_usage_workflows_of_a_platform_component_be_decided = CClass(practice, 'How should the features and usage workflows of a platform component be decided?')
build_dp = CClass(practice, 'Build DP')
test_dp = CClass(practice, 'Test DP')
deploy_dp = CClass(practice, 'Deploy DP')
publish_dp = CClass(practice, 'Publish DP')
connect_and_read_dp = CClass(practice, 'Connect and Read DP')
monitor_dp = CClass(practice, 'Monitor DP')
govern_dp = CClass(practice, 'Govern DP')
evolve_dp = CClass(practice, 'Evolve DP')
version_dp = CClass(practice, 'Version DP')
how_to_enable_developers_to_correctly_assemble_all_code_units_and_treat_them_as_a_single_architectural_quantum = CClass(practice, 'How to enable developers to correctly assemble all code units and treat them as a single architectural quantum?')
how_to_make_the_experience_of_discovering_detailed_information_of_a_product_uniform = CClass(practice, 'How to make the experience of discovering detailed information of a product uniform?')
how_to_enable_consumers_to_provide_the_feedback_on_a_product = CClass(practice, 'How to enable comnsumers to provide the feedback on a product?')
how_to_safely_change_products_and_notify_changes = CClass(practice, 'How to safely change products and how to notify changes?')
how_to_automate_building_and_delivery_of_dps = CClass(practice, 'How to automate building and delivery of DPs?')
product_blueprint = CClass(practice, 'Product Blueprint')
personas_first = CClass(practice, 'Personas-first')
tool_first = CClass(practice, 'Tool-first')
build = CClass(practice, 'Build')
buy = CClass(practice, 'Buy')
data_product_metric = CClass(practice, 'Data Product Metric')
ci_cd_integration = CClass(practice, 'CI-CD Integration')
iac_blueprint = CClass(practice, 'IaC Blueprint')
data_catalog_template = CClass(practice, 'Data Catalog Template')
register_data_products = CClass(practice, 'Register Data Products')
search_data_products = CClass(practice, 'Search Data Products')
monitor_data_mesh = CClass(practice, 'Monitor Data Mesh')
govern_data_mesh = CClass(practice, 'Govern Data Mesh')
how_to_provide_a_uniform_experience_for_registering_and_browsing_data_products = CClass(practice, 'How to provide a uniform experience for registering and browsing data products?')
data_mesh_dashboard = CClass(practice, 'Data Mesh Dashboard')
how_to_enforce_global_policies = CClass(practice, 'How to enforce global policies?')
how_to_enforce_data_contracts = CClass(practice, 'How to enforce data contracts?')
data_product_registry = CClass(practice, 'Data Product Registry')
what_should_be_displaced_in_the_dashboard = CClass(practice, 'What should be displaced in the dashboard?')
automated = CClass(practice, 'Automated')
manual_or_semi_automated = CClass(practice, 'Manual or Semi-Automated')
data_product_access_history = CClass(practice, 'Data Product Access History')

# decisions, options, and contexts

infra_decision = CClass(decision, "Which capabilities/APIs should be offered by the infrastructure utility plane for executing data product components, and how?")
add_decision_option_link(infra_decision, ingesting_data_from_various_sources,
                         "Option")
add_decision_option_link(infra_decision, sending_data_to_various_sinks,
                         "Option")
add_decision_option_link(infra_decision, transforming_data,
                         "Option")
add_decision_option_link(infra_decision, storing_various_data,
                         "Option")
add_decision_option_link(infra_decision, storing_other_various_assets,
                         "Option")

ing_fed = \
    federated_query_engine.add_links(ingesting_data_from_various_sources, role_name="from", stereotype_instances=can_use)[0]
ing_stream = \
    stream_batch_data_connectors.add_links(ingesting_data_from_various_sources, role_name="from", stereotype_instances=can_use)[0]

send_stream = \
    stream_batch_data_connectors.add_links(sending_data_to_various_sinks, role_name="from", stereotype_instances=can_use)[0]
trans_batch = \
    batch_stream_data_processors.add_links(transforming_data, role_name="from", stereotype_instances=can_use)[0]
support_trans = \
    how_to_support_orchestration_of_complex_data_transformations.add_links(transforming_data, role_name="from", stereotype_instances=can_use)[0]
trans_bi = \
    bi_tools.add_links(transforming_data, role_name="from", stereotype_instances=can_use)[0]
trans_eng = \
    how_to_support_generalists_as_well_data_engineers_in_product_teams_in_writing_data_transformations.add_links(transforming_data, role_name="from", stereotype_instances=can_use)[0]
pol_store = \
    polygot_data_storage.add_links(storing_various_data, role_name="from", stereotype_instances=can_use)[0]
even_plat = \
    event_stream_platform.add_links(storing_various_data, role_name="from", stereotype_instances=can_use)[0]
store_reg = \
    schema_registry.add_links(storing_other_various_assets, role_name="from", stereotype_instances=uses)[0]
store_model = \
    model_store.add_links(storing_other_various_assets, role_name="from", stereotype_instances=can_use)[0]
store_meta = \
    metadata_store.add_links(storing_other_various_assets, role_name="from", stereotype_instances=uses)[0]
leg_stream = \
    legacy_and_operational_system_connectors.add_links(stream_batch_data_connectors, role_name="from", stereotype_instances=uses)[0]
bi_stream = \
    bi_tool_connectors.add_links(stream_batch_data_connectors, role_name="from", stereotype_instances=uses)[0]
orches_pipe = \
    pipeline_workflow.add_links(how_to_support_orchestration_of_complex_data_transformations, role_name="from", stereotype_instances=uses)[0]
pipe_pipe = \
    pipeline_orchestrator.add_links(pipeline_workflow, role_name="from", stereotype_instances=uses)[0]
pipe_conn = \
    connector_repository.add_links(pipeline_connectors, role_name="from", stereotype_instances=uses)[0]
pipe_cuss = \
    pipeline_connectors.add_links(how_to_support_customization_and_reuse_of_pipelines, role_name="from", stereotype_instances=uses)[0]
pipe_temp = \
    pipeline_templates.add_links(how_to_support_customization_and_reuse_of_pipelines, role_name="from", stereotype_instances=uses)[0]
data_pipe = \
    data_pipeline.add_links(pipeline_workflow, role_name="from", stereotype_instances=uses)[0]
ml_data = \
    data_pipeline.add_links(ml_pipeline, role_name="from", stereotype_instances=uses)[0]
work_ml = \
    ml_pipeline.add_links(pipeline_workflow, role_name="from", stereotype_instances=uses)[0]
temp_pipe = \
    pipeline_templates.add_links(pipeline_workflow, role_name="from", stereotype_instances=uses)[0]
temp_cus = \
    how_to_support_customization_and_reuse_of_pipelines.add_links(pipeline_workflow, role_name="from", stereotype_instances=uses)[0]
ext_sup = \
    external_dsl.add_links(how_to_support_generalists_as_well_data_engineers_in_product_teams_in_writing_data_transformations, role_name="from", stereotype_instances=uses)[0]
emb_sup = \
    embedded_dsl.add_links(how_to_support_generalists_as_well_data_engineers_in_product_teams_in_writing_data_transformations, role_name="from", stereotype_instances=uses)[0]
low_gen = \
    low_no_code_programming_model.add_links(how_to_support_generalists_as_well_data_engineers_in_product_teams_in_writing_data_transformations, role_name="from", stereotype_instances=uses)[0]
low_gen = \
    template_repository.add_links(pipeline_templates, role_name="from", stereotype_instances=uses)[0]

gov_decision = CClass(decision, "Which capabilities should be offered by the data infrastructure plane for various governance functions at the product level and mesh level and how?")
add_decision_option_link(gov_decision, cataloging_product_assets,
                         "Option")
add_decision_option_link(gov_decision, defining_and_enforcing_of_governance_policies,
                         "Option")
add_decision_option_link(gov_decision, monitoring_infrastructure_resources,
                         "Option")

how_cat = \
    how_to_catalog_various_assets.add_links(cataloging_product_assets, role_name="from", stereotype_instances=can_use)[0]
api_how = \
    api_catalog.add_links(how_to_catalog_various_assets, role_name="from", stereotype_instances=can_use)[0]
data_how = \
    data_catalog.add_links(how_to_catalog_various_assets, role_name="from", stereotype_instances=can_use)[0]
model_how = \
    model_store.add_links(how_to_catalog_various_assets, role_name="from", stereotype_instances=can_use)[0]
pub_cat = \
    how_to_publish_assets_information.add_links(cataloging_product_assets, role_name="from", stereotype_instances=can_use)[0]
prop_cat = \
    how_to_propagate_the_changes_to_the_status_of_assets.add_links(cataloging_product_assets, role_name="from", stereotype_instances=can_use)[0]
pull_cat = \
    pull_model.add_links(how_to_publish_assets_information, role_name="from", stereotype_instances=can_use)[0]
push_cat = \
    push_model.add_links(how_to_publish_assets_information, role_name="from", stereotype_instances=can_use)[0]
pull_prop = \
    pull_model.add_links(how_to_propagate_the_changes_to_the_status_of_assets, role_name="from", stereotype_instances=can_use)[0]
push_prop = \
    push_model.add_links(how_to_propagate_the_changes_to_the_status_of_assets, role_name="from", stereotype_instances=can_use)[0]
pol_for = \
    policy_as_code.add_links(defining_and_enforcing_of_governance_policies, role_name="from", stereotype_instances=can_use)[0]
auth_pol = \
    authoring_tools.add_links(policy_as_code, role_name="from", stereotype_instances=can_use)[0]
pol_pol = \
    policy_engines.add_links(policy_as_code, role_name="from", stereotype_instances=can_use)[0]
qual_pol = \
    data_quality_checkers.add_links(policy_as_code, role_name="from", stereotype_instances=can_use)[0]
access_pol = \
    access_and_identity_manager.add_links(policy_as_code, role_name="from", stereotype_instances=can_use)[0]
priv_pol = \
    privacy_enhancing_technologies.add_links(policy_as_code, role_name="from", stereotype_instances=can_use)[0]
alert_mon = \
    alert_generation.add_links(monitoring_infrastructure_resources, role_name="from", stereotype_instances=can_use)[0]
log_mon = \
    log_management.add_links(monitoring_infrastructure_resources, role_name="from", stereotype_instances=can_use)[0]
res_mon = \
    resource_usage_and_cost_management.add_links(monitoring_infrastructure_resources, role_name="from", stereotype_instances=can_use)[0]

dep_decision = CClass(decision, "Which capabilities should be offered by the infrastructure utility plane for deploying products, and how?")
add_decision_option_link(dep_decision, what_deployment_options_should_be_supported,
                         "Option")
add_decision_option_link(dep_decision, how_should_resources_be_provisioned_and_managed,
                         "Option")
add_decision_option_link(dep_decision, how_should_resources_be_shared_among_domain_terms_while_ensuring_workload_isolation,
                         "Option")
net_what = \
    networking.add_links(what_deployment_options_should_be_supported, role_name="from", stereotype_instances=can_use)[0]
com_what = \
    compute.add_links(what_deployment_options_should_be_supported, role_name="from", stereotype_instances=can_use)[0]
con_com = \
    containers.add_links(compute, role_name="from", stereotype_instances=can_use)[0]
vm_com = \
    vms.add_links(compute, role_name="from", stereotype_instances=can_use)[0]
fa_com = \
    faas.add_links(compute, role_name="from", stereotype_instances=can_use)[0]
con_con = \
    container_orchestrators.add_links(containers, role_name="from", stereotype_instances=can_use)[0]
reg_con = \
    container_registry.add_links(containers, role_name="from", stereotype_instances=can_use)[0]
fa_fa = \
    faas_orchestrators.add_links(faas, role_name="from", stereotype_instances=can_use)[0]
build_how = \
    build_scripts_and_ui.add_links(how_should_resources_be_provisioned_and_managed, role_name="from", stereotype_instances=can_use)[0]
auto_how = \
    auto_scaling.add_links(how_should_resources_be_provisioned_and_managed, role_name="from", stereotype_instances=can_use)[0]
iac_how = \
    iac.add_links(how_should_resources_be_provisioned_and_managed, role_name="from", stereotype_instances=can_use)[0]
iac_orch = \
    iac_based_orchestrators.add_links(iac, role_name="from", stereotype_instances=can_use)[0]
vpc_how = \
    vpc.add_links(how_should_resources_be_shared_among_domain_terms_while_ensuring_workload_isolation, role_name="from", stereotype_instances=can_use)[0]
mutli_how = \
    multi_tenancy.add_links(how_should_resources_be_shared_among_domain_terms_while_ensuring_workload_isolation, role_name="from", stereotype_instances=can_use)[0]

cross_decision = CClass(decision, "What are the cross-cutting capabilities and processes of the infrastructure plane?")
add_decision_option_link(cross_decision, how_to_automate_building_delivery_and_deployment_of_product_and_platform_components,
                         "Option")
add_decision_option_link(cross_decision, what_should_be_the_form_of_the_apis_of_the_infrastructure_utility_plane,
                         "Option")
add_decision_option_link(cross_decision, should_a_platform_component_be_built_or_bought,
                         "Option")
add_decision_option_link(cross_decision, how_should_the_features_and_usage_workflows_of_a_platform_component_be_decided,
                         "Option")

ci_how = \
    ci_cd_pipeline.add_links(how_to_automate_building_delivery_and_deployment_of_product_and_platform_components, role_name="from", stereotype_instances=can_use)[0]
ci_ci = \
    ci_cd_platform.add_links(ci_cd_pipeline, role_name="from", stereotype_instances=can_use)[0]
ci_ver = \
    version_control_system.add_links(ci_cd_pipeline, role_name="from", stereotype_instances=can_use)[0]
lib_wha = \
    library.add_links(what_should_be_the_form_of_the_apis_of_the_infrastructure_utility_plane, role_name="from", stereotype_instances=can_use)[0]
cli_wha = \
    cli.add_links(what_should_be_the_form_of_the_apis_of_the_infrastructure_utility_plane, role_name="from", stereotype_instances=can_use)[0]
ui_wha = \
    web_ui.add_links(what_should_be_the_form_of_the_apis_of_the_infrastructure_utility_plane, role_name="from", stereotype_instances=can_use)[0]
api_wha = \
    web_api.add_links(what_should_be_the_form_of_the_apis_of_the_infrastructure_utility_plane, role_name="from", stereotype_instances=can_use)[0]
build_should = \
    build.add_links(should_a_platform_component_be_built_or_bought, role_name="from", stereotype_instances=can_use)[0]
buy_should = \
    buy.add_links(should_a_platform_component_be_built_or_bought, role_name="from", stereotype_instances=can_use)[0]
pers_work = \
    personas_first.add_links(how_should_the_features_and_usage_workflows_of_a_platform_component_be_decided, role_name="from", stereotype_instances=can_use)[0]
tool_work = \
    tool_first.add_links(how_should_the_features_and_usage_workflows_of_a_platform_component_be_decided, role_name="from", stereotype_instances=can_use)[0]

product_decision = CClass(decision, "Which capabilities should be offered by the data product experience plane?")
add_decision_option_link(product_decision, build_dp,
                         "Option")
add_decision_option_link(product_decision, test_dp,
                         "Option")
add_decision_option_link(product_decision, deploy_dp,
                         "Option")
add_decision_option_link(product_decision, publish_dp,
                         "Option")
add_decision_option_link(product_decision, connect_and_read_dp,
                         "Option")
add_decision_option_link(product_decision, monitor_dp,
                         "Option")
add_decision_option_link(product_decision, govern_dp,
                         "Option")
add_decision_option_link(product_decision, evolve_dp,
                         "Option")
add_decision_option_link(product_decision, version_dp,
                         "Option")

dev_build = \
    how_to_enable_developers_to_correctly_assemble_all_code_units_and_treat_them_as_a_single_architectural_quantum.add_links(build_dp, role_name="from", stereotype_instances=can_use)[0]
dev_test = \
    how_to_enable_developers_to_correctly_assemble_all_code_units_and_treat_them_as_a_single_architectural_quantum.add_links(test_dp, role_name="from", stereotype_instances=can_use)[0]
dev_dep = \
    how_to_enable_developers_to_correctly_assemble_all_code_units_and_treat_them_as_a_single_architectural_quantum.add_links(deploy_dp, role_name="from", stereotype_instances=can_use)[0]
connect_make = \
    how_to_make_the_experience_of_discovering_detailed_information_of_a_product_uniform.add_links(connect_and_read_dp, role_name="from", stereotype_instances=can_use)[0]
monitor_make = \
    how_to_make_the_experience_of_discovering_detailed_information_of_a_product_uniform.add_links(test_dp, role_name="from", stereotype_instances=can_use)[0]
enable_connect = \
    how_to_enable_consumers_to_provide_the_feedback_on_a_product.add_links(connect_and_read_dp, role_name="from", stereotype_instances=can_use)[0]
evolve_safely = \
    how_to_safely_change_products_and_notify_changes.add_links(evolve_dp, role_name="from", stereotype_instances=can_use)[0]
version_safely = \
    version_dp.add_links(how_to_safely_change_products_and_notify_changes, role_name="from", stereotype_instances=can_use)[0]
push_not = \
    push_pull_notfication.add_links(how_to_safely_change_products_and_notify_changes, role_name="from", stereotype_instances=can_use)[0]
data_enable = \
    data_product_code_repository.add_links(how_to_enable_consumers_to_provide_the_feedback_on_a_product, role_name="from", stereotype_instances=can_use)[0]
low_feedback = \
    low_level_catalog_apis.add_links(how_to_enable_consumers_to_provide_the_feedback_on_a_product, role_name="from", stereotype_instances=can_use)[0]
data_discover = \
    data_product_metric.add_links(how_to_make_the_experience_of_discovering_detailed_information_of_a_product_uniform, role_name="from", stereotype_instances=can_use)[0]
contract_discover = \
    data_product_contract.add_links(how_to_make_the_experience_of_discovering_detailed_information_of_a_product_uniform, role_name="from", stereotype_instances=can_use)[0]
contract_publish = \
    data_product_contract.add_links(publish_dp, role_name="from", stereotype_instances=can_use)[0]
blue_dev = \
    product_blueprint.add_links(how_to_enable_developers_to_correctly_assemble_all_code_units_and_treat_them_as_a_single_architectural_quantum, role_name="from", stereotype_instances=can_use)[0]
ci_automate = \
    ci_cd_integration.add_links(how_to_automate_building_and_delivery_of_dps, role_name="from", stereotype_instances=can_use)[0]
iac_blue = \
    iac_blueprint.add_links(product_blueprint, role_name="from", stereotype_instances=can_use)[0]
catalog_template = \
    data_catalog_template.add_links(product_blueprint, role_name="from", stereotype_instances=can_use)[0]
low_catalog = \
    low_level_catalog_apis.add_links(data_catalog_template, role_name="from", stereotype_instances=can_use)[0]
data_calc = \
    metric_calculation_pipeline.add_links(data_product_metric, role_name="from", stereotype_instances=can_use)[0]

experience_decision = CClass(decision, "What capabilities should be offered by a data mesh experience plane and how?")
add_decision_option_link(experience_decision, register_data_products,
                         "Option")
add_decision_option_link(experience_decision, search_data_products,
                         "Option")
add_decision_option_link(experience_decision, monitor_data_mesh,
                         "Option")
add_decision_option_link(experience_decision, govern_data_mesh,
                         "Option")

uniform_reg = \
    how_to_provide_a_uniform_experience_for_registering_and_browsing_data_products.add_links(register_data_products, role_name="from", stereotype_instances=can_use)[0]
uniform_search = \
    how_to_provide_a_uniform_experience_for_registering_and_browsing_data_products.add_links(search_data_products, role_name="from", stereotype_instances=can_use)[0]
mon_dash = \
    data_mesh_dashboard.add_links(monitor_data_mesh, role_name="from", stereotype_instances=can_use)[0]
enf_pol = \
    how_to_enforce_global_policies.add_links(govern_data_mesh, role_name="from", stereotype_instances=can_use)[0]
enf_gov = \
    how_to_enforce_data_contracts.add_links(govern_data_mesh, role_name="from", stereotype_instances=can_use)[0]
aut_pol = \
    automated.add_links(how_to_enforce_global_policies, role_name="from", stereotype_instances=can_use)[0]
aut_con = \
    automated.add_links(how_to_enforce_data_contracts, role_name="from", stereotype_instances=can_use)[0]
man_pol = \
    manual_or_semi_automated.add_links(how_to_enforce_global_policies, role_name="from", stereotype_instances=can_use)[0]
man_con = \
    manual_or_semi_automated.add_links(how_to_enforce_data_contracts, role_name="from", stereotype_instances=can_use)[0]
reg_prov = \
    data_product_registry.add_links(how_to_provide_a_uniform_experience_for_registering_and_browsing_data_products, role_name="from", stereotype_instances=can_use)[0]
reg_dash = \
    data_product_registry.add_links(what_should_be_displaced_in_the_dashboard, role_name="from", stereotype_instances=can_use)[0]
dash_dash = \
    what_should_be_displaced_in_the_dashboard.add_links(data_mesh_dashboard, role_name="from", stereotype_instances=can_use)[0]
access_dash = \
    data_product_access_history.add_links(what_should_be_displaced_in_the_dashboard, role_name="from", stereotype_instances=can_use)[0]
mesh_dash = \
    data_mesh_graphs.add_links(what_should_be_displaced_in_the_dashboard, role_name="from", stereotype_instances=can_use)[0]
alert_dash = \
    alerts.add_links(what_should_be_displaced_in_the_dashboard, role_name="from", stereotype_instances=can_use)[0]
alert_auto = \
    alerts.add_links(automated, role_name="from", stereotype_instances=can_use)[0]
high_auto = \
    high_level_policy_enforcement_api.add_links(automated, role_name="from", stereotype_instances=can_use)[0]
high_manual = \
    high_level_policy_enforcement_api.add_links(manual_or_semi_automated, role_name="from", stereotype_instances=can_use)[0]


# decision links
add_links({infra_decision: [gov_decision],
           gov_decision: [dep_decision],
           dep_decision: [cross_decision],
           cross_decision: [product_decision],
           product_decision: [experience_decision]},
          role_name="next decision", stereotype_instances=consider_if_not_decided_yet)

# decision views
forces_class_objects = [f.class_object for f in force.all_classes]

_all = CBundle("_all", elements=infra_decision.class_object.get_connected_elements())
inter_decision_links_view = CBundle("inter_decision_links",
                                    elements=[infra_decision, gov_decision, dep_decision, cross_decision, product_decision, experience_decision])

infra_decision_view = CBundle("infra_decision",
                                    elements=infra_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                           gov_decision.class_object,
                                            dep_decision.class_object,
                                            cross_decision.class_object,
                                            product_decision.class_object,
                                            experience_decision.class_object
                                        ]))

gov_decision_view = CBundle("gov_decision",
                                    elements=gov_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                           infra_decision.class_object,
                                            dep_decision.class_object,
                                            cross_decision.class_object,
                                            product_decision.class_object,
                                            experience_decision.class_object
                                        ]))

dep_decision_view = CBundle("dep_decision",
                                    elements=dep_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            infra_decision.class_object,
                                            gov_decision.class_object,
                                            cross_decision.class_object,
                                            product_decision.class_object,
                                            experience_decision.class_object
                                        ]))

cross_decision_view = CBundle("cross_decision",
                                    elements=cross_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            infra_decision.class_object,
                                            gov_decision.class_object,
                                            dep_decision.class_object,
                                            product_decision.class_object,
                                            experience_decision.class_object
                                        ]))

product_decision_view = CBundle("product_decision",
                                    elements=product_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            infra_decision.class_object,
                                            gov_decision.class_object,
                                            dep_decision.class_object,
                                            cross_decision.class_object,
                                            experience_decision.class_object
                                        ]))

experience_decision_view = CBundle("experience_decision",
                                    elements=experience_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            infra_decision.class_object,
                                            gov_decision.class_object,
                                            dep_decision.class_object,
                                            cross_decision.class_object,
                                            product_decision.class_object
                                        ]))


self_serve_platform_views = [
    _all, {},
    inter_decision_links_view, {},
    infra_decision_view, {},
    gov_decision_view, {},
    dep_decision_view, {},
    cross_decision_view, {},
    product_decision_view, {},
     experience_decision_view, {}
]


