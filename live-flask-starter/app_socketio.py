import logging
import os
from flask import Flask
from flask_socketio import SocketIO
from dotenv import load_dotenv
from deepgram import (
    DeepgramClient,
    LiveTranscriptionEvents,
    LiveOptions,
    DeepgramClientOptions,
    SpeakOptions
)
from mem0 import Memory  # Import the Memory class
import sys
import subprocess
from queue import Queue
import threading
import io
from pydub import AudioSegment
from pydub.playback import play

# Add the parent directory to the Python path
parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(parent_dir))

# Initialize the PersonalAITutor class
from hosted_mem0 import PersonalAITutor
ai_tutor = PersonalAITutor()

load_dotenv()


app_socketio = Flask("app_socketio")
socketio = SocketIO(app_socketio, cors_allowed_origins=['http://127.0.0.1:8000'])

API_KEY = os.getenv("DEEPGRAM_API_KEY")
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Set up client configuration
config = DeepgramClientOptions(
    verbose=logging.WARN,  # Change to logging.INFO or logging.DEBUG for more verbose output
    options={"keepalive": "true"}
)

deepgram = DeepgramClient(API_KEY, config)

dg_connection = None



# Initialize the Memory class
memory = Memory()

tts_running = threading.Event()
tts_process = None

tts_stop_event = threading.Event()

def on_message(self, result, **kwargs):
    global tts_process, tts_stop_event
    transcript = result.channel.alternatives[0].transcript
    if len(transcript) > 0:
        print(result.channel.alternatives[0].transcript)
        socketio.emit('transcription_update', {'transcription': transcript})
        
        if "stop" in transcript.lower():
            tts_stop_event.set()  # Signal to stop the TTS playback
            print("Stopping TTS")
            if tts_process and tts_process.is_alive():
                tts_process.join(timeout=1)  # Wait for the thread to finish
            return

        if "hey friend" in transcript.lower() or "hey fran" in transcript.lower() or "hey frank" in transcript.lower():
            print("Keyphrase detected! Waiting for query...")
            if "hey friend" in transcript.lower():
                query = transcript.lower().split("hey friend", 1)[1].strip()
            elif "hey fran" in transcript.lower():
                query = transcript.lower().split("hey fran", 1)[1].strip()
            elif "hey frank" in transcript.lower():
                query = transcript.lower().split("hey frank", 1)[1].strip()
            else:
                query = ""
            
            if query:
                print(f"Query received: {query}")
                user_id = 'nik124912412841962839'  # Nik's user ID
                query_queue.put((query, user_id))
            else:
                print("No query detected after keyphrase.")

def on_open(self, open, **kwargs):
    print(f"\n\n{open}\n\n")

def on_close(self, close, **kwargs):
    print(f"\n\n{close}\n\n")

def on_error(self, error, **kwargs):
    print(f"\n\n{error}\n\n")

@socketio.on('audio_stream')
def handle_audio_stream(data):
    if dg_connection:
        # print("Processing audio chunk")
        dg_connection.send(data)

@socketio.on('toggle_transcription')
def handle_toggle_transcription(data):
    print("toggle_transcription", data)
    action = data.get("action")
    if action == "start":
        print("Starting Deepgram connection")
        initialize_deepgram_connection()

@socketio.on('connect')
def server_connect():
    print('Client connected')

@socketio.on('restart_deepgram')
def restart_deepgram():
    print('Restarting Deepgram connection')
    initialize_deepgram_connection()

def initialize_deepgram_connection():
    global dg_connection
    # Initialize Deepgram client and connection
    dg_connection = deepgram.listen.live.v("1")

    dg_connection.on(LiveTranscriptionEvents.Open, on_open)
    dg_connection.on(LiveTranscriptionEvents.Transcript, on_message)
    dg_connection.on(LiveTranscriptionEvents.Close, on_close)
    dg_connection.on(LiveTranscriptionEvents.Error, on_error)

    # Define the options for the live transcription
    options = LiveOptions(model="nova-2", language="en-US") # interim result autorim zen for noise

    try:
        if dg_connection.start(options) is False:
            print("Failed to start connection")
            exit()
        else:
            print("Deepgram connection established")
    except Exception as e:
        print(f"Error during transcription: {str(e)}")

# Initialize TTS engine
def speak_text(text):
    global tts_process, tts_stop_event
    
    options = SpeakOptions(
        model="aura-stella-en",
        encoding="linear16",
        container="wav"
    )

    # Add natural pauses and filler words to the text
    text = text.replace("...", " ... ")  # Ensure proper spacing for ellipses
    text = text.replace("um", " um ").replace("uh", " uh ")  # Add filler words

    try:
        filename = "output.wav"
        SPEAK_OPTIONS = {"text": text}
        
        # Call the save method to generate the TTS audio and save it to a file
        response = deepgram.speak.v("1").save(filename, SPEAK_OPTIONS, options)
        
        # Load the audio file and play it
        audio = AudioSegment.from_wav(filename)
        
        def play_audio():
            if not tts_stop_event.is_set():
                play(audio)
        
        tts_stop_event.clear()
        tts_process = threading.Thread(target=play_audio)
        tts_process.start()
    except Exception as e:
        print(f"Error in TTS API call: {str(e)}")

query_queue = Queue()

# Test the TTS function with a sample text
test_text = "Hello, this is a test of the Deepgram TTS using the Stella voice."
print('triggering speak text')
speak_text(test_text)


def process_queries():
    while True:
        query, user_id = query_queue.get()
        if query is None:
            break
        try:
            related_memories = ai_tutor.search_memories(query=query, user_id=user_id)
            if related_memories:
                print("Profile information found:")
                response_text = "Here's what I know about Nik Shevchenko: "
                # Only process the first memory
                mem = related_memories[0]
                first_sentence = mem['text'].split('.')[0] + '.'
                print(f"Content: {first_sentence}")
                if 'score' in mem:
                    print(f"Relevance Score: {mem['score']}")
                print("---")
                response_text += first_sentence + " "
                socketio.emit('profile_info', {'memories': [mem]})
                speak_text(response_text)
            else:
                print("No relevant profile information found.")
                response_text = "I'm sorry, I couldn't find any relevant information about Nik Shevchenko."
                socketio.emit('profile_info', {'message': 'No relevant information found.'})
                speak_text(response_text)
        except Exception as e:
            print(f"Error processing query: {str(e)}")
        query_queue.task_done()

# Start the query processing thread
query_thread = threading.Thread(target=process_queries)
query_thread.start()

if __name__ == '__main__':
    try:
        logging.info("Starting SocketIO server.")
        socketio.run(app_socketio, debug=True, allow_unsafe_werkzeug=True, port=8081, use_reloader=False)

    finally:
        # Signal the query processing thread to stop
        query_queue.put((None, None))
        query_thread.join()
