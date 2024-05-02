import time
from concurrent.futures import ProcessPoolExecutor


def living_room_cleaning():
    print("リビングルームを掃除します。")
    time.sleep(20)
    print("リビングルームの掃除が終わりました。")


def kitchen_cleaning():
    print("キッチンを掃除します。")
    time.sleep(15)
    print("キッチンの掃除が終わりました。")


def bathroom_cleaning():
    print("バスルームを掃除します。")
    time.sleep(10)
    print("バスルームの掃除が終わりました。")


def bedroom_cleaning():
    print("ベッドルームを掃除します。")
    time.sleep(5)
    print("ベッドルームの掃除が終わりました。")


def main():
    with ProcessPoolExecutor(max_workers=4) as executor:
        executor.submit(living_room_cleaning)
        executor.submit(kitchen_cleaning)
        executor.submit(bathroom_cleaning)
        executor.submit(bedroom_cleaning)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"実行時間: {end - start}")
