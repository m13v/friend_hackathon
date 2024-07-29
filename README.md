

# What is this?

This was a two day hackathon at AGI House SF on July 28, 2024
https://partiful.com/e/AzVSvX4VB2cwWs52I0FW

# What is does
1. It takes images from Openglass, finds faces in the local db, so that it knows who you are talking to.
2. It has an audio deepgram assistant that listens to your key phrases "Hey Friend" to trigger query to DB using mem0, and read back to you its contents
* These two pieces should be linked together into a proper flow, but I didn't have time to do it


The repo contains multiple scripts that do not as a coherent independent application, but it still runs:
Get started:
1. Start ngrok endpoint:
```bash
ngrok http 8080 
```
2. Copy the endpoint to your Friend app
-> Settings
-> Developer mode
-> On Memory Created endpoint: ..... (right now only this endpoint works for openglass)

3. Start app to process requests from Friend app from the root directory
```bash
python app.py
```
4. Start qdrant vector db. I first built it from source and then ran it
```bash
git clone https://github.com/qdrant/qdrant.git
cargo build --release
./target/release/qdrant
```
5. Add data to qdrant db using mem0. Look through store_nik.py file to see the data we are adding and function we call. 
We call mem0 trhough the class PersonalAITutor that is defined in hosted_mem0.py 
```bash
python store_nik.py # but first explore the content
python check_qdrant.py # let's check that vectors are in db
```
6. Start deepgram app to query 
```bash
cd live-flask-start
python app_socketio.py
python app.py
```
Then open the suggested localhost to see the UI, but keep the server terminal open to see the logs


Made by Matthew Diakonov