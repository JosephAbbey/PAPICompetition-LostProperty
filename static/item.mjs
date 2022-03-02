import * as config from "./config.mjs";

export default class CatalogueItem extends HTMLElement {
    constructor() {
        super();

        var data = JSON.parse(this.attributes.data.value);

        this.attrs = {
            colour: data.colour,
            "found-in": data.location,
            title: data.title,
            category: data.category,
            id: this.attributes.id.value,
            image: this.attributes.id.value
        }
    
        const _style = document.createElement('style');
        const _template = document.createElement('template');
    
        _style.innerHTML = `
          img {
            width: 6rem;
            height: 6rem;
            display: inline-block;
            border-radius: 0.625rem;
          }
          div {
            display: grid;
            grid-template-columns: 6.5rem 12rem;
            padding: 1rem;
            margin: 0.5rem;
            border-radius: 1rem;
            border: 1px solid #000;
            width: fit-content;
            cursor: pointer;
          }
          span {
            font-size: 2rem;
            font-weight: 400;
          }
        `;
    
        _template.innerHTML = `
          <div>
            <img title="${this.attrs.title}" src="${config.PHOTO_API + this.attrs.image}" />
            <span>
              ${this.attrs.title}
            </span>
            ${this.attrs.colour}
            ${this.attrs.category}
            ${this.attrs["found-in"]}
          </div>
        `;

        this.onclick = () => window.location = `/item?id=${this.attrs.id}`;
    
        this.attachShadow({ mode: 'open' });
        this.shadowRoot.appendChild(_style);
        this.shadowRoot.appendChild(_template.content.cloneNode(true));
    }
}