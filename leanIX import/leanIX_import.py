#!/usr/bin/env python

import sys
import sqlite3
import json

sys.path = ['../src'] + sys.path

from leanix import *

if __name__ == "__main__":
    con = None

    client = swagger.ApiClient(
        apiToken='7Sg8BZ98UXaKPYAMcH8KEhPVJLkq4esfYvTYE2D5', 
        tokenProviderHost='svc.leanix.net', 
        basePath='https://app.leanix.net/innogyCZpoc/api/v1'
    )

    # list of processes
    #processesApi = ProcessesApi.ProcessesApi(client)
    #processes = processesApi.getProcesses();
    #for service in processes:
    #    print service.ID, " ", service.name

    try:
        con = sqlite3.connect('leanix_import.db')
        con.row_factory = sqlite3.Row
    
        cur = con.cursor()

        # Service dependency
        ####################
        #cur.execute("select e1.leanix as sourceLeanix, e1.Name as sourceName, e2.leanix as targetLeanix, e2.name as targetName from elements e1 join relations on e1.ID = relations.Source join elements e2 on e2.ID = relations.Target where e1.Type = 'BusinessService' and e1.leanix != '\N' and e2.leanix != '\N' order by e1.Name, e2.Name")
        #rows = cur.fetchall()

        #resourcesApi = ResourcesApi.ResourcesApi(client)
        #for row in rows:
            #print "%s (%s) -> %s (%s)" % (row["sourceName"], row["sourceLeanix"], row["targetName"], row["targetLeanix"])
        #    data = {
        #        "ID": "",
        #        "factSheetID": row["sourceLeanix"],
        #        "factSheetRefID": row["targetLeanix"],
        #        "dependencyTypeID": 3
        #    }
        #    print json.dumps(data)

        #    response = resourcesApi.createFactSheetHasRequires(ID=row["sourceLeanix"], body=data)
        #    print response

        # Consumer services dependency
        ##############################
        cur.execute("select usergroup, service from consumers_services where usergroup not in ('1200051901', '1200051913')")
        rows = cur.fetchall()

        consumersApi = ConsumersApi.ConsumersApi(client)
        for row in rows:
            #print "%s (%s) -> %s (%s)" % (row["sourceName"], row["sourceLeanix"], row["targetName"], row["targetLeanix"])
            data = {
                "ID": "",
                "resourceID": row["service"],
                "consumerID": row["usergroup"],
                "comment": "",
                "technicalSuitabilityID": "3",
                "usageTypeID": "1",
                "numberOfUsers": 0
            }
            print json.dumps(data)

            response = consumersApi.createResourceHasConsumer(ID=row["usergroup"], body=data)
            print response


    except sqlite3.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)
    
    finally:
        if con:
            con.close()

    sys.exit(0);