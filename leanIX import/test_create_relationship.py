#!/usr/bin/env python

import sys

sys.path = ['../src'] + sys.path

from leanix import *

if __name__ == "__main__":
    client = swagger.ApiClient(
        apiToken='7Sg8BZ98UXaKPYAMcH8KEhPVJLkq4esfYvTYE2D5', 
        tokenProviderHost='svc.leanix.net', 
        basePath='https://app.leanix.net/innogyCZpoc/api/v1'
    )
    
resourcesApi = ResourcesApi.ResourcesApi(client)
response = resourcesApi.createFactSheetHasRequiredby('1900117532', body={'ID': '', 'factSheetID': '1900117368', 'factSheetRefID': '1900117532', 'dependencyTypeID': '3'})
print response