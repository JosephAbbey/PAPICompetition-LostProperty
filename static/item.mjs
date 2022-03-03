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
            width: 7rem;
            height: 7rem;
            display: inline-block;
            border-radius: 0.625rem;
            object-fit: cover;
          }
          .wrapper {
            display: grid;
            grid-template-columns: 7.5rem 12rem;
            padding: 1rem;
            margin: 0.5rem;
            border-radius: 1rem;
            border: 1px solid #000;
            width: fit-content;
            cursor: pointer;
            color: white;
          }
          span {
            font-size: 2rem;
            font-weight: 400;
            display: block;
          }
          .icon {
            height: 1rem;
            width: auto;
            border-radius: 0;
          }
          .colour {
            width: 1rem;
            height: 1rem;
            background-color: ${this.attrs.colour};
            border-radius: 20%;
            display: inline-block;
          }
        `;
    
        _template.innerHTML = `
          <div class="wrapper">
            <div>
              <img title="${this.attrs.title}" src="${config.PHOTO_API + this.attrs.image}" />
            </div>
            <div>
              <span>
                ${this.attrs.title}
              </span>
              <div class="colour"></div> ${this.attrs.colour}                   <br />
              <img class="icon" src="/static/icons/${this.attrs.category}.svg"></img> ${this.attrs.category}     <br />
              <img class="icon" src="/static/icons/door.svg"></img> ${this.attrs["found-in"]}  <br />
            </div>
          </div>
        `;

        this.onclick = () => window.location = `/item?id=${this.attrs.id}`;
    
        this.attachShadow({ mode: 'open' });
        this.shadowRoot.appendChild(_style);
        this.shadowRoot.appendChild(_template.content.cloneNode(true));
    }
}