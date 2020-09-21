'use strict';

import dom from './dom-pruebas.js';//clase estatica
import cText from './cifrado.js';//clase estatica

let prueba="";

((doc, win) => {
	doc.addEventListener('DOMContentLoaded',event => {
		let textArea=dom.getElemento("text");
		let clave=dom.getElemento("cla");
		textArea.value="Algoritmo de cifrado simétrico usando transposición en bloques, alteraciones y sustitución de caracteres Ascii.";
		
/* 		//3566480
		for (let index = 0; index < 1000000; index++) {
			prueba+=String.fromCharCode(aleatorio(32,255));
		}
 */
		textArea.value=prueba;
		dom.setEvento("enc","click",cb=>{
			textArea.value=cText.cifrar(clave.value,textArea.value);
		});

		dom.setEvento("denc","click",cb=>{
			textArea.value=cText.descifrar(clave.value,textArea.value);
		});

		let sleep=(milliseconds)=>{
			const date = Date.now();
			let currentDate = null;
			do {
				currentDate = Date.now();
			} while (currentDate - date < milliseconds);
		}
	});

	let aleatorio=(a=0,b=6)=>{
		return Math.round(Math.random()*(b-a)+parseInt(a));
	}
})(document, window);


