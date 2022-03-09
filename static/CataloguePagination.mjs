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
        `;

        // var el = document.createElement('button');
        // if (!(this.attrs.current > 2)) el.disabled = true;
        // el.innerText = '«';
        // el.onclick = () => setURLParameter('page', '1');
        // _template.content.appendChild(el);

        // var el1 = document.createElement('button');
        // if (!(this.attrs.current > 1)) el1.disabled = true;
        // el1.innerText = this.attrs.current - 1;
        // el1.onclick = () => setURLParameter('page', this.attrs.current - 1);
        // _template.content.appendChild(el1);

        // var el2 = document.createElement('button');
        // el2.innerText = this.attrs.current;
        // _template.content.appendChild(el2);

        // var el3 = document.createElement('button');
        // if (!(this.attrs.current < this.attrs.final)) el3.disabled = true;
        // el3.innerText = this.attrs.current + 1;
        // el3.onclick = () => setURLParameter('page', this.attrs.current + 1);
        // _template.content.appendChild(el3);

        // var el4 = document.createElement('button');
        // if (!(this.attrs.current < this.attrs.final - 1)) el4.disabled = true;
        // el4.innerText = '»';
        // el4.onclick = () => setURLParameter('page', this.attrs.final);
        // _template.content.appendChild(el4);

        // var el5 = document.createElement('div');
        // el5.appendChild(_template.content.cloneNode(true));

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
                    ${this.attrs.current - 1}
                </button>
                <button>${this.attrs.current}</button>
                <button
                    ${
                        this.attrs.current < this.attrs.final - 1
                            ? ''
                            : 'disabled'
                    }
                    onclick="CataloguePagination.setURLParameter('page', 
                        '${this.attrs.current + 1}'
                    )"
                >
                    ${this.attrs.current + 1}
                </button>
                <button
                    ${this.attrs.current < this.attrs.final ? '' : 'disabled'}
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
