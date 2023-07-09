Simform Bot

This is an AI powered bot.
Need a data sample like in `text.txt` using which it generates embeddings and saves them in FAISS for further use.

Given the question/user form the input bot will look for the answers associated with certain keywords in the `text.txt` file and returns the relevent answer.

## How to run?

Clone this repo
```bash
git clone https://github.com/Jvdboss7/simformBotTest
```
Install all the requirements (create vertual environament if required)
```bash
pip install -r requirements.txt
```
set openai api key as environamental variable
```bash
export OPENAI_API_KEY="your-openai-api-key"
```
run the chainlit application
```bash
chainlit run chainlit.py -w
```

You can acces the frontend in any browser with port number `8000`

 http://localhost:8000/


### sample output response

![image2](https://github.com/Jvdboss7/simformBotTest/assets/70039145/45ff7830-bb4b-44fc-bfc4-1cce519849c8)

