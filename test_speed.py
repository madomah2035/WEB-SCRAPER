import speedtest as st
from concurrent.futures import ThreadPoolExecutor


def speed_test():
    test = st.Speedtest()

    test.get_best_server()

    with ThreadPoolExecutor() as exe:
        upload_future = exe.submit(get_upload_speed, test)
        download_future = exe.submit(get_download_speed, test)

        up_speed = upload_future.result()
        down_speed = download_future.result()


    print(f"Upload Speed is: {up_speed / 10 ** 6: .2f} Mbps")
    print("{} {:.2f} {}".format("Download Speed is:", down_speed / 10 ** 6, "Mbps"))

    get_ping_results(test)

def get_upload_speed(test):
    return test.upload()
    # up_speed = test.upload()


def get_download_speed(test):
    return test.download()
    # down_speed = test.download()


def get_ping_results(test):
    ping = test.results.ping
    if ping <= 30:
        print(f"Ping: {ping:.2f} ms; Your internet speed is excellent for real time activities like gaming and video conferencing!")
    elif 30 < ping <= 50:
        print(f"Ping: {ping:.2f} ms; Your internet speed is good and still suitable for most activities!")
    elif 50 < ping <= 100:
        print(f"Ping: {ping:.2f} ms; Average internet speed, can be noticeable in real time activities!")
    else:
        print(f"Ping: {ping:.2f} ms; Poor internet speed, noticeable lags in gaming and video chats!")


speed_test()
