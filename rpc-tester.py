import requests
import time

def test_rpc(url):
    payload = {"jsonrpc":"2.0","id":"7","method":"getRecentBlockhash","params":[]}
    headers={'Content-Type': 'application/json'}
    total = 0

    try:
        for i in range(10):
            start = time.perf_counter()
            rpc_request=requests.post(url=url,json=payload,headers=headers)
            final = time.perf_counter() - start
            if rpc_request.status_code != 200:
                if rpc_request.status_code == 405:
                    return 'Make sure you are using a valid rpc'
                elif rpc_request.status_code == 403:
                    return 'Make sure you have your IP whitelisted'
                elif rpc_request.status_code == 404:
                    return 'Not Found'
                else:
                    return rpc_request.status_code

            print(f"Request {i+1} "+ "completed in {0:.6f}ms".format(final))
            total += final

        return 'Average: {0:.6f}ms'.format(total/10) 
    except requests.exceptions.MissingSchema:
        return 'Invalid URL'
    except requests.exceptions.ConnectionError:
        return 'Check URL again'
finished = False
while not finished:
    rpc = input('Enter a RPC: ')
    print(test_rpc(rpc))

    try_again = input('Try another RPC? (y/n): ')
    
    if try_again.lower() == 'n':
        print('Exiting...')
        finished = True
    elif try_again.lower() == 'y':
        continue
    else:
        print("Enter a valid string")