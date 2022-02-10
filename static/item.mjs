export default class CatalogueItem extends HTMLElement {
    constructor() {
        super();

        this.attrs = {
            colour: this.attributes.colour.value,
            "found-in": this.attributes["found-in"].value,
            title: this.attributes.title.value,
            category: this.attributes.category.value
        }
    
        const _style = document.createElement('style');
        const _template = document.createElement('template');
    
        _style.innerHTML = `
        img {
            width: 100px;
            height: 100px;
            display: inline-block;
        }
        h1 {
          color: tomato;
          display: inline-block;
        }
        `;
    
        _template.innerHTML = `
        <img src="die" />
        <h1>
          ${this.attrs.title}
        </h1>
      `;
    
        this.attachShadow({ mode: 'open' });
        this.shadowRoot.appendChild(_style);
        this.shadowRoot.appendChild(_template.content.cloneNode(true));
    }
}