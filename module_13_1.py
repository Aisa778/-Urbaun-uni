import asyncio

async def start_strongman(name, power):
    for i in range(1,5+1):
        print(f'Силач {name} начал соревнования.')
        await asyncio.sleep(1//power)
        print(f'Силач {name} поднял {i} шар.')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Илья Муромец', 10))
    task_2 = asyncio.create_task(start_strongman('Добрыня Никитич', 9))
    task_3 = asyncio.create_task(start_strongman('Алеша Попович', 8))

    await task_1
    await task_2
    await task_3

asyncio.run(start_tournament())