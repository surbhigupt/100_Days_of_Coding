import java.io._
import java.math._
import java.security._
import java.text._
import java.util._
import java.util.concurrent._
import java.util.function._
import java.util.regex._
import java.util.stream._

object Solution {



    def main(args: Array[String]) {
        val stdin = scala.io.StdIn

        val n = stdin.readLine.trim.toInt

        def f(x: Double): Double = {
            f2(x, 9)
        }

        def fact(x: Int): Int = if (x <= 1) 1 else x*fact(x-1)

        def f2(x: Double, i: Int): Double = {
            if(i==0) 1 else Math.pow(x, i) / fact(i) + f2(x, i-1)
        }

        for (nItr <- 1 to n) {
            val x = stdin.readLine.trim.toDouble
            println(f(x))
        }
    }
}
