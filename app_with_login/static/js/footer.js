(function createFooterText(){
	const today = new Date();
	const year = today.getFullYear();
	const footerTextElement = document.querySelector('.footer-text');
	footerTextElement.innerHTML = `Francisco Charles ©️ <b>${year}</b>`
})();