#!/bin/bash
kdialog --passivepopup "Time Tracker started."
nohup ~/python_venv/py3_qt/bin/python ~/git_repos/time_tracker/time_tracker.py &
kdialog --passivepopup $(jobs)
#disown "%nohup"
