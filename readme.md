**Local Grafana dashboard to monitor prices of items in Guild Wars 2 Trading Post**

The "grafana" folder contains the json describing two monitoring panels and the alerts put in place in the "Glob of Ectoplasm" one.

The "ectoplasm" panel contains alerts to signal when it could be profitable to sell the item.

A firing alert will be notified over discord, through the use of a webhook.

The "python" folder contains the python code used to scrape the info from GW2 API and write it down in a local MySQL DataBase.

![Dashboard](/dashboard.jpg)
