If elasticsearch times out and cannot connect to ports 9200 and 9300, modify
the file ``/etc/elasticsearch/elasticsearch.yml`` to uncomment that line and
set to local host:

network.host: 127.0.0.1

