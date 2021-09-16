import System.IO
import Data.List.Split

-- ,を付与して文字列を結合
listToLine :: [String] -> String
listToLine = foldl1 (\acc x -> acc ++ "," ++ x)

-- 先頭に通し番号を付与
addIndex :: [String] -> [String]
addIndex = zipWith (\ a b -> show a ++ "," ++ b) [1..]

-- ",半角空白を削除
dropdQuotation :: [String] -> [String]
dropdQuotation = fmap (filter (/= '"') . filter (/= ' '))

main:: IO()
main = do
        handle <- openFile "/KEN_ALL.CSV" ReadMode
        contents <- hGetContents handle
        -- putStrLn contents
        let line = lines contents
        writeFile "/code/export/KEN_ALL_X.CSV" "No.,Oldcode,Headcode,ZIPcode,Prefectures_Kana,City_Kana,Address_Kana,Prefectures,City,Address\n"
        (appendFile "/code/export/KEN_ALL_X.CSV" . unlines) $ addIndex $ dropdQuotation $ fmap (listToLine . take 9 . splitOn "," ) line

        hClose handle
