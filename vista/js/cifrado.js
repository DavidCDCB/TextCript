'use strict';

export default class Cifrado{

	/**
	 * aplica de manera secuencial todos los procesos de cifrado
	 * @param {String} el valor de la clave 
	 * @param {String} el texto a cifrar 
	 */
	static cifrar(vlc,texto){
		let ch=[vlc.length],cadB="";
		ch=this.cadChar(vlc);
		
		for(let i in ch)
			cadB+=this.cadBin(ch[i]);

		if(vlc.length>0){
			let girado=this.opMatriz(texto,4,cadB);
			let trucado=this.Truncar(girado);
			let cifrado=this.nSutitucion(trucado,vlc,cadB,1);
			return cifrado.split("").reverse().join("");
		}else{
			return texto;
		}
	}

	static descifrar(vlc,texto){
		let ch=[vlc.length],cadB="";
		ch=this.cadChar(vlc);

		for(let i in ch)
			cadB+=this.cadBin(ch[i]);

		if(vlc.length>0){
			let cifrado=this.nSutitucion(texto.split("").reverse().join(""),vlc,cadB,2);
			let trucado=this.Truncar(cifrado);
			let girado=this.opMatriz(trucado,4,cadB);
			return girado;
		}else{
			return texto;
		}
	}

	/**
	 * Toma porsiones del texto y crea matrices de 4x4
	 * @param {String} texto ingredado 
	 * @param {String} arrc dimencion de la matriz por defecto 4
	 * @param {Array} lsita de binarios de la contraseña
	 */
	static opMatriz(text,arrc=4,ab) {
		let ind = 0,nR=0;
		let m=new Array(arrc);
		let textR=new Array(text.length);
		let size = text.length;
		let cadR,resultado=text,progreso=-1;

		let mt=new Array(arrc);
		let mt1=new Array(arrc);
		let mt2=new Array(arrc);
		let mt3=new Array(arrc);

		for(let i of ab.split("")){
			if(i=="1")nR++;
		}

		//si el tamaño de la matriz en mayor que el texto
		if((arrc*arrc)<text.length){

			for(let i = 0; i < text.length; i++)
				textR[i]=text[i];
			
			for(let i = 0; i < m.length; i++)
				m[i]=new Array(arrc);
			
			while (ind <= text.length) {
				size -= (arrc*arrc);
				
				if (size > 0) {
					for(let f = 0; f < m.length; f++) {
						for(let c = 0; c < m.length; c++) {
							  m[f][c] = text[ind];
							  ind++;
						}
					}

					mt=new Array(arrc);
					mt1=new Array(arrc);
					mt2=new Array(arrc);
					mt3=new Array(arrc);
					
					for(let i = 0; i < mt.length; i++){
						mt[i]=new Array(arrc);
						mt1[i]=new Array(arrc);
						mt2[i]=new Array(arrc);
						mt3[i]=new Array(arrc);
					}

					//transpuesta
					for(let f = 0; f < m.length; f++) {
						for (let c = 0; c < m[f].length; c++) {
							  mt[c][f] = m[f][c];
						}
					}

					//espejo x y giro
					for(let f = 0; f < m.length; f++) {
						for (let c = m[f].length-1; c >= 0; c--) {
							  mt1[c][f] = mt[f][c];
						}
					}

					//espejo y
					for(let f = 0; f < m.length; f++) {
						for (let c = 0; c < m[f].length; c++) {
							  mt2[m.length-1-f][c] = mt1[f][c];
						}
					}
					
					//espejo x
					for(let f = 0; f < m.length; f++) {
						for (let c = 0; c < m[f].length; c++) {
							  mt3[f][m.length-1-c] = mt2[f][c];
						}
					}

					//rotado
					for(let f = 0; f < m.length; f++) {
						mt3[f]=this.Rotar(mt3[f],nR).split("");
					}

					m = mt3;
					ind -= (arrc*arrc);
					for(let f = 0; f < m.length; f++) {
						for(let c = 0; c < m.length; c++) {
							textR[ind] = m[f][c];
							ind++;
						}
					}

					let cadR="";
					for(let i = 0; i < textR.length; i++){
						cadR+=textR[i];
					}
					resultado=cadR;
					
				} else
					ind++;

				
				if(progreso==-1||progreso<parseInt((ind*100)/text.length)){
					progreso=parseInt((ind*100)/text.length);
					console.log(progreso+"% "+text.length);
				}
			}
		}
		console.log("operado");
		return resultado;
   }

   /**
	* Intercambia parejas de caracteres
	* @param {String} texto 
	*/
	static Truncar(text) {
		let t;
		let textR=new Array(text.length);

		for(let i = 0; i < text.length; i++)
			textR[i]=text[i];
		
		for(let i = 0; i < textR.length; i += 2) {
			if (i < textR.length - 1) {
				t = textR[i];
				textR[i] = textR[i + 1];
				textR[i + 1] = t;
			}
		}

		let cadR="";

		for(let i = 0; i < text.length; i++){	
			cadR+=textR[i];
		}
		console.log("truncado");
		return cadR;
	}

