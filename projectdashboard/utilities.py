# Author: Sheeba Samuel, <sheeba.samuel@uni-jena.de> https://github.com/Sheeba-Samuel

import omero
from omero.gateway import BlitzGateway
import logging

thisHost = 'localhost'
thisPort = 4064


def get_receptor_light_service(conn):
    sessionId = conn.getEventContext().sessionUuid
    c = omero.client(thisHost, thisPort)
    sf = c.joinSession(sessionId)
    return sf.getReceptorLightService()

def get_receptor_light_search_service(conn):
    sessionId = conn.getEventContext().sessionUuid
    c = omero.client(thisHost, thisPort)
    sf = c.joinSession(sessionId)
    return sf.getReceptorLightSearchService()

def get_receptor_light_file_service(conn):
    sessionId = conn.getEventContext().sessionUuid
    c = omero.client(thisHost, thisPort)
    sf = c.joinSession(sessionId)
    return sf.getReceptorLightFileManager()

def getUuid(conn):
    sessionId = conn.getEventContext().sessionUuid
    return sessionId

def get_admin_service(conn):
    sessionId = conn.getEventContext().sessionUuid
    c = omero.client(thisHost, thisPort)
    sf = c.joinSession(sessionId)
    return sf.getAdminService()

def get_experimenter_name(conn, owner_id):
    ad = get_admin_service(conn)
    experimenter = ad.getExperimenter(owner_id)
    experimenter_name = experimenter.getFirstName().getValue() + experimenter.getMiddleName().getValue() + experimenter.getLastName().getValue()
    return experimenter_name

def get_experimenters_list(conn):
    conn.SERVICE_OPTS.setOmeroGroup('-1')
    experimenterList = list(conn.getObjects("Experimenter"))
    return experimenterList
