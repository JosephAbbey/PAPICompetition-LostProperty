import * as config from "./config.mjs";

export default class CatalogueItem extends HTMLElement {
    constructor() {
        super();

        this.attrs = {
            colour: this.attributes.colour.value,
            "found-in": this.attributes["found-in"].value,
            title: this.attributes.title.value,
            category: this.attributes.category.value,
            image: this.attributes.image.value
        }
    
        const _style = document.createElement('style');
        const _template = document.createElement('template');
    
        _style.innerHTML = `
        img {
          width: 6rem;
          height: 6rem;
          display: inline-block;
        }
        div {
          display: grid;
          grid-template-columns: 6.5rem 12rem;
          padding: 1rem;
          margin: 0.5rem;
          border-radius: 1rem;
          border: 1px solid #000;
          width: fit-content;
        }
        `;
    
        _template.innerHTML = `
        <div>
          <img title="${this.attrs.title}" src="${config.PHOTO_API + this.attrs.image}" />
          <h1>
            ${this.attrs.title}
          </h1>
        </div>
      `;
    
        this.attachShadow({ mode: 'open' });
        this.shadowRoot.appendChild(_style);
        this.shadowRoot.appendChild(_template.content.cloneNode(true));
    }
}