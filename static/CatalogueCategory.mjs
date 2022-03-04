import * as config from "./config.mjs";

export default class CatalogueCategory extends HTMLElement {
    constructor() {
        super();

        this.attrs = {
            category: this.attributes.category.value
        }
    
        this._style = document.createElement('style');
        const _template = document.createElement('template');
    
        this.refreshStyle();
    
        _template.innerHTML = `
            <div id="${this.attrs.category}" class="wrapper">${this.attrs.category}</div>
        `;
            
        this.onclick = () => {
            var oldhash = window.location.hash
            window.location = `#${this.attrs.category}`
            document.querySelectorAll("catalogue-item").forEach(a => a.refreshStyle());
            if (oldhash) document.querySelectorAll(oldhash).forEach(a => a.refreshStyle());
            this.refreshStyle();
        };
        
        this.attachShadow({ mode: 'open' });
        this.shadowRoot.appendChild(this._style);
        this.shadowRoot.appendChild(_template.content.cloneNode(true));
    }

    refreshStyle() {
        this._style.innerHTML = `
            .wrapper {
                display: inline-block;
                padding: 0.25em;
                margin-left: 0.25em;
                margin-bottom: 0.25em;
                border-radius: 0.5em;
                border: 1px solid #000;
                min-width: 5em;
                text-align: center;
                cursor: pointer;
                ${((this.attrs.category == "All" && !Boolean(window.location.hash)) || window.location.hash.substring(1) == this.attrs.category) ? `
                    background-color: #000;
                ` : '' }
            }
        `;
    }
}