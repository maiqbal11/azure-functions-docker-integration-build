import argparse
import requests

ADD_OR_UPDATE_ENDPOINT = 'AddOrUpdateHostingConfiguration'


def parse_args():
    parser = argparse.ArgumentParser(
        description='Add or Update Hosting Configuration')
    parser.add_argument('--proxy-address', dest='proxy_address')
    parser.add_argument('--proxy-username', dest='proxy_username')
    parser.add_argument('--proxy-password', dest='proxy_password')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    add_or_update_address = '/'.join([args.proxy_address,
                                      ADD_OR_UPDATE_ENDPOINT])

    add_or_update_data = [
        {
            'configurationKey': 'ServiceFabricContainersDynamicPlaceholdersEnabled',
            'configurationValue': 1
        },
        {
            'configurationKey': 'ServiceFabricContainersEnabled',
            'configurationValue': 1
        },
        {
            'configurationKey': 'ServiceFabricContainersDefaultMaxWorkersPerSite',
            'configurationValue': 3
        },
        {
            'configurationKey': 'AddSiteRestrictedTokenEnabled',
            'configurationValue': 1
        },
        {
            'configurationKey': 'GetWorkersForHostNameStaleCacheFallbackTimeout',
            'configurationValue': 5000
        }
    ]

    for datum in add_or_update_data:
        add_or_update_response = requests.post(url=add_or_update_address,
                                               json=datum,
                                               auth=(args.proxy_username,
                                                     args.proxy_password))

        print(add_or_update_response.text)
