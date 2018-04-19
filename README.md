
# Creating and deploying a simple Python Flask web app on Heroku (Spring 2018)

These instructions are a combined, abridged versions of these tutorials:

- [Introduction to Simple Web Applications with Flask]
- [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python#introduction).

This tutorial assumes you have **Python 3.6** and **Flask** installed, though the instructions can be modified to fit whatever is on your system.


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


Clone a copy of the app:

```sh
$ cd /tmp # or whatever directory you want to play in
$ git clone https://github.com/stanfordjournalism/flask-hello-heroku
```

Test it out for yourself:

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

If the login was successful, you should be able to run the following `whoami` subcommand:

```sh
$ heroku auth:whoami
you@email.com
```






### Initialize a Heroku app from the command-line


```sh
$ heroku create
```

You should see the following output:

```
https://evening-garden-86557.herokuapp.com/ | https://git.heroku.com/evening-garden-86557.git
```

This means that your Heroku account now has an application running at the given URL. In the above example, that URL is:

https://evening-garden-86557.herokuapp.com/

For your app URL, you won't see anything but this boilerplate page:

![boilerplate page](https://i.imgur.com/zcZ1oG5.png)


You'll see this app listed on your account page:

https://dashboard.heroku.com/apps

![apps page](https://i.imgur.com/JjrHrsK.png)


## Deploy the app


Push to Heroku's git repo for your code.

```sh
$ git push heroku master
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

- Create a new route and template that interprets a number argument as the number of randomized images to display. e.g. `https://yourapp.com/4` should show 4 images.

