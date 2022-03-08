export default class CataloguePagination extends HTMLElement {
    constructor() {
        super();

        this.attrs = {
            current: this.attributes.current.value,
            final: this.attributes.final.value
        }
    
        this._style = document.createElement('style');
        const _template = document.createElement('template');

        this._style.innerHTML = `

        `
    
        _template.innerHTML = `
            <a href="/"><<</a>
            <a href="/"><</a>
            <a href="/">1</a>
            <a href="/">2</a>
            <a href="/">3</a>
            <a href="/">></a>
            <a href="/">>></a>
        `;
    
        this.attachShadow({ mode: 'open' });
        this.shadowRoot.appendChild(this._style);
        this.shadowRoot.appendChild(_template.content.cloneNode(true));
    }
}