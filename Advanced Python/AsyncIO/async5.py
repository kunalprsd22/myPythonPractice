
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
    try:
        user, orders, products = await asyncio.gather(
            fetch_profile(),
            fetch_orders(),
            fetch_products()
        )
        print(user)
        print(orders)
        print(products)

    except ValueError as error:
        print(f"Request failed: {error}")


asyncio.run(main())
