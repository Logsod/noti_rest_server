-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.26 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for cartridges
CREATE DATABASE IF NOT EXISTS `cartridges` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `cartridges`;

-- Dumping structure for table cartridges.base_state
CREATE TABLE IF NOT EXISTS `base_state` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cartridge_id` int DEFAULT '0',
  `amount` int DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb3;

-- Dumping data for table cartridges.base_state: ~4 rows (approximately)
DELETE FROM `base_state`;
/*!40000 ALTER TABLE `base_state` DISABLE KEYS */;
INSERT INTO `base_state` (`id`, `cartridge_id`, `amount`) VALUES
	(17, 25, 10),
	(18, 26, 45),
	(22, 28, 0),
	(23, 29, 11),
	(28, 33, 25);
/*!40000 ALTER TABLE `base_state` ENABLE KEYS */;

-- Dumping structure for table cartridges.cartridge_dep
CREATE TABLE IF NOT EXISTS `cartridge_dep` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cartridge_id` int DEFAULT '0',
  `printer_id` int DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=167 DEFAULT CHARSET=utf8mb3;

-- Dumping data for table cartridges.cartridge_dep: ~35 rows (approximately)
DELETE FROM `cartridge_dep`;
/*!40000 ALTER TABLE `cartridge_dep` DISABLE KEYS */;
INSERT INTO `cartridge_dep` (`id`, `cartridge_id`, `printer_id`) VALUES
	(132, 26, 13),
	(133, 26, 14),
	(134, 27, 13),
	(135, 28, 15),
	(136, 28, 16),
	(137, 28, 43),
	(138, 29, 18),
	(139, 29, 19),
	(140, 29, 20),
	(141, 30, 21),
	(142, 31, 21),
	(143, 32, 22),
	(144, 32, 23),
	(145, 32, 24),
	(146, 33, 25),
	(147, 33, 26),
	(148, 33, 27),
	(149, 33, 28),
	(150, 34, 29),
	(151, 35, 29),
	(152, 36, 29),
	(153, 37, 29),
	(154, 38, 30),
	(155, 39, 34),
	(156, 40, 35),
	(157, 41, 36),
	(158, 42, 37),
	(159, 43, 38),
	(160, 44, 39),
	(161, 45, 38),
	(162, 46, 40),
	(163, 47, 44),
	(164, 48, 44),
	(165, 49, 44),
	(166, 50, 44);
/*!40000 ALTER TABLE `cartridge_dep` ENABLE KEYS */;

