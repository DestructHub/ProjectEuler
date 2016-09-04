(defn solution
  []
  (->> (range 1 100)
       (reduce *')
       (str)
       (seq)
       (pmap #(Character/getNumericValue %))
       (reduce +)
       (str)))
