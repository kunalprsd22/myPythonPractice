import asyncio

async def fetch_user():
    await asyncio.sleep(1)
    raise ValueError("User service failed")


async def main():
    try:
        user = await fetch_user()
        print(user)

    except ValueError as error:
        print(f"Error occurred: {error}")

    print("Application continues")


asyncio.run(main())
