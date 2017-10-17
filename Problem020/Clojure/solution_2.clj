;; very very VERY slow solution: take 1min to finish. (hahaha)

(defn solution
  []
  (->> (range 1 100)
       (reduce *')
       (str)
       (seq)
       (pmap #(Character/getNumericValue %))
       (reduce +)
       (str)))

(println (solution))
;; weird bug here: if I don't force exit, the process continue about 1min
;; without need. Clojure 1.8.0 here. Need report bug?
(System/exit 0)
