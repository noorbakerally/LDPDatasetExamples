This page records LDPs generated within the following scenarios:

1. Data portals in countries
2. Parking in Grenoble
3. DCAT catalogs from data portals in France

To generate the LDPs, their LDP datasets have been generated using BlazeLDP and then exposed using InterLDP.



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

For the above 5 LDP designs, we deploy 5 LDPs for each 22 DCAT datasets (110 in all). A description of all the 110 LDPs is available in RDF at . Using this RDF file, we generate another LDP based on the design document which serves as an entry point for all the 110 LDPs. The entry point LDP can be found at http://opensensingcity.emse.fr/ldpdfend/designs and can be viewed via the LDP browser at http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/designs

All the remaining 110 LDPs can described below


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


### Open Data Angers [City]
Portal URL: [https://data.angers.fr/explore/?sort=modified](https://data.angers.fr/explore/?sort=modified)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/angers/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/angers/d1/catalog

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/angers/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/angers/d2/catalog

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/angers/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/angers/d3/catalog

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/angers/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/angers/d4/catalog

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/angers/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/angers/d5/catalog


### Bistrotdepays
Portal URL: [https://bistrotdepays.opendatasoft.com](https://bistrotdepays.opendatasoft.com)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d1/catalog

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d2/catalog

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d3/catalog

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d4/catalog

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/bistrotdepays/d5/catalog


### dataNova
Portal URL: [https://datanova.legroupe.laposte.fr](https://datanova.legroupe.laposte.fr)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/datanova/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datanova/d1/catalog

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/datanova/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datanova/d2/catalog

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/datanova/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datanova/d3/catalog

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/datanova/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datanova/d4/catalog

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/datanova/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datanova/d5/catalog


### Data Sarthe
Portal URL: [https://data.sarthe.fr](https://data.sarthe.fr)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/sarthe/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sarthe/d1/catalog

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/sarthe/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sarthe/d2/catalog

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/sarthe/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sarthe/d3/catalog

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/sarthe/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sarthe/d4/catalog

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/sarthe/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sarthe/d5/catalog


### Data Enedis
Portal URL: [https://data.enedis.fr](https://data.enedis.fr)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/enedis/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/enedis/d1/catalog

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/enedis/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/enedis/d2/catalog

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/enedis/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/enedis/d3/catalog

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/enedis/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/enedis/d4/catalog

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/enedis/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/enedis/d5/catalog


### Open data hauts-de-seine
Portal URL: [https://opendata.hauts-de-seine.fr](https://opendata.hauts-de-seine.fr)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d1/catalog

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d2/catalog

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d3/catalog

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d4/catalog

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/hauts-de-seine/d5/catalog


### Grand Poitiers Open Data [City]
Portal URL: [https://data.grandpoitiers.fr](https://data.grandpoitiers.fr)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d1/catalog

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d2/catalog

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d3/catalog

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d4/catalog

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/grandpoitiers/d5/catalog


### Data Ile de France
Portal URL: [https://data.iledefrance.fr/](https://data.iledefrance.fr/)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/iledefrance/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/iledefrance/d1/catalog

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/iledefrance/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/iledefrance/d2/catalog

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/iledefrance/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/iledefrance/d3/catalog

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/iledefrance/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/iledefrance/d4/catalog

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/iledefrance/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/iledefrance/d5/catalog


### Data Info Locale
Portal URL: [https://datainfolocale.opendatasoft.com/](https://datainfolocale.opendatasoft.com/)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d1/catalog

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d2/catalog

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d3/catalog

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d4/catalog

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/datainfolocale/d5/catalog


### Open Data La Haute-garonne
Portal URL: [https://data.haute-garonne.fr](https://data.haute-garonne.fr)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d1/catalog

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d2/catalog

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d3/catalog

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d4/catalog

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/haute-garonne/d5/catalog


### Navitia
Portal URL: [https://navitia.opendatasoft.com](https://navitia.opendatasoft.com)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/navitia/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/navitia/d1/catalog

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/navitia/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/navitia/d2/catalog

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/navitia/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/navitia/d3/catalog

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/navitia/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/navitia/d4/catalog

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/navitia/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/navitia/d5/catalog


### Open Data Corsia
Portal URL: [https://www.data.corsica](https://www.data.corsica)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/corsica/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/corsica/d1/catalog

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/corsica/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/corsica/d2/catalog

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/corsica/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/corsica/d3/catalog

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/corsica/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/corsica/d4/catalog

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/corsica/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/corsica/d5/catalog


### Paris Data [City]
Portal URL: [https://opendata.paris.fr](https://opendata.paris.fr)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/paris/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/paris/d1/catalog

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/paris/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/paris/d2/catalog

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/paris/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/paris/d3/catalog

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/paris/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/paris/d4/catalog

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/paris/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/paris/d5/catalog


### Data Ratp
Portal URL: [https://data.ratp.fr](https://data.ratp.fr)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/ratp/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/ratp/d1/catalog

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/ratp/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/ratp/d2/catalog

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/ratp/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/ratp/d3/catalog

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/ratp/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/ratp/d4/catalog

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/ratp/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/ratp/d5/catalog


### Rennes Metropole [City]
Portal URL: [https://data.iledefrance.fr/](https://data.iledefrance.fr/)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d1/catalog

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d2/catalog

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d3/catalog

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d4/catalog

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/rennesmetropole/d5/catalog


### SNCF Open Data
Portal URL: [https://data.iledefrance.fr/](https://data.iledefrance.fr/)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/sncf/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sncf/d1/catalog

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/sncf/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sncf/d2/catalog

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/sncf/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sncf/d3/catalog

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/sncf/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sncf/d4/catalog

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/sncf/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/sncf/d5/catalog


### Ile de France Mobilite
Portal URL: [https://opendata.stif.info](https://opendata.stif.info)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/stif/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/stif/d1/catalog

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/stif/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/stif/d2/catalog

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/stif/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/stif/d3/catalog

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/stif/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/stif/d4/catalog

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/stif/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/stif/d5/catalog


### Data Toulouse Metropole [City]
Portal URL: [https://data.toulouse-metropole.fr](https://data.toulouse-metropole.fr)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/toulouse/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/toulouse/d1/catalog

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/toulouse/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/toulouse/d2/catalog

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/toulouse/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/toulouse/d3/catalog

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/toulouse/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/toulouse/d4/catalog

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/toulouse/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/toulouse/d5/catalog


### Ville D'Agen Open Data [City]
Portal URL: [https://data.agen.fr](https://data.agen.fr)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/agen/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/agen/d1/catalog

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/agen/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/agen/d2/catalog

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/agen/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/agen/d3/catalog

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/agen/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/agen/d4/catalog

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/agen/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/agen/d5/catalog


### DATA ISSY.com
Portal URL: [https://data.issy.com](https://data.issy.com)

#### LDP based on Design1:

- URL:http://opensensingcity.emse.fr/ldpdfend/issy/d1/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/issy/d1/catalog

#### LDP based on Design2:

- URL:http://opensensingcity.emse.fr/ldpdfend/issy/d2/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/issy/d2/catalog

#### LDP based on Design3:

- URL:http://opensensingcity.emse.fr/ldpdfend/issy/d3/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/issy/d3/catalog

#### LDP based on Design4:

- URL:http://opensensingcity.emse.fr/ldpdfend/issy/d4/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/issy/d4/catalog

#### LDP based on Design5:

- URL:http://opensensingcity.emse.fr/ldpdfend/issy/d5/catalog
- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/issy/d5/catalog
