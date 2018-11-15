# Gauntlet Hangouts Tool
A simple Python script that allows easy filtering of Gauntlet Hangout events.

Gauntlet Hangouts is Gauntlet RPG's space for playing roleplaying games online. Their calendar hosts over 100 game events per month. The games played cover a variety of systems and genres, with an emphasis on indie RPGs, story games, and the OSR.

## Under Development
This was initially a tool for personal use but I later decided to share it with the community once it is finished. This tool is still under development and just has a Python script that works from the command line.

## Usage
General usage for this tool.

```
usage: gauntlet-hangouts.py [-h] [-r] [-f] [-u] [-w] [-s] [-t TIMESLOT] {fetch,filter,open}

positional arguments:
  {fetch,filter,open}   The command to execute.

optional arguments:
  -h, --help            show this help message and exit
  -r, --refresh         Force a refresh.
  -f, --full            Include full events.
  -u, --unavailable     Include events that are not available yet for non-"Hangous Friend" patreon
                        subscribers.
  -w, --waitlist        Include events that has a waitlist.
  -s, --session         Show only the first session.
  -t TIMESLOT, --timeslot TIMESLOT
                        Additional parameters as time. Format example: 8:30-18:00)
```

For example, if you want to list down games that are full but have no waitlist between 8:30AM to 11:00AM, you can pass the command below:

```
gauntlet-hangouts.py filter -fw -t 8:30-11:00
```

## Technical Details
This script uses Selenium Python to open up the [RSVP website](https://gauntlet-hangouts.firebaseapp.com/all-events-info), it downloads all of the events data saves it to a file which allows for easy and faster filtering in the future.

The technical challenge is getting the link for the individual events as the website is rendered so that each link is done through a Javascript event. The current approach of opening an event page using the `open` command works but still can be improved.
