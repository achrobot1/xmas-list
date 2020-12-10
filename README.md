# 🎁 Christmas List Tracking app 🎁 
> December 2020

See my writeup [here](https://achrobot1.github.io/projects/xmas-list.html).


## Summary
This project was made to keep track of the Christmas lists of my family members. I used Python Django to create a small app where users can create a Christmas list which is visible to all other users. Users can view the lists of all other users, and claim gifts that they want to give. This way family members can avoid getting duplicate gifts for someone.

Once a user claims a gift, all other users, with the exception of the gift requestor, will be able to see that the gift was claimed by someone. The gift requestor has no visibility into which gifts have been claimed for them, so that no surprises are ruined 😊


## Usage
For my family's privacy, I will not share the link to the live deployed app, but instead provide instruction for hosting this project locally.

I used `pipenv` as my python environment to save me the headache of mismatched dependencies. This is the only real dependency, as `pipenv` takes care of packages used within the environment. `pipenv` can be installed:
```
pip install pipenv
``` 

or (depending on which version of pip one is using, and what it is aliased to)
```
pip3 install pipenv
``` 

An environment shell started with:
```
pipenv shell
```

Once the environment has been set up (all dependencies installed), a local server can be instantiated with:
```
cd xmas_list
python manage.py runserver
```


