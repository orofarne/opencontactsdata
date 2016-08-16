#!/bin/bash -ex

rm -f items.jl

SPIDERS=`scrapy list`

for spider in $SPIDERS
do
	scrapy crawl "$spider"
done
