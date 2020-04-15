#!/bin/bash

docker exec -ti `docker ps | grep covid-simulation | cut -d" " -f1` bash
