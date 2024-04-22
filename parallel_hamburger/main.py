import time
from concurrent.futures import ProcessPoolExecutor


def parallel_hamburger(cooking_time: float):
    # 注文
    print("非常に豪華なハンバーガーを注文しました。")
    print("支払い料金の準備をします。")
    time.sleep(2)
    print("キッチンの男に注文内容を伝えます。")
    time.sleep(3)
    print("料金を支払います。")
    print("料金を受け取ります。")

    # ハンバーガーの準備
    print("非常に豪華なハンバーガーを作ります。")
    time.sleep(cooking_time)
    print("非常に豪華なハンバーガーの準備ができました。")

    # ハンバーガーを食べる
    print("非常に豪華なハンバーガーを受け取ります。")
    print("テーブルに座ります。")
    print("ハンバーガーをいただきます。")


def main():
    """NOTE:
    フロー
        注文
        ハンバーガーの準備
        ハンバーガーを食べる（ハンバーガーの準備中に恋人との会話ができない）
    """
    print(f"開始時刻: {time.strftime('%X')}")

    with ProcessPoolExecutor(max_workers=2) as executor:
        executor.submit(parallel_hamburger, 10)
        executor.submit(parallel_hamburger, 15)

    print(f"終了時刻: {time.strftime('%X')}")


if __name__ == "__main__":
    main()
