import gleam/io
import gleam/string

pub fn main() {
  let x = string.uppercase(string.capitalise("hello world"))
  io.println(x)
}