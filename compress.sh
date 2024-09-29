#!/bin/bash
ls | grep .pdf | awk '{ print "\"","ps2pdf -dPDFSETTINGS=/ebook",$1,substr($1, 1, length($1)-4)"-tmp.pdf","\"" }' | xargs -L1 sh -c
ls | grep tmp.pdf | awk '{ print "\"","ps2pdf -dPDFSETTINGS=/screen",$1,substr($1, 1, length($1)-8)"-compressed.pdf","\"" }' | xargs -L1 sh -c
ls | grep tmp | awk ' { print "\"","rm -f ",$1,"\"" } ' | xargs -L1 sh -c