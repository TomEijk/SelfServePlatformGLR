# API design


## Decision: Which architectural design elements should be offered by the Data Infrastructure Provisioning Plane?
**Evidences:** s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s25, s26, s27, s28, s29, s30, s31, s32, s33, s34, s35, s37, s38, s40, s41, s42, s43, p1, p2, p3, p4, p5, p6

**Context:** 

### **Solution Options**
#### Solution 1: Workflow Automation Engine
**Evidences:** s19, s21, s26, s32, s40, p2, p5

**Forces:**
- Ease of Administration (++) [s16]
- Discoverability (+) [s3, s9, s32, s35]
- Time-to-Value (+) [s12]
- Agility (++) [s9, s20, s21, s22, s37]
- Maintenance Needs (-) [s27]
- Control over data (-) [s1, s8]

#### Solution 2: Access controls
**Evidences:** s2, s3, s5, s8, s9, s11, s13, s15, s16, s17, s26, s27, s28, s29, s31, s32, s33, s35, s42, s43

**Forces:**
- Transparency (+) [s32]
- Security (++) [s2, s3, s5, s7, s8, s9, s11, s13, s15, s16, s17, s26, s27, s28, s29, s30, s31, s32, s35, s43, p1, p3]
- Compatability (+) [s4, s32, s40, s41]
- Complexity (-) [s1, s4, s12, s17, s18, s40]
- Maintenance Needs (--) [s27]

#### Solution 3: Interconnectivity
**Evidences:** s1, s11, s14, s17, s31, s33, p6

**Forces:**
- Interoperability (++) [s4, s10, s15, s16, s17, s30, s38, s42]
- Agility (+) [s9, s20, s21, s22, s37]
- Efficiency (+) [s4, s25, s37]
- Complexity (-) [s1, s4, s12, s17, s18, s40]
- Domain-agnostic (-) [s1]

#### Solution 4: Data Transformation Orchestration
**Evidences:** s5, s6, s11, s12, s13, s16, s17, s18, s26, s27, s28, s30, s31, s33, s35, s37, s38, s40, s41, s42, s43, p1, p5

**Forces:**
- Resource deployment process (+) [s17]
- Efficiency (+) [s4, s25, s37]
- Automation (+) [s15, s18, s19, s41]
- Latency (-) [s29]
- Time-to-Value (-) [s12]

#### Solution 5: VMs
**Evidences:** s26, s30, s33, p4

**Forces:**
- Scalability (+) [s1, s6, s9, s12, s13, s16, s29, s31, s42]
- Elastic (+) [s4]
- Complexity (-) [s1, s4, s12, s17, s18, s40]
- Time-to-Value (-) [s12]

#### Solution 6: Container Registry
**Evidences:** s10, s26, s29, s30, p2, p5


#### Solution 7: Data Source Ingestion
**Evidences:** s3, s4, s12, s13, s14, s18, s20, s22, s25, s27, s28, s30, s31, s33, s34, s40, s41

**Forces:**
- Data Freshness (++) [s7, s17]
- Interoperability (+) [s4, s10, s15, s16, s17, s30, s38, s42]
- Discoverability (+) [s3, s9, s32, s35]
- Resource deployment process (-) [s17]
- Complexity (-) [s1, s4, s12, s17, s18, s40]
- Time-to-Value (-) [s12]

#### Solution 8: Managed Compute Infrastructure
**Evidences:** s3, s4, s5, s11, s12, s13, s16, s27, s30, s32, s33, s34, s35

**Forces:**
- Scalability (++) [s1, s6, s9, s12, s13, s16, s29, s31, s42]
- Accessibility (+) [s2, s9, s26, s27, s30, s42]
- Global governance (+) [s7, s9]
- Complexity (-) [s1, s4, s12, s17, s18, s40]
- Maintenance Needs (-) [s27]

#### Solution 9: Polygot Storage Option
**Evidences:** s1, s3, s5, s6, s7, s11, s13, s15, s16, s18, s26, s27, s29, s30, s31, s33, s34, s35, s40, s41, s43, p3

**Forces:**
- Autonomous (++) [s2, s6, s9, s10, s13, s16, s20, s38]
- Scalability (+) [s1, s6, s9, s12, s13, s16, s29, s31, s42]
- Adapt to changing volumes (++) [s4]
- Data movement (-) [s7, s8, s9]
- Complexity (-) [s1, s4, s12, s17, s18, s40]

#### Solution 10: Custom Platforms
**Evidences:** s1, s8, s10, s12, s15, s40, s41

**Forces:**
- Agility (+) [s9, s20, s21, s22, s37]
- Time-to-Value (+) [s12]
- Compatability (+) [s4, s32, s40, s41]
- Complexity (-) [s1, s4, s12, s17, s18, s40]
- Entry Barrier (-) [s16, s34]

