
import asyncio
import time


async def fetch_user():
    print("Fetching user...")
    time.sleep(2)
    return "User data"


async def fetch_orders():
    print("Fetching orders...")
    time.sleep(4)
    return "Orders data"


async def fetch_products():
    print("Fetching products...")
    time.sleep(6)
    return "Products data"


async def main():
    start = time.perf_counter()

    user = await fetch_user()
    orders = await fetch_orders()
    products = await fetch_products()

    print(user)
    print(orders)
    print(products)


    print("Total:", time.perf_counter() - start)


asyncio.run(main())
