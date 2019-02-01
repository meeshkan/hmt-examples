# Getting started with Meeshkan command-line


### Installation
First check that you have installed `meeshkan` in your Python
[virtual environment](https://docs.python.org/3/tutorial/venv.html) with
````bash
pip install --upgrade meeshkan
````
Note that only **Python >= 3.6.2** is supported at the moment.

Check that the package is properly installed by running the command
```bash
$ meeshkan
```
If `meeshkan` is found in your path, the available commands are listed.

### Setup

Meeshkan first needs to be setup with
```bash
$ meeshkan setup
```
You will be prompted for the API key you got when registering at
[meeshkan.com](https://meeshkan.com) so fill that in.

### Submit jobs
Start the Meeshkan agent:
```bash
$ meeshkan start
```

Submit the script [first_job.py](./first_job.py):
```bash
$ meeshkan submit first_job.py
```
If you added the [Slack integration](https://www.meeshkan.com/docs/slack), you should have
received a notification for job being started and finished.

Submit the script with a given name:
```bash
$ meeshkan submit --name "My first job" first_job.py
```
Now your notifications contain the job name.

`meeshkan` can also notify you when things go wrong.
To see how this works, submit a failing script:
```bash
$ meeshkan submit --name "World will burn" failing_job.py
```

View the jobs you have submitted:
```bash
$ meeshkan list
```

Now that you know the basics, get started [writing Python](../writing-scripts)
using ``meeshkan`` to customize your job updates!