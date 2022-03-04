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
            image: this.attributes.id.value,
            "in-list": Boolean(this.attributes["in-list"]?.value)
        }
    
        const _style = document.createElement('style');
        const _template = document.createElement('template');
    
        _style.innerHTML = `
          img {
            width: 7em;
            height: 7em;
            display: inline-block;
            border-radius: 0.625em;
            object-fit: cover;
          }
          span {
            font-size: 2em;
            font-weight: 400;
            display: block;
          }
          .wrapper {
            display: grid;
            grid-template-columns: 7.5em 1fr;
            margin: 0.5em;
          }
          .icon {
            height: 1em;
            width: auto;
            border-radius: 0;
          }
          .colour {
            width: 1em;
            height: 1em;
            background-color: ${this.attrs.colour};
            border-radius: 20%;
            display: inline-block;
          }
          ${this.attrs["in-list"] ? `
            .wrapper {
              grid-template-columns: 7.5em 12em;
              padding: 1em;
              border-radius: 1em;
              border: 1px solid #000;
              width: fit-content;
              cursor: pointer;
            }
          ` : `
            .wrapper {
              font-size: 3rem;
            }
          `}
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
              <img class="icon" alt="icon" src="/static/icons/${this.attrs.category}.svg"></img> ${this.attrs.category}     <br />
              <img class="icon" alt="icon" src="/static/icons/door.svg"></img> ${this.attrs["found-in"]}  <br />
            </div>
          </div>
        `;

        this.onclick = () => { if (this.attrs["in-list"]) { window.location = `/item?id=${this.attrs.id}` } };
    
        this.attachShadow({ mode: 'open' });
        this.shadowRoot.appendChild(_style);
        this.shadowRoot.appendChild(_template.content.cloneNode(true));
    }
}