DevOps Lab 2020 (Janary - Aprile)
Homework3: Maxim Filipovich

Description: <br>
This app outputs next information:
- Snapshot ID 
- Timestamp w-day/month/day of month/time/ year
- % of CPU load 
- % of disk usage
- % of usage virtual memory
- IO information
- network packets sent

This information could be writed in json/txt (info.<json/txt>) file in your current directory.

How it works: <br>
Application recieves two parameters:<br>
- chose type of output file (default: txt, you may choose: txt/help)
- interval (in seconds) (by default 300 seconds)

```bash
# for help
snapshot -h
# for run by default
snapshot 
# takes snaphosts every 60 second and put it into json file
snapshot json 60
# takes snaphosts every 60 second and put it into  txt file
snapshot txt 60
```
```bash
How to setup: <br>
Before using this application please install `psutil` with `pip` (pip install psutil). Python version `3.6.8` requaried.

Created a distributive package of the script (to make wheel from source files):
`python3 setup.py bdist_wheel --universal`

Package has to be located in the parent directory.
```
