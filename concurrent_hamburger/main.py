import asyncio
import time


async def order_now():
    print("非常に豪華なハンバーガーを注文しました。")
    print("支払い料金の準備をします。")
    await asyncio.sleep(2)
    print("料金を支払います。")


async def place_order():
    print("キッチンの男に注文内容を伝えます。")
    await asyncio.sleep(3)
    print("料金を受け取ります。")
    print("番号札になります。")


async def cooking():
    print("非常に豪華なハンバーガーを作ります。")
    await asyncio.sleep(10)
    print("非常に豪華なハンバーガーの準備ができました。")


async def conversation_with_someone_you_like():
    print("テーブルに座ります。")
    print("恋人と会話をします。")
    await asyncio.sleep(25)
    print("会話を終了します。")
    print("ハンバーガーを持ってくるね")


def eating():
    print("ハンバーガーをいただきます。")


async def concurrent_hamburger():
    """NOTE:
    フロー:
        注文
        ハンバーガーの準備
        恋人との会話
        ハンバーガーを食べる
    """
    # NOTE: asyncio.TaskGroupはPython3.11で追加されているものになるため注意
    async with asyncio.TaskGroup() as tg:
        tg.create_task(order_now())
        tg.create_task(place_order())

        print(f"タスクの開始時刻: {time.strftime('%X')}")

    print(f"タスクの終了時刻: {time.strftime('%X')}")

    async with asyncio.TaskGroup() as tg:
        tg.create_task(cooking())
        tg.create_task(conversation_with_someone_you_like())

        print(f"タスクの開始時刻: {time.strftime('%X')}")

    print(f"タスクの終了時刻: {time.strftime('%X')}")
    eating()


def main():
    asyncio.run(concurrent_hamburger())


if __name__ == "__main__":
    main()
