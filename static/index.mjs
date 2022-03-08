import CatalogueItem from "./CatalogueItem.mjs";
import CatalogueCategory from "./CatalogueCategory.mjs";
import CataloguePagination from "./CataloguePagination.mjs";
import NavTop from "./NavTop.mjs";

customElements.define('catalogue-item', CatalogueItem);
customElements.define('catalogue-category', CatalogueCategory);
customElements.define('catalogue-pagination', CataloguePagination);
customElements.define('nav-top', NavTop);