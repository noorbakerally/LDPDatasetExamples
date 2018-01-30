# Experiment4
The [Grenoble Open Data Portal](http://http://data.metropolegrenoble.fr/) provides a [dataset](http://data.metropolegrenoble.fr/ckan/dataset/parkings-relais-p-r) about [incentive parking lots](https://en.wikipedia.org/wiki/Park_and_ride). The datset itself is divided into two sub-dataset: static and dynamic. The static part provides fixed information about the incentive parkings lots such as address, types, geographical details etc. It is provided into two distributions that are in CSV and GeoJSOn, both of which contain similar information. The dynamic part provides real-time information about the number of parking spaces available in the parking lots defined in the static part. It is available in JSON. For the static part, we use its CSV distribution and for the dynamic part, we use it JSON distribution. 

In the [design document](https://github.com/noorbakerally/LDPDatasetExamples/blob/master/DesignDocuments/dGrenobleParking.ttl), for both the static and dynamic part, RDF liftings rules are provided. 

Using ShapeLDP, the dynamic LDP dataset is generated from the design document with respect to the data sources. The dynamic LDP dataset is then exposed via InterLDP operating in dynamic mode. 
Resulting LDP: 
- LDP URL: http://opensensingcity.emse.fr/ldpdfend/grenoble/parkings
- Browser LDP via LDP Browser at: http://opensensingcity.emse.fr/ldp-browser?http://opensensingcity.emse.fr/ldpdfend/grenoble/parkings