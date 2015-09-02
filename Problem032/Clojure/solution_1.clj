(def xs (for [ x (range 1 (inc 9999))
               y (range 1 (inc 99))
               :let [xy (* x y)]
               :when (= "123456789" (apply str(sort (str x y xy))))
             ] xy))
           
(reduce + (distinct xs))
