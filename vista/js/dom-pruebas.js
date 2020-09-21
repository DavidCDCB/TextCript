'use strict';

export default class DOMPruebas {

	static textToObj(text){
		return (new window.DOMParser()).parseFromString(text,"text/html");
	}

	static getRandomInt(min, max){
		return Math.floor(Math.random() * (max - min + 1)) + min;
	}

	static aplicarEstilo(obj,style){
		obj.className=style;//remplaza la clase anterior
	}

	static tieneAttr(attr,obj){
		return obj.hasAttribute(attr);
	}

	static tieneClass(clase,obj){
		return obj.classList.contains(clase);
	}

	static agregarText(text,obj){
		obj.insertAdjacentText("afterend",text);
	}

	static getAdyacente(tip,obj){
		if(tip=="sig"){
			obj=obj.nextSibling;
			while(obj.nodeName=="#text"){
				obj=obj.nextSibling;
			}
			return obj;
		}else{
			obj=obj.previousSibling;
			while(obj.nodeName=="#text"){
				obj=obj.previousSibling;
			}
			return obj;
		}
	}

	static getEvento(obj){
		return obj.getEventListeners();
	}

	static setEvento(obj,tipo,cb){
		this.getElemento(obj).addEventListener(tipo,cb);
	}

	static insertAfter(parent, node, ind) {
		parent.insertBefore(node, parent.childNodes[ind]);
	}

	static cambiarHijo(parent,n){
		parent.parentNode.replaceChild(n,parent);
	}

	static elementosEspecificos(obj,select){
		return obj.querySelectorAll(select);
	}

	static inArray(value,arr) {
		for (let i=0; i < arr.length; i++) {
			if (arr[i] === value) {
				return true;
			}
		}
		return false;
	}

	static ocultar(obj){
		if ( obj.style.display != 'none' )
			obj.style.display = 'none';
		else
			obj.style.display = '';
	}


	static index(id,contenedor){
		let hijo;
		if (contenedor.childElementCount>0) {
			for (let i = 0; hijo = contenedor.children[i]; i++) {
				if(hijo.id==id)return i;
			}
		}
	}

	static enlistarAttr(obj){
		let attr;
		let list=Array();
		for (let i = 0; attr = obj.attributes[i]; i++) {
			list.push([attr.nodeName,`'${attr.nodeValue}'`]);
		}
		return list;
	}

	static removerHijo(selector){
		let elemento = document.querySelector(selector);
		if (elemento) {
			elemento.parentNode.removeChild(elemento);
		}
	}

	static crearElemento(data=""){//div#id.clases ...,contenido
		let datos=data.split("#");
		let obj=document.createElement(datos[0]);
		obj.id=datos[1].split(".")[0];
		obj.innerHTML=datos[1].split(",")[1];;
		return obj;
	}

	static capturarNodos(nodo,elementos){//----------
		let hijo;
		if (nodo.childElementCount>0) {//verifica que el nodo tenga hijos
			for (let i = 0; hijo = nodo.children[i]; i++) {
				elementos.push([hijo.tagName,hijo.id,hijo.attributes,hijo.classList]);
				this.capturarNodos(hijo,elementos);
			}
		}
		return elementos;
	}

	static capturarTexto(parent,select){
		let elementos=parent.getElementsByTagName(select),text=Array();
		for(let dat of elementos)text.push(elementos.textContent);
		return text;
	}

	static getHijos(nodo){
		let arr=Array(),hijo;
		if (nodo.childElementCount>0) {
			for (let i = 0; hijo = nodo.children[i]; i++) arr.push(hijo);
			return arr;
		}else
			return null;
	}

	static cambiarTexto(nodo,ter,rem){
		let text="";
		if(nodo.tagName=="TEXTAREA")text+=nodo.value;
		else text+=nodo.innerText;
		for (let i = 0; text.search(ter) != -1; i++) {
			text=text.replace(ter,rem);
		}

		if(nodo.tagName=="TEXTAREA")nodo.value=text;
		else nodo.innerText=text;
	}

	static aplicarEventos(tip,list,cl){
		for(let dat of list){
			dat.addEventListener(tip,e=>{
				cl(e.target);
				e.stopPropagation();
				e.preventDefault();
			});
		}
	}

	static CrearTabla(id,tabla,m,estilos){
		let tab;
		let cont=0;
		if(!document.getElementById(tabla)){
			let contenedor=document.getElementById(id);
			tab=document.createElement('table');
			tab.setAttribute('id',tabla);
			contenedor.appendChild(tab);

			m.forEach(f=>{
				let tr=tab.insertRow();
				f.forEach(c=>{
					let td=tr.insertCell();
					td.setAttribute('id',cont++);
					td.setAttribute('value',c);
					td.innerHTML="<span id='celda'>"+c+"</span>";
				});
			});
			tab.classList.add(estilos);
		}
		return tab;
	}
    /**
     * Agrega el prefijo '#' a un identificador para aquellos casos en que se
     * requiera acceder mediante querySelector o queryAll
     * @param {String} id El id del elemento a buscar
     */
    static normalize(id) {
        id = id.trim();
        if (id.charAt(0) !== '#') {
            id = '#' + id;
        }
        return id;
    }

