def f(delim:Int,arr:List[Int]):List[Int] = for(e <- arr if e<delim) yield e