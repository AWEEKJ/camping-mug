#!/usr/bin/env bash
cd deploy && docker-compose up -d --build
docker-compose ps
docker-compose logs