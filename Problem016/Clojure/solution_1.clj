(defn solution
  []
  (->>
   (repeat 1000 2)
   (reduce *')
   (str)
   (seq)
   (map #(Character/digit % 10))
   (reduce +)))

(println (solution))
