//NAVBAR --------------------------------------
const logout = () => {
  _clearCookies();
  window.location.href = "/";
};

const _clearCookies = () => {
  let cookies = document.cookie.split(";");

  for (const cookie of cookies) {
    let igualPos = cookie.indexOf("=");
    let nomeCookie = igualPos > -1 ? cookie.substr(0, igualPos) : cookie;
    document.cookie =
      nomeCookie + "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
  }
};