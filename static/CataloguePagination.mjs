import setURLParameter from './setURLParameter.mjs';

export default class CataloguePagination extends HTMLElement {
    constructor() {
        super();

        window.CataloguePagination = { setURLParameter };

        this.attrs = {
            current: parseInt(this.attributes.current.value),
            final: parseInt(this.attributes.final.value),
        };

        this._style = document.createElement('style');
        const _template = document.createElement('template');

        this._style.innerHTML = `
        div {
            display: inline-block;
            padding: 0;
            margin-left: 0.25em;
            margin-bottom: 0.25em;
            border-radius: 0.5em;
            border: 1px solid #000;
            min-width: 5em;
            text-align: center;
        }

        button {
            font-size: 1.2em;
            color: white;
            padding: 0.25em 0.5em;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            border-radius: 0.25em;
            background: transparent;
            border: none;
            cursor: pointer;
        }

        button:disabled {
            color: #fff1;
        }

        button:disabled:hover {
            background: transparent;
        }

        button:hover {
            background-color: #11111188;
        }

        button.active {
            background-color: #11111188;
        }
        `;

        _template.innerHTML = `
            <div>
                <button
                    ${this.attrs.current > 2 ? '' : 'disabled'}
                    onclick="CataloguePagination.setURLParameter('page', '1')"
                >«</button>
                <button
                    ${this.attrs.current > 1 ? '' : 'disabled'}
                    onclick="CataloguePagination.setURLParameter('page', 
                        '${this.attrs.current - 1}'
                    )"
                >
                    ${this.attrs.current - 1 < 1 ? "&nbsp;&nbsp;" : this.attrs.current - 1}
                </button>
                <button class="active">${this.attrs.current}</button>
                <button
                    ${this.attrs.current < this.attrs.final ? '' : 'disabled'}
                    onclick="CataloguePagination.setURLParameter('page', 
                        '${this.attrs.current + 1}'
                    )"
                >
                    ${this.attrs.current + 1}
                </button>
                <button
                    ${
                        this.attrs.current < this.attrs.final - 1
                            ? ''
                            : 'disabled'
                    }
                    onclick="CataloguePagination.setURLParameter('page', 
                        '${this.attrs.final}'
                    )"
                >»</button>
            </div>
        `;

        this.attachShadow({ mode: 'open' });
        this.shadowRoot.appendChild(this._style);
        this.shadowRoot.appendChild(_template.content.cloneNode(true));
    }
}
