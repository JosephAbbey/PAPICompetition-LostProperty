export default function setURLParameter(param, value) {
    var url = new URL(window.location.href);
    url.searchParams.set(param, value);
    window.location = url;
}
