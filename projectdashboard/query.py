#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: Sheeba Samuel, Friedrich-Schiller University, Jena
Email: caesar@uni-jena.de
Date created: 26.01.2018
'''

import logging


def get_dataset_id_filter(datasetIds):
    query = ""
    for datasetid in datasetIds:
        if datasetid:
            query = query + "?dataset=" + ':dataset_' + str(datasetid) + " ||"
    return query[:-2]


def get_sparql_query(datasetIds, query_type):
    dataset_filter_query = get_dataset_id_filter(datasetIds)
    if query_type == 'plot':
        query = "Select ?Experiment ?Name ?AgentName ?AgentRole ?generatedTime WHERE { \
                ?Experiment  a :Experiment ; :name ?Name . \
                ?Experiment :status ?status FILTER(?status=1) . \
                ?Experiment :hasDataset ?dataset FILTER(" + dataset_filter_query + ") . \
  				?Experiment  prov:wasAttributedTo ?Agent .   \
                ?Agent :name ?AgentName ; rdfs:label ?AgentRole . \
                OPTIONAL { ?Experiment prov:generatedAtTime ?generatedTime } \
                }"
    elif query_type == 'agents':
        query = "SELECT DISTINCT ?Experiment ?Agent ?AgentName ?Role ?RoleIn WHERE {  \
                ?Experiment  a :Experiment ; :name ?Name . \
                ?Experiment :status ?status FILTER(?status=1) . \
                ?Experiment :hasDataset ?dataset FILTER(" + dataset_filter_query + ") . \
                { ?Experiment prov:wasAttributedTo ?Agent . \
                  ?Agent :name ?AgentName FILTER(?AgentName!='') \
                  ?Agent rdfs:label ?Role . \
                } UNION { \
                ?Experiment p-plan:correspondsToVariable ?Material . \
                ?Material :name ?RoleIn . \
                ?Material prov:wasAttributedTo ?Agent . \
                ?Agent :name ?AgentName FILTER(?AgentName!='') \
                ?Agent rdfs:label ?Role . \
                }  . }"
    elif query_type in ['Vector', 'Plasmid', 'Protein', 'Chemical', 'DNA', 'RNA', 'Solution', 'RestrictionEnzyme', 'FluorescentProtein', 'Oligonucleotide']:
        query = get_usedin_materials(query_type, dataset_filter_query)
    elif query_type == 'externalresources':
        query = "Select DISTINCT ?publication ?subplan ?Experiment WHERE { \
                ?publication a :Publication . \
                ?publication p-plan:isVariableOfPlan ?subplan . \
                ?subplan p-plan:isSubPlanOfPlan ?exp . \
                ?exp  a :Experiment . \
                ?exp :name ?Experiment . \
                ?exp :status ?status FILTER(?status=1) .  \
                ?exp :hasDataset ?dataset FILTER(" + dataset_filter_query + ") . \
                }"
    elif query_type == 'filesusedinstep':
        query = get_usedin_materials('File', dataset_filter_query)
    elif query_type == 'scriptusedinexperiment':
        query = "Select DISTINCT ?NotebookName ?generatedAtTime ?modifiedAtTime ?NotebookStep ?StepType ?OutputType ?OutputName ?OutputValue WHERE { \
                ?notebook a :Notebook . \
                ?notebook :name ?NotebookName . \
                ?notebook prov:generatedAtTime ?generatedAtTime . \
                ?notebook :modifiedAtTime ?modifiedAtTime . \
                ?NotebookStep p-plan:isStepOfPlan ?notebook . \
                ?NotebookStep p-plan:hasOutputVar ?output . \
                ?NotebookStep :type ?StepType . \
                ?output prov:value ?OutputValue . \
                ?output :type ?OutputType . \
                ?output :name ?OutputName \
                }"
    elif query_type == 'steps':
        query = "SELECT DISTINCT ?Experiment ?step ?description WHERE { \
                ?exp a :Experiment . \
                ?exp :name ?Experiment . \
                ?exp :status ?status FILTER(?status=1) .  \
                ?exp :hasDataset ?dataset FILTER(" + dataset_filter_query + ") . \
                ?subplan p-plan:isSubPlanOfPlan ?exp . \
                { ?step p-plan:isStepOfPlan ?subplan } UNION {?step p-plan:isStepOfPlan ?subplan } \
                ?step :description ?description \
                }"
    elif query_type == 'devices':
        query = "SELECT DISTINCT ?InstrumentType ?DeviceType ?Manufacturer ?Model ?SerialNumber ?LotNumber  WHERE { \
                ?image a :Image . \
                ?dataset a :Dataset . \
                ?dataset :id ?datasetid FILTER(" + dataset_filter_query + ") . \
                ?image :belongsToDataset ?dataset . \
                ?image :ref-instrument ?instrument . \
                ?InstrumentType :ref-instrument ?instrument . \
                ?InstrumentType :id ?id . \
                ?InstrumentType rdf:type ?DeviceType . \
                OPTIONAL { ?InstrumentType :manufacturer ?Manufacturer  }  \
                OPTIONAL { ?InstrumentType :model ?Model  }  \
                OPTIONAL { ?InstrumentType :serialnumber ?SerialNumber  } \
                OPTIONAL { ?InstrumentType :lotnumber ?LotNumber  } \
                }"
    elif query_type == 'Detector':
        query = get_used_devices(query_type, dataset_filter_query)
    elif query_type == 'Objective':
        query = get_used_devices(query_type, dataset_filter_query)
    elif query_type == 'LightSource':
        query = get_used_devices(query_type, dataset_filter_query)
    elif query_type == 'Dichroic':
        query = get_used_devices(query_type, dataset_filter_query)
    elif query_type == 'Filter':
        query = get_used_devices(query_type, dataset_filter_query)
    elif query_type == 'Laser':
        query = get_used_devices(query_type, dataset_filter_query)
    elif query_type == "Filament":
        query = get_used_devices(query_type, dataset_filter_query)
    elif query_type == "generalsettings":
        query = "Select ?Experiment ?MicroscopeConfiguration ?AdditionalInformation WHERE { \
                ?exp a :Experiment . \
                ?exp :name ?Experiment . \
                ?exp :status ?status FILTER(?status=1). \
                ?exp :datasetid ?datasetid FILTER(" + dataset_filter_query + ") . \
                OPTIONAL { ?exp :microscopeconfig ?MicroscopeConfiguration } . \
                OPTIONAL { ?exp :additionalinformation ?AdditionalInformation } \
                }"
    elif query_type == 'ObjectiveSettings':
        query = get_used_devices_settings(query_type, dataset_filter_query)
    elif query_type == 'DetectorSetting':
        query = get_used_devices_settings(query_type, dataset_filter_query)
    elif query_type == 'LightSettings':
        query = get_used_devices_settings(query_type, dataset_filter_query)
    elif query_type == 'FilterSetting':
        query = get_used_devices_settings(query_type, dataset_filter_query)
    elif query_type == 'outputgraphs':
        query = "SELECT * WHERE { { \
                { SELECT ?MicroscopeConfiguration WHERE {?exp  a :Experiment . ?exp :microscopeconfig ?MicroscopeConfiguration }} UNION \
                {SELECT ?Preparation WHERE {?exp  a :Experiment . ?vec :preparation ?Preparation }} \
                }}"
    elif query_type == 'versionhistory':
        query = "Select DISTINCT ?firstVersionId ?currentVersionId WHERE { \
                ?exp  a :Experiment .  \
                OPTIONAL { ?exp prov:wasDerivedFrom ?original } . \
                OPTIONAL { ?original prov:wasDerivedFrom ?another } . \
                OPTIONAL { ?another a prov:PrimarySource } . \
                OPTIONAL { ?another :uid ?firstVersionId } \
                }"
    elif query_type == 'image':
        query = "SELECT DISTINCT ?Image WHERE { \
                ?image a :Image . \
                ?dataset a :Dataset . \
                ?dataset :id ?datasetid FILTER(" + dataset_filter_query + ") . \
                ?image :belongsToDataset ?dataset . \
                ?image :name ?Image . \
                }"

    else:
        query = None

    return query


def get_usedin_materials(query_type, dataset_filter_query):
    query = "Select DISTINCT ?material ?Name ?usedin ?usedinstep WHERE { \
                ?material a :" + query_type + " . \
                ?material :name ?Name . \
                { \
                    ?usedin p-plan:correspondsToVariable ?material . \
                    ?usedinstep p-plan:hasInputVar ?material \
            	} \
                UNION { \
                    ?usedin :reference ?material . \
                } \
                }"

    return query


def get_used_devices(query_type, dataset_filter_query):
    query = "SELECT DISTINCT ?instrument_part ?dataset ?image WHERE { \
            ?image a :Image .  \
            ?dataset a :Dataset FILTER(" + dataset_filter_query + ") . \
            ?dataset prov:hadMember ?image . \
            ?instrument p-plan:correspondsToVariable ?image .\
            ?instrument_part :isPartOf ?instrument . \
            ?instrument_part a :" + query_type  + ". \
            }"
    return query


def get_used_devices_settings(query_type, dataset_filter_query):
    query = "SELECT DISTINCT ?instrument_part_setting ?dataset ?image WHERE { \
            ?image a :Image .  \
            ?dataset a :Dataset FILTER(" + dataset_filter_query + ") . \
            ?dataset prov:hadMember ?image . \
            ?instrument p-plan:correspondsToVariable ?image .\
            ?instrument_part :isPartOf ?instrument . \
            ?instrument_part :hasSetting ?instrument_part_setting . \
            ?instrument_part_setting a :" + query_type + ". \
            }"
    return query

def get_prop_object(subject):
    query = "SELECT DISTINCT ?prop ?object WHERE { "\
            ":" + subject + " ?prop ?object . }"
    return query
