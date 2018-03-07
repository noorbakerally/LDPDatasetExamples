# Important Links:
## LDP-DL Technical Report: http://w3id.org/ldpdl/technical_report.pdf
## LDP-DL RDF Syntax and Semantics: http://w3id.org/ldpdl/

This page describes experiments performed to validate the use of [LDP-DL](https://w3id.org/ldpdl/) to validate the requirements described in the [technical report](http://w3id.org/ldpdl/technical_report.pdf). There are 6 experiments. Firstly, we describe how the experiments validate the requirements then we describe the experiments themselves. In all the experiments, the main tools that are used are:
- ShapeLDP (Link to Github Repo: https://github.com/noorbakerally/ShapeLDP)
- InterLDP (Link to Github Repo: https://github.com/noorbakerally/InterLDP)
- POSTerLDP (Link to Github Repo: https://github.com/noorbakerally/POSTerLDP)

Also, our LDPs can be browsed using our LDP browser, HubbleLDP (Link to Github Repo: https://github.com/noorbakerally/HubbleLDP)

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
| [Experiment1](https://stackedit.io/viewer#!url=https://raw.githubusercontent.com/noorbakerally/LDPDatasetExamples/master/experiment1.md) | &#10004;   |    |    |  &#10004;   |  &#10004;  |
| [Experiment2](https://stackedit.io/viewer#!url=https://raw.githubusercontent.com/noorbakerally/LDPDatasetExamples/master/experiment2.md) | &#10004;   |    |    |    | &#10004;   |
| [Experiment3](https://stackedit.io/viewer#!url=https://raw.githubusercontent.com/noorbakerally/LDPDatasetExamples/master/experiment4.md) | &#10004;    | &#10004;   |    |    | &#10004;   |
| [Experiment4](https://stackedit.io/viewer#!url=https://raw.githubusercontent.com/noorbakerally/LDPDatasetExamples/master/experiment4.md) | &#10004;    |  &#10004;  | &#10004;   |    |&#10004;    |
| [Experiment5](https://stackedit.io/viewer#!url=https://raw.githubusercontent.com/noorbakerally/LDPDatasetExamples/master/experiment5.md) | &#10004;    |    |    |    | &#10004;   |

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
1. [Experiment 1](https://stackedit.io/viewer#!url=https://raw.githubusercontent.com/noorbakerally/LDPDatasetExamples/master/experiment1.md)
2. [Experiment 2](https://stackedit.io/viewer#!url=https://raw.githubusercontent.com/noorbakerally/LDPDatasetExamples/master/experiment2.md)
3. [Experiment 3](https://stackedit.io/viewer#!url=https://raw.githubusercontent.com/noorbakerally/LDPDatasetExamples/master/experiment3.md)
4. [Experiment 4](https://stackedit.io/viewer#!url=https://raw.githubusercontent.com/noorbakerally/LDPDatasetExamples/master/experiment4.md)
5. [Experiment 5](https://stackedit.io/viewer#!url=https://raw.githubusercontent.com/noorbakerally/LDPDatasetExamples/master/experiment5.md)










