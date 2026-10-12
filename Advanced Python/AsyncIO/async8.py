
import asyncio


async def download_file():
    try:
        print("Download started")

        await asyncio.sleep(10)

        print("Download completed")
        return "file.pdf"

    except asyncio.CancelledError:
        print("Download cancelled")
        raise


async def main():
    task = asyncio.create_task(download_file())

    await asyncio.sleep(2)

    print("Cancelling download...")
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Main received cancellation")


asyncio.run(main())
