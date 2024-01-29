# LaunchpadSimple

A simple MIDI remote script to use the Novation Launchpad Mini MK3 with Ableton Live

## How to install

### Prerequisites

- Make sure you have Python 3 installed
- Make sure you have the Python library [python-dotenv](https://pypi.org/project/python-dotenv/) installed

### Preparation

Find out the path to your Ableton Live user library folder. On Windows, this would typically be `\Users\[username]\Documents\User Library`, on Mac `/Users/[username]/Music/Ableton/User Library`.

Copy the file `.env.example` to `.env`.

Edit the `.env` file. Change the value of `TARGET_DIRECTORY` to your user library, suffixed with `Remote Scripts\LaunchpadSimple`.

- Windows example: `TARGET_DIRECTORY="C:\Users\[username]\Documents\User Library\Remote Scripts\LaunchpadSimple"`
- Mac example: `TARGET_DIRECTORY="/Users/[username]/Music/Ableton/User Library/Remote Scripts/LaunchpadSimple"`

### Installation

Run the Python script `install.py`:

```
python install.py
```

If everything is set up properly, this will create a new directory `LaunchpadSimple` in user User Library's `Remote Scripts` subdirectory and copy over all the relevant files to use this remote script with Ableton Live.

Start Ableton Live. 

Open Live's Preferences and go to the Link/MIDI tab. 

In the list of Control Surfaces, select `LaunchpadSimple` and set the input and output port to `LPMiniMK3 MIDI`.

In the list of MIDI Ports, find the `In` and `Out` entries for `LaunchpadSimple` and tick the boxes `Track`, `Sync` and `Remote` for each.

## Development

### Logging

The LaunchpadSimple remote script writes log messages to the standard log file of Ableton live. Log messages are prefixed with `LS_LOG` so that they can be easily found and grepped.

The location of the log file varies between Mac and Windows and also changes with every version update of Ableton Live.

Example for the log file path on a German Windows machine:

* `/c/Dokumente\ und\ Einstellungen/wieka/Anwendungsdaten/Ableton/Live\ 11.3.21/Preferences/Log.txt`

Assuming the path to the log file is the one from this example, we can view the log output using this command:

```
tail -f /c/Dokumente\ und\ Einstellungen/wieka/Anwendungsdaten/Ableton/Live\ 11.3.21/Preferences/Log.txt | grep -oG "LS_LOG.*"
```

### Updating

While working on the remote scripts, when you want to test your latest changes in Ableton Live:

* On the command line, run `python install.py`
* In Live, go to Preferences > Link/MIDI
* In the MIDI remote surfaces list, switch the entry where it says `LaunchpadSimple` to some other entry in the pulldown menu, then back to `LaunchpadSimple`