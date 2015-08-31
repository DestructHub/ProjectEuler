;; Author: G4BB3R

(def fib (cons 0 (cons 1 (lazy-seq (map + fib (rest fib))))))

(def resultado
    (reduce + 0 (filter #(== 0 (rem %1 2)) (take-while (fn [a] (<= a 4000000)) fib))))

(println resultado)
