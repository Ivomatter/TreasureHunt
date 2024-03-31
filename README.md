Loc8r is an AI-based treasure hunt game. 
First, the player would create a room, configure it, and add photos of the play environment. 
Then an AI would find the objects that are present in the pictureas. 
In the end, different model would create riddles for these objects.
Multiple players can enter each room with a code given when creating it.

To start the server, make sure you have the latest version of Python installed, then:
1. clone repository and cd to ./thunt
2. Create a venv: python -m venv ./.venv
3. Select venv as active environment and activate it: ./.venv/scripts/activate
3. Install dependencies:
   * pip install openai
   * pip install flask
   * pip install ultralytics
   * pip install imagesize
4. Start the server with ./server.py
5. Navigate to http://localhost:5000/


