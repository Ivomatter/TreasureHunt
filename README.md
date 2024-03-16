# TreasureHunt

How to install and boot:
    1. Install Node.js
    2. cmd: npm install -g react-native-cli
    3. cmd: npm install -g expo
    4. powershell as administrator: Set-ExecutionPolicy RemoteSigned 

Setup ngrok (used to let the phone app connect to the backend:):
    1.Create account and login https://dashboard.ngrok.com/signup
    2.Included ngrok is for windows, if running on MacOS/Linux, download respective version
    3.Open ngrok

Open 2 terminals in code
First terminal:
    1. cd ./server
    2. python -m venv ./.venv
    3. activate venv with "./.venv/scripts/activate" //COULD BE DIFFERENT FOR MAC
    4. pip install flask
    5. python server.py
    6. check which port the server is running on - for me it's 5000 by default.
    7. go to ngrok and execute with respective port: "ngrok http [port]" so for me "ngrok http 5000"
    
Second terminal:
    npx expo start --tunnel

should be all done

