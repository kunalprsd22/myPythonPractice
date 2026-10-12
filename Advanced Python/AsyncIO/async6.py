import asyncio


async def fetch_profile():
    await asyncio.sleep(1)
    return "Profile loaded"


async def fetch_orders():
    await asyncio.sleep(2)
    raise ValueError("Orders service failed")


async def fetch_products():
    await asyncio.sleep(3)
    return "Products loaded"


async def main():
    results = await asyncio.gather(
        fetch_profile(),
        fetch_orders(),
        fetch_products(),
        return_exceptions=True
    )

    for result in results:
        if isinstance(result, Exception):
            print("Failed:", result)
        else:
            print("Success:", result)


asyncio.run(main())