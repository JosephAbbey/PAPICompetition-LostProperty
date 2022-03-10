export default class NavTop extends HTMLElement {
    constructor() {
        super();

        const _style = document.createElement('style');
        const _template = document.createElement('template');

        _style.innerHTML = `
          .navbar {
            background-color: #393948;
            height: calc(3em + 9px);
            display: grid;
            grid-template-columns: 10em calc(100% - 10em);
          }

          .navbar > div:nth-of-type(1) {
            background-color: #5172E7;
            height: calc(3em + 9px);
            width: 10em;
            position: relative;
            cursor: pointer;
            display: inline-block;
          }

          .navbar > div:nth-of-type(1) > img {
            height: 80%;
            display: inline-block;
            margin-top: 3%;
            margin-left: 0.5em;
          }

          .navbar > div:nth-of-type(1) > span {
            position: absolute;
            inset: 1em 3.5em;
            color: aliceblue;
          }

          .navbar > div:nth-of-type(2) {
            display: inline-block;
          }

          .categories {
              display: flex;
              flex-wrap: nowrap;
              overflow-x: scroll;
              padding: 0.5em;
              background-color: #393948;
          }

          /* Scrollbar */
          /* width */
          ::-webkit-scrollbar {
              width: 10px;
              height: 10px;
          }

          /* Track */
          ::-webkit-scrollbar-track {
              background: #555;
          }

          /* Handle */
          ::-webkit-scrollbar-thumb {
              background: #999;
          }

          /* Handle on hover */
          ::-webkit-scrollbar-thumb:hover {
              background: #222;
          }
        `;

        _template.innerHTML = `
          <div class="navbar">
            <div onclick="window.location = '/'">
              <img src="/static/logo.png" alt="logo"></img>
              <span>LostProperty</span>
            </div>
            ${
                window.location.pathname == 'items'
                    ? `<div>
                        <div class="categories">
                          ${this.innerHTML}
                        </div>
                      </div>`
                    : ''
            }
          </div>
        `;

        this.attachShadow({ mode: 'open' });
        this.shadowRoot.appendChild(_style);
        this.shadowRoot.appendChild(_template.content.cloneNode(true));
    }
}
