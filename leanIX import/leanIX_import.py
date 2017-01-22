#!/usr/bin/env python

import sys
import sqlite3

sys.path = ['../src'] + sys.path

from leanix import *

con = None

try:
    con = sqlite3.connect('leanix_import.db')
    con.row_factory = sqlite3.Row
    
    cur = con.cursor()

    cur.execute("select e1.leanix as sourceLeanix, e1.Name as sourceName, e2.leanix as targetLeaninx, e2.name as targetName from elements e1 join relations on e1.ID = relations.Source join elements e2 on e2.ID = relations.Target where e1.Type = 'BusinessService' and e1.leanix != '\N' and e2.leanix != '\N' order by e1.Name, e2.Name")

    rows = cur.fetchall()
    for row in rows:
        print "%s -> %s" % (row["sourceLeanix"], row["targetLeaninx"])

except sqlite3.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)
finally:
    if con:
        con.close()


sys.exit(0);

if __name__ == "__main__":
    client = swagger.ApiClient(
        apiToken='7Sg8BZ98UXaKPYAMcH8KEhPVJLkq4esfYvTYE2D5', 
        tokenProviderHost='svc.leanix.net', 
        basePath='https://app.leanix.net/innogyCZpoc/api/v1'
    )

    processesApi = ProcessesApi.ProcessesApi(client)
    processes = processesApi.getProcesses();

    for service in processes:
        print service.ID, " ", service.name
