#!/usr/bin/env python3

import asyncio

async def mysleep(n):
    print(f"I will be sleeping for {n} seconds")
    await asyncio.sleep(n)
    print(f"I have been sleeping for {n} seconds")

async def main():
    res = [asyncio.create_task(mysleep(i)) for i in range(10)]
    await asyncio.gather(*res)

if __name__ == "__main__":
    asyncio.run(main())
    