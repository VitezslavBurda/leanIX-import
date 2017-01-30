#!/usr/bin/env python

import sys
import json
import csv

sys.path = ['../src'] + sys.path

from leanix import *

if __name__ == "__main__":
    client = swagger.ApiClient(
        apiToken='7Sg8BZ98UXaKPYAMcH8KEhPVJLkq4esfYvTYE2D5', 
        tokenProviderHost='svc.leanix.net', 
        basePath='https://app.leanix.net/innogyCZpoc/api/v1'
    )
    
# export consumers
#consumersApi = ConsumersApi.ConsumersApi(client)
#response = consumersApi.getConsumers()
#for row in response:
#        print row.ID, "\t", row.name

# export IT services
resourcesApi = ResourcesApi.ResourcesApi(client)
response = resourcesApi.getResources()

with open('leanix-resources.csv', 'wb') as f:
    writer = csv.writer(f)
    for row in response:
        print row.ID, "\t", row.name
        writer.writerow([row.ID, row.reference, row.name])