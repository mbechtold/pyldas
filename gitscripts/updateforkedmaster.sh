#!/bin/bash

### git remote, only when not added yet (first time)
# git remote add upstream https://github.com/alexgruber/pyldas
#git remote -v
# (1) update forked master
git checkout master
git fetch upstream
git merge upstream/master
# commit (-->local)
git commit -am "forked pyldas updated"
git push
# (2) update branch from forked master
git checkout MB
git merge master
git push


