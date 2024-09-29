#!/bin/bash
ls | grep compressed | awk ' { print "\"","rm -f ",$1,"\"" } ' | xargs -L1 sh -c