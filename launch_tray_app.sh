#!/bin/bash
kdialog --passivepopup "Time Tracker started."
cd ~/git_repos/time_tracker/
nohup ~/python_venv/py3_qt/bin/python ~/git_repos/time_tracker/time_tracker.py &
kdialog --passivepopup $!
#disown "%nohup"
