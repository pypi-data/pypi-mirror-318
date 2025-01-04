# jj-clean

I have just started using jj and want to start using it on top of
my currentn git repos, inclusing some that I collaborate on others with.
One of the things I notices is that when I run `tig --all`, jj completely
blows up my repo. This is because jj puts a git refs on absolutely
everything so that git won't garbage collect it. Which includes working copy
commits that I am never going to go back and look at, but jj needs to
keep them around so that the undo system can work (at least I think that's why).

So, this script is my hack to clean out all of these refs from the `.git/refs` directory
so that they don't show up in a normal git tree viewer. There may be a more native
way to do this, but like I said, I just started using jj...

This script should probably not be used by anyone other than me right now, it
does not allow for _any_ configuration.
