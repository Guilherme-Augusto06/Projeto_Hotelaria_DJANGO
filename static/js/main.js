$(".custom-carousel").owlCarousel({
	autoWidth: true,
	loop: true
  });
  $(document).ready(function () {
	$(".custom-carousel .item").click(function () {
	  $(".custom-carousel .item").not($(this)).removeClass("active");
	  $(this).toggleClass("active");
	});
  });
	  


  // Capturar a URL da imagem
var imagemUrl = document.querySelector('#comprasContainer img').getAttribute('src');

// Definir a imagem como fundo do contêiner
document.getElementById('comprasContainer').style.backgroundImage = 'url(' + imagemUrl + ')';
