;Author: tkovs

(defn solve []
    (let [sum_square (reduce +' (map (fn [x] (* x x)) (range 1 101)))
          square_sum (* (reduce +' (range 1 101)) (reduce +' (range 1 101)))]
            (- square_sum sum_square)))

(println(solve))