	/**
	 * Rota los elementos de una lista hacie la derecha
	 * @param {Array} La lista de elementos 
	 * @param {Int} El numero de rotaciones
	 */
	static Rotar(arr, n) {
		let textR=new Array(text.length);

		for(let i = 0; i < arr.length; i++)
			textR[i]=arr[i];
		
		let aux = "", tran = "";
		for(let i = 0; i < n; i++) {
			 tran = textR[textR.length - 1];
			 for(let j = 0; j < textR.length; j++) {
					aux = textR[j];
					textR[j] = tran;
					tran = aux;
			 }
		}

		let cadR="";

		for(let i = 0; i < arr.length; i++)	
			cadR+=textR[i];

		//console.log(textR);
		return cadR;

	}

	/**
	 * Rota los elementos de una lista hacie la izquierda
	 * @param {Array} La lista de elementos 
	 * @param {Int} El numero de rotaciones
	 */
	static RotarI(arr, n) {
		let textR=new Array(text.length);
		let cadR="";
		
		for(let i = 0; i < arr.length; i++)
			textR[i]=arr[i];
		
		let aux = 0, tran = 0;

		for(let i = 0; i < n; i++) {
			 tran = textR[0];
			 for(let j = textR.length - 1; j >= 0; j--) {
					aux = textR[j];
					textR[j] = tran;
					tran = aux;
			 }
		}

		for(let i = 0; i < arr.length; i++)	
			cadR+=textR[i];
		
		return cadR;

	}

	/**
	 * Convierte los elementos de una lista a su correspondiente numero char
	 * @param {String} cadena de elementos 
	 */
	static cadChar(str){
		let ch=[str.length];
		let str1="";
		for(let i in str)
			ch[i]=str.charCodeAt(i);
		return ch;
	}

	/**
	 * Convierte un numero a binario
	 * @param {Int} numero a convertir
	 */
	static cadBin(num){
		let bin="";
		while(num>=1){
			bin=(num%2)+bin;
			num=parseInt(num/2);
		}
		return bin;
	}

	static binCad(bin){
		let num=0,cu=1;
		for(let i=bin.length-1;i>=0;i--){
			if(bin[i]=="1"){
				num+=parseInt(cu);
			}
			cu=parseInt(cu*2);
		}
		return num;
	}


	/**
	 * Sustituye los caracteres por equivalente desfasado en un rango de caracteres especifico
	 * @param {String} Texto
	 * @param {String} Clave
	 * @param {Array} Lista de binarios de la clave 
	 * @param {Int} tipo de operacion 
	 */
	static nSutitucion(t,c,ab,tip){
		let des=0;
		let ch=[c.length];
		let cht=[t.length];
		let charList=new Array();
		let nCeros=0,nUnos=0,progreso=-1;

		ch=this.cadChar(c);
		cht=this.cadChar(t);

		charList.push("	");
		charList.push(String.fromCharCode(10));
		for (let index = 32; index <= 255; index++) {
			charList.push(String.fromCharCode(index));
		}
		
		for(let i of ab.split("")){
			if(i=="1")nUnos++;
			else nCeros++;
		}

		for(let i in ab.split("")){
			if(ab.split("")[i]=="1")des = parseInt((ch[ch.length - 1]) - nUnos + parseInt(i));
			else des = parseInt((ch[0]) - nCeros - parseInt(i));

			des-=ch.length;
			
			if(des<0)des*=-1;
			if(des==0)des++;

			for(let i in cht){
				//if (cht[i] != 10){
					if(tip==1)cht[i] = this.desfazar(String.fromCharCode(cht[i]),des,true,charList);
					else cht[i] = this.desfazar(String.fromCharCode(cht[i]),des,false,charList);
				//}
			}

			if(progreso==-1||progreso<parseInt((i*100)/ab.split("").length)){
				progreso=parseInt((i*100)/ab.split("").length);
				console.log(progreso+"% "+ab.split("").length);
			}
		}

		t="";
		for(let i in cht)
			t+=String.fromCharCode(cht[i]);
			
		console.log("sustituido");
		return t;
	}

	static desfazar(letra,desface,cifrar,charList){
		let newNLetra="";
		let index="";
		
		for (const key of charList) {
			if(key==letra){
				index=charList.indexOf(key);
				for (let i = 0; i < desface; i++) {
					if(cifrar){
						index++;
						if(index==charList.length){
							index=0;
						}
						newNLetra=charList[index];	
						
					}else{
						index--;
						if(index<0){
							index=charList.length-1;
						}
						newNLetra=charList[index];	
					}
				}

			}
		}
		
		if(newNLetra!=""){
			return newNLetra.charCodeAt(0);
		}else{
			return letra
		}
	}

}
