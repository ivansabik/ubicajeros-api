API de sucursales bancarias México
===========

## Bancomer

Falta limpiar los jsons

#### 1.json

https://raw.githubusercontent.com/mexicapis/sucursales-bancos-api/master/bancomer/1.json

Al parecer trae:

 - Cajeros automáticos
 - Sucursales

```
curl -o cajas_rapidas.json 'http://184.106.19.51/BuscadorSucursales/ServicioMapa.asmx/BusquedaCodigoPostalRadio' -H 'Origin: http://184.106.19.51' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36' -H 'Content-Type: application/json; charset=UTF-8' -H 'Accept: */*' -H 'Referer: http://184.106.19.51/buscadorsucursales/Buscador.aspx' -H 'Connection: keep-alive' --data-binary '{"idCategoria":"1","latitud":"19.3885                                           ","longitud":"-99.2291                                          ","radio":9001000}' --compressed
```

#### 2.json

https://raw.githubusercontent.com/mexicapis/sucursales-bancos-api/master/bancomer/2.json

Al parecer trae:

 - Practicajas

```
curl -o cajeros.json 'http://184.106.19.51/BuscadorSucursales/ServicioMapa.asmx/BusquedaCodigoPostalRadio' -H 'Origin: http://184.106.19.51' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36' -H 'Content-Type: application/json; charset=UTF-8' -H 'Accept: */*' -H 'Referer: http://184.106.19.51/buscadorsucursales/Buscador.aspx' -H 'Connection: keep-alive' --data-binary '{"idCategoria":"76","latitud":"19.3885                                           ","longitud":"-99.2291                                          ","radio":9001000}' --compressed
```

####  3.json

https://raw.githubusercontent.com/mexicapis/sucursales-bancos-api/master/bancomer/3.json

Al parecer trae:

 - Kioskos

```
curl -o kioskos.json 'http://184.106.19.51/BuscadorSucursales/ServicioMapa.asmx/BusquedaCodigoPostalRadio' -H 'Origin: http://184.106.19.51' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36' -H 'Content-Type: application/json; charset=UTF-8' -H 'Accept: */*' -H 'Referer: http://184.106.19.51/buscadorsucursales/Buscador.aspx' -H 'Connection: keep-alive' --data-binary '{"idCategoria":"77","latitud":"19.3885                                           ","longitud":"-99.2291                                          ","radio":9001000}' --compressed
```

#### 4.json

https://raw.githubusercontent.com/mexicapis/sucursales-bancos-api/master/bancomer/4.json

Al parecer trae:

 - Retiro en establecimientos
 - Caja express

```
curl -o 4.json 'http://184.106.19.51/BuscadorSucursales/ServicioMapa.asmx/BusquedaCodigoPostalRadio' -H 'Origin: http://184.106.19.51' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36' -H 'Content-Type: application/json; charset=UTF-8' -H 'Accept: */*' -H 'Referer: http://184.106.19.51/buscadorsucursales/Buscador.aspx' -H 'Connection: keep-alive' --data-binary '{"idCategoria":"78","latitud":"19.3885                                           ","longitud":"-99.2291                                          ","radio":9001000}' --compressed
```

#### 5.json

https://raw.githubusercontent.com/mexicapis/sucursales-bancos-api/master/bancomer/5.json

```
curl -o 5.json 'http://184.106.19.51/BuscadorSucursales/ServicioMapa.asmx/BusquedaCodigoPostalRadio' -H 'Origin: http://184.106.19.51' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36' -H 'Content-Type: application/json; charset=UTF-8' -H 'Accept: */*' -H 'Referer: http://184.106.19.51/buscadorsucursales/Buscador.aspx' -H 'Connection: keep-alive' --data-binary '{"idCategoria":"79","latitud":"19.3885                                           ","longitud":"-99.2291                                          ","radio":9001000}' --compressed
```
