#!/usr/bin/env bash
docker run --rm -v `pwd`:/build -w /build lsstsqre/lsst-texmf:latest sh -c 'make clean; make'
