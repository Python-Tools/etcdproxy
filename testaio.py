import asyncio
from etcdproxy import EtcdProxy


async def main() -> None:
    etcd = EtcdProxy()
    etcd.initialize_from_url("etcd+async://localhost:12379")
    print(etcd.aio)
    await etcd.put('/key', 'dooot')
    print(await etcd.get('/key'))
    await etcd.close()

asyncio.run(main())