    /**
     * Devuelve true si se encuentra un elemento con el ID dado como argumento
     * @param {String} id El id del elemento a buscar
     */
    static existeElemento(id) {
        id = this.normalize(id);
        const elemento = document.querySelector(id);
        return (typeof(elemento) != 'undefined' && elemento != null);
    }

    /**
     * Retorna el elemento correspondiente a un ID dado como argumento
     * @param {String} idElemento El ID del elemento que se retornará
     */
    static getElemento(idElemento) {
        idElemento = this.normalize(idElemento);
        return document.querySelector(idElemento);
    }

    /**
     * Devuelve el total de elementos de un determinado tipo que se encuentran
     * dentro de un contenedor dado como segundo argumento
     * @param {String} tipoElemento El tipo de elemento a buscar ('input', 'div', 'textarea', ...)
     * @param {String} contenedor El elemento contenedor en el que se buscará
     */
    static totalElementos(tipoElemento, contenedor = document) {
        if (typeof(contenedor) === 'string') {
            contenedor = this.normalize(contenedor);
            contenedor = document.querySelector(contenedor);
        }
        return contenedor.getElementsByTagName(tipoElemento).length;
    }

    /**
     * Devuelve el número de hijos director de determinado tipo, existentes en un contenedor
     * @param {*} contenedor El ID del contenedor donde se buscarán los hijos directos
     * @param {*} tipoElemento El tipo de elemento a buscar ('input', 'div', 'textarea', ...)
     */
    static totalHijosDirectos(contenedor, tipoElemento) {
        contenedor = this.normalize(contenedor);
        return document.querySelectorAll(`${contenedor} > ${tipoElemento}`).length;
    }

    /**
     * Un simple ejemplo de cómo asignar contenido HTML en las celdas de una tabla
     * @param {String} idTabla El ID de la tabla que se alterará
     */
    static reemplazarContenidoTabla(idTabla) {
        let k = 0;
        let imagenes = ['eye.png', 'shaka-sign.png', 'slideshare-logo.png'];
        let tabla = this.getElemento(idTabla);

        for (let i = 1, fila; fila = tabla.rows[i]; i++) {
            for (let j = 0, celda; celda = fila.cells[j]; j++) {
                // la siguiente línea muestra el contenido actual de las celdas
                console.log(`Valor[${i}, ${j}] = ${celda.innerHTML}`);
                // enseguida se cambia los textos por defecto, por imágenes
                celda.innerHTML = `<img src="./vista/images/${imagenes[k]}" alt="img[${i}, ${j}]" width="64" height="64"/>`;
                k++;
                if (k === imagenes.length) {
                    k = 0;
                }
            }
        }
    }

	static listarTextoEtiquetas(contenedor=document){

		let listaElementosDelPadre=this.elementosEspecificos(contenedor, "a");

		let f=(elementoOnClick)=>{

			if(!this.tieneAttr("fueOprimido",elementoOnClick)){
				elementoOnClick.setAttribute("fueOprimido", "false");
				document.querySelector('#cdcbUltrarebuscado').classList.add(elementoOnClick.textContent);
				console.log(document.querySelector('#cdcbUltrarebuscado').classList);

			}
		}

		this.aplicarEventos("click", listaElementosDelPadre, f);

	}
    /*
        CONVERTIR A FUNCIONES FLECHA las funciones anteriores
        Funciones sugeridas:
        - Función que retorne un array de todos los elementos de determinado tipo dado como argumetno, en determinado contenedor
        - Función que reemplace cierta incidencia de texto por un nuevo texto, ambos dados como argumentos.
        * Función que retorne un objeto cuyos atributos corresponden a todas las entradas de datos dadas en un formulario.
        - Función que aplique una clase CSS cuyo nombre se da como argumento a los elementos hijos de un elemento dado
          como argumento
        - Devolver el número de elementos
        * Función que liste el texto de todas las etiquetas anchor a las que aún no se les ha dado click y que forman parte de
          un contenedor determinado

        Documentos sugeridos:
        - https://www.sitepoint.com/dom-manipulation-vanilla-javascript-no-jquery/
        - https://vanillajstoolkit.com/helpers/
        - http://eloquentjavascript.net/  <<
        - https://plainjs.com/javascript/
        - https://code.tutsplus.com/es/tutorials/the-30-css-selectors-you-must-memorize--net-16048
        - https://stackoverflow.com/questions/11455515/how-to-check-whether-dynamically-attached-event-listener-exists-or-not
    */

}
