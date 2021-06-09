summary: In this tutorial, we will learn how to setup our own tutorial repositories using codelab and git actions.
id: how-to-create-your-own-codelab
categories: Tutorial
tags: 
status: Published
authors: Sparsh A.
Feedback Link: https://form.jotform.com/211377288388469

# How to create your own codelab (automated)

<!-- ------------------------ -->
## Prepare your Tutorial
Duration: 5

### Setup Jupyter

We chose jupyter notebooks as an ideal choice for preparing tutorials because it integrates markdown with code, images and million other things. If you do not have a jupyter environment setup locally, you can choose [Colab](https://colab.research.google.com/) or [Binder](https://mybinder.org/v2/gh/jupyterlab/jupyterlab-demo/master?urlpath=lab/tree/demo) to prepare your notebook on cloud for free.

### Create Tutorial
Write down your desired tutorial in colab as per [these](https://github.com/googlecodelabs/tools/blob/master/FORMAT-GUIDE.md) markdown instructions.

<!-- ------------------------ -->
## Setup Git Repository
Duration: 10

This step is a one-time setup process. We will use GitHub to maintain and host our codelab site for free.

### Fork
Fork [this](https://github.com/sparsh-ai/codelabs) repo.

### Rename (optional)
Rename this forked repo if you want. You can choose any name you like.

### Update 
Update the ```config.txt``` file, which is present in the root folder of this forked repo. Replace the two variables:
1. Put your ```<git username>```.github.io in the TGTBASE variable.
2. Put your ```repo name``` in the TGTSITE variable.

e.g. for a git user ```sparsh-ai``` and repo name ```codelab```, the updated file would look like this:
```bash
export TGTBASE="sparsh-ai.github.io"
export TGTSITE="codelabs"
```

### Customize (optional)
You can customize both landing page and codelabs.

<aside class="positive">
Codelab customization is mainly done via tags that we provide during the creation of jupyter notebook based tutorials.
</aside>

We can customize the following items in landing page by simple modifications.
1. Change Header and Logo
2. Add Category
3. Add View
4. Change Footer

<!-- ------------------------ -->
## Add new Codelabs
Duration: 5

To add a new codelab to the codelab site, pull the repo, add our notebook and push it back to the master.

### Pull the repo
Pull the repo using ```git pull origin master``` where origin is pointed to your repo where codelabs site is hosted. If repo is already there, you can opt for ```git pull --rebase origin master``` instead.

### Add tutorial notebook
Add your tutorial notebook in the ```_notebook``` folder. Make sure the notebook format is following the codelab markdown guidelines and the extension is ```.ipynb```.

### Push the repo
Push the updated repo changes to master branch using the standard set of add -> commit -> push chain. e.g. you can use ```git add . && git commit -m 'new build' && git push origin master``` to push the changes.

<!-- ------------------------ -->
## Conclusion
Duration: 1

Git actions workflow named ```CI``` would automatically start deploying latest changes of the master branch. You can check the status in ```Actions``` tab of your git repo.

To access the codelabs site, go to your github pages URL. The typical URL format is ```https://<user_name>.github.io/<repo_name>```.

Verify the functionality and modify/enhance the process as per requirements.

#### Have a Question?
- https://form.jotform.com/211377288388469

#### Github Issues
- https://github.com/recohut/reco-step/issues
