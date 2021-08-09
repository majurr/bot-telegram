from netifaces import interfaces, ifaddresses, AF_INET

def meu_ip():
    """[Retorna o IP da rede local do dispositivo conectato]

    Returns:
        [str]: [interface + ip address]
    """
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}])]
        if ifaceName[0] == 'w':
            return "interface: {} {}".format(ifaceName, addresses)
