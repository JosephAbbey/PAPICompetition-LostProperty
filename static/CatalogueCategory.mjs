import * as config from './config.mjs';
import setURLParameter from './setURLParameter.mjs';

export default class CatalogueCategory extends HTMLElement {
    constructor() {
        super();

        this.attrs = {
            category: this.attributes.category.value,
        };

        this._style = document.createElement('style');
        const _template = document.createElement('template');

        this.refreshStyle();

        _template.innerHTML = `
            <div id="${this.attrs.category}" class="wrapper">
                ${
                    this.attrs.category != 'Other'
                        ? `<img class="icon" alt="icon" src="/static/icons/${this.attrs.category.toLowerCase()}.svg"></img>`
                        : ''
                }
                ${this.attrs.category}
            </div>
        `;

        this.onclick = () => setURLParameter('category', this.attrs.category);
        this.attachShadow({ mode: 'open' });
        this.shadowRoot.appendChild(this._style);
        this.shadowRoot.appendChild(_template.content.cloneNode(true));
    }

    refreshStyle() {
        this._style.innerHTML = `
            .wrapper {
                display: inline-block;
                padding: 0.25em 1em;
                margin-left: 0.25em;
                border-radius: 0.5em;
                border: 1px solid #000;
                min-width: 4em;
                text-align: center;
                cursor: pointer;
                ${
                    (this.attrs.category == 'All' &&
                        config.url.searchParams.get('category') == null) ||
                    config.url.searchParams.get('category') ==
                        this.attrs.category
                        ? `
                    background-color: #000;
                `
                        : ''
                }
            }
            .icon {
                height: 1em;
                width: auto;
                border-radius: 0;
            }
        `;
    }
}
