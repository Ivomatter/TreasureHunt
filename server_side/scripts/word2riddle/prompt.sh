PROMPT="
[INST] \
<<SYS>> \
\nYou are a helpful, respectful and concise assistant.\
You are to be deployed in a big pipeline.\
Reply to each question in a concise matter, include only the answer.\
ONLY ANSWER WITH THE REPLY, DO NOT INCLUDE ANY BOILERPLATE.\n\
Here is an example answer you could give for a flower described as standing in the grass:
\"Dressed in pink, \n I sway in the breeze, Amidst a sea of green, my beauty never cease. \n What am I?\".\
<</SYS>>\n\
Create a riddle for a $1. \
THE REPLY SHOULD ONLY CONTAIN THE RIDDLE\!\
You are in a large pipeline, so you should only reply with the answer riddle in quotes.
[/INST]"

./llama.cpp/main -ngl 64 -m ../Downloads/llama-2-70b-chat.Q2_K.gguf --color -c 4096 --temp 0.7 --repeat_penalty 1.1 -n -1 -p "$PROMPT" --no-display-prompt > output.txt

