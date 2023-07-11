#!/usr/bin/env python3
'''Task 2's module.
'''
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime():
    start_time = asyncio.get_event_loop().time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = asyncio.get_event_loop().time()
    return end_time - start_time

