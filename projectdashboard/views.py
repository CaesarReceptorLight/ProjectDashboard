#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: Sheeba Samuel, Friedrich-Schiller University, Jena
Email: caesar@uni-jena.de
Date created: 26.01.2018
'''

from django.http import HttpResponse, Http404

from omeroweb.webclient.decorators import login_required
from django.shortcuts import render

import omero
import utilities
import semanticQuery
import query

import logging

import json
from datetime import datetime
import re


class HttpJsonResponse(HttpResponse):
    def __init__(self, content, cls=json.JSONEncoder.default):
        HttpResponse.__init__(
            self, json.dumps(content, cls=cls),
            content_type="application/json"
        )


class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


def get_experiment_from_dataset(conn, datasetId):
    """ Get experiment id from the dataset with ReceptorLight Service
        @param rlService ReceptorLight Service
        @param datasetId Dataset Id to which the experiment belongs
        @type datasetId Integer
    """
    rlService = utilities.get_receptor_light_service(conn)
    exp = rlService.getExperimentByDatasetId(datasetId)
    exp_details = {}
    if exp:
        if int(exp.getStatus().getValue()) == 1:
            exp_details['id'] = int(exp.getUId().getValue())
            exp_details['name'] = str(exp.getName().getValue())
    return exp_details


@login_required(setGroupContext=True)
def getProjectDashboard(request, conn=None, **kwargs):
    projectId = request.POST.get("projectId", 0)
    project = conn.getObject("Project", projectId)
    datasetIds = []
    if project is None:
        raise Http404
    for datasetObj in project.listChildren():
        datasetIds.append(int(datasetObj.getId()))

    return render(request, 'projectdashboard/preview.html', {'projectId': projectId, 'datasetIds': datasetIds})


@login_required(setGroupContext=True)
def getServerResponse(request, conn=None, **kwargs):
    project_id = kwargs['project_id']
    query_type = kwargs['input_type']
    project = conn.getObject("Project", project_id)
    datasetIds = []
    if project is None:
        raise Http404
    for datasetObj in project.listChildren():
        datasetIds.append(int(datasetObj.getId()))

    sparql_query = query.get_sparql_query(datasetIds, query_type)
    if sparql_query:
        sparql_response = semanticQuery.get_sparql_query_results(sparql_query)
    else:
        sparql_response = None

    return HttpJsonResponse(
        {
            'response': sparql_response
        },
        cls=DatetimeEncoder
    )


@login_required(setGroupContext=True)
def getPropertyResponse(request, conn=None, **kwargs):
    query_type = kwargs['input']
    # project_id = kwargs['project_id']
    # query_type = kwargs['input_type']
    # project = conn.getObject("Project", project_id)
    # datasetIds = []
    # if project is None:
    #     raise Http404
    # for datasetObj in project.listChildren():
    #     datasetIds.append(int(datasetObj.getId()))

    sparql_query = query.get_prop_object(query_type)

    if sparql_query:
        sparql_response = semanticQuery.get_sparql_query_results(sparql_query)
    else:
        sparql_response = None

    if not sparql_response:
        return
    bindings = sparql_response['results']['bindings']

    property_json = {}
    for uid, val in enumerate(bindings):
        prop = val['prop']['value']

        property_json[prop] = val['object']['value']


    return HttpJsonResponse(
        {
            'response': property_json
        },
        cls=DatetimeEncoder
    )