#### **Next Decision**: What elements should be included in the user interface (UI) of a self-serve platform?


## Decision: What elements should be considered when designing a Data Product Developer Experience Plane?
**Evidences:** s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s15, s16, s17, s18, s19, s20, s21, s24, s25, s26, s27, s28, s29, s30, s31, s32, s33, s34, s35, s38, s39, s40, s41, s42, s43, p1, p2, p3, p4, p5, p6

**Context:** 

### **Solution Options**
#### Solution 1: Build, deploy, monitor DP
**Evidences:** s3, s5, s9, s11, s13, s15, s16, s17, s18, s31, s33, s39, s42, p5, p6

**Forces:**
- Maintenance Needs (+) [s27]
- Scalability (+) [s6, s9, s12, s13, s16, s24, s29, s31, s42]
- Time-to-Value (+) [s12]
- Transparency (+) [s32]

#### Solution 2: Version DP
**Evidences:** s5, s30, s31, s33, p1, p2, p3, p4, p5, p6

**Forces:**
- Federated analytics (+) [s9, s16]
- Reduce work done by data product team (+) [s17]
- Easily Replicable (+) [s19]
- Control over data (-) [s8]

#### Solution 3: Secure DP
**Evidences:** s2, s3, s5, s7, s8, s9, s11, s13, s15, s16, s17, s24, s26, s27, s28, s29, s30, s31, s32, s33, s35, s42, s43, p1, p3, p4

**Forces:**
- Security (+) [s2, s3, s5, s7, s8, s9, s11, s13, s15, s16, s17, s24, s26, s27, s28, s29, s30, s31, s32, s35, s43, p1, p3]
- Control over data (+) [s8]
- Entry Barrier (-) [s16, s34]
- Usability (-) [s16]

#### Solution 4: Read DP
**Evidences:** s2, s5, s9, s11, s26, s27, s30, s42, p6

**Forces:**
- Discoverability (+) [s3, s9, s32, s35]
- Searchability (+) [s3, s11]
- Abstract away computational details (+) [s4]

#### Solution 5: Establish Data Contract
**Evidences:** s11, s17, s34, s40, p1, p2, p5

**Forces:**
- Global governance (++) [s7, s9]
- Discoverability (+) [s3, s9, s32, s35]
- Searchability (+) [s3, s11]
- Inconsistencies between deployed resources and declrared code in source control (-) [s17]
- Maintenance Needs (-) [s27]
- Redeliveries (-) []

#### Solution 6: Declaratively create DP
**Evidences:** s4, s5, s11, s12, s13, s17, s19, s20, s27, s28, s30, s31, s33, s39, p3, p4, p6

**Forces:**
- Scalability (+) [s6, s9, s12, s13, s16, s24, s29, s31, s42]
- Duplication (+) [s15, s30, s35]
- Automation (+) [s15, s18, s19, s24, s41]
- Reduce work done by data product team (-) [s17]

#### Solution 7: Testing DP for Deployment and Provisioning
**Evidences:** s6, s18, s25, p1, p2, p3, p4, p5, p6

**Forces:**
- Discoverability (+) [s3, s9, s32, s35]
- Maintenance Needs (+) [s27]
- Accuracy (+) [s21]
- Time-to-Value (-) [s12]

#### Solution 8: Feedback Loop
**Evidences:** s10, s39, p3, p4, p5

**Forces:**
- Usability (+) [s16]
- Understandability (+) [s12]
- Discoverability (+) [s3, s9, s32, s35]
- Accuracy (-) [s21]
- Agility (-) [s9, s20, s21, s39]

#### Solution 9: CRUD operations
**Evidences:** s21, s41, p2, p3, p4, p5, p6

**Forces:**
- Abstract away computational details (+) [s4]
- Reduce work done by data product team (+) [s17]

#### **Next Decision**: What elements should be included in the user interface (UI) of a self-serve platform?


## Decision: What capabilities are accessible more conveniently on a Data Mesh Supervision Plane?
**Evidences:** s1, s3, s4, s5, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s21, s22, s25, s29, s30, s31, s32, s34, s35, s36, s37, s38, s39, s40, s41, s42, s43, p1, p2, p3, p4, p5, p6

**Context:** 

### **Solution Options**
#### Solution 1: Schema Registry
**Evidences:** s4, s8, s12, s16, s32, s35, s36, p1, p2, p3, p4, p5

**Forces:**
- Automation (+) [s15, s18, s41]
- Interoperability (+) [s4, s10, s15, s16, s17, s30, s38, s42]
- Delegated ownership (+) [s1, s9, s30, s36, s42, s43]
- Complexity (-) [s1, s4, s12, s17, s18, s40]
- Maintenance Needs (-) []

