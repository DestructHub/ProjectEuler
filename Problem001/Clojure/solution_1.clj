;; My first code in Clojure
;; Manoel Vilela

;; return true if number is divisible by 5 or 3
(defn mod35 [n]
  (=
    (or
      ( = (mod n 5) 0)
      ( = (mod n 3) 0)
    )
    true
  )
)

;; summation of n numbers of a list
(defn sum [numbers-list]
  (reduce + numbers-list)
)

;; solution of problem1
(defn solution [x]
  (sum
    (filter mod35 (range 1 x))
  )
)

(solution 1000)
