library(DiagrammeR)
x <- grViz("
      digraph {
      layout = twopi
      node [shape = circle]
      A -> {B C D} 
      }")
print(x)