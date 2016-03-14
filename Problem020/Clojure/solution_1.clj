;Author: tkovs

(defn sum [x]
    (apply + (map #(Integer. (str %)) (str x))))

(defn solve []
    (sum (reduce *' (range 1 100))))

(println(solve))