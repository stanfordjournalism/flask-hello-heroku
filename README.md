
# Creating and deploying a simple Python Flask web app on Heroku (Spring 2018)

These instructions are a combined, abridged versions of these tutorials:

- [Introduction to Simple Web Applications with Flask](http://www.compjour.org/lessons/flask-single-page/)
- [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python#introduction).

This tutorial assumes you have **Python 3.6** and **Flask** installed, though the instructions can be modified to fit whatever is on your system.

The deployed app on Heroku *might* be live at this URL:

https://evening-garden-86557.herokuapp.com/


(An older version of this tutorial can be found at: https://github.com/datademofun/heroku-basic-flask)


<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  

- [Clone the sample app](#clone-the-app)
- [Create a Heroku account and download Heroku CLI](#create-a-heroku-account-and-download-heroku-cli)
  - [Authenticate with Heroku from the command-line](#authenticate-with-heroku-from-the-command-line)
  - [Initialize a Heroku app from the command-line](#initialize-a-heroku-app-from-the-command-line)
- [Deploy the app](#deploy-the-app)
  - [Spin up a "dyno"](#spin-up-a-dyno)
- [Updating the app](#updating-the-app)
- [Iteration ideas](#iteration-ideas)
  - [HTML](#html)
  - [CSS](#css)
  - [Python/Jinja](#pythonjinja)
  - [Flask](#flask)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Clone the app

This tutorial and its code is hosted on Github:

https://github.com/stanfordjournalism/flask-hello-heroku

Which means we can clone the source code from the command-line like this:

```sh
$ cd /tmp # or whatever directory you want to play in
$ git clone https://github.com/stanfordjournalism/flask-hello-heroku
```

### Test the Flask app on localhost

It's a basic Python Flask app, which means we can run it locally like this:

```sh
$ cd flask-hello-heroku
$ python app.py
```


Visiting [http://127.0.0.1/:5000](http://127.0.0.1/:5000) or [http://localhost:5000/](http://localhost:5000/) should show a page like this:

![sample homepage](https://i.imgur.com/SVAsKI0.png)



## Create a Heroku account and download Heroku CLI

Sign up here for a free account: https://signup.heroku.com/dc

The [Heroku Command-Line Interface](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) (Heroku CLI) is a program for running Heroku commands from your system's shell, e.g. MacOS Terminal and Windows Powershell. You can download the installers here:

- OSX: https://cli-assets.heroku.com/heroku-cli/channels/stable/heroku-cli.pkg
- Win64: https://cli-assets.heroku.com/heroku-cli/channels/stable/heroku-cli-x64.exe

### Authenticate with Heroku from the command-line

If you created a Heroku account and logged in, you've already authenticated (i.e. signed in) to Heroku via your web browser. But we want to also access our Heroku account via the command-line.

Go to your system shell and run the following command -- then type in your account info (email and password):

```sh
$ heroku login
```

You'll see this prompt:

```
Enter your Heroku credentials.
Email: you@email.com
Password (typing will be hidden):
Authentication successful.
```

If the login was successful, you should be able to run the following `whoami` subcommand:

```sh
$ heroku auth:whoami
you@email.com
```






### Initialize a Heroku app from the command-line

OK, assuming your current working directory is still the same directory you cloned into, e.g. `/tmp/flask-hello-heroku` -- you can run the `pwd` shell command to figure it out -- the next step is to instantiate a "Heroku app" in the directory:


```sh
$ heroku create
```

You should see the following output:

```
https://evening-garden-86557.herokuapp.com/ | https://git.heroku.com/evening-garden-86557.git
```

The first URL is where your app "lives" -- in the above example, this is:

```
https://evening-garden-86557.herokuapp.com/
```


For an entirely new app, you'd see this boilerplate page:

![boilerplate page](https://i.imgur.com/zcZ1oG5.png)



The second URL from the `heroku create` command is the address for the **git repo** Heroku has created for your app:

```
https://git.heroku.com/evening-garden-86557.git
```

When Heroku "deploys" our app, it spins up some space and processing on its cloud server and downloads our source code onto that server. We can think of Heroku as running a `git clone` command onto their cloud server. The git URL they give us is that git repo they clone from.

By default, the `heroku create` command should have set your repo to have a "remote" repo named `heroku` which lives at the git URL.

Every time we make changes to our codebase (which [we do later in this lesson](#deploy-heroku-app)), we do a `git push` to `heroku master`:

```sh
$ git push heroku master
```


### Using Heroku's web console to see your apps

If you ever get lost at the command-line, you can visit your Heroku account page and apps listing at this URL:

https://dashboard.heroku.com/apps


You'll see your active Heroku apps listed:

![apps page](https://i.imgur.com/JjrHrsK.png)

And clicking on an app brings up this dashboard:

![img app dashboard](https://i.imgur.com/zZDd0kS.png)


--------------------------


<a name="deploy-heroku-app" id="deploy-heroku-app"></a>

## Deploying a Heroku app

When you cloned the repo from [my original source repo](https://github.com/stanfordjournalism/flask-hello-heroku), you also copied some Git-related configuration, including the address of the `origin` repo:

```
https://github.com/stanfordjournalism/flask-hello-heroku
```

(the config info is stored in a hidden file named `./git/config`)


Running `heroku create` in this repo directory makes a change to the config file:


```
[remote "heroku"]
  url = https://git.heroku.com/evening-garden-86557.git
  fetch = +refs/heads/*:refs/remotes/heroku/*
```

You shouldn't have to ever edit this (at least for this demo purposes). This is just to acquaint you with some of the conventions and configuration of Heroku (or any other deployment service).

The upshot is that cloning app code to our own computers means that that code is only on our computer. Running `heroku create` sets up space on Heroku for our app code. To actually get our app code running:



Push to Heroku's git repo for your code.

```sh
$ git push heroku master
```

You should see a bunch of server log code:

```
Delta compression using up to 8 threads.
Compressing objects: 100% (40/40), done.
Writing objects: 100% (49/49), 146.94 KiB | 16.33 MiB/s, done.
Total 49 (delta 16), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> Python app detected
remote:  !     No 'Pipfile.lock' found! We recommend you commit this into your repository.
remote: -----> Installing python-3.6.4
remote: -----> Installing pip
remote: -----> Installing dependencies with Pipenv 11.8.2…
remote:        Installing dependencies from Pipfile…
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote: 
remote: -----> Compressing...
```


### Spin up a "dyno"

"Dyno" is Heroku's term for cloud server/resource. The following command ensures that Heroku has allocated clouds to your little app:

```sh
$ heroku ps:scale web=1
```

You should see output that looks like this:

```
Scaling dynos... done, now running web at 1:Free
```



## Updating the app

Let's make a change to the app. In the file [templates/homepage.html](templates/homepage.html), the HTML for the page headline is this generic snippet:

```html
        <h1>My test homepage!</h1>
```

Change it to something else, like:

```html
        <h1>Dan's AWESOME homepage!</h1>
```

-- and save the file (templates/homepage.html)

If you run your app locally, i.e. `python app.py`, you'll see the changes. But the change you made was only to your local copy of the file. We have to get that updated code onto Heroku's server.

To do this, we have to use `git` to `add` and `commit` the changes before doing a `push` to Heroku's server:


```sh
$ git add templates/homepage.html
$ git commit -m 'changed homepage'
$ git push heroku master
```



## Iteration ideas

Try out these variations to test out your knowledge of web app dev:


### HTML

- Make the source code URL (in the footer) be an actual clickable hyperlink
- Change what the photo links to when clicked on
- Change the page's *meta* **title**
- Instead of showing the photo at `/static/images/stanfordlove.jpg`, use an image from [placeholder.com](https://placeholder.com), [placecage.com](http://placecage.com), [morganfillman.space](https://morganfillman.space) or [placekitten.com](http://placekitten.com). Or from these [other placeholder sites](https://www.johanbostrom.se/blog/the-best-image-placeholder-services-on-the-web).



### CSS

- Style the site using a CSS stylesheet from [Bootstrap](https://getbootstrap.com/docs/4.1/getting-started/download/)
- In `mystyles.css`:
  - Put a border around the photo -- I like using the [`outline`](https://developer.mozilla.org/en-US/docs/Web/CSS/outline) property
  - Put some space (e.g. `margin`) between the top of the page and the photo
  - Make the timestamp **bold** and in a different color, like `hotpink`
  - Change the default body font
  - Change the headline font to a [Google Web Font](https://fonts.google.com/)
  

### Python/Jinja

- Pretty-format the current time notification
- Randomize the image/placeholder site shown
- Show a random selection of randomly sized photos

### Flask

- Configure the app to **not** be in `debug` mode
- Create a new route and template that interprets a number argument as the number of randomized images to display. e.g. `https://yourapp.com/4` should show 4 images.

