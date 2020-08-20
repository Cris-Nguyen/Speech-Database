# Speech database maker
Make speech dataset for Speech Recognition or Speech Synthesis with youtube data for Vietnamese and other languages

### 1. Crawl audio data from youtube
- Put youtube playlist(or video) links you want to download in playlists.txt. Default folder to save audio is audio/
- Run ``` python youtube_crawl.py ```

### 2. Decode raw audio and get transcript
- Here i crawl and make database for Vietnamese. You can also make database for other languages
- Here i use autosub for decoding. Other option maybe Google API
- Run ``` python transcript.py ```

### 3. Extract csv file
- Extract csv file from database contains 2 columns: audio_path and sub
- Run ``` python make_db.py ```

### 4. Split data randomly to train/test
- Split data to train/test data with ratio 80 - 20
- Run ``` python split.py ```