-- Dumping structure for table cartridges.cartridge_model
CREATE TABLE IF NOT EXISTS `cartridge_model` (
  `id` int NOT NULL AUTO_INCREMENT,
  `model` char(255) DEFAULT NULL,
  `depString` text,
  KEY `Index 1` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb3;

-- Dumping data for table cartridges.cartridge_model: ~25 rows (approximately)
DELETE FROM `cartridge_model`;
/*!40000 ALTER TABLE `cartridge_model` DISABLE KEYS */;
INSERT INTO `cartridge_model` (`id`, `model`, `depString`) VALUES
	(26, '505A', 'Canon i-SENSYS MF411dw\nHP LaserJet P2035'),
	(27, 'Canon 719', 'Canon i-SENSYS MF411dw'),
	(28, '35A / 85A / 725', 'Canon i-SENSYS LBP6020\nCanon i-SENSYS LBP6030\nCanon i-SENSYS LBP6000'),
	(29, '728 / 78A / 278', 'Canon i-SENSYS MF4430\nCanon i-SENSYS MF4450\nCanon i-SENSYS MF4580dn'),
	(30, 'Xerox B215 (106R04348)', 'XEROX WorkCentre B215DNI'),
	(31, 'Xerox B215 Drum (101R00664)', 'XEROX WorkCentre B215DNI'),
	(32, 'ML-1610', 'Samsung ML-1610\nSamsung ML-2510\nSamsung ML-2015'),
	(33, '12A / 703', 'Canon LBP2900\nHP LaserJet M1319f\nHP LaserJet 1018\nHP LaserJet 1010'),
	(34, 'Cartridge 054 C', 'Canon i-SENSYS MF645Cx'),
	(35, 'Cartridge 054 M', 'Canon i-SENSYS MF645Cx'),
	(36, 'Cartridge 054 Y', 'Canon i-SENSYS MF645Cx'),
	(37, 'Cartridge 054 K', 'Canon i-SENSYS MF645Cx'),
	(38, '283 / 737', 'Canon i-SENSYS MF216n'),
	(39, 'Туба 1230D / MP 2000', 'Richo MB 9118D'),
	(40, 'TK-3160', 'Kyocera ECOSYS P3045dn'),
	(41, 'TK-1140', 'kyocera fs-1035mfp'),
	(42, 'Ricoh MP 2014', 'Ricoh M 2701'),
	(43, 'Ricoh SP330L', 'Ricoh SP 330SN'),
	(44, 'ML-1710D3', 'Samsung ML 1710'),
	(45, 'Richo sp330', 'Ricoh SP 330SN'),
	(46, 'ML-1210', 'Samsung ML 1210'),
	(47, 'Canon 729 C', 'Samsung LBP7010C'),
	(48, 'Canon 729 M', 'Samsung LBP7010C'),
	(49, 'Canon 729 Y', 'Samsung LBP7010C'),
	(50, 'Canon 729 Bk', 'Samsung LBP7010C');
/*!40000 ALTER TABLE `cartridge_model` ENABLE KEYS */;

-- Dumping structure for table cartridges.cartridge_state
CREATE TABLE IF NOT EXISTS `cartridge_state` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cartridge_id` int DEFAULT NULL,
  `state` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=168 DEFAULT CHARSET=utf8mb3;

-- Dumping data for table cartridges.cartridge_state: ~134 rows (approximately)
DELETE FROM `cartridge_state`;
/*!40000 ALTER TABLE `cartridge_state` DISABLE KEYS */;
INSERT INTO `cartridge_state` (`id`, `cartridge_id`, `state`) VALUES
	(11, 0, 1),
	(17, 14, 1),
	(19, 0, 1),
	(24, 0, 1),
	(25, 0, 1),
	(26, 25, 2),
	(27, 26, 3),
	(28, 26, 3),
	(29, 26, 3),
	(30, 26, 3),
	(31, 26, 3),
	(32, 26, 3),
	(33, 26, 3),
	(34, 26, 3),
	(35, 26, 3),
	(36, 26, 3),
	(37, 26, 3),
	(38, 26, 3),
	(39, 26, 3),
	(44, 26, 4),
	(45, 26, 4),
	(46, 26, 4),
	(47, 26, 4),
	(48, 26, 4),
	(49, 26, 4),
	(50, 26, 4),
	(51, 26, 4),
	(52, 26, 4),
	(53, 26, 4),
	(54, 26, 4),
	(55, 26, 4),
	(56, 26, 4),
	(57, 26, 4),
	(58, 26, 4),
	(59, 26, 4),
	(60, 26, 4),
	(61, 26, 4),
	(62, 26, 4),
	(63, 26, 4),
	(65, 27, 4),
	(66, 27, 4),
	(67, 27, 4),
	(68, 27, 4),
	(69, 28, 4),
	(70, 28, 4),
	(71, 28, 4),
	(72, 28, 4),
	(73, 28, 4),
	(74, 28, 4),
	(75, 28, 4),
	(76, 28, 3),
	(77, 28, 3),
	(78, 28, 3),
	(79, 28, 3),
	(80, 28, 3),
	(81, 28, 3),
	(82, 28, 3),
	(83, 28, 4),
	(84, 28, 4),
	(85, 28, 4),
	(86, 28, 4),
	(87, 28, 4),
	(88, 28, 4),
	(89, 28, 4),
	(90, 28, 4),
	(91, 28, 4),
	(92, 28, 4),
	(93, 28, 4),
	(94, 28, 4),
	(95, 28, 4),
	(96, 28, 4),
	(97, 28, 4),
	(98, 28, 4),
	(99, 28, 4),
	(100, 28, 4),
	(101, 28, 4),
	(102, 28, 4),
	(103, 28, 4),
	(104, 28, 4),
	(105, 28, 4),
	(106, 28, 4),
	(107, 28, 4),
	(108, 28, 4),
	(109, 28, 4),
	(110, 28, 4),
	(111, 28, 4),
	(112, 28, 4),
	(113, 28, 3),
	(114, 28, 3),
	(115, 28, 3),
	(116, 28, 3),
	(117, 28, 3),
	(118, 28, 3),
	(119, 28, 3),
	(120, 28, 3),
	(121, 28, 3),
	(122, 28, 3),
	(123, 28, 3),
	(124, 28, 3),
	(125, 28, 3),
	(126, 28, 3),
	(127, 28, 3),
	(128, 28, 3),
	(129, 28, 3),
	(130, 28, 3),
	(131, 28, 3),
	(132, 28, 3),
	(133, 28, 3),
	(134, 28, 3),
	(135, 28, 3),
	(136, 28, 3),
	(137, 28, 3),
	(138, 28, 3),
	(139, 28, 3),
	(140, 28, 3),
	(141, 28, 3),
	(142, 28, 3),
	(143, 29, 4),
	(144, 29, 2),
	(145, 29, 3),
	(146, 29, 3),
	(147, 29, 3),
	(148, 29, 3),
	(149, 29, 3),
	(150, 29, 3),
	(151, 29, 3),
	(152, 29, 3),
	(153, 29, 3),
	(154, 29, 3),
	(155, 29, 3),
	(156, 29, 3),
	(157, 29, 3),
	(158, 26, 3),
	(159, 26, 2),
	(160, 26, 2),
	(161, 26, 2),
	(162, 26, 1),
	(163, 29, 3),
	(164, 29, 1),
	(165, 29, 1),
	(166, 26, 3),
	(167, 29, 1);
/*!40000 ALTER TABLE `cartridge_state` ENABLE KEYS */;

-- Dumping structure for table cartridges.log
CREATE TABLE IF NOT EXISTS `log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action` text,
  `timestamp` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb3;

-- Dumping data for table cartridges.log: ~0 rows (approximately)
DELETE FROM `log`;
/*!40000 ALTER TABLE `log` DISABLE KEYS */;
INSERT INTO `log` (`id`, `action`, `timestamp`) VALUES
	(1, 'Взято картриджей', '2021-09-28 15:43:22'),
	(2, 'Взято картриджей:505A', '2021-09-28 15:53:34'),
	(3, 'Взято картриджей:728 / 78A / 278', '2021-09-28 15:54:12'),
	(4, 'Взято картриджей:2 модель:728 / 78A / 278', '2021-09-28 15:55:31'),
	(5, 'Взято картриджей:1 модель:505A', '2021-09-28 15:58:10'),
	(6, 'Взято картриджей:1 модель:728 / 78A / 278', '2021-09-28 15:58:10'),
	(7, 'Взято картриджей:4 модель:505A', '2021-09-28 15:58:43'),
	(8, 'Новое количество:3 модель:505A', '2021-09-28 15:59:13'),
	(9, 'Новое количество:11 модель:505A', '2021-09-28 15:59:26'),
	(10, 'Новое количество:11 модель:728 / 78A / 278', '2021-09-28 15:59:26'),
	(11, 'Запись была удалена: модель:ML-1610', '2021-09-28 16:02:18'),
	(12, 'Запись была удалена: модель:ML-1610', '2021-09-28 16:02:48'),
	(13, 'Запись была удалена: модель:12A / 703', '2021-09-28 16:02:48'),
	(14, 'Добавлено:1 модель:505A', '2021-09-28 16:04:43'),
	(15, 'Добавлено:31 модель:505A', '2021-09-28 16:04:55'),
	(16, 'Добавлено:1 модель:505A', '2021-09-28 16:05:09'),
	(17, 'Добавлено:23 модель:12A / 703', '2021-09-28 16:08:20'),
	(18, 'Добавлено:2 модель:12A / 703', '2021-09-28 16:08:31'),
	(19, 'Картридж:159 Ожидание Изменен наОжидание', '2021-09-28 16:20:35'),
	(20, 'Картридж:160 Ожидание Изменен на Ожидание', '2021-09-28 16:21:13'),
	(21, 'Картридж:161 Работа Изменен на Ожидание', '2021-09-28 16:21:50'),
	(22, 'Картридж:166 Работа Изменен на Заправка', '2021-09-28 16:22:06'),
	(23, 'Картридж:163 Работа Изменен на Заправка', '2021-09-28 16:22:06'),
	(24, 'Картридж:27 Ожидание Изменен на Заправка', '2021-09-28 16:22:22'),
	(25, 'Картридж:30 Ожидание Изменен на Заправка', '2021-09-28 16:22:22'),
	(26, 'Картридж:158 Ожидание Изменен на Заправка', '2021-09-28 16:22:22');
/*!40000 ALTER TABLE `log` ENABLE KEYS */;

-- Dumping structure for table cartridges.printer
CREATE TABLE IF NOT EXISTS `printer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `model_id` int DEFAULT '0',
  `comment` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb3;

-- Dumping data for table cartridges.printer: ~8 rows (approximately)
DELETE FROM `printer`;
/*!40000 ALTER TABLE `printer` DISABLE KEYS */;
INSERT INTO `printer` (`id`, `model_id`, `comment`) VALUES
	(26, 13, 'Юридический отдел'),
	(27, 13, 'Бухгалтерия Мат. отдел'),
	(28, 14, 'Морозова О.М.'),
	(29, 14, 'Луценко Н.И.'),
	(30, 14, 'Трипузова '),
	(31, 14, 'Бушева Е.В.'),
	(32, 14, 'Денисова С.И.'),
	(33, 14, 'Клишина Е.С.');
/*!40000 ALTER TABLE `printer` ENABLE KEYS */;

-- Dumping structure for table cartridges.printer_model
CREATE TABLE IF NOT EXISTS `printer_model` (
  `id` int NOT NULL AUTO_INCREMENT,
  `model` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb3;

-- Dumping data for table cartridges.printer_model: ~29 rows (approximately)
DELETE FROM `printer_model`;
/*!40000 ALTER TABLE `printer_model` DISABLE KEYS */;
INSERT INTO `printer_model` (`id`, `model`) VALUES
	(13, 'Canon i-SENSYS MF411dw'),
	(14, 'HP LaserJet P2035'),
	(15, 'Canon i-SENSYS LBP6020'),
	(16, 'Canon i-SENSYS LBP6030'),
	(17, 'HP LaserJet P1505'),
	(18, 'Canon i-SENSYS MF4430'),
	(19, 'Canon i-SENSYS MF4450'),
	(20, 'Canon i-SENSYS MF4580dn'),
	(21, 'XEROX WorkCentre B215DNI'),
	(22, 'Samsung ML-1610'),
	(23, 'Samsung ML-2510'),
	(24, 'Samsung ML-2015'),
	(25, 'Canon LBP2900'),
	(26, 'HP LaserJet M1319f'),
	(27, 'HP LaserJet 1018'),
	(28, 'HP LaserJet 1010'),
	(29, 'Canon i-SENSYS MF645Cx'),
	(30, 'Canon i-SENSYS MF216n'),
	(32, 'Xerox CopyCentre C118'),
	(33, 'Xerox Phaser 3160'),
	(34, 'Richo MB 9118D'),
	(35, 'Kyocera ECOSYS P3045dn'),
	(36, 'kyocera fs-1035mfp'),
	(37, 'Ricoh M 2701'),
	(38, 'Ricoh SP 330SN'),
	(39, 'Samsung ML 1710'),
	(40, 'Samsung ML 1210'),
	(43, 'Canon i-SENSYS LBP6000'),
	(44, 'Samsung LBP7010C');
/*!40000 ALTER TABLE `printer_model` ENABLE KEYS */;

-- Dumping structure for table cartridges.state
CREATE TABLE IF NOT EXISTS `state` (
  `id` int NOT NULL AUTO_INCREMENT,
  `state_name` varchar(255) DEFAULT NULL,
  KEY `Index 1` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;

-- Dumping data for table cartridges.state: ~4 rows (approximately)
DELETE FROM `state`;
/*!40000 ALTER TABLE `state` DISABLE KEYS */;
INSERT INTO `state` (`id`, `state_name`) VALUES
	(1, 'Работа'),
	(2, 'Ожидание'),
	(3, 'Заправка'),
	(4, 'Склад БУ');
/*!40000 ALTER TABLE `state` ENABLE KEYS */;

-- Dumping structure for table cartridges.test
CREATE TABLE IF NOT EXISTS `test` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` text NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;

-- Dumping data for table cartridges.test: ~0 rows (approximately)
DELETE FROM `test`;
/*!40000 ALTER TABLE `test` DISABLE KEYS */;
INSERT INTO `test` (`id`, `title`) VALUES
	(1, 'tittle');
/*!40000 ALTER TABLE `test` ENABLE KEYS */;

-- Dumping structure for table cartridges.tokens
CREATE TABLE IF NOT EXISTS `tokens` (
  `id` int NOT NULL AUTO_INCREMENT,
  `token` varchar(255) NOT NULL,
  `owner` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  FULLTEXT KEY `Index 2` (`token`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb3;

-- Dumping data for table cartridges.tokens: ~7 rows (approximately)
DELETE FROM `tokens`;
/*!40000 ALTER TABLE `tokens` DISABLE KEYS */;
INSERT INTO `tokens` (`id`, `token`, `owner`) VALUES
	(18, '2f7a3d06da104b1e98f1381fdf3dfcc7', 1),
	(24, '0730d2da05844748a388b6ca6a2806bb', 1),
	(25, '5f2e875ae1d2420690916c3bba34e3b8', 2),
	(26, '5f8adaf197144c1b9bd25a8116b6b236', 2),
	(27, '909deb3f6aca40edb19648b63ecfe526', 1),
	(28, 'b6eb842546ff46d980239d743954fea3', 2),
	(29, 'ca92da67289348d4ba83b3c87245ffc9', 1);
/*!40000 ALTER TABLE `tokens` ENABLE KEYS */;

-- Dumping structure for table cartridges.users
CREATE TABLE IF NOT EXISTS `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `login` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;

-- Dumping data for table cartridges.users: ~2 rows (approximately)
DELETE FROM `users`;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`id`, `login`, `password`) VALUES
	(1, 'test', 'test'),
	(2, 'user', 'user');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
