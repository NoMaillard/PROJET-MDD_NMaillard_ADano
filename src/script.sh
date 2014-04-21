#!/bin/sh
osascript -e '
tell application "iTerm"
    activate
    tell i term application "System Events" to keystroke "w" using command down
    set myterm to (make new terminal)
    tell myterm
        launch session "Default Session"
        tell the last session to write text "cd /Users/Noe/Documents/Cours/S2/MDD/src && python ./main.py"
    end tell
end tell'