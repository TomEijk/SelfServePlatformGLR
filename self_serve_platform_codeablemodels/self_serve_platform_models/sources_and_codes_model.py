from self_serve_platform_models.self_serve_platform_model import *
from codeable_models import CClass, add_links
from self_serve_platform_codeablemodels.generators.metamodels.GT_coding import code, source
from metamodels.domain_metamodel import domain_metaclass
from metamodels.guidance_metamodel import decision, design_solution, force, design_solution_dependencies

# add code as superclass to all possible codes used below
for classifier in [decision, domain_metaclass, design_solution, force, design_solution_dependencies,
                   ]:
    classifier.superclasses = classifier.superclasses + [code]

# ### Sources ###

s1 = CClass(source, "s1", values={
    "title": "Design considerations for self-serve data platforms",
    "url": "https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/cloud-scale-analytics/architectures/self-serve-data-platforms",
    "archive url": "https://bit.ly/self-serve-platform-s1",
    "tiny url": "https://tinyurl.com/self-serve-plaform-s1",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s1_codes = [api_catalog, data_catalog, cataloging_function, single_data_landing_zone, multiple_data_landing_zones, cdc, mapping_decision, decentralization,
            hub_generic_special_data_landing_zones, data_lineage, mdm, ml_services, data_lake_services, mesh_decision, infra_provision_decision,
            complexity, distinguish, domain_agnostic, regional_legal, control_over_data, delegated_ownership, polygot_storage_option,
            redeliveries,self_serve_decision, scalability, large_scale_enterprise, functional_and_regionally_aligned_data_landing_zones, other_platforms,
            networking, private_endpoints, flexibility, research_groups, data_governance_function]
add_links({s1: s1_codes}, role_name="contained_code")

s2 = CClass(source, "s2", values={
    "title": "Governance: Your Data Mesh Self-Service Depends on It",
    "url": "https://thenewstack.io/governance-your-data-mesh-self-service-depends-on-it/",
    "archive url": "https://bit.ly/self-serve-platform-s2",
    "tiny url": "https://tinyurl.com/self-serve-plaform-s2",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s2_codes = [event_streaming_backbone,self_serve_decision,data_product_developer_decision, register_derived_data_as_data_product, lambda_architecture, autonomous, mapping_decision, data_governance_function,
            kappa_architecture, access_control,role_based_access_control,infra_provision_decision, secure_dp, security, data_lineage, accessibility, read_dp, multiple_data_landing_zones]
add_links({s2: s2_codes}, role_name="contained_code")

s3 = CClass(source, "s3", values={
    "title": "Data Mesh From an Engineering Perspective",
    "url": "https://www.datamesh-architecture.com/",
    "archive url": "https://tinyurl.com/self-serve-plaform-s3",
    "tiny url": "https://tinyurl.com/self-serve-plaform-s3",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s3_codes = [data_source_ingestion, distributed_file_storage, access_control, role_based_access_control,mesh_decision, secure_dp, security, data_catalog, cataloging_function, visualization_function, alerting, build_deploy_monitor_dp, decentralization, self_serve_decision, managed_compute_infrastructure,
            manage_read_write_permissions, searchability, centrally_govern, policy_automation, query_engine, infra_provision_decision,data_observability, discoverability, discovery_and_explore_dps, query_recommendation_function, data_product_developer_decision, polygot_storage_option]
add_links({s3: s3_codes}, role_name="contained_code")

s4 = CClass(source, "s4", values={
    "title": "Your Data Mesh Can’t Be Self-Serve Just for Developers",
    "url": "https://towardsdatascience.com/your-data-mesh-cant-be-self-serve-just-for-developers-34bdeddc257e",
    "archive url": "https://bit.ly/self-serve-platform-s4",
    "tiny url": "https://tinyurl.com/self-serve-platform-s4",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s4_codes = [managed_compute_infrastructure,mesh_decision, data_product_developer_decision, abstact_away_details, elastic, adapt_to_changing_volumes, data_source_ingestion, infra_provision_decision,
            no_code_transformation, dependable_pipeline_management, automated_issue_detection, alerting, data_observability, resolution, schema_registry, data_governance_function, application_build_function,
            configure_depency, configure_scheduling,self_serve_decision, decentralization, compatibility, efficiency, interoperability, complexity, declaratively_create_dp]
add_links({s4: s4_codes}, role_name="contained_code")

s5 = CClass(source, "s5", values={
    "title": "Data Mesh Principles and Logical Architecture",
    "url": "https://martinfowler.com/articles/data-mesh-principles.html#LogicalArchitectureAMulti-planeDataPlatform",
    "archive url": "https://bit.ly/self-serve-platform-s5",
    "tiny url": "https://tinyurl.com/self-serve-platform-s5",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s5_codes = [distributed_file_storage, query_engine, query_recommendation_function, data_transformation_orchestration, data_transformation_function, managed_compute_infrastructure, polygot_storage_option,
            access_control,self_serve_decision, role_based_access_control, secure_dp, security, manage_security_policies_of_dps, manage_emergent_graphs_of_dps, mesh_decision, data_product_developer_decision, infra_provision_decision,
            discovery_and_explore_dps, declaratively_create_dp, read_dp, version_dp, build_deploy_monitor_dp]
add_links({s5: s5_codes}, role_name="contained_code")

s6 = CClass(source, "s6", values={
    "title": "Data Mesh — A Self-service Infrastructure at DPG Media with Snowflake",
    "url": "https://levelup.gitconnected.com/data-mesh-a-self-service-infrastructure-at-dpg-media-with-snowflake-566f108a98db",
    "archive url": "https://bit.ly/self-serve-platform-s6",
    "tiny url": "https://tinyurl.com/self-serve-platform-s6",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s6_codes = [separating_compute_from_compute, separating_storage_and_compute, scalability, autonomous, delegated_ownership, data_governance_function, self_serve_decision, polygot_storage_option, testing_dp,
            restore_data_without_backups,data_product_developer_decision, infra_provision_decision, in_place_consumption, scale_across_platforms_and_regions, data_transformation_orchestration, data_transformation_function]
add_links({s6: s6_codes}, role_name="contained_code")

s7 = CClass(source, "s7", values={
    "title": "Domain centric architecture : Data driven business process powered by Snowflake Data Sharing",
    "url": "https://businesstechnologiesjourney.blogspot.com/2020/12/domain-centric-architecture-data-driven.html",
    "archive url": "https://bit.ly/self-serve-platform-s7",
    "tiny url": "https://tinyurl.com/self-serve-platform-s7",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s7_codes = [in_place_consumption,mesh_decision, infra_provision_decision, data_product_developer_decision,api_catalog, data_movement, global_governance, freshness, data_governance_function, secure_dp, security, self_serve_decision, polygot_storage_option]
add_links({s7: s7_codes}, role_name="contained_code")

s8 = CClass(source, "s8", values={
    "title": "How JPMorgan Chase built a data mesh architecture to drive significant value to enhance their enterprise data platform",
    "url": "https://aws.amazon.com/blogs/big-data/how-jpmorgan-chase-built-a-data-mesh-architecture-to-drive-significant-value-to-enhance-their-enterprise-data-platform/",
    "archive url": "https://bit.ly/self-serve-platform-s8",
    "tiny url": "https://tinyurl.com/self-serve-platform-s8",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s8_codes = [in_place_consumption,api_catalog, data_movement,mesh_decision, access_control,role_based_access_control, secure_dp, security, infra_provision_decision, other_platforms, multiple_data_landing_zones, mapping_decision,
            data_integration_function,data_product_developer_decision, control_over_data, schema_registry, self_serve_decision]
add_links({s8: s8_codes}, role_name="contained_code")

s9 = CClass(source, "s9", values={
    "title": "Build a data mesh on Google Cloud with Dataplex, now generally available",
    "url": "https://cloud.google.com/blog/products/data-analytics/build-a-data-mesh-on-google-cloud-with-dataplex-now-generally-available",
    "archive url": "https://bit.ly/self-serve-platform-s9",
    "tiny url": "https://tinyurl.com/self-serve-platform-s9",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s9_codes = [in_place_consumption,api_catalog,infra_provision_decision, data_movement, data_product_developer_decision, data_catalog, cataloging_function, manage_read_write_permissions, autonomous, mesh_decision, secure_dp, security, set_privacy_dp,
            delegated_ownership, global_governance, access_control, federated_analytics, compatible_metadata, agility, log_management, data_observability, role_based_access_control,
            runtime_metadata, metadata_management, scalability,self_serve_decision, accessibility, read_dp, build_deploy_monitor_dp, decentralization, discovery_and_explore_dps, discoverability]
add_links({s9: s9_codes}, role_name="contained_code")

s10 = CClass(source, "s10", values={
    "title": "Aligning Business Intelligence and AI/ML with a Data Mesh Platform on AWS",
    "url": "https://aws.amazon.com/blogs/apn/aligning-business-intelligence-and-ai-ml-with-a-data-mesh-platform-on-aws/",
    "archive url": "https://bit.ly/self-serve-platform-s10",
    "tiny url": "https://tinyurl.com/self-serve-platform-s10",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s10_codes = [data_catalog, cataloging_function, metadata_management, infra_provision_decision, mesh_decision, other_platforms, data_observability,
             feedback_loop, data_lineage,self_serve_decision, autonomous, interoperability, container_registry, api_catalog,data_product_developer_decision, application_build_function]
add_links({s10: s10_codes}, role_name="contained_code")

s11 = CClass(source, "s11", values={
    "title": "Data mesh: a new paradigm for data management",
    "url": "https://siliconangle.com/2021/10/27/data-mesh-new-paradigm-data-management/",
    "archive url": "https://bit.ly/self-serve-platform-s11",
    "tiny url": "https://tinyurl.com/self-serve-platform-s11",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s11_codes = [access_control,role_based_access_control,mesh_decision,self_serve_decision, secure_dp, security, build_deploy_monitor_dp, declaratively_create_dp, distributed_file_storage, document_dp,api_catalog, knowledge_graph, searchability, managed_compute_infrastructure, data_transformation_function,
             data_transformation_orchestration, policy_automation, query_engine, query_recommendation_function, read_dp, central_search_function, set_privacy_dp, networking, infra_provision_decision, data_product_developer_decision, polygot_storage_option]
add_links({s11: s11_codes}, role_name="contained_code")

s12 = CClass(source, "s12", values={
    "title": "Untangle your mess and knit your mesh: A cross-company point of view",
    "url": "https://www2.deloitte.com/content/dam/Deloitte/be/Documents/technology/consulting_untangle_your_mess_and_knit_your_mesh_deloitte_be_report_en.pdf",
    "archive url": "https://bit.ly/self-serve-platform-s12",
    "tiny url": "https://tinyurl.com/self-serve-platform-s12",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s12_codes = [elastic_performance_engine,schema_registry, data_product_developer_decision, scalability, ad_hoc_exploration, feature_engineering, understandability, data_transformation_function, data_transformation_orchestration,
             data_source_ingestion,mesh_decision, unified_batch_stream_processing_service, complexity, declaratively_create_dp, application_build_function,
             data_governance_function, other_platforms, infra_provision_decision, time_to_value, self_serve_decision, managed_compute_infrastructure]
add_links({s12: s12_codes}, role_name="contained_code")

s13 = CClass(source, "s13", values={
    "title": "Self-Serve Data Platform",
    "url": "https://www.advancinganalytics.co.uk/blog/2021/8/5/data-mesh-deep-dive",
    "archive url": "https://bit.ly/self-serve-platform-s13",
    "tiny url": "https://tinyurl.com/self-serve-platform-s13",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s13_codes = [infrastructure_as_code,mesh_decision, declaratively_create_dp, distributed_file_storage, polygot_storage_option, query_engine, query_recommendation_function, data_transformation_orchestration,role_based_access_control, access_control, secure_dp, security, build_deploy_monitor_dp, autonomous, data_transformation_function,
             data_catalog, cataloging_function,self_serve_decision, alerting, data_observability, data_lineage, data_source_ingestion, infra_provision_decision, data_product_developer_decision, scalability, managed_compute_infrastructure]
add_links({s13: s13_codes}, role_name="contained_code")

s14 = CClass(source, "s14", values={
    "title": "Building a data mesh architecture in azure part 7",
    "url": "https://mrpaulandrew.com/2022/04/19/building-a-data-mesh-architecture-in-azure-part-7/",
    "archive url": "https://bit.ly/self-serve-platform-s14",
    "tiny url": "https://tinyurl.com/self-serve-platform-s14",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s14_codes = [research_groups,data_governance_function,mesh_decision,self_serve_decision, sql_endpoint,api_catalog, log_management, infra_provision_decision, networking, usability, software_as_a_service, data_catalog, cataloging_function, knowledge_graph, data_source_ingestion, data_lineage, data_observability]
add_links({s14: s14_codes}, role_name="contained_code")

s15 = CClass(source, "s15", values={
    "title": "Data Mesh – Rethinking Enterprise Data Architecture",
    "url": "https://www.cuelogic.com/blog/data-mesh",
    "archive url": "https://bit.ly/self-serve-platform-s15",
    "tiny url": "https://tinyurl.com/self-serve-platform-s15",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s15_codes = [access_control,data_governance_function,mesh_decision,self_serve_decision, role_based_access_control, secure_dp, security, configure_scheduling,api_catalog, polygot_storage_option, infra_provision_decision, configure_depency, configure_thresholds, data_catalog, cataloging_function, distributed_file_storage, build_deploy_monitor_dp, data_product_developer_decision,
             interoperability, automation, decentralization, other_platforms, duplication]
add_links({s15: s15_codes}, role_name="contained_code")

s16 = CClass(source, "s16", values={
    "title": "Data Mesh and Starburst: Self-Service Data Infrastructure",
    "url": "https://www.starburst.io/blog/data-mesh-starburst-self-service-data-infrastructure/",
    "archive url": "https://bit.ly/self-serve-platform-s16",
    "tiny url": "https://tinyurl.com/self-serve-platform-s16",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s16_codes = [polygot_storage_option,data_governance_function, managed_compute_infrastructure, federated_analytics, in_place_consumption,role_based_access_control, access_control, secure_dp, security, alerting, query_engine, query_recommendation_function, log_management, data_observability, data_transformation_orchestration,
             build_deploy_monitor_dp, sql_endpoint,data_catalog, cataloging_function, data_lineage, infra_provision_decision, data_product_developer_decision, autonomous, interoperability, ease_of_administration, scalability,
             usability, data_transformation_function, metadata_management, schema_registry, entry_barier, mesh_decision, self_serve_decision]
add_links({s16: s16_codes}, role_name="contained_code")

s17 = CClass(source, "s17", values={
    "title": "Data Mesh and Starburst: Self-Service Data Infrastructure",
    "url": "https://cloud.google.com/architecture/design-self-service-data-platform-data-mesh",
    "archive url": "https://bit.ly/self-serve-platform-s17",
    "tiny url": "https://tinyurl.com/self-serve-platform-s17",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s17_codes = [build_deploy_monitor_dp, data_catalog, cataloging_function, mdm, data_transformation_orchestration, policy_automation, dependable_pipeline_management, infrastructure_as_code, declaratively_create_dp, data_observability, log_management, freshness,
             api_catalog,data_governance_function,self_serve_decision, access_control,role_based_access_control, secure_dp, security, networking, manage_security_policies_of_dps, metadata_management, resource_deployment_process, ci_cd_process, complexity, interoperability, data_transformation_function,
             inconsistencies_between_deployed_resources_and_declared_code_in_source_control, sql_endpoint, visualization_function, event_streaming_backbone, in_place_consumption, research_groups, uptime_checks,
             alerting, reduce_work_data_product_team, infra_provision_decision, data_product_developer_decision, mesh_decision, document_dp, application_build_function]
add_links({s17: s17_codes}, role_name="contained_code")

s18 = CClass(source, "s18", values={
    "title": "The Google Technology Landscape for a Self-Service Data Platform",
    "url": "https://www.linkedin.com/pulse/landscape-technologies-self-service-data-platform-sandeep/?trk=portfolio_article-card_title",
    "archive url": "https://bit.ly/self-serve-platform-s18",
    "tiny url": "https://tinyurl.com/self-serve-platform-s18",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s18_codes = [data_catalog,api_catalog,mesh_decision,self_serve_decision, cataloging_function, data_source_ingestion, event_streaming_backbone, visualization_function, build_deploy_monitor_dp, unified_batch_stream_processing_service, distributed_file_storage, polygot_storage_option,
             data_transformation_orchestration, log_management, data_observability, cost_management, data_product_developer_decision, infra_provision_decision, automation, complexity, data_transformation_function, testing_dp]
add_links({s18: s18_codes}, role_name="contained_code")

s19 = CClass(source, "s19", values={
    "title": "Turning Airflow into a full self service Data Platform",
    "url": "https://danielrcarletti.medium.com/turning-airflow-into-a-full-self-service-data-platform-b67eccdd3445",
    "archive url": "https://bit.ly/self-serve-platform-s19",
    "tiny url": "https://tinyurl.com/self-serve-platform-s19",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s19_codes = [infrastructure_as_code, declaratively_create_dp, easily_replicable, workflow_automation_engine, infra_provision_decision, automation, data_product_developer_decision]
add_links({s19: s19_codes}, role_name="contained_code")

s20 = CClass(source, "s20", values={
    "title": "Self Service Data Platform",
    "url": "https://dywhin.com/self-service-data-platform/",
    "archive url": "https://bit.ly/self-serve-platform-s20",
    "tiny url": "https://tinyurl.com/self-serve-platform-s20",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s20_codes = [data_source_ingestion, visualization_function, infrastructure_as_code,
             infra_provision_decision, declaratively_create_dp, autonomous, agility, data_product_developer_decision]
add_links({s20: s20_codes}, role_name="contained_code")

s21 = CClass(source, "s21", values={
    "title": "ACHIEVING ENTERPRISE SELF-SERVICE DATA: THE SIX PILLARS OF COMPREHENSIVE CAPABILITIES",
    "url": "https://radiantadvisors.com/storage/uploads/2c152ae4b.pdf",
    "archive url": "https://bit.ly/self-serve-platform-s21",
    "tiny url": "https://tinyurl.com/self-serve-platform-s21",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s21_codes = [data_catalog, cataloging_function, data_lineage, accuracy, workflow_automation_engine, infra_provision_decision, data_governance_function,
             crud_operations,api_catalog, agility, log_management, data_observability, data_product_developer_decision, mesh_decision, self_serve_decision]
add_links({s21: s21_codes}, role_name="contained_code")

s22 = CClass(source, "s22", values={
    "title": "Create A Road Map For A Real-Time, Agile, Self-Service Data Platform",
    "url": "https://silo.tips/download/res83321",
    "archive url": "https://bit.ly/self-serve-platform-s22",
    "tiny url": "https://tinyurl.com/self-serve-platform-s22",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s22_codes = [in_place_consumption, unified_batch_stream_processing_service, data_source_ingestion, mdm, metadata_management, self_serve_decision,
             infra_provision_decision, mesh_decision, agility, application_build_function]
add_links({s22: s22_codes}, role_name="contained_code")

s23 = CClass(source, "s23", values={
    "title": "Why zulily created a self-service marketing analytics platform with Tableau and Google BigQuery",
    "url": "https://www.tableau.com/blog/why-zulily-created-self-service-marketing-analytics-platform-tableau-and-google",
    "archive url": "https://bit.ly/self-serve-platform-s23",
    "tiny url": "https://tinyurl.com/self-serve-platform-s23",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s23_codes = [sql_endpoint, mdm]
add_links({s23: s23_codes}, role_name="contained_code")

s24 = CClass(source, "s24", values={
    "title": "How we scale our data platform efficiently and reliably",
    "url": "https://building.nubank.com.br/distributing-the-data-team-to-boost-innovation-reliably/",
    "archive url": "https://bit.ly/self-serve-platform-s24",
    "tiny url": "https://tinyurl.com/self-serve-platform-s24",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s24_codes = [alerting, automated_issue_detection,self_serve_decision, data_product_developer_decision, efficiency, scalability, automation, delegated_ownership, secure_dp, security, cataloging_function, quality_management, data_governance_function]
add_links({s24: s24_codes}, role_name="contained_code")

s25 = CClass(source, "s25", values={
    "title": "How does the banking industry build a self-service data platform?",
    "url": "https://www.mo4tech.com/how-does-the-banking-industry-build-a-self-service-data-platform.html",
    "archive url": "https://bit.ly/self-serve-platform-s25",
    "tiny url": "https://tinyurl.com/self-serve-platform-s25",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s25_codes = [sql_endpoint, avoids_information_island, data_source_ingestion, unified_batch_stream_processing_service,data_governance_function,
             testing_dp, efficiency, data_product_developer_decision, api_catalog, infra_provision_decision,mesh_decision, self_serve_decision]
add_links({s25: s25_codes}, role_name="contained_code")

s26 = CClass(source, "s26", values={
    "title": "Meet Data Hub: Delivery Hero’s Data Mesh Platform?",
    "url": "https://tech.deliveryhero.com/meet-data-hub-delivery-heros-data-mesh-platform/",
    "archive url": "https://bit.ly/self-serve-platform-s26",
    "tiny url": "https://tinyurl.com/self-serve-platform-s26",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s26_codes = [unified_batch_stream_processing_service, access_control,role_based_access_control, secure_dp, security, container_registry, distributed_file_storage, separating_storage_and_compute, VMs, data_transformation_orchestration, polygot_storage_option,
             infra_provision_decision,data_product_developer_decision, workflow_automation_engine, application_build_function, accessibility, read_dp, self_serve_decision, data_transformation_function]

add_links({s26: s26_codes}, role_name="contained_code")

s27 = CClass(source, "s27", values={
    "title": "Building a Data Mesh on Databricks — Fast",
    "url": "https://towardsdatascience.com/building-a-data-mesh-on-databricks-fast-25bf9a9bf0b2",
    "archive url": "https://bit.ly/self-serve-platform-s27",
    "tiny url": "https://tinyurl.com/self-serve-platform-s27",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s27_codes = [infrastructure_as_code, access_control,role_based_access_control, secure_dp, security, data_catalog, cataloging_function, distributed_file_storage, data_source_ingestion, no_code_transformation, query_engine, query_recommendation_function, infra_provision_decision, managed_compute_infrastructure, polygot_storage_option,
             maintenance_needs, declaratively_create_dp,data_governance_function, data_transformation_orchestration, data_transformation_function, accessibility, read_dp, data_product_developer_decision, self_serve_decision]
add_links({s27: s27_codes}, role_name="contained_code")

s28 = CClass(source, "s28", values={
    "title": "Applying the Data Mesh Approach Through a Data Product Platform ",
    "url": "https://dzone.com/articles/top-challenges-in-data-mesh-and-how-a-data-product",
    "archive url": "https://bit.ly/self-serve-platform-s28",
    "tiny url": "https://tinyurl.com/self-serve-platform-s28",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s28_codes = [access_control,role_based_access_control,data_governance_function, secure_dp, security, data_transformation_orchestration, infrastructure_as_code, declaratively_create_dp, data_transformation_function,
             infra_provision_decision, self_serve_decision, data_source_ingestion, data_catalog, cataloging_function, data_product_developer_decision]
add_links({s28: s28_codes}, role_name="contained_code")

s29 = CClass(source, "s29", values={
    "title": "The Definitive Guide To Building A Data Mesh With Event Streams",
    "url": "https://www.lightnetics.com/topic/33104/the-definitive-guide-to-building-a-data-mesh-with-event-streams",
    "archive url": "https://bit.ly/self-serve-platform-s29",
    "tiny url": "https://tinyurl.com/self-serve-platform-s29",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s29_codes = [access_control,role_based_access_control, secure_dp, security, data_catalog,infra_provision_decision,data_product_developer_decision, cataloging_function, distributed_file_storage, separating_storage_and_compute, kappa_architecture, lambda_architecture, application_build_function, polygot_storage_option,
             scalability, latency, self_serve_decision, container_registry, api_catalog, data_governance_function, mesh_decision]
add_links({s29: s29_codes}, role_name="contained_code")

s30 = CClass(source, "s30", values={
    "title": "Deploying Data Products at the speed of the business",
    "url": "https://dataception.com/Data-Mesh-Deploying-Data-Products-at-the-speed-of-the-business.html",
    "archive url": "https://bit.ly/self-serve-platform-s30",
    "tiny url": "https://tinyurl.com/self-serve-platform-s30",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s30_codes = [container_registry, VMs, infrastructure_as_code, managed_compute_infrastructure, data_catalog, cataloging_function, data_transformation_orchestration, secure_dp, security, data_transformation_function,
             version_dp, data_lineage, data_source_ingestion, dependable_pipeline_management, distributed_file_storage, separating_storage_and_compute, interoperability, delegated_ownership, data_governance_function,
             metadata_management, polygot_storage_option,self_serve_decision, infra_provision_decision, data_product_developer_decision,api_catalog, mesh_decision, duplication, accessibility, read_dp, declaratively_create_dp]
add_links({s30: s30_codes}, role_name="contained_code")

s31 = CClass(source, "s31", values={
    "title": "Deconstructing Data Mesh Principles",
    "url": "https://medium.com/slalom-data-ai/data-mesh-232e50f42e66",
    "archive url": "https://bit.ly/self-serve-platform-s31",
    "tiny url": "https://tinyurl.com/self-serve-platform-s31",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s31_codes = [access_control,data_governance_function,self_serve_decision, role_based_access_control, secure_dp, security, dependable_pipeline_management, infrastructure_as_code, declaratively_create_dp, log_management, infra_provision_decision, data_product_developer_decision, scalability, data_observability, polygot_storage_option,
             data_transformation_orchestration, data_transformation_function,api_catalog, register_derived_data_as_data_product, separating_storage_and_compute, version_dp, networking, build_deploy_monitor_dp, data_source_ingestion, mesh_decision]
add_links({s31: s31_codes}, role_name="contained_code")

s32 = CClass(source, "s32", values={
    "title": "Data Movement in Netflix Studio via Data Mesh",
    "url": "https://netflixtechblog.com/data-movement-in-netflix-studio-via-data-mesh-3fddcceb1059",
    "archive url": "https://bit.ly/self-serve-platform-s32",
    "tiny url": "https://tinyurl.com/self-serve-platform-s32",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s32_codes = [schema_registry,data_governance_function,data_product_developer_decision, register_derived_data_as_data_product,api_catalog, access_control,role_based_access_control, secure_dp, security, cdc, knowledge_graph, log_management, sql_endpoint, infra_provision_decision, transparency, managed_compute_infrastructure,
             workflow_automation_engine,self_serve_decision, query_engine, query_recommendation_function, mesh_decision, data_catalog, cataloging_function, compatibility, discoverability, discovery_and_explore_dps, data_observability]
add_links({s32: s32_codes}, role_name="contained_code")

s33 = CClass(source, "s33", values={
    "title": "Data Platform in a mesh architecture",
    "url": "https://www.thoughtworks.com/about-us/events/webinars/core-principles-of-data-mesh/data-platform-in-a-mesh-architecture",
    "archive url": "https://bit.ly/self-serve-platform-s33",
    "tiny url": "https://tinyurl.com/self-serve-platform-s33",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s33_codes = [data_catalog,self_serve_decision, cataloging_function, data_lineage, quality_management, build_deploy_monitor_dp, data_transformation_orchestration, data_transformation_function, query_engine, query_recommendation_function, infra_provision_decision, data_product_developer_decision,
             self_serve_ui, ci_cd_process, infrastructure_as_code, declaratively_create_dp, dependable_pipeline_management, version_dp, runtime_observability, application_bootstraps, data_source_ingestion, managed_compute_infrastructure,
             separating_compute_from_compute, VMs, access_control,role_based_access_control, secure_dp ,networking, separating_storage_and_compute, polygot_storage_option, application_build_function]
add_links({s33: s33_codes}, role_name="contained_code")

s34 = CClass(source, "s34", values={
    "title": "Early Adoption of the Self-Service Data Infrastructure",
    "url": "https://www.starburst.io/blog/early-adoption-of-the-self-service-data-infrastructure/",
    "archive url": "https://bit.ly/self-serve-platform-s34",
    "tiny url": "https://tinyurl.com/self-serve-platform-s34",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s34_codes = [distributed_file_storage, managed_compute_infrastructure,api_catalog, metadata_management, polygot_storage_option, document_dp, data_governance_function,
             query_engine, data_product_developer_decision, self_serve_decision, query_recommendation_function, sql_endpoint, infra_provision_decision, mesh_decision, data_source_ingestion, entry_barier]
add_links({s34: s34_codes}, role_name="contained_code")

s35 = CClass(source, "s35", values={
    "title": "Data Mesh Principles and Architecture",
    "url": "https://medium.com/@samueldavidwinter/data-mesh-principles-and-architecture-ce0eb6494502",
    "archive url": "https://bit.ly/self-serve-platform-s35",
    "tiny url": "https://tinyurl.com/self-serve-platform-s35",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s35_codes = [polygot_storage_option, dependable_pipeline_management, data_catalog, cataloging_function, access_control,role_based_access_control, secure_dp, security, decentralization, duplication,
             schema_registry,data_product_developer_decision,self_serve_decision, managed_compute_infrastructure, separating_compute_from_compute, discoverability,
             data_transformation_orchestration, data_transformation_function, cross_cutting_concerns, self_serve_ui, infra_provision_decision, mesh_decision]
add_links({s35: s35_codes}, role_name="contained_code")

s36 = CClass(source, "s36", values={
    "title": "Data Mesh Principles and Architecture",
    "url": "https://www.thoughtworks.com/insights/blog/data-mesh-its-not-about-tech-its-about-ownership-and-communication",
    "archive url": "https://bit.ly/self-serve-platform-s36",
    "tiny url": "https://tinyurl.com/self-serve-platform-s36",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s36_codes = [schema_registry, data_quality_management, knowledge_graph, mesh_decision, delegated_ownership, decentralization, data_observability, cataloging_function,
             duplication, scalability, data_governance_function, self_serve_decision, ]
add_links({s36: s36_codes}, role_name="contained_code")

s37 = CClass(source, "s37", values={
    "title": "Establishing the Data Mesh Ecosystem",
    "url": "https://towardsdatascience.com/establishing-the-data-mesh-ecosystem-172d9512f43d?gi=58d0c72d6a1f",
    "archive url": "https://bit.ly/self-serve-platform-s37",
    "tiny url": "https://tinyurl.com/self-serve-platform-s37",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s37_codes = [data_transformation_orchestration,mesh_decision,self_serve_decision, data_transformation_function, data_catalog,api_catalog, cataloging_function, infra_provision_decision, agility, efficiency, data_governance_function]
add_links({s37: s37_codes}, role_name="contained_code")

s38 = CClass(source, "s38", values={
    "title": "Data Mesh: Making Climate Data Easy to Find, Use, and Share",
    "url": "https://towardsdatascience.com/making-climate-data-easy-to-find-use-and-share-5190a0926407",
    "archive url": "https://bit.ly/self-serve-platform-s38",
    "tiny url": "https://tinyurl.com/self-serve-platform-s38",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s38_codes = [data_transformation_orchestration, mesh_decision,self_serve_decision, data_transformation_function,api_catalog, data_catalog, cataloging_function,data_governance_function, infra_provision_decision, data_product_developer_decision, interoperability, autonomous]
add_links({s38: s38_codes}, role_name="contained_code")

s39 = CClass(source, "s39", values={
    "title": "Rethinking the API Platform",
    "url": "https://medium.com/geekculture/rethinking-the-api-platform-7a7642c48bfa",
    "archive url": "https://bit.ly/self-serve-platform-s39",
    "tiny url": "https://tinyurl.com/self-serve-platform-s39",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s39_codes = [data_governance_function, cross_cutting_concerns, alerting, log_management,api_catalog, build_deploy_monitor_dp, infrastructure_as_code, data_product_developer_decision, declaratively_create_dp, agility, efficiency, data_observability,
             mesh_decision, feedback_loop, application_build_function, self_serve_decision ]
add_links({s39: s39_codes}, role_name="contained_code")

s40 = CClass(source, "s40", values={
    "title": "Data Platforms: The Past",
    "url": "https://medium.com/alexandre-beauvois/modern-data-stack-as-a-service-1-3-1a1813c38633",
    "archive url": "https://bit.ly/self-serve-platform-s40",
    "tiny url": "https://tinyurl.com/self-serve-platform-s40",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s40_codes = [data_source_ingestion,data_product_developer_decision, mesh_decision,self_serve_decision,  separating_storage_and_compute,api_catalog, separating_compute_from_compute, self_serve_ui, document_dp, complexity,data_observability, alerting, polygot_storage_option, data_governance_function,
             data_transformation_orchestration, data_transformation_function, other_platforms, compatibility, infra_provision_decision, workflow_automation_engine]
add_links({s40: s40_codes}, role_name="contained_code")

s41 = CClass(source, "s41", values={
    "title": "Data Platforms: The Present",
    "url": "https://medium.com/@abeauvois/modern-data-stack-as-a-service-2-3-9a15fd8dfb31",
    "archive url": "https://bit.ly/self-serve-platform-s41",
    "tiny url": "https://tinyurl.com/self-serve-platform-s41",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s41_codes = [separating_compute_from_compute, separating_storage_and_compute, polygot_storage_option, no_code_transformation, data_source_ingestion, automation, compatibility, data_product_developer_decision, self_serve_decision,
            mesh_decision, data_quality_management, self_serve_ui, other_platforms,api_catalog, infra_provision_decision, crud_operations, data_transformation_orchestration, data_transformation_function, data_governance_function]
add_links({s41: s41_codes}, role_name="contained_code")

s42 = CClass(source, "s42", values={
    "title": "Data Platforms: The Future",
    "url": "https://medium.com/@abeauvois/data-platforms-the-future-7175a354bea2",
    "archive url": "https://bit.ly/self-serve-platform-s42",
    "tiny url": "https://tinyurl.com/self-serve-platform-s42",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s42_codes = [api_catalog, build_deploy_monitor_dp, data_catalog, cataloging_function, no_code_transformation, data_transformation_orchestration, knowledge_graph, event_streaming_backbone, infra_provision_decision, data_product_developer_decision,
             mesh_decision, accessibility,self_serve_decision, read_dp, access_control, role_based_access_control, secure_dp,data_governance_function, delegated_ownership, interoperability, scalability, data_transformation_function]
add_links({s42: s42_codes}, role_name="contained_code")

s43 = CClass(source, "s43", values={
    "title": "Data Mesh in Practice: How Europe’s Leading Online Platform for Fashion Goes Beyond the Data Lake",
    "url": "https://mr-oceanblue.medium.com/data-mesh-in-practice-how-europes-leading-online-platform-for-fashion-goes-beyond-the-data-lake-652d2550bcf",
    "archive url": "https://bit.ly/self-serve-platform-s43",
    "tiny url": "https://tinyurl.com/self-serve-platform-s43",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s43_codes = [polygot_storage_option,data_product_developer_decision, dependable_pipeline_management, data_catalog, cataloging_function, access_control,data_governance_function, role_based_access_control, secure_dp, security, event_streaming_backbone, data_transformation_orchestration, data_transformation_function,
             metadata_management, data_quality_management,self_serve_decision, infra_provision_decision, mesh_decision, delegated_ownership, quality_management]
add_links({s43: s43_codes}, role_name="contained_code")

p1 = CClass(source, "p1", values={
    "title": "Interview Expert 1",
    "url": "https://github.com/TomEijk/Data_as_a_Product_GLR/tree/master/python/self-serve-platform_codeablemodels/field_notes_open_coding_axial_coding",
    "archive url": "https://bit.ly/self-serve-platform-p1",
    "tiny url": "https://tinyurl.com/self-serve-platform-p1",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
p1_codes = [persona_to_tool_approach,mesh_decision, functional_and_regionally_aligned_data_landing_zones, data_transformation_orchestration, document_dp, data_transformation_function, version_dp, testing_dp, api_catalog,
            manage_emergent_graphs_of_dps, data_catalog,schema_registry, cataloging_function,role_based_access_control, secure_dp, security, data_product_developer_decision, mapping_decision, infra_provision_decision, self_serve_decision]
add_links({p1: p1_codes}, role_name="contained_code")

p2 = CClass(source, "p2", values={
    "title": "Interview Expert 2",
    "url": "https://github.com/TomEijk/Data_as_a_Product_GLR/tree/master/python/self-serve-platform_codeablemodels/field_notes_open_coding_axial_coding",
    "archive url": "https://bit.ly/self-serve-platform-p2",
    "tiny url": "https://tinyurl.com/self-serve-platform-p2",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
p2_codes = [multiple_data_landing_zones, api_catalog,self_serve_decision, workflow_automation_engine, schema_registry, data_catalog, cataloging_function, document_dp, crud_operations, testing_dp, change_management, container_registry, version_dp,
            knowledge_graph, mdm, data_quality_management, manage_emergent_graphs_of_dps, visualization_function, mapping_decision, infra_provision_decision, data_product_developer_decision, mesh_decision]
add_links({p2: p2_codes}, role_name="contained_code")

p3 = CClass(source, "p3", values={
    "title": "Interview Expert 3",
    "url": "https://github.com/TomEijk/Data_as_a_Product_GLR/tree/master/python/self-serve-platform_codeablemodels/field_notes_open_coding_axial_coding",
    "archive url": "https://bit.ly/self-serve-platform-p3",
    "tiny url": "https://tinyurl.com/self-serve-platform-p3",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
p3_codes = [hub_generic_special_data_landing_zones,mesh_decision, multiple_data_landing_zones, functional_and_regionally_aligned_data_landing_zones, role_based_access_control, secure_dp, security, unified_batch_stream_processing_service, polygot_storage_option,
            declaratively_create_dp, knowledge_graph,schema_registry,api_catalog, feedback_loop, mdm, data_integration_function, mapping_decision, infra_provision_decision, crud_operations, data_product_developer_decision, self_serve_decision, version_dp, testing_dp]
add_links({p3: p3_codes}, role_name="contained_code")

p4 = CClass(source, "p4", values={
    "title": "Interview Expert 4",
    "url": "https://github.com/TomEijk/Data_as_a_Product_GLR/tree/master/python/self-serve-platform_codeablemodels/field_notes_open_coding_axial_coding",
    "archive url": "https://bit.ly/self-serve-platform-p4",
    "tiny url": "https://tinyurl.com/self-serve-platform-p4",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
p4_codes = [data_product_as_self_serve, data_catalog, cataloging_function,api_catalog, VMs, declaratively_create_dp, feedback_loop, alerting, log_management, testing_dp, knowledge_graph, mdm, role_based_access_control, secure_dp,
            visualization_function,schema_registry, infra_provision_decision, data_product_developer_decision, mesh_decision, self_serve_decision, version_dp,data_observability, crud_operations]
add_links({p4: p4_codes}, role_name="contained_code")

p5 = CClass(source, "p5", values={
    "title": "Interview Expert 5",
    "url": "https://github.com/TomEijk/Data_as_a_Product_GLR/tree/master/python/self-serve-platform_codeablemodels/field_notes_open_coding_axial_coding",
    "archive url": "https://bit.ly/self-serve-platform-p5",
    "tiny url": "https://tinyurl.com/self-serve-platform-p5",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
p5_codes = [hub_generic_special_data_landing_zones,schema_registry, multiple_data_landing_zones, workflow_automation_engine, testing_dp, document_dp, crud_operations, build_deploy_monitor_dp, data_transformation_orchestration, data_catalog, cataloging_function, alerting, knowledge_graph, container_registry,
            api_catalog, manage_emergent_graphs_of_dps, data_transformation_function, devsecops_pipeline, mapping_decision, infra_provision_decision, data_product_developer_decision, mesh_decision, self_serve_decision, version_dp, feedback_loop]
add_links({p5: p5_codes}, role_name="contained_code")

p6 = CClass(source, "p6", values={
    "title": "Interview Expert 6",
    "url": "https://github.com/TomEijk/Data_as_a_Product_GLR/tree/master/python/self-serve-platform_codeablemodels/field_notes_open_coding_axial_coding",
    "archive url": "https://bit.ly/self-serve-platform-p6",
    "tiny url": "https://tinyurl.com/self-serve-platform-p6",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})

p6_codes = [multiple_data_landing_zones, networking, data_catalog,api_catalog, cataloging_function, build_deploy_monitor_dp, infrastructure_as_code, declaratively_create_dp, testing_dp, read_dp, business_glossary, experimental_platform, data_observability, data_governance_function,
            mapping_decision, infra_provision_decision, data_product_developer_decision, mesh_decision, self_serve_decision, version_dp, crud_operations]
add_links({p6: p6_codes}, role_name="contained_code")

