(defn solution
  []
  (->>
   (for [x (range 100 1000) y (range 100 1000)
         :let [p (* x y)]
         :when (= (reverse (str p)) (seq (str p)))] p)
   (apply max)))
