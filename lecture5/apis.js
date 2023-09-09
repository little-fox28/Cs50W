document.addEventListener("DOMContentLoaded", function () {
  document.querySelector("form").onsubmit = () => {
    fetch("https://vn-public-apis.fpo.vn/districts/getAll")
      .then((response) => response.json())
      .then((data) => {
        const input = document.querySelector("#find").value.toLowerCase();
        const districtsData = data.data.data;

        for (const district of districtsData) {
          if (input === district.name.toLowerCase()) {
            document.querySelector("#district").innerHTML = district.name;
            return;
          } else {
            document.querySelector("#district").innerHTML =
              "Cannot find district";
          }
        }
      })
      .catch((error) => {
        console.log(error);
      });

    return false;
  };
});
