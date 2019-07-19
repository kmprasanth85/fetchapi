# Mac Address Lookup API

The code written in python 

Both the python code and docker build file are pushed in to public git repository.

clone the git repository and build the docker image.
```
$ docker build -t macaddr -f macaddr .

```
You can run the docker simply and run the python code for MAC address lookup.

```

$ docker run -it dockerimagid /bin/bash
$ python macaddfetch.py

```

While runng this command you can fetch all the details of that mac address.
