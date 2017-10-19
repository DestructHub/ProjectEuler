fun main(args: Array<String>) {
  val seq = (1..999)
            .asSequence()
            .filter { it % 3 == 0 || it % 5 == 0 }
            .sum()
  println(seq)
}
