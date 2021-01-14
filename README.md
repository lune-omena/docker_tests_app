# Tests on using Docker

### First Step

Create a docker image for a simple server/api with Flask that says Hello World.

### Second Step

Create a docker image for a python script that says Hello World, and that receives arguments to be writed on screen. The arguments can be actual paths to volumes (files and folders).

### Third Step

Create a docker image for a python script that says Hello World, and that receives input and output arguments that are actual path to volumes, apply some function on the input data and write the result file to the output path argument.

### Repository Structure

```
.
├─ data
│   └─ input
│      └─ data.csv
│   └─ output
├─ src
│   └── app.py
├─ steps
│   ├─ first_step
│   ├─ second_step
│   └─ third_step
├─ Dockerfle
├─ README.md
└─ requirements.txt
```


\*Note: in the data folder is a simple hand-generated csv for test purposes. 

**The generated Dockerfiles for each step are stored in the Steps folder.**


## References:

https://www.docker.com/blog/containerized-python-development-part-1/

https://docs.docker.com/get-started/ (video)

https://docs.docker.com/storage/volumes/
