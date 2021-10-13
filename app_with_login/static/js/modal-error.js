(function addEventCloseError(){
	const errorElement = document.querySelector('.error-container');
	const buttonCloseError = document.querySelector('.error-close');
	
	buttonCloseError.addEventListener('click', _ => {
		errorElement.remove();
	})
})();