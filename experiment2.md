# Experiment2
The DCAT dataset from [Bistrodepays Open Data Portal](https://bistrotdepays.opendatasoft.com) is deployed on two different LDP implementations: [Apache Marmotta](http://marmotta.apache.org/) and [Gold](http://marmotta.apache.org/).

## Data source description
Source URL: https://bistrotdepays.opendatasoft.com/api/v2/catalog/exports/ttl

## Design document description
The design document used is Design2 as it was used in [Experiment1](#experiment1)

## Deployment description
ShapeLDP is used to generate the static LDP dataset from using the design document with respect to the data sources. Then POSTerLDP consumes the static LDP dataset, generates LDP POST requests for LDP resources from the static LDP dataset and sends them on 2 LDP servers that are instances of Apache Marmotta and Gold respectively.

## Resulting LDPs
- Resulting LDP on LDP Server (Apache Marmotta)
	- URL: http://opensensingcity.emse.fr/ldpapp/marmotta-bistro/catalog
	- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpapp/marmotta-bistro/catalog
- Resulting LDP on LDP Server (Gold)
	- URL:http://opensensingcity.emse.fr/ldpapp/gold-bistro/catalog/
	- Browse via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpapp/gold-bistro/catalog/