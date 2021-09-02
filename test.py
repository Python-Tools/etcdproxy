from etcdproxy import EtcdProxy

etcd = EtcdProxy()

etcd.initialize_from_url("etcd://localhost:12379")

etcd.put('/key', 'dooot')
print(etcd.get('/key'))

etcd.close()