function showname () {
      var nameas = document.getElementById('text');
      var button = document.getElementById("first")
      nameas.innerHTML = button.files.item(0).name;
      document.getElementById("buttonText1").style.pointerEvents = "auto";

    };



