from etcdproxy import EtcdProxy

etcd = EtcdProxy()

etcd.initialize_from_url("etcd://localhost:12379")

etcd.put(b'/key', b'dooot')
print(etcd.get(b'/key'))

etcd.close()
