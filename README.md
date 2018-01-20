# Important Links:
## LDP-DL Technical Report: http://w3id.org/ldpdl/technical_report.pdf
## LDP-DL RDF Syntax and Semantics: http://w3id.org/ldpdl/

This page describes experiments performed to validate the use of [LDP-DL](https://w3id.org/ldpdl/) to validate the requirements described in the its [technical report](http://w3id.org/ldpdl/technical_report.pdf). There are 6 experiments. Firstly, we describe how the experiments validate the requirements then we describe the experiments themselves. In all the experiments, the main tools that are used are:
- ShapeLDP (Link to Github Repo: https://github.com/noorbakerally/ShapeLDP)
- InterLDP (Link to Github Repo: https://github.com/noorbakerally/InterLDP)
- POSTerLDP (Link to Github Repo: https://github.com/noorbakerally/POSTerLDP)


## Requirements Validation
The requirements outlined in LDP-DL technical report in Section 3 are:
- R1: Compatibility with the LDP standard
- R2: Open to heterogeneous data sources
- R3: Cope with hosting constraints
- R4: Reusability of the design document
- R5: Automatization of LDP Generation

The table below summarizes how the different experiments satisfy the requirements

|             | R1 | R2 | R3 | R4 | R5 |
|-------------|:--:|:--:|:--:|:--:|:--:|
| [Experiment1](#experiment1) | &#10004;   |    |    |    |  &#10004;  |
| [Experiment2](#experiment2) | &#10004;   |    |    |    | &#10004;   |
| [Experiment3](#experiment3) | &#10004;    | &#10004;   |    |    | &#10004;   |
| [Experiment4](#experiment4) | &#10004;    |  &#10004;  | &#10004;   |    |&#10004;    |
| [Experiment5](#experiment5) | &#10004;    |    |    |    | &#10004;   |

### R1: Compatibility with the LDP standard
In all experiments, all the LDPs generated are fully compatible with the LDP standard. But in particular, Experiment2 shows the static LDP datasets generated using ShapeLDP can be deployed on any compatible LDP server accepting POST requests. Thus, our approach for generating LDP is also compatible with all existing LDP server implementations.

### R2: Open to heterogeneous data sources
In both [Experiment2](#experiment2) and [Experiment3](#experiment3), R2 is satisfied by generating LDPs from data sources in two formats: CSV and JSON.

### R3: Cope with hosting constraints
In [Experiment3](#experiment3), we satisfy R3 by showing that the LDP is capable of always fetching fresh data from the real-time data dynamically from the original source without having the data in its environment 

### R4: Reusability of the design document
In [Experiment1](#experiment1), we satisfy R4 by showing that the same design document can be reused over multiple data sources (22 in all)

### R5: Automatization of LDP Generation
The automatization the generation of LDPs involves two parts: LDP design automatization and LDP deployment automatization. In our experiments, we satisfy by the latter either by directing exposing static (or dynamic) LDP datasets via InterLDP or deploying the LDP resources from them on an LDP server accepting POST requests using POSTerLDP.

The automatization of LDP design is not yet achieved. But in [Experiment5](#experiment5), our generic designs (Design6 and Design8) are used directly on data sources that uses OWL/RDFS vocabularies. The extra constraints on the data sources is that there should be cycles on in the class hierarchy else theoritically, ShapeLDP will try to generate an infinite static (or dynamic) LDP dataset. 


## Experiments

### Experiment1

#### Data source description
<a href="https://www.opendatasoft.com/a-comprehensive-list-of-all-open-data-portals-around-the-world/#/france">OpenDataSoft</a> provides open data portals for a number of countries. We choose the data portals from France and download their DCAT dataset wherever it is available. We obtained 22 DCAT datasets for 22 data portals and for each of them, we deploy 7 LDPs based on the designs described in the next section.


#### Design documents description
- Design1:
	- Description: Design1 describes an LDP where for each catalog and dataset, an LDP container is generated and for each distribution, an LDP RDF source is generated. For an LDP container generated for a particular catalog, there is a Null LDP container `datasets` to groups all the LDP containers generated for the datasets of the catalog. Also, for an LDP container generated for a particular dataset, there is a Null LDP container `distributions` to groups all the LDP containers generated for the distributions of the datasets.
	- URL: https://github.com/noorbakerally/LDPDatasetExamples/blob/master/DesignDocuments/d1.ttl
- Design2:
	- Description: Design2 is similar to Design1 except that it does not contains additional Null LDP containers for datasets and distributions.
	- URL:  https://github.com/noorbakerally/LDPDatasetExamples/blob/master/DesignDocuments/d2.ttl 
- Design3:
	- Description: Design3 describes an LDP where the datasets in a catalogs are organized in terms of the languages of the datasets 	 	
	- URL:  	 https://github.com/noorbakerally/LDPDatasetExamples/blob/master/DesignDocuments/d3.ttl
- Design4:
	- Description: Design4 describes an LDP where the datasets in a catalogs are organized in terms of the languages of the datasets 	
	- URL: 	 https://github.com/noorbakerally/LDPDatasetExamples/blob/master/DesignDocuments/d4.ttl
- Design5:
 	- Description: Design5 is somewhat a merge of Design3 and Design4 whereby datasets of a catalogs are organized in terms of both languages and themes
	- URL: 	 https://github.com/noorbakerally/LDPDatasetExamples/blob/master/DesignDocuments/d5.ttl
- Design6: 
	- Description: It is a generic design that provides a description of an LDP.   There is a top LDP container that groups all LDP-RSs describing all classes. These LDP-RS are LDP-BCs that contain two containers: for grouping the class subclasses and its instances. In the subclass (resp. instance) container , a container is generated for all subclasses (resp. instances). The <a href="https://github.com/noorbakerally/LDPDatasetExamples/blob/master/DesignDocuments/d6.ttl#L42">definition for creating subclasses</a> is recursive so that subclasses containers are recursively created till leaves.  
	- URL: https://github.com/noorbakerally/LDPDatasetExamples/blob/master/DesignDocuments/d6.ttl

-  Design8:
 	- Description: Design8 is a generic design. For each class, an LDP container is created. In it, an LDP container which contains an LDP RDF source for every instance of the class and an LDP container which contains LDP containers for every subclass of the class are created. The <a href="https://github.com/noorbakerally/LDPDatasetExamples/blob/54d390fa8941924392a29510742ac9b243ffa70f/DesignDocuments/d8.ttl#L38">definition for creating subclasses</a> is recursive so that subclasses containers are recursively created till leaves.  
	- URL: 	 https://github.com/noorbakerally/LDPDatasetExamples/blob/master/DesignDocuments/d6.ttl

#### Deployment description
For the above 7 designs documents, static LDP datasets are generated for the 22 DCAT datasets. All the static LDP datasets are then exposed via InterLDP. In all,  154 (22 x 7) LDPs are generated. The details of all generated LDPs are given in the next section.

#### Resulting LDPs
##### DataTourism62
Portal URL: [https://tourisme62.opendatasoft.com](https://tourisme62.opendatasoft.com)
Source URL: https://tourisme62.opendatasoft.com/api/v2/catalog/exports/ttl

###### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/tourism62/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/tourism62/d1/catalog

###### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/tourism62/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/tourism62/d2/catalog

###### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/tourism62/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/tourism62/d3/catalog

###### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/tourism62/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/tourism62/d4/catalog

###### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/tourism62/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/tourism62/d5/catalog

###### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/tourism62/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/tourism62/d6/classes

###### LDP based on Design8:

- URL:http://opensensingcity.emse.fr/ldpdfend/tourism62/d8/resources
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/tourism62/d8/resources


##### Open Data Angers [City]
Portal URL: [https://data.angers.fr/explore/?sort=modified](https://data.angers.fr/explore/?sort=modified)
Source URL: https://data.angers.fr/api/v2/catalog/exports/ttl

###### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/angers/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/angers/d1/catalog

###### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/angers/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/angers/d2/catalog

###### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/angers/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/angers/d3/catalog

###### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/angers/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/angers/d4/catalog

###### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/angers/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/angers/d5/catalog

###### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/angers/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/angers/d6/classes

###### LDP based on Design8:

- URL:http://opensensingcity.emse.fr/ldpdfend/angers/d8/resources
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/angers/d8/resources


##### Bistrotdepays
Portal URL: [https://bistrotdepays.opendatasoft.com](https://bistrotdepays.opendatasoft.com)
Source URL: https://bistrotdepays.opendatasoft.com/api/v2/catalog/exports/ttl

###### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d1/catalog

###### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d2/catalog

###### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d3/catalog

###### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d4/catalog

###### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d5/catalog

###### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d6/classes

###### LDP based on Design8:

- URL:http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d8/resources
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d8/resources


##### dataNova
Portal URL: [https://datanova.legroupe.laposte.fr](https://datanova.legroupe.laposte.fr)
Source URL: https://datanova.legroupe.laposte.fr/api/v2/catalog/exports/ttl

###### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/datanova/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datanova/d1/catalog

###### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/datanova/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datanova/d2/catalog

###### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/datanova/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datanova/d3/catalog

###### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/datanova/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datanova/d4/catalog

###### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/datanova/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datanova/d5/catalog

###### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/datanova/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datanova/d6/classes

###### LDP based on Design8:

- URL:http://opensensingcity.emse.fr/ldpdfend/datanova/d8/resources
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datanova/d8/resources


##### Data Sarthe
Portal URL: [https://data.sarthe.fr](https://data.sarthe.fr)
Source URL: https://data.sarthe.fr/api/v2/catalog/exports/ttl

###### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/sarthe/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sarthe/d1/catalog

###### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/sarthe/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sarthe/d2/catalog

###### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/sarthe/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sarthe/d3/catalog

###### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/sarthe/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sarthe/d4/catalog

###### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/sarthe/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sarthe/d5/catalog

###### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/sarthe/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sarthe/d6/classes

###### LDP based on Design8:

- URL:http://opensensingcity.emse.fr/ldpdfend/sarthe/d8/resources
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sarthe/d8/resources


##### Data Enedis
Portal URL: [https://data.enedis.fr](https://data.enedis.fr)
Source URL: https://data.enedis.fr/api/v2/catalog/exports/ttl

###### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/enedis/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/enedis/d1/catalog

###### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/enedis/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/enedis/d2/catalog

###### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/enedis/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/enedis/d3/catalog

###### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/enedis/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/enedis/d4/catalog

###### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/enedis/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/enedis/d5/catalog

###### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/enedis/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/enedis/d6/classes

###### LDP based on Design8:

- URL:http://opensensingcity.emse.fr/ldpdfend/enedis/d8/resources
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/enedis/d8/resources


##### Open data hauts-de-seine
Portal URL: [https://opendata.hauts-de-seine.fr](https://opendata.hauts-de-seine.fr)
Source URL: https://opendata.hauts-de-seine.fr/api/v2/catalog/exports/ttl

###### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d1/catalog

###### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d2/catalog

###### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d3/catalog

###### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d4/catalog

###### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d5/catalog

###### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d6/classes

###### LDP based on Design8:

- URL:http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d8/resources
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d8/resources


##### Grand Poitiers Open Data [City]
Portal URL: [https://data.grandpoitiers.fr](https://data.grandpoitiers.fr)
Source URL: https://data.grandpoitiers.fr/api/v2/catalog/exports/ttl

###### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d1/catalog

###### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d2/catalog

###### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d3/catalog

###### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d4/catalog

###### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d5/catalog

###### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d6/classes

###### LDP based on Design8:

- URL:http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d8/resources
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d8/resources


##### Data Ile de France
Portal URL: [https://data.iledefrance.fr/](https://data.iledefrance.fr/)
Source URL: https://data.iledefrance.fr/api/v2/catalog/exports/ttl

###### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/iledefrance/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/iledefrance/d1/catalog

###### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/iledefrance/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/iledefrance/d2/catalog

###### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/iledefrance/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/iledefrance/d3/catalog

###### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/iledefrance/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/iledefrance/d4/catalog

###### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/iledefrance/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/iledefrance/d5/catalog

###### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/iledefrance/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/iledefrance/d6/classes

###### LDP based on Design8:

- URL:http://opensensingcity.emse.fr/ldpdfend/iledefrance/d8/resources
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/iledefrance/d8/resources


##### Data Info Locale
Portal URL: [https://datainfolocale.opendatasoft.com/](https://datainfolocale.opendatasoft.com/)
Source URL: https://datainfolocale.opendatasoft.com/api/v2/catalog/exports/ttl

###### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d1/catalog

###### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d2/catalog

###### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d3/catalog

###### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d4/catalog

###### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d5/catalog

###### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d6/classes

###### LDP based on Design8:

- URL:http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d8/resources
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d8/resources


##### Open Data La Haute-garonne
Portal URL: [https://data.haute-garonne.fr](https://data.haute-garonne.fr)
Source URL: https://data.haute-garonne.fr/api/v2/catalog/exports/ttl

###### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d1/catalog

###### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d2/catalog

###### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d3/catalog

###### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d4/catalog

###### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d5/catalog

###### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d6/classes

###### LDP based on Design8:

- URL:http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d8/resources
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d8/resources


##### Navitia
Portal URL: [https://navitia.opendatasoft.com](https://navitia.opendatasoft.com)
Source URL: https://navitia.opendatasoft.com/api/v2/catalog/exports/ttl

###### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/navitia/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/navitia/d1/catalog

###### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/navitia/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/navitia/d2/catalog

###### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/navitia/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/navitia/d3/catalog

###### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/navitia/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/navitia/d4/catalog

###### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/navitia/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/navitia/d5/catalog

###### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/navitia/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/navitia/d6/classes

###### LDP based on Design8:

- URL:http://opensensingcity.emse.fr/ldpdfend/navitia/d8/resources
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/navitia/d8/resources


##### Open Data Corsia
Portal URL: [https://www.data.corsica](https://www.data.corsica)
Source URL: https://www.data.corsica/api/v2/catalog/exports/ttl

###### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/corsica/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/corsica/d1/catalog

###### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/corsica/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/corsica/d2/catalog

###### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/corsica/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/corsica/d3/catalog

###### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/corsica/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/corsica/d4/catalog

###### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/corsica/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/corsica/d5/catalog

###### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/corsica/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/corsica/d6/classes

###### LDP based on Design8:

- URL:http://opensensingcity.emse.fr/ldpdfend/corsica/d8/resources
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/corsica/d8/resources


##### Paris Data [City]
Portal URL: [https://opendata.paris.fr](https://opendata.paris.fr)
Source URL: https://opendata.paris.fr/api/v2/catalog/exports/ttl

###### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/paris/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/paris/d1/catalog

###### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/paris/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/paris/d2/catalog

###### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/paris/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/paris/d3/catalog

###### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/paris/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/paris/d4/catalog

###### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/paris/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/paris/d5/catalog

###### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/paris/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/paris/d6/classes

###### LDP based on Design8:

- URL:http://opensensingcity.emse.fr/ldpdfend/paris/d8/resources
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/paris/d8/resources


##### Data Ratp
Portal URL: [https://data.ratp.fr](https://data.ratp.fr)
Source URL: https://data.ratp.fr/api/v2/catalog/exports/ttl

###### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/ratp/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/ratp/d1/catalog

###### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/ratp/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/ratp/d2/catalog

###### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/ratp/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/ratp/d3/catalog

###### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/ratp/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/ratp/d4/catalog

###### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/ratp/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/ratp/d5/catalog

###### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/ratp/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/ratp/d6/classes

###### LDP based on Design8:

- URL:http://opensensingcity.emse.fr/ldpdfend/ratp/d8/resources
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/ratp/d8/resources


##### Rennes Metropole [City]
Portal URL: [https://data.iledefrance.fr/](https://data.iledefrance.fr/)
Source URL: https://data.rennesmetropole.fr/api/v2/catalog/exports/ttl
Source URL: https://data.rennesmetropole.fr/api/v2/catalog/exports/ttl

###### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d1/catalog

###### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d2/catalog

###### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d3/catalog

###### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d4/catalog

###### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d5/catalog

###### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d6/classes

###### LDP based on Design8:

- URL:http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d8/resources
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d8/resources


##### SNCF Open Data
Portal URL: [https://data.iledefrance.fr/](https://data.iledefrance.fr/)
Source URL: https://ressources.data.sncf.com/api/v2/catalog/exports/ttl

###### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/sncf/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sncf/d1/catalog

###### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/sncf/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sncf/d2/catalog

###### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/sncf/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sncf/d3/catalog

###### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/sncf/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sncf/d4/catalog

###### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/sncf/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sncf/d5/catalog

###### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/sncf/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sncf/d6/classes

###### LDP based on Design8:

- URL:http://opensensingcity.emse.fr/ldpdfend/sncf/d8/resources
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sncf/d8/resources


##### Ile de France Mobilite
Portal URL: [https://opendata.stif.info](https://opendata.stif.info)
Source URL: https://opendata.stif.info/api/v2/catalog/exports/ttl

###### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/stif/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/stif/d1/catalog

###### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/stif/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/stif/d2/catalog

###### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/stif/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/stif/d3/catalog

###### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/stif/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/stif/d4/catalog

###### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/stif/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/stif/d5/catalog

###### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/stif/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/stif/d6/classes

###### LDP based on Design8:

- URL:http://opensensingcity.emse.fr/ldpdfend/stif/d8/resources
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/stif/d8/resources


##### Data Toulouse Metropole [City]
Portal URL: [https://data.toulouse-metropole.fr](https://data.toulouse-metropole.fr)
Source URL: https://data.toulouse-metropole.fr/api/v2/catalog/exports/ttl

###### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/toulouse/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/toulouse/d1/catalog

###### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/toulouse/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/toulouse/d2/catalog

###### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/toulouse/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/toulouse/d3/catalog

###### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/toulouse/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/toulouse/d4/catalog

###### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/toulouse/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/toulouse/d5/catalog

###### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/toulouse/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/toulouse/d6/classes

###### LDP based on Design8:

- URL:http://opensensingcity.emse.fr/ldpdfend/toulouse/d8/resources
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/toulouse/d8/resources


##### Ville D'Agen Open Data [City]
Portal URL: [https://data.agen.fr](https://data.agen.fr)
Source URL: https://data.agen.fr/api/v2/catalog/exports/ttl

###### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/agen/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/agen/d1/catalog

###### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/agen/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/agen/d2/catalog

###### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/agen/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/agen/d3/catalog

###### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/agen/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/agen/d4/catalog

###### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/agen/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/agen/d5/catalog

###### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/agen/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/agen/d6/classes

###### LDP based on Design8:

- URL:http://opensensingcity.emse.fr/ldpdfend/agen/d8/resources
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/agen/d8/resources


##### DATA ISSY.com
Portal URL: [https://data.issy.com](https://data.issy.com)
Source URL: https://data.issy.com/api/v2/catalog/exports/ttl

###### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/issy/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/issy/d1/catalog

###### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/issy/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/issy/d2/catalog

###### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/issy/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/issy/d3/catalog

###### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/issy/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/issy/d4/catalog

###### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/issy/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/issy/d5/catalog

###### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/issy/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/issy/d6/classes

###### LDP based on Design8:

- URL:http://opensensingcity.emse.fr/ldpdfend/issy/d8/resources
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/issy/d8/resources

### Experiment2
The DCAT dataset from [Bistrodepays Open Data Portal](https://bistrotdepays.opendatasoft.com) is deployed on two different LDP implementations: [Apache Marmotta](http://marmotta.apache.org/) and [Gold](http://marmotta.apache.org/).

#### Data source description
Source URL: https://bistrotdepays.opendatasoft.com/api/v2/catalog/exports/ttl

#### Design document description
The design document used is Design2 as it was used in [Experiment1](#experiment1)

#### Deployment description
ShapeLDP is used to generate the static LDP dataset from using the design document with respect to the data sources. Then POSTerLDP consumes the static LDP dataset, generates LDP POST requests for LDP resources from the static LDP dataset and sends them on 2 LDP servers that are instances of Apache Marmotta and Gold respectively.

#### Resulting LDPs
- Resulting LDP on LDP Server (Apache Marmotta)
	- URL: http://opensensingcity.emse.fr/ldpapp/marmotta-bistro/catalog
	- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpapp/marmotta-bistro/catalog
- Resulting LDP on LDP Server (Gold)
	- URL:http://opensensingcity.emse.fr/ldpapp/gold-bistro/catalog/
	- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpapp/gold-bistro/catalog/

### Experiment3
The following two datasets are considered:
1.  https://opendata.paris.fr/explore/dataset/velib-emplacement-des-stations (GeoJSON)
2.   https://opendata.paris.fr/explore/dataset/liste-des-stations-de-services-de-vehicules (CSV)

Both datasets are obtained from [Paris Open Data Portal](https://opendata.paris.fr/page/home/).  The first dataset describes bicycle station in Paris and the second dataset describe service stations for shared vehicles in Paris.

In the [design document](https://github.com/noorbakerally/ParisDataPlatform/blob/master/designDocument.ttl), the data sources are provided together with their lifting rules.  With respect to these data sources, the LDP dataset is generated and exposed via an LDP:
- LDP URL: http://opensensingcity.emse.fr/ldpdfend/city/paris
- Browse LDP via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/city/paris


### Experiment4
The [Grenoble Open Data Portal](http://http://data.metropolegrenoble.fr/) provides a [dataset](http://data.metropolegrenoble.fr/ckan/dataset/parkings-relais-p-r) about [incentive parking lots](https://en.wikipedia.org/wiki/Park_and_ride). The datset itself is divided into two sub-dataset: static and dynamic. The static part provides fixed information about the incentive parkings lots such as address, types, geographical details etc. It is provided into two distributions that are in CSV and GeoJSOn, both of which contain similar information. The dynamic part provides real-time information about the number of parking spaces available in the parking lots defined in the static part. It is available in JSON. For the static part, we use its CSV distribution and for the dynamic part, we use it JSON distribution. 

In the [design document](https://github.com/noorbakerally/LDPDatasetExamples/blob/master/DesignDocuments/dGrenobleParking.ttl), for both the static and dynamic part, RDF liftings rules are provided. 

Using ShapeLDP, the dynamic LDP dataset is generated from the design document with respect to the data sources. The dynamic LDP dataset is then exposed via InterLDP operating in dynamic mode. 
Resulting LDP: 
- LDP URL: http://opensensingcity.emse.fr/ldpdfend/grenoble/parkings
- Browser LDP via LDP Browser at: http://opensensingcity.emse.fr/ldp-browser?http://opensensingcity.emse.fr/ldpdfend/grenoble/parkings

### Experiment 5
In this experiment, the two generic designs documents are used to deploy the [BBC wildlife dataset](https://github.com/noorbakerally/bbc-wildlife).

#### Data source description
Source URL: https://github.com/noorbakerally/bbc-wildlife

#### Design document description
The two generic designs, Design6 and Design8 are used as in [Experiment1](#experiment1)

#### Deployment description
For the same data source, ShapeLDP is used to generate the static LDP dataset using the two design documents  to generate two different static LDP datasets that are then deployed via InterLDP. 

#### Resulting LDPs
- Resulting LDP based on Design6
	- URL:http://opensensingcity.emse.fr/ldpdfend/d6/bbc/life/classes
	- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/d6/bbc/life/classes
	
- Resulting LDP based on Design8
	- URL:http://opensensingcity.emse.fr/ldpdfend/d8/bbc/life/resources
	- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/d8/bbc/life/resources
