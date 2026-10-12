import asyncio
import time

async def fetch_user():
    print("Fetching user...")
    await asyncio.sleep(2)
    return "User data"

async def fetch_orders():
    print("Fetching orders...")
    await asyncio.sleep(3)
    return "Orders data"

async def fetch_products():
    print("Fetching products...")
    await asyncio.sleep(1)
    return "Products data"

async def main():
    start = time.perf_counter()

    user, orders, products = await asyncio.gather(
        fetch_user(),
        fetch_orders(),
        fetch_products()
    )

    print(user)
    print(orders)
    print(products)

    print(f"Total: {time.perf_counter() - start:.2f} seconds")


asyncio.run(main())
