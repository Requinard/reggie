#!/bin/bash

docker build -t requinard2/reggie-server reggie-server
docker push requinard2/reggie-server

docker build -t requinard2/reggie-nginx reggie-nginx
docker push requinard2/reggie-nginx

docker build -t requinard2/reggie-prometheus reggie-prometheus
docker push requinard2/reggie-prometheus
