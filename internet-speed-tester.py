import speedtest


def bytes_to_mb(bytes):
    KB = 1024
    MB = KB * KB
    return int(bytes / MB)


st = speedtest.Speedtest()

start = input('Press Enter to Start')
down_speed = str(bytes_to_mb(st.download()))
up_speed = str(bytes_to_mb(st.upload()))
ping = st.results.ping

print('Download Speed: ' + down_speed + ' mb/s')
print('Upload Speed: ' + up_speed + ' mb/s')
print('Ping: ')
print(ping)