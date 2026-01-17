import speedtest

def realizar_test():
    
    test = speedtest.Speedtest()

    print('Buscando el mejor sevidor...')

    test.get_best_server()

    print('Midiendo velocidad de descarga...')

    velocidad_descarga = test.download()

    print('midiendo velocidad de subida...')
    velocidad_subida = test.upload()

    print('\n--- RESULTADOS ---')
    print(f'Velocidad de Descarga: {velocidad_descarga / 10**6:.2f} Mbps')
    print(f'Velocidad de subida: {velocidad_subida / 10**6:.2f} Mbps')

if __name__ == '__main__':
    realizar_test()