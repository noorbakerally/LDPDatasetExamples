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