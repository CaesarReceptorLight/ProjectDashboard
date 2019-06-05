#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: Sheeba Samuel, Friedrich-Schiller University, Jena
Email: caesar@uni-jena.de
Date created: 26.01.2018
'''

import logging
from SPARQLWrapper import SPARQLWrapper, JSON

caesar_sparql_endpoint = SPARQLWrapper("http://localhost:8125/rdf4j-server/repositories/FederationStore_RL_OMERO")


def get_sparql_query_prefix():
    prefix = "PREFIX : <https://w3id.org/reproduceme#> " + \
             "PREFIX p-plan: <http://purl.org/net/p-plan#> " + \
             "PREFIX prov: <http://www.w3.org/ns/prov#>" +\
             "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"
    return prefix

def get_sparql_query_results(sparql_query):
    prefix = get_sparql_query_prefix()
    query = prefix + sparql_query

    caesar_sparql_endpoint.setQuery(query)

    caesar_sparql_endpoint.setReturnFormat(JSON)
    results = caesar_sparql_endpoint.query().convert()
    return results
