<?php
ini_set('memory_limit', '-1');
$json_sucursales = file_get_contents('2.json');
$sucursales = json_decode($json_sucursales);
# Limpiando
$scrapped_sucursales = $sucursales->d;
# var_dump($scrapped_sucursales);
$sucursales = array();
foreach($scrapped_sucursales as $scrappped_sucursal) {
	$sucursal = array();
	$sucursal['nombre'] = $scrappped_sucursal->Nombre;
	$sucursal['lat'] = $scrappped_sucursal->Latitud;
	$sucursal['lon'] = $scrappped_sucursal->Longitud;
	$campos = $scrappped_sucursal->Campos;
	$sucursal['domicilio'] = $campos[6]->Valor;
	$sucursal['categoria'] = $campos[4]->Valor;
	$sucursal['calle'] = $campos[7]->Valor;
	$sucursal['num_ext'] = $campos[8]->Valor;
	$sucursal['colonia'] = $campos[35]->Valor;
	$sucursal['cp'] = $campos[9]->Valor;
	$sucursal['ciudad'] = $campos[12]->Valor;
	$sucursal['estado'] = $campos[28]->Valor;
	$sucursal['id_estado'] = $campos[27]->Valor;
	$sucursal['id_municipio'] = $campos[30]->Valor;
	$sucursal['id_localidad'] = $campos[32]->Valor;
	$sucursal['id_colonia'] = $campos[34]->Valor;
	$sucursales[] = $sucursal;
}
file_put_contents('2_.json', json_encode($sucursales));

        echo '<pre>';
        var_dump($sucursales);
        echo '</pre>';
?>
