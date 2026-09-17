import asyncio
from datetime import datetime

async def background_logger():
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")

        with open("background_log.txt", "a") as file:
            file.write(f"Background task running: {current_time}\n")

        print("Background task: log saved")

        await asyncio.sleep(3)


async def main_task():
    for i in range(1, 6):
        print(f"Main task: Working... {i}")
        await asyncio.sleep(1)


async def main():
    # Start background task
    asyncio.create_task(background_logger())

    # Main task continues
    await main_task()


asyncio.run(main())