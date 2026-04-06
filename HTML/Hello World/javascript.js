

// Wrap every letter in a span
var textWrapper = document.querySelector('.ml13');
textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");



anime.timeline({loop: true})
  .add({
    targets: '.ml13 .letter',
    translateY: [3,3],
    translateX: [3,0],	
    translateZ: 0,
    opacity: [1,1],
    easing: "easeOutExpo",
    duration: 5,
    delay: (el, i) => 1 + 1 * i
  }).add({
    targets: '.ml13 .letter',
    translateY: [-3,-3],
    translateX: [0,-3],
    opacity: [1,1],
    easing: "easeInExpo",
    duration: 5,
    delay: (el, i) => 1 + 1 * i
  });
  
  
