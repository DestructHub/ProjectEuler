(defn solution
  []
  (->> (range 1 100)
       (reduce *')
       (str)
       (seq)
       (map #(Character/getNumericValue %))
       (reduce +)
       (println))
