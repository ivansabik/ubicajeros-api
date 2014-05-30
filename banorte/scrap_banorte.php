#!/usr/bin/php -q
<?php

# Para el curlin
$corresponsales = array(
    '7-ELEVEN',
    'DEL+SOL',
    'SORIANA',
    'TELECOMM-TELEGRAFOS',
    'TIENDAS-EXTRA',
    'WOOLWORTH'
    );
$estados = array(
    'AGUASCALIENTES',
    'BAJA+CALIFORNIA',
    'BAJA+CALIFORNIA+SUR',
    'CAMPECHE',
    'CHIAPAS',
    'CHIHUAHUA',
    'COAHUILA',
    'COLIMA',
    'DISTRITO+FEDERAL',
    'DURANGO',
    'ESTADO+DE+MEXICO',
    'GUANAJUATO',
    'GUERRERO',
    'HIDALGO',
    'JALISCO',
    'MICHOACAN',
    'MORELOS',
    'NAYARIT',
    'NUEVO+LEON',
    'OAXACA',
    'PUEBLA',
    'QUERETARO',
    'QUINTANA+ROO',
    'SAN+LUIS+POTOSI',
    'SINALOA',
    'SONORA',
    'TABASCO',
    'TAMAULIPAS',
    'TLAXCALA',
    'VERACRUZ',
    'YUCATAN',
    'ZACATECAS'
);
# El puro curleo
foreach ($estados as $estado) {
	# Cajeros
	$curl_cmd = "curl -o cajeros_" . $estado . ".htm 'http://www.banorte.com.mx/portal/personas/informacion.web?grupo=95&elemento=1825&isSubmission=true&state=" . $estado . "&city=&hasDollars=' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Connection: keep-alive' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Referer: http://www.banorte.com/portal/personas/informacion.web?grupo=95&elemento=1825' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36' --compressed";
    shell_exec($curl_cmd);
	# Sucursales
	$curl_cmd = "curl -o sucursales_" . $estado . ".htm 'http://www.banorte.com.mx/portal/personas/informacion.web?grupo=95&elemento=1825&isSubmission=true&state=" . $estado ."&city=&hasDollars=' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Connection: keep-alive' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Referer: http://www.banorte.com/portal/personas/informacion.web?grupo=95&elemento=1825' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36' --compressed";
    shell_exec($curl_cmd);
    # Corresponsales
    foreach($corresponsales as $corresponsal) {
        $curl_cmd = "curl -o corresponsales_" . $corresponsal ."_" . $estado . ".htm 'http://www.banorte.com/portal/personas/informacion.web?grupo=95&elemento=1826&isSubmission=true&type=" . $corresponsal . "&state=" . $estado . "&city=&street=&colony=&postalCode=&cr=' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Connection: keep-alive' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Referer: http://www.banorte.com.mx/portal/personas/informacion.web?grupo=95&elemento=1824&isSubmission=true&state=AGUASCALIENTES&city=&street=&colony=&postalCode=&cr=' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36' --compressed";
        shell_exec($curl_cmd);
    }
}

print "Listo, checa los archivines".PHP_EOL;