#### Solution 2: API Catalog
**Evidences:** s1, s7, s8, s9, s10, s11, s14, s15, s17, s18, s21, s25, s29, s30, s31, s32, s34, s37, s38, s39, s40, s41, s42, p1, p2, p3, p4, p5, p6

**Forces:**
- Searchability (+) [s3, s11]
- Discoverability (+) [s3, s9, s32, s35]
- Usability (++) [s14, s16]
- Maintenance Needs (-) []
- Resource deployment process (-) [s17]

#### Solution 3: Data Observability
**Evidences:** s3, s4, s9, s10, s13, s14, s16, s17, s18, s21, s31, s32, s36, s39, s40, p4, p6

**Forces:**
- Data Quality (++) []
- Data Freshness (+) [s7, s17]
- Accuracy (+) [s21]
- Transparency (++) [s32]
- Maintenance Needs (-) []
- Time-to-Value (-) [s12]

#### Solution 4: Metadata Management
**Evidences:** s9, s10, s16, s17, s22, s30, s34, s43

**Forces:**
- Ad hoc exploration (++) [s12]
- Discoverability (++) [s3, s9, s32, s35]
- Searchability (++) [s3, s11]
- Accessibility (+) [s9, s30, s42]
- Delegated ownership (+) [s1, s9, s30, s36, s42, s43]
- Feature Engineering (+) [s12]
- Maintenance Needs (-) []

#### **Next Decision**: What elements should be included in the user interface (UI) of a self-serve platform?


## Decision: What elements should be included in the user interface (UI) of a self-serve platform?
**Evidences:** s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s21, s22, s24, s25, s26, s27, s28, s29, s30, s31, s32, s33, s34, s35, s36, s37, s38, s39, s40, s41, s42, s43, p1, p2, p3, p4, p5, p6

**Context:** 

### **Solution Options**
#### Solution 1: Cataloging Function
**Evidences:** s1, s3, s9, s10, s13, s14, s15, s16, s17, s18, s21, s24, s27, s28, s29, s30, s32, s33, s35, s36, s37, s38, s42, s43, p1, p2, p4, p5, p6

**Forces:**
- Discoverability (++) [s3, s9, s32, s35]
- Searchability (++) [s3, s11]
- Usability (+) [s14, s16]
- Understandability (+) [s12]
- Duplication (+) [s15, s30, s35, s36]
- Resource deployment process (-) [s17]
- Complexity (-) [s1, s4, s12, s17, s18, s40]
- Maintenance Needs (-) [s27]

#### Solution 2: Data Transformation Function
**Evidences:** s5, s6, s11, s12, s13, s16, s17, s18, s26, s27, s28, s30, s31, s33, s35, s37, s38, s40, s41, s42, s43, p1, p5

**Forces:**
- Flexibility (++) [s1]
- Feature Engineering (+) [s12]
- Inconsistencies between deployed resources and declrared code in source control (-) [s17]
- Maintenance Needs (-) [s27]

#### Solution 3: Role-based Access Control
**Evidences:** s2, s3, s5, s8, s9, s11, s13, s15, s16, s17, s26, s27, s28, s29, s31, s32, s33, s35, s42, s43, p1, p3, p4

**Forces:**
- Delegated ownership (+) [s1, s6, s9, s24, s30, s36, s42, s43]
- Control over data (+) [s1, s8]
- Accessibility (+) [s2, s9, s26, s27, s30, s42]
- Transparency (++) [s32]
- Security (+) [s2, s3, s5, s7, s8, s9, s11, s13, s15, s16, s17, s24, s26, s27, s28, s29, s30, s31, s32, s35, s43, p1, p3]
- Agility (-) [s9, s21, s22, s37, s39]
- Efficiency (-) [s4, s24, s25, s37, s39]

#### Solution 4: Data Governance function
**Evidences:** s1, s2, s4, s6, s7, s12, s14, s15, s16, s17, s21, s24, s25, s27, s28, s29, s30, s31, s32, s34, s36, s37, s38, s39, s40, s41, s42, s43, p6

**Forces:**
- Transparency (+) [s32]
- Security (++) [s2, s3, s5, s7, s8, s9, s11, s13, s15, s16, s17, s24, s26, s27, s28, s29, s30, s31, s32, s35, s43, p1, p3]
- Control over data (++) [s1, s8]
- Global governance (+) [s7, s9]
- Decentralization (-) [s1, s3, s4, s9, s15, s35, s36]
- Flexibility (-) [s1]

