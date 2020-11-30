**Local Grafana dashboard to monitor prices of items in Guild Wars 2 Trading Post**

I wanted to practice a bit with Grafana and decided to do so by applying it to Guild Wars 2, a MMO that has a special place in my heart.

Guild Wars 2 provide [APIs](https://wiki.guildwars2.com/wiki/API:Main) to retrieve different information about the game and its elements.

In particular, it is possible to retrieve buy and sell prices of any item in the Trading Post, the internal market entirely controlled by the players.

There are already different tools that monitor the TP, like [GW2Spidy](https://www.gw2spidy.com/), but I wanted to create a home version of them while practicing with Python, Grafana and MySQL.

Moreover, through Grafana notification settings, I was able to put in place an alerting and notification system, that sends a notification on a personal Discord server any time an alert is triggered.

**Architecture**

This is the current architecture of the project:

![Schema](/pictures/schema.png)


The "grafana" folder contains the json describing two monitoring panels and the alerts put in place in the "Glob of Ectoplasm" one.

The "ectoplasm" panel contains alerts to signal when it could be profitable to sell the item.

It is needed to manually set up the desired threshold and alerts for any panel (any item) on Grafana.


**Discord Notification**

To setup notifications on a Discord server, we need to create a new notification from Grafana, and use the webhook of the Discord server:

![Notif](/pictures/notif.png)

![Webhook](/pictures/webhook.png)

To visualize on discord a picture of the graph when the alert is triggered, it is needed to install [Grafana Image Renderer Plugin](https://grafana.com/grafana/plugins/grafana-image-renderer)

In this way the notification on Discord will be like this one:

![DiscordNotification](/pictures/discordnotif.png)
