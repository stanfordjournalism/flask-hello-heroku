# Quick Heroku start

These instructions are an abridged version of the tutorial found on Heroku's site: [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python#introduction).

This tutorial assumes you have **Python 3.6 installed**, though the instructions can be modified to fit whatever is on your system.

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


## Clone an app and deploy it to Heroku


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



