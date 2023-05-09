-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2023-05-08 10:27:39
-- 伺服器版本： 10.4.21-MariaDB
-- PHP 版本： 8.0.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫: `mid_courseselectsystem`
--

-- --------------------------------------------------------

--
-- 資料表結構 `db_course`
--

CREATE TABLE `db_course` (
  `"選課代號"` int(4) NOT NULL,
  `"課程名稱"` varchar(14) DEFAULT NULL,
  `"開課班級"` varchar(8) DEFAULT NULL,
  `"開課科系"` varchar(6) DEFAULT NULL,
  `"開課年級"` varchar(6) DEFAULT NULL,
  `"學分數"` int(1) DEFAULT NULL,
  `"必選修"` varchar(1) DEFAULT NULL,
  `"開課單位"` varchar(6) DEFAULT NULL,
  `"開課人數"` int(2) DEFAULT NULL,
  `"已收授人數"` int(3) DEFAULT NULL,
  `"授課教師"` varchar(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `db_course`
--

INSERT INTO `db_course` (`"選課代號"`, `"課程名稱"`, `"開課班級"`, `"開課科系"`, `"開課年級"`, `"學分數"`, `"必選修"`, `"開課單位"`, `"開課人數"`, `"已收授人數"`, `"授課教師"`) VALUES
(1309, '機率論', '資訊二丙', '資訊', '二', 3, 'M', '資訊工程學系', 54, 52, '游景盛'),
(1310, '系統分析與設計', '資訊二甲', '資訊', '二', 3, 'O', '資訊工程學系', 80, 0, '蔡明翰'),
(1311, '互連網路', '資訊二甲', '資訊', '二', 3, 'O', '資訊工程學系', 70, 0, '劉宗杰'),
(1312, '多媒體系統', '資訊二甲', '資訊', '二', 3, 'O', '資訊工程學系', 70, 0, '葉春秀'),
(1313, '資訊與網路安全', '資訊二甲', '資訊', '二', 3, 'O', '資訊工程學系', 75, 0, '劉宗杰'),
(1314, 'UNIX應用與實務', '資訊二甲', '資訊', '二', 2, 'O', '資訊工程學系', 73, 0, '竇其仁'),
(1315, '系統程式', '資訊二丙', '資訊', '二', 3, 'M', '資訊工程學系', 54, 52, '黃志銘'),
(1316, '資料庫系統', '資訊二丙', '資訊', '二', 3, 'M', '資訊工程學系', 54, 52, '林明言'),
(1317, '班級活動', '資訊二丁', '資訊', '二', 0, 'M', '資訊工程學系', 60, 60, '林哲維'),
(1318, '系統程式', '資訊二丁', '資訊', '二', 3, 'M', '資訊工程學系', 60, 60, '劉宗杰'),
(1319, '資料庫系統', '資訊二丁', '資訊', '二', 3, 'M', '資訊工程學系', 60, 60, '許懷中'),
(1320, '機率與統計', '資訊二丁', '資訊', '二', 3, 'M', '資訊工程學系', 60, 60, '劉怡芬'),
(1321, '系統分析與設計', '資訊二丙', '資訊', '二', 3, 'O', '資訊工程學系', 85, 0, '洪振偉'),
(1322, '電子商務安全', '資訊二丙', '資訊', '二', 3, 'O', '資訊工程學系', 85, 0, '周澤捷'),
(1325, 'UNIX應用與實務', '資訊二甲', '資訊', '二', 2, 'O', '資訊工程學系', 60, 0, '劉明機'),
(1328, '組合數學', '資訊二甲', '資訊', '二', 3, 'O', '資訊工程學系', 85, 85, '游景盛'),
(1329, '電子商務安全', '資訊二甲', '資訊', '二', 3, 'O', '資訊工程學系', 85, 0, '魏國瑞'),
(1346, '文獻研討(二)', '資訊碩一', '資訊', '碩一', 1, 'M', '資訊工程學系', 40, 30, '林志敏'),
(1347, '文獻研討(二)', '資訊碩一', '資訊', '碩一', 1, 'M', '資訊工程學系', 30, 30, '楊濬中'),
(1348, '資訊專題研討(二)', '資訊碩一', '資訊', '碩一', 1, 'M', '資訊工程學系', 50, 30, '薛念林'),
(1349, '具體數學', '資訊碩一', '資訊', '碩一', 3, 'O', '資訊工程學系', 35, 0, '黃秀芬'),
(1350, '型樣識別', '資訊碩一', '資訊', '碩一', 3, 'O', '資訊工程學系', 30, 0, '劉怡芬'),
(1351, '研究報告寫作', '資訊碩一', '資訊', '碩一', 2, 'O', '資訊工程學系', 30, 0, '劉明機'),
(1352, '計算機視覺', '資訊碩一', '資訊', '碩一', 3, 'O', '資訊工程學系', 35, 0, '蔡明翰'),
(1353, '雲端計算', '資訊碩一', '資訊', '碩一', 3, 'O', '資訊工程學系', 30, 0, '林佩君'),
(1354, '無線隨意與感測網路技術與應用', '資訊碩一', '資訊', '碩一', 3, 'O', '資訊工程學系', 35, 0, '陳烈武'),
(1355, '知識管理與創新', '資訊碩一', '資訊', '碩一', 3, 'O', '資訊工程學系', 35, 0, '劉明機'),
(1356, '資料探勘', '資訊碩一', '資訊', '碩一', 3, 'O', '資訊工程學系', 35, 0, '林明言'),
(2134, '會計學(二)', '企管一乙', '企管', '一', 3, 'M', '企業管理學系', 80, 60, '施念恕'),
(2135, '會計學(二)實習', '企管一乙', '企管', '一', 0, 'M', '企業管理學系', 80, 60, '張巧旻'),
(2136, '經濟學(二)', '企管一乙', '企管', '一', 3, 'M', '企業管理學系', 84, 60, '陳依依'),
(2137, '經濟學(二)實習', '企管一乙', '企管', '一', 1, 'M', '企業管理學系', 84, 60, '范瑋庭'),
(2138, '管理學', '企管一乙', '企管', '一', 3, 'M', '企業管理學系', 80, 60, '張秀樺'),
(2139, '資訊網路', '企管一乙', '企管', '一', 2, 'M', '企業管理學系', 60, 60, '劉冠良'),
(2148, '商業規劃', '企管一乙', '企管', '一', 2, 'O', '企業管理學系', 60, 0, '王淑娟'),
(2149, '管理與統計', '企管一乙', '企管', '一', 3, 'O', '企業管理學系', 60, 0, '黃鼎翔'),
(2912, '電影與性別', '通識－人文(H)', '通識', '人文(H)', 2, 'O', '通識核心課程', 78, 0, '余國強'),
(2919, '生命科學', '通識－自然(N)', '通識', '自然(N)', 2, 'O', '通識核心課程', 80, 0, '葉怡巖'),
(2964, '服務學習專題', '通識－社會(S)', '通識', '社會(S)', 2, 'O', '通識核心課程', 80, 0, '宋懷德'),
(2983, '智慧綠台灣', '通識－統合(M)', '通識', '統合(M)', 2, 'O', '通識核心課程', 40, 0, '趙又嬋'),
(3011, '從人類學看世界', '通識－統合(M)', '通識', '統合(M)', 2, 'O', '通識核心課程', 30, 0, '陳玉苹');

-- --------------------------------------------------------

--
-- 資料表結構 `db_courseselected`
--

CREATE TABLE `db_courseselected` (
  `"學生姓名 "` varchar(7) DEFAULT NULL,
  `"學生學號"` varchar(8) NOT NULL,
  `"學生班級"` varchar(6) DEFAULT NULL,
  `"已選課程代碼"` int(4) NOT NULL,
  `"學分數"` int(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `db_courseselected`
--

INSERT INTO `db_courseselected` (`"學生姓名 "`, `"學生學號"`, `"學生班級"`, `"已選課程代碼"`, `"學分數"`) VALUES
('劉哈咂', 'D070003', '資訊碩一', 1346, 1),
('劉哈咂', 'D070003', '資訊碩一', 1347, 1),
('劉哈咂', 'D070003', '資訊碩一', 1348, 1),
('陳吧啦', 'D1060001', '資訊二丁', 1317, 0),
('陳吧啦', 'D1060001', '資訊二丁', 1318, 3),
('陳吧啦', 'D1060001', '資訊二丁', 1319, 3),
('陳吧啦', 'D1060001', '資訊二丁', 1320, 3),
('吳嘎搭', 'D1060002', '企管一乙', 2134, 3),
('吳嘎搭', 'D1060002', '企管一乙', 2135, 0),
('吳嘎搭', 'D1060002', '企管一乙', 2136, 3),
('吳嘎搭', 'D1060002', '企管一乙', 2137, 1),
('吳嘎搭', 'D1060002', '企管一乙', 2138, 3),
('吳嘎搭', 'D1060002', '企管一乙', 2139, 2);

-- --------------------------------------------------------

--
-- 資料表結構 `db_coursetime`
--

CREATE TABLE `db_coursetime` (
  `"選課代號"` int(4) NOT NULL,
  `"授課教室"` varchar(7) DEFAULT NULL,
  `"課程星期` varchar(5) NOT NULL,
  `"課程開始節次"` int(1) NOT NULL,
  `"課程結束節次"` int(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `db_coursetime`
--

INSERT INTO `db_coursetime` (`"選課代號"`, `"授課教室"`, `"課程星期`, `"課程開始節次"`, `"課程結束節次"`) VALUES
(1309, '資電205', '一', 1, 2),
(1309, '資電248', '一', 7, 7),
(1310, '資電403', '一', 3, 4),
(1310, '資電306', '四', 2, 2),
(1311, '資電234', '三', 6, 8),
(1312, '資電234', '二', 6, 8),
(1313, '資電306', '三', 4, 4),
(1313, '資電103', '四', 2, 3),
(1314, '資電234', '三', 9, 10),
(1315, '資電104', '一', 3, 4),
(1315, '資電104', '二', 4, 4),
(1316, '資電402', '三', 6, 6),
(1316, '資電504', '五', 1, 2),
(1317, '資電512', '四', 6, 6),
(1318, '資電306', '一', 3, 4),
(1318, '資電103', '四', 4, 4),
(1319, '資電402', '一', 6, 6),
(1319, '資電504', '二', 3, 4),
(1320, '資電404', '一', 7, 7),
(1320, '資電404', '四', 7, 8),
(1321, '資點403', '一', 3, 4),
(1321, '資電306', '四', 2, 2),
(1322, '資電404', '三', 11, 13),
(1325, '資電234', '四', 9, 10),
(1328, '資電403', '二', 9, 10),
(1329, '資電102', '一', 11, 13),
(1346, '資電518', '一', 9, 10),
(1347, '資電311', '五', 9, 10),
(1348, '資電403', '二', 7, 8),
(1349, '資電102', '一', 1, 2),
(1349, '資電102', '三', 1, 1),
(1350, '資電404', '四', 3, 4),
(1351, '資電204', '三', 5, 5),
(1352, '資電403', '二', 11, 13),
(1353, '資電102', '三', 8, 9),
(1354, '資電404', '一', 7, 7),
(1355, '資電234', '五', 3, 4),
(1356, '資電403', '五', 6, 6),
(2134, '商308', '一', 11, 13),
(2135, '體124', '一', 2, 4),
(2136, '忠B03', '二', 6, 6),
(2137, '商302', '三', 8, 9),
(2138, '商309', '五', 11, 13),
(2139, '商311', '五', 2, 4),
(2148, '科行204', '二', 1, 2),
(2149, '行206', '三', 11, 13),
(2912, '人407', '一', 1, 2),
(2919, '行政二館205', '三', 6, 7),
(2964, '男舍B11', '一', 6, 7),
(2983, '人B117A', '二', 3, 4),
(3011, '人708', '二', 3, 4);

-- --------------------------------------------------------

--
-- 資料表結構 `db_students`
--

CREATE TABLE `db_students` (
  `"學生姓名"` varchar(6) DEFAULT NULL,
  `"學生學號"` varchar(8) NOT NULL,
  `"學生班級"` varchar(6) DEFAULT NULL,
  `"已選學分"` varchar(6) DEFAULT NULL,
  `"密碼"` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `db_students`
--

INSERT INTO `db_students` (`"學生姓名"`, `"學生學號"`, `"學生班級"`, `"已選學分"`, `"密碼"`) VALUES
('劉哈咂 ', 'D0760003', '資訊碩一', '3', 'test3'),
('陳吧啦', 'D1060001', '資訊二丁', '9', 'test1'),
('吳嘎搭', 'D1060002', '企管一乙', '10', 'test2');

-- --------------------------------------------------------

--
-- 資料表結構 `db_studentsfocus`
--

CREATE TABLE `db_studentsfocus` (
  `"學生姓名 "` varchar(7) DEFAULT NULL,
  `"學生學號"` varchar(8) NOT NULL,
  `"學生班級"` varchar(6) DEFAULT NULL,
  `"已關注課程代碼"` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `db_studentsfocus`
--

INSERT INTO `db_studentsfocus` (`"學生姓名 "`, `"學生學號"`, `"學生班級"`, `"已關注課程代碼"`) VALUES
('劉哈咂', 'D070003', '資訊碩一', 1346),
('劉哈咂', 'D070003', '資訊碩一', 1347),
('陳吧啦', 'D1060001', '資訊二丁', 1317),
('陳吧啦', 'D1060001', '資訊二丁', 1320),
('吳嘎搭', 'D1060002', '企管一乙', 2134),
('吳嘎搭', 'D1060002', '企管一乙', 2139);

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `db_course`
--
ALTER TABLE `db_course`
  ADD PRIMARY KEY (`"選課代號"`);

--
-- 資料表索引 `db_courseselected`
--
ALTER TABLE `db_courseselected`
  ADD PRIMARY KEY (`"學生學號"`,`"已選課程代碼"`);

--
-- 資料表索引 `db_coursetime`
--
ALTER TABLE `db_coursetime`
  ADD PRIMARY KEY (`"選課代號"`,`"課程星期`,`"課程開始節次"`);

--
-- 資料表索引 `db_students`
--
ALTER TABLE `db_students`
  ADD PRIMARY KEY (`"學生學號"`);

--
-- 資料表索引 `db_studentsfocus`
--
ALTER TABLE `db_studentsfocus`
  ADD PRIMARY KEY (`"學生學號"`,`"已關注課程代碼"`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;