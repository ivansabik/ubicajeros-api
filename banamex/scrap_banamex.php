#!/usr/bin/php -q
<?php

foreach (range(1, 32) as $estado) {
	# Sucursales
	$curl_cmd = "curl -o sucursales_" . $estado. ".psv 'http://portal.banamex.com.mx/c719_050/mapasAction.do?opcion=buscar' -H 'Origin: http://portal.banamex.com.mx' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Accept: */*' -H 'Referer: http://portal.banamex.com.mx/mapas/index.jsp?idioma=esp&xhost=http://www.banamex.com/' -H 'Connection: keep-alive' --data 'accion=sucursal-porDom&estado=" . $estado . "&idcd=&iddel=&nomsuc=&numsuc=&loc=&calle=&colonia=&calle1=&calle2=&cp=&plaza=&servicio=&dias=&horario=&tipoBus=100&idioma=esp' --compressed";
    shell_exec($curl_cmd);
    # Cajeros
    $curl_cmd = "curl -o cajeros_" . $estado. ".psv 'http://portal.banamex.com.mx/c719_050/mapasAction.do?opcion=buscar' -H 'Origin: http://portal.banamex.com.mx' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Accept: */*' -H 'Referer: http://portal.banamex.com.mx/mapas/index.jsp?idioma=esp&xhost=http://www.banamex.com/' -H 'Connection: keep-alive' --data 'accion=cajero-porDom&estado=" . $estado . "&idcd=&iddel=&nomsuc=&numsuc=&loc=&calle=&colonia=&calle1=&calle2=&cp=&plaza=&servicio=&dias=&horario=&tipoBus=100&idioma=esp' --compressed";
    shell_exec($curl_cmd);
    # Sucursales auto
    $curl_cmd = "curl -o sucursales_auto_" . $estado. ".psv 'http://portal.banamex.com.mx/c719_050/mapasAction.do?opcion=buscar' -H 'Origin: http://portal.banamex.com.mx' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Accept: */*' -H 'Referer: http://portal.banamex.com.mx/mapas/index.jsp?idioma=esp&xhost=http://www.banamex.com/' -H 'Connection: keep-alive' --data 'accion=sucuauto-porDom&estado=" . $estado ."&idcd=&iddel=&nomsuc=&numsuc=&loc=&calle=&colonia=&calle1=&calle2=&cp=&plaza=&servicio=&dias=&horario=&tipoBus=100&idioma=esp' --compressed";
    shell_exec($curl_cmd);
}

print "Listo, checa los archivines".PHP_EOL;
