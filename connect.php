<!doctype html>
    <head>
        <title>SQL_injection</title>
    </head>
    <body>
        <h1>學生成績查詢系統</h1>

        <!-- 
            form：讓使用者輸入資料，並把結果傳給 PHP(或其他能與資料庫溝通的語言)，
            讓 PHP 用這筆資料跟資料庫做溝通。

            以下程式碼傳到 PHP 的變數會長這樣，$_POST["name"]
        -->
        <form method="POST">
            <p> 輸入姓名: <input type="text" name="name" ><br> </p>
            <p> <input type="submit" value="查詢"><br> </p>
        </form>

        <!-- 以下內嵌 PHP -->
        <?php
            //-------------------連接資料庫------------------------- 
            $host = 'localhost';
            $dbuser ='test';
            $port='3307';
            $dbpassword = 'test';
            $dbname = 'mid_courseselectsystem';

            $link = mysqli_connect($host,$dbuser,$dbpassword,$dbname,$port);

            //----------------------------------------------------- 

            if ($link) { // 如果連線成功

                //$_POST[""] 為從 form 傳入的值，引號內容為 form 設置的 name
                //以此程式碼為例就是 $_POST["name"]
                //isset 用來判斷此變數有無設置
                if(isset($_POST["name"])){ //如果已經設置此變數

//======================================== 以下為你需要動到的部分 ==========================================
                      
                    //把使用者輸入的資料存入變數 $targetName，也就是你要搜尋的學生名。
                    $targetName = $_POST["name"]; 

                    //========== 請補上 sql 語句 ===========
                    //我需要從 `students`.`score` 裡面找到 name = $targetName 時的 name 和 score
                    $sql = "SELECT `name`, `score` FROM `students`.`score` WHERE `name`= '$targetName' ";  
                    
//======================================== 以上為你需要動到的部分 ==========================================

                    //在目標資料庫執行 sql 語句的結果
                    $result = mysqli_query($link,$sql);

                    // 一個陣列，用於儲存返回值
                    $datas = []; 

                    if ($result) { //如果在目標資料庫執行 sql 語句成功

                        // mysqli_num_rows:回傳結果總共有幾筆資料
                        // 所以大於 0 代表有資料
                        if (mysqli_num_rows($result)>0) {

                            // mysqli_fetch_assoc:取得一筆值，型態為陣列
                            // PHP 裡陣列的 index 不一定要整數，可以是一個字串
                            // 假設輸入 JoJo，
                            // $row 為 $row[name] = JoJo，$row[score] = 87
                            // 所以 $datas 是一個儲存陣列的陣列 
                            while ($row = mysqli_fetch_assoc($result)) {
                                // 每跑一次迴圈抓一筆值，放進datas
                                $datas[] = $row;
                            }
                        }
                    }
                    else {
                        echo "{$sql} 語法執行失敗，錯誤訊息: " . mysqli_error($link);
                    }

                    //---------------------------- 處理完資料後印出 ----------------

                    if(!empty($datas)){// 如果資料不為空，就印出資料
                        
                        echo nl2br("\n查詢結果: \n");

                        // 把 $datas 的值存入 $value
                        // 因為 $datas 的值是陣列，所以 $value 也是陣列
                        // 前面說過 PHP 裡陣列的 index 不一定要整數，可以是一個字串
                        // 此時以字串表示
                        foreach ($datas as $value){
                            echo "Student: ";
                            echo $value['name'];
                            echo "'s score is ";
                            echo $value['score'];
                            echo nl2br("\n");
                        }   
                    }
                    else { // 為空表示沒資料
                        
                        echo nl2br("\n查無資料");
                    }                    
                    //------------------------------------------------------------- 

                    // 釋放資料庫查到的記憶體
                    mysqli_free_result($result);

                    // 關閉連線
                    mysqli_close($link);

                }    
            }
            else{ 
                echo mysqli_connect_error();
            }    
        ?>
    </body>
<!doctype html>



