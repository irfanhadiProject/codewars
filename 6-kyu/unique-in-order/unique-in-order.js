var uniqueInOrder=function(iterable){
  //your code here - remember iterable can be a string or an array
  const unique = []
  for (let i = 0; i < iterable.length; i++) {
    if (i == 0 || iterable[i] != iterable[i - 1]) {
      unique.push(iterable[i])
    }
  }
  return unique
}