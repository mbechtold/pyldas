# Setup Notes

### clone pyldas from mbechtold, forked from alexgruber
git clone https://github.com/mbechtold/pyldas
git branch -a
### add MB branch
git checkout MB
git branch -a

# resolve conflicts
git config merge.tool vimdiff      
git mergetool
Now if your terminal has any GUI capability and you have compiled Vim correctly with GUI support, you can use your mouse to click on the bottom split to edit it. Or if you are a Vim ninja, you can use the keyboard shortcut to move to different splits.
Ctrl w + h   # move to the split on the left 
Ctrl w + j   # move to the split below
Ctrl w + k   # move to the split on top
Ctrl w + l   # move to the split on the right
You can either incorporate the changes by manually editing the MERGED split, or use Vim shortcuts pull from one of the LOCAL, BASE ad REMOTE versions.
:diffg RE  # get from REMOTE
:diffg BA  # get from BASE
:diffg LO  # get from LOCAL

