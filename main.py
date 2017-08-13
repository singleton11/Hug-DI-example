import hug
from nameko.standalone.rpc import ClusterRpcProxy

cluster_proxy: ClusterRpcProxy = ClusterRpcProxy({
    # Do not hardcode this option, and the best is getting from environment
    # variables
    'AMQP_URI': 'amqp://guest@127.0.0.1:5672//'
})
started_proxy = cluster_proxy.start()


@hug.directive()
def rpc_cluster(**kwargs) -> ClusterRpcProxy:
    return started_proxy


@hug.get()
def hello(rpc: rpc_cluster) -> str:
    return (
        f'Temperature is {rpc.temperature_service.get_temperature()}, '
        f'Humidity is {rpc.humidity_service.get_humidity()}'
    )
