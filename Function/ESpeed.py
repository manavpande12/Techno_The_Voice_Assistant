import speedtest
from SpeakGet.Talk import speak

def humansize(nbytes):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])

def check_internet_speed():
    speak("Ok, sir. Let me calculate. It may take a while; you may continue another task.")
    try:
        st = speedtest.Speedtest()
        st.get_best_server()

        # Perform the download speed test
        download_speed = st.download() / 1000000  # Convert to Mbps

        # Perform the upload speed test
        upload_speed = st.upload() / 1000000  # Convert to Mbps

        # Perform the ping test
        ping_result = st.results.ping

        # Format results
        formatted_ping = f"{ping_result:.0f} ms"
        formatted_download_speed = f"{download_speed:.2f} Mbps"
        formatted_upload_speed = f"{upload_speed:.2f} Mbps"

        # Speak the results
        speak(f"Ping: {formatted_ping}")
        speak(f"Download speed: {formatted_download_speed}")
        speak(f"Upload speed: {formatted_upload_speed}")

    except speedtest.SpeedtestException as e:
        speak("An error occurred during the speed test. Please try again later.")
