#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import json
import requests
from core import conf as Config
from core import report as rep
from core import report as Report

def Parse(url, type, auth=None, data=None):
    api_url = Config.api_url
    api_version = Config.api_version
    report = Report.Report()
    reqHeaders = {}

    '''
    Lag: self.generateSignature()
    if hasattr(Config, 'clientId') and hasattr(Config, 'userKey'):
        reqHeaders = {
            'Content-Type': 'application/json',
            'miraiex-user-clientid': Config.clientId,
            'miraiex-user-access-key': self.generateSignature(Config.userKey)
        }
    '''
    if hasattr(Config, 'accessKey'):
        reqHeaders = {
            'Content-Type': 'application/json',
            'miraiex-access-key': Config.accessKey
        }

    if auth and not reqHeaders:
        report.error(content="Missing API keys")

    if url:
        if url != '/time':
            url = api_url + api_version + url
        else:
            url = api_url + url

        if type == "delete":
            response = requests.delete(url, headers=reqHeaders)
            if response.text:
                report.notice(content="Post response: " + response.text)
                    
        if type == "post":
            response = requests.post(url, json=data, headers=reqHeaders)
            if response.text:
                report.notice(content="Post response: " + response.text)

        if type == "get":
            if not auth:
                response = requests.get(url)
            else:
                response = requests.get(url, headers=reqHeaders)

            if response.status_code == 200:
                return json.loads(response.content.decode('utf-8'))
            elif response.status_code == 404:
                error = "404 - File not found"
            elif response.status_code == 401:
                error = "401 - Authentication failed"
            elif response.status_code == 400:
                error = "400 - Bad request"                              
            else:
                message = json.loads(response.content.decode('utf-8'))
                error = message[0]

    else:
        report.error(content="No url specified")
