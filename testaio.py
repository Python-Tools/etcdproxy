import asyncio
from etcdproxy import EtcdProxy


async def main() -> None:
    etcd = EtcdProxy()
    etcd.initialize_from_url("etcd+async://localhost:12379")
    print(etcd.aio)
    await etcd.put(b'/key', b'doootaio')
    print(await etcd.get(b'/key'))
    await etcd.close()

asyncio.run(main())