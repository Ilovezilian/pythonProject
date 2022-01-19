# LogStash
## Download Logstash
[Download Logstash](https://www.elastic.co/downloads/logstash)

## Start Service
``` cmd
cd ${logstash_home_path}

 bin/logstash -f logstash.conf

 bin/logstash -f config/first-pipeline.conf --config.reload.automatic

 bin/logstash -f config/first-pipeline.conf --config.test_and_exit
```

## Document
[Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html)
