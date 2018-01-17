# Important Links:
## LDP-DL Technical Report: http://w3id.org/ldpdl/technical_report.pdf
## LDP-DL RDF Syntax and Semantics: http://w3id.org/ldpdl/

# Experiments done using ShapeLDP, InterLDP and LDP implementations

This page records LDP datasets generated by <a href="https://github.com/noorbakerally/ShapeLDP">ShapeLDP</a> and deployed via an LDP using InterLDP. The generation of these LDP datasets and their deployment occured in the following scenarios:

1. Data portals in countries
2. Parking in Grenoble
3. DCAT catalogs from data portals in France 

All LDPs mentioned on this page can be browsed using GeminiLDP (our LDP browser)

# Data portals in different countries

- Original data source (https://tinyurl.com/y7jmnea): contains a number of countries and data portals associated to them
- Design document: https://github.com/noorbakerally/LDPDatasetExamples/blob/master/DesignDocuments/dCountryPortals.ttl 
- LDP description: The LDP shows a number of countries and for each countries, provides data portals associated with them
- LDP URL: http://opensensingcity.emse.fr/ldpdfend/dataportals/countries
- LDP Browser URL: http://opensensingcity.emse.fr/ldp-browser?http://opensensingcity.emse.fr/ldpdfend/dataportals/countries	 
# Parking in Grenoble

- Original data source: The data source consists of two parts, the static data which provides general details about the parking facility and a dynamic part which provides information about its parking availability status

	- static data source: http://data.metropolegrenoble.fr/ckan/dataset/parkings-relais-p-r/resource/ff54c102-b032-49b2-b4f8-9cae9fde863f
	- dynamic data source: http://data.metropolegrenoble.fr/ckan/dataset/parkings-relais-p-r/resource/457aa891-b53e-4a5d-aa9b-1be62201c088 

- Design document: https://github.com/noorbakerally/LDPDatasetExamples/blob/master/DesignDocuments/dCountryPortals.ttl 
- LDP description: The LDP operates in virtual mode and provide data which is generated at the request time using both the static and dynamic data
- LDP URL: http://opensensingcity.emse.fr/ldpdfend/grenoble/parkings
- LDP Browser URL: http://opensensingcity.emse.fr/ldp-browser?http://opensensingcity.emse.fr/ldpdfend/grenoble/parkings 	
# DCAT catalogs from data portals in France

Original data source description: <a href="https://www.opendatasoft.com/a-comprehensive-list-of-all-open-data-portals-around-the-world/#/france">OpenDataSoft</a> provides open data portals for a number of countries. We choose the data portals from France and download their DCAT dataset wherever it is available. We obtained 22 DCAT datasets for 22 data portals and for each of them, we deploy 5 LDPs based on the following designs:

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
 	- Description: Design6 is a generic design. For each class, an LDP container is created. In it, an LDP container which contains an LDP RDF source for every instance of the class and an LDP container which contains LDP containers for every subclass of the class are created. The <a href="https://github.com/noorbakerally/LDPDatasetExamples/blob/master/DesignDocuments/d6.ttl#L42">definition for creating subclasses</a> is recursive so that subclasses containers are recursively created till leaves.  
	- URL: 	 https://github.com/noorbakerally/LDPDatasetExamples/blob/master/DesignDocuments/d6.ttl

For the above 6 LDP designs, we deploy 5 LDPs for each 22 DCAT datasets (136 in all). A description of all the 136 LDPs is available in RDF at . Using this RDF file, we generate another LDP based on the design document which serves as an entry point for all the 136 LDPs. The entry point LDP can be found at http://opensensingcity.emse.fr/ldpdfend/designs and can be viewed via the LDP browser at http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/designs

All the remaining 136 LDPs can described below

### DataTourism62
Portal URL: [https://tourisme62.opendatasoft.com](https://tourisme62.opendatasoft.com)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/tourism62/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/tourism62/d1/catalog

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/tourism62/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/tourism62/d2/catalog

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/tourism62/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/tourism62/d3/catalog

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/tourism62/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/tourism62/d4/catalog

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/tourism62/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/tourism62/d5/catalog

#### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/tourism62/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/tourism62/d6/classes


### Open Data Angers [City]
Portal URL: [https://data.angers.fr/explore/?sort=modified](https://data.angers.fr/explore/?sort=modified)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/angers/d1/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/angers/d1/classes

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/angers/d2/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/angers/d2/classes

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/angers/d3/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/angers/d3/classes

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/angers/d4/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/angers/d4/classes

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/angers/d5/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/angers/d5/classes

#### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/angers/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/angers/d6/classes


### Bistrotdepays
Portal URL: [https://bistrotdepays.opendatasoft.com](https://bistrotdepays.opendatasoft.com)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d1/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d1/classes

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d2/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d2/classes

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d3/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d3/classes

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d4/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d4/classes

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d5/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d5/classes

#### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d6/classes


### dataNova
Portal URL: [https://datanova.legroupe.laposte.fr](https://datanova.legroupe.laposte.fr)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/datanova/d1/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datanova/d1/classes

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/datanova/d2/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datanova/d2/classes

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/datanova/d3/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datanova/d3/classes

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/datanova/d4/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datanova/d4/classes

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/datanova/d5/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datanova/d5/classes

#### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/datanova/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datanova/d6/classes


### Data Sarthe
Portal URL: [https://data.sarthe.fr](https://data.sarthe.fr)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/sarthe/d1/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sarthe/d1/classes

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/sarthe/d2/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sarthe/d2/classes

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/sarthe/d3/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sarthe/d3/classes

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/sarthe/d4/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sarthe/d4/classes

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/sarthe/d5/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sarthe/d5/classes

#### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/sarthe/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sarthe/d6/classes


### Data Enedis
Portal URL: [https://data.enedis.fr](https://data.enedis.fr)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/enedis/d1/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/enedis/d1/classes

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/enedis/d2/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/enedis/d2/classes

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/enedis/d3/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/enedis/d3/classes

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/enedis/d4/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/enedis/d4/classes

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/enedis/d5/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/enedis/d5/classes

#### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/enedis/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/enedis/d6/classes


### Open data hauts-de-seine
Portal URL: [https://opendata.hauts-de-seine.fr](https://opendata.hauts-de-seine.fr)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d1/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d1/classes

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d2/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d2/classes

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d3/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d3/classes

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d4/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d4/classes

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d5/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d5/classes

#### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d6/classes


### Grand Poitiers Open Data [City]
Portal URL: [https://data.grandpoitiers.fr](https://data.grandpoitiers.fr)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d1/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d1/classes

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d2/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d2/classes

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d3/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d3/classes

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d4/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d4/classes

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d5/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d5/classes

#### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d6/classes


### Data Ile de France
Portal URL: [https://data.iledefrance.fr/](https://data.iledefrance.fr/)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/iledefrance/d1/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/iledefrance/d1/classes

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/iledefrance/d2/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/iledefrance/d2/classes

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/iledefrance/d3/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/iledefrance/d3/classes

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/iledefrance/d4/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/iledefrance/d4/classes

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/iledefrance/d5/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/iledefrance/d5/classes

#### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/iledefrance/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/iledefrance/d6/classes


### Data Info Locale
Portal URL: [https://datainfolocale.opendatasoft.com/](https://datainfolocale.opendatasoft.com/)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d1/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d1/classes

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d2/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d2/classes

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d3/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d3/classes

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d4/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d4/classes

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d5/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d5/classes

#### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d6/classes


### Open Data La Haute-garonne
Portal URL: [https://data.haute-garonne.fr](https://data.haute-garonne.fr)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d1/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d1/classes

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d2/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d2/classes

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d3/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d3/classes

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d4/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d4/classes

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d5/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d5/classes

#### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d6/classes


### Navitia
Portal URL: [https://navitia.opendatasoft.com](https://navitia.opendatasoft.com)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/navitia/d1/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/navitia/d1/classes

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/navitia/d2/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/navitia/d2/classes

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/navitia/d3/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/navitia/d3/classes

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/navitia/d4/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/navitia/d4/classes

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/navitia/d5/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/navitia/d5/classes

#### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/navitia/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/navitia/d6/classes


### Open Data Corsia
Portal URL: [https://www.data.corsica](https://www.data.corsica)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/corsica/d1/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/corsica/d1/classes

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/corsica/d2/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/corsica/d2/classes

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/corsica/d3/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/corsica/d3/classes

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/corsica/d4/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/corsica/d4/classes

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/corsica/d5/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/corsica/d5/classes

#### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/corsica/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/corsica/d6/classes


### Paris Data [City]
Portal URL: [https://opendata.paris.fr](https://opendata.paris.fr)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/paris/d1/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/paris/d1/classes

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/paris/d2/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/paris/d2/classes

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/paris/d3/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/paris/d3/classes

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/paris/d4/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/paris/d4/classes

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/paris/d5/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/paris/d5/classes

#### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/paris/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/paris/d6/classes


### Data Ratp
Portal URL: [https://data.ratp.fr](https://data.ratp.fr)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/ratp/d1/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/ratp/d1/classes

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/ratp/d2/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/ratp/d2/classes

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/ratp/d3/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/ratp/d3/classes

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/ratp/d4/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/ratp/d4/classes

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/ratp/d5/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/ratp/d5/classes

#### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/ratp/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/ratp/d6/classes


### Rennes Metropole [City]
Portal URL: [https://data.iledefrance.fr/](https://data.iledefrance.fr/)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d1/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d1/classes

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d2/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d2/classes

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d3/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d3/classes

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d4/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d4/classes

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d5/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d5/classes

#### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d6/classes


### SNCF Open Data
Portal URL: [https://data.iledefrance.fr/](https://data.iledefrance.fr/)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/sncf/d1/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sncf/d1/classes

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/sncf/d2/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sncf/d2/classes

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/sncf/d3/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sncf/d3/classes

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/sncf/d4/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sncf/d4/classes

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/sncf/d5/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sncf/d5/classes

#### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/sncf/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sncf/d6/classes


### Ile de France Mobilite
Portal URL: [https://opendata.stif.info](https://opendata.stif.info)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/stif/d1/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/stif/d1/classes

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/stif/d2/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/stif/d2/classes

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/stif/d3/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/stif/d3/classes

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/stif/d4/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/stif/d4/classes

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/stif/d5/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/stif/d5/classes

#### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/stif/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/stif/d6/classes


### Data Toulouse Metropole [City]
Portal URL: [https://data.toulouse-metropole.fr](https://data.toulouse-metropole.fr)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/toulouse/d1/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/toulouse/d1/classes

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/toulouse/d2/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/toulouse/d2/classes

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/toulouse/d3/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/toulouse/d3/classes

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/toulouse/d4/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/toulouse/d4/classes

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/toulouse/d5/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/toulouse/d5/classes

#### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/toulouse/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/toulouse/d6/classes


### Ville D'Agen Open Data [City]
Portal URL: [https://data.agen.fr](https://data.agen.fr)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/agen/d1/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/agen/d1/classes

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/agen/d2/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/agen/d2/classes

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/agen/d3/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/agen/d3/classes

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/agen/d4/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/agen/d4/classes

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/agen/d5/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/agen/d5/classes

#### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/agen/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/agen/d6/classes


### DATA ISSY.com
Portal URL: [https://data.issy.com](https://data.issy.com)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/issy/d1/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/issy/d1/classes

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/issy/d2/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/issy/d2/classes

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/issy/d3/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/issy/d3/classes

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/issy/d4/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/issy/d4/classes

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/issy/d5/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/issy/d5/classes

#### LDP based on Design6:

- URL:http://opensensingcity.emse.fr/ldpdfend/issy/d6/classes
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/issy/d6/classes


