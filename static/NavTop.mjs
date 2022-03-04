export default class NavTop extends HTMLElement {
    constructor() {
        super();
    
        const _style = document.createElement('style');
        const _template = document.createElement('template');
    
        _style.innerHTML = `
          .navbar {
            background-color: #393948;
            height: 3rem;
          }

          .navbar div {
            background-color: #5172E7;
            height: 100%;
            width: 10rem;
            position: relative;
            cursor: pointer;
          }

          .navbar div img {
            height: 80%;
            display: inline-block;
            margin-top: 3%;
            margin-left: 0.5rem;
          }

          .navbar span {
            position: absolute;
            inset: 0.8rem 3.5rem;
            color: aliceblue;
          }
        `;
    
        _template.innerHTML = `
          <div class="navbar">
            <div onclick="window.location = '/'">
              <img src="/static/logo.png" alt="logo"></img>
              <span>LostProperty</span>
            </div>
          </div>
        `;

        this.attachShadow({ mode: 'open' });
        this.shadowRoot.appendChild(_style);
        this.shadowRoot.appendChild(_template.content.cloneNode(true));
    }
}