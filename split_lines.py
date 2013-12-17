def show():
    request = '''
    CONNECT %s:%s HTTP/1.1
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:26.0) Gecko/20100101 Firefox/26.0
    Proxy-Connection: keep-alive
    Connection: keep-alive
    Host: %s 
    '''
    delimiter = '\r\n'
    def clear_request(request):
        for one in request.split('\n'):
            one = one.strip()
            if one:
                yield one
    request = delimiter.join(clear_request(request))
    request += delimiter
    print request

show()
