
function x() {
  w = window.innerWidth
  console.log(w)
  if (w >= 1000) {
    document.getElementById('boxcontainer').width = w * 0.5
  }
  else {
    document.getElementById('boxcontainer').width = w * 0.8
  }
}
x()
