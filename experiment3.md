# Experiment3
The following two datasets are considered:
1.  https://opendata.paris.fr/explore/dataset/velib-emplacement-des-stations (GeoJSON)
2.   https://opendata.paris.fr/explore/dataset/liste-des-stations-de-services-de-vehicules (CSV)

Both datasets are obtained from [Paris Open Data Portal](https://opendata.paris.fr/page/home/).  The first dataset describes bicycle station in Paris and the second dataset describe service stations for shared vehicles in Paris.

In the [design document](https://github.com/noorbakerally/ParisDataPlatform/blob/master/designDocument.ttl), the data sources are provided together with their lifting rules.  With respect to these data sources, the LDP dataset is generated and exposed via an LDP:
- LDP URL: http://opensensingcity.emse.fr/ldpdfend/city/paris
- Browse LDP via LDP Browser http://opensensingcity.emse.fr/ldp-browser?iri=http://opensensingcity.emse.fr/ldpdfend/city/paris