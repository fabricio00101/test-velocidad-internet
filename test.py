import speedtest

def realizar_test():
    
    test = speedtest.Speedtest(secure=True)

    print('Buscando el mejor sevidor...')

    test.get_best_server()

    print('Midiendo velocidad de descarga...')

    velocidad_descarga = test.download()

    print('Midiendo velocidad de subida...')
    velocidad_subida = test.upload()

    descarga_mbs = velocidad_descarga / (8 * 10**6)
    subida_mbs = velocidad_subida / (8 * 10**6)

    print('\n--- RESULTADOS ---')
    print(f'Velocidad de Descarga: {descarga_mbs:.2f} Mb/s')
    print(f'Velocidad de subida: {subida_mbs:.2f} Mbp/s')

if __name__ == '__main__':
    realizar_test()