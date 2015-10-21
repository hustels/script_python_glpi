
--
-- Base de datos: `compras`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ordenadores`
--

CREATE TABLE `ordenadores` (
  `id` int(11) NOT NULL,
  `peticionario` varchar(60) NOT NULL,
  `num_serie` varchar(60) NOT NULL,
  `fecha_compra` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `ordenadores`
--

INSERT INTO `ordenadores` (`id`, `peticionario`, `num_serie`, `fecha_compra`) VALUES
(1, 'JUAN FRANCISCO NAVARRO DE LA CRUZ', '853H8W1', '2013-01-03'),
(2, 'MARTA MARJALIZO TERUEL', '114H8W1', '2013-01-03'),
(4, 'MARIA PILAR SANZ PARDO', 'DZ3H8W1', '2013-01-03'),
(5, 'MONICA VILLARES SOUTO', 'D57H8W1', '2013-01-08'),
(6, 'CAYETANA BULNES DELGADO ', '497H8W1', '2013-01-16'),
(7, 'GUILLERMO PALMA CARRILLO ', '3F3H8W1', '2013-01-25'),
(8, 'GUILLERMO PALMA CARRILLO ', '4D3H8W1', '2013-01-25'),
(10, 'JUAN LUIS MARTINEZ', '994H8W1', '2013-02-06');
