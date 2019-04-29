#!/bin/bash

git checkout master
git checkout --patch MB <filename>
git commit -a
git push

