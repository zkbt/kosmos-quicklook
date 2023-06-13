# how to use `pre-commit`

[`pre-commit`](https://pre-commit.com) is a neat little tool for making sure some tools get run every time someone tries to commit to the repository. `pre-commit` is included as a `[develop]` dependency, so if you instaled this package via something like `pip install -e '.[develop]'`, you should already have it.

I copied in a `.pre-commit-config.yaml` file to define what should be run before committing. It was made following instructions at https://pre-commit.com, including running `pre-commit sample-config` to get a sample start to the config file. I made some modifications based on the example at [exoplanet](https://github.com/exoplanet-dev/exoplanet/blob/main/.pre-commit-config.yaml) to add `black`, apparently both for the code and for the documentation notebooks.

I ran `pre-commit autoupdate` to assign the current latest versions of the tools. These won't naturally update, so if there are changes to them, we should rerun `pre-commit autoupdate` at some point to update the version numbers.

I ran `pre-commit install` to connect it to the repository.

I ran `pre-commit run --all-files` to run it on everything that had already been committed. We should redo this if we change the pre-commit rules at any point.

From now on, it will run these tools every time we try to make a commit to the repository!
