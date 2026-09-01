Safari AI Distraction Blocker
A tool for macOS that uses AI to keep an eye on your activity when using Safari and to judge if you are going to distracting websites.
The project involves the use of Groq to check websites that have recently been visited; when a distracting website is detected, the program automatically deletes the Safari history, closes all of the Safari tabs and terminates Safari.

Features
🤖 AI-powered website distraction detection
🌐 Monitors Safari browsing history
⏱️ Checks browsing activity every 10 seconds
🧠 Uses an LLM to determine whether a website is distracting
🧹 Automatically clears Safari history when a distraction is detected
🚪 Closes all open Safari tabs
🛑 Terminates Safari after detecting a distraction
🔍 Uses the website's primary purpose rather than simply matching a list of known domains
How It Works
The application continuously performs the following process:
Safari History
     │
     ▼
Read recent websites
     │
     ▼
Take the latest 6 items (so the LLM isn't being overwhelmed)
     │
     ▼
Send websites to AI classifier
     │
     ▼
   ┌───────────────┐
   │ Distraction?  │
   └───────┬───────┘
           │
      ┌────┴────┐
      │         │
     YES        NO
      │         │
      ▼         ▼
Clear Safari   Continue
history        monitoring
      │
      ▼
Close tabs
      │
      ▼
Quit Safari
The classifier gives only a yes or a no answer, and if the answer is no then it means that at least one of the websites in the list is regarded as distracting.
Project Structure
.
├── Ai.py
├── Main.py
├── osscripts.py
└── README.md

Main.py
The main program reads the History.db file of Safari, retrieves the browsing history, selects the six most recent entries, and passes them on to the AI classifier.
When the classifier identifies a distraction, it carries out the Safari automation scripts and then terminates Safari.

Ai.py
Handles communication with Groq.

osscripts.py
The AppleScript commands used for automating Safari are included.
The project includes scripts for:
Closing all Safari tabs
Clearing Safari history
Prompt for the LLM

Requirements
macOS
Safari
Python 3
A Groq API key
The Python groq package



⚠️ Important Warning
The program will carry out destructive actions if it identifies a distraction.
A detected distraction can cause the program to:
Clear Safari history
Close Safari tabs
Kill the Safari process
The actions are carried out using AppleScript and pkill.
I recommend that you use this project entirely at your own risk and ensure that you understand its function before running it on a machine which contains important browsing sessions or history.

Privacy
The data from your most recent Safari browsing session is retrieved from Safari's local history database and then forwarded to the Groq API that has been configured for classification.
You should not use this project if the browsing data you are dealing with is of something you are not comfortable sending to the AI service that has been configured.

Potential improvements include:

Allow users to customize distraction categories

Add logging

Improve error handling

Add a whitelist for allowed websites

Add a user-configurable monitoring interval

Support additional browsers

Disclaimer
The software is being offered for use in educational and personal productivity contexts. However, the author cannot be held responsible for any consequences such as lost browsing history, closed tabs, interrupted work, or other effects that may result from using the software.