#### Solution 5: Application build function
**Evidences:** s4, s10, s12, s17, s22, s26, s29, s33, s39

**Forces:**
- Automation (+) [s15, s18, s24, s41]
- Agility (+) [s9, s21, s22, s37, s39]
- Time-to-Value (+) [s12]
- Complexity (-) [s1, s4, s12, s17, s18, s40]
- Global governance (-) [s7, s9]

#### Solution 6: Query Recommendation Function
**Evidences:** s3, s5, s11, s13, s16, s27, s32, s33, s34

**Forces:**
- Searchability (+) [s3, s11]
- Discoverability (+) [s3, s9, s32, s35]
- Ad hoc exploration (+) [s12]
- Usability (++) [s14, s16]
- Flexibility (-) [s1]
- Transparency (-) [s32]

#### **Next Decision**:  How to align a self-serve platform and its components with data mesh?


## Decision:  How to align a self-serve platform and its components with data mesh?
**Evidences:** s1, s2, s8, p1, p2, p3, p5, p6

**Context:** 

### **Solution Options**
#### Solution 1: Single Infrastructure Provisioning and Data Product Developer Experience Plane
**Evidences:** s1


#### Solution 2: Source system- and consumer-aligned Infrastructure Provisioning and Data Product Developer Experience Planes
**Evidences:** s1, s2, s8, p2, p3, p5, p6

**Forces:**
- Automation (+) []
- Resource deployment process (+) []
- Efficiency (+) []
- Agility (+) []
- Latency (-) []
- Data Freshness (-) []

#### Solution 3: Hub-, generic-, and special Infrastructure Provisioning and Data Product Developer Experience Planes
**Evidences:** s1, p3, p5

**Forces:**
- Agility (+) []
- Flexibility (+) [s1]
- Adapt to changing volumes (+) []
- Autonomous (+) [s2]
- Interoperability (-) []
- Avoids Information Island (-) []
- Discoverability (-) []

#### Solution 4: Functional and Eegionally Infrastructure Provisioning and Data Product Developer Experience Planes
**Evidences:** s1, p1, p3

**Forces:**
- Federated analytics (+) []
- Flexibility (+) [s1]
- Delegated ownership (-) [s1]
- Agility (-) []

#### Solution 5: Multiple Data Mesh Governance Planes
**Evidences:** s1

**Forces:**
- Scalability (+) [s1]
- Decentralization (+) [s1]
- Global governance (+) []
- Delegated ownership (+) [s1]
- Agility (-) []
- Time-to-Value (-) []



# Forces: 
- Complexity [s1, s4, s12, s17, s18, s40]
- Data Quality []
- Transparency [s32]
- Latency [s29]
- Maintenance Needs [s27]
- Duplication [s15, s30, s35, s36]
- Ease of Administration [s16]
- Time-to-Value [s12]
- Agility [s9, s20, s21, s22, s37, s39]
- Data Freshness [s7, s17]
- Interoperability [s4, s10, s15, s16, s17, s30, s38, s42]
- Decentralization [s1, s3, s4, s9, s15, s35, s36]
- Compatability [s4, s32, s40, s41]
- Efficiency [s4, s24, s25, s37, s39]
- Distinguish [s1]
- Domain-agnostic [s1]
- Flexibility in regional or legal boundaries [s1]
- Control over data [s1, s8]
- Redeliveries [s1]
- Scalability [s1, s6, s9, s12, s13, s16, s24, s29, s31, s36, s42]
- Searchability [s3, s11]
- Discoverability [s3, s9, s32, s35]
- Abstract away computational details [s4]
- Elastic [s4]
- Adapt to changing volumes [s4]
- Autonomous [s2, s6, s9, s10, s13, s16, s20, s38]
- Data movement [s7, s8, s9]
- Global governance [s7, s9]
- Federated analytics [s9, s16]
- Delegated ownership [s1, s6, s9, s24, s30, s36, s42, s43]
- Flexibility [s1]
- Ad hoc exploration [s12]
- Feature Engineering [s12]
- Understandability [s12]
- Accessibility [s2, s9, s26, s27, s30, s42]
- Automation [s15, s18, s19, s24, s41]
- Usability [s14, s16]
- Resource deployment process [s17]
- Inconsistencies between deployed resources and declrared code in source control [s17]
- Reduce work done by data product team [s17]
- Easily Replicable [s19]
- Accuracy [s21]
- Avoids Information Island [s25]
- Container Registry [s10, s26, s29, s30, p2, p5]
- Entry Barrier [s16, s34]
- Security [s2, s3, s5, s7, s8, s9, s11, s13, s15, s16, s17, s24, s26, s27, s28, s29, s30, s31, s32, s35, s43, p1, p3]


