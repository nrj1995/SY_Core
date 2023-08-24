

     /***********************************go to top button********************************/
    //get the button
    mygototopbutton = document.getElementById('topbutton');

    //when user scrolls down 20px from the top of the document, shows the button
    window.onscroll = function () { scrollFunction() };

    function scrollFunction() {
      if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mygototopbutton.style.display = "block";
      } else {
        mygototopbutton.style.display = "none";
      }
    }

    //when user click goto top button, scroll to the top of the document
    function topFunction() {
      document.body.scrollTop = 0;//sfari
      document.documentElement.scrollTop = 0;// for crome, firefox
    }
    // Just for testing
    const animationSpeed = 50; // Counter increment per interval
    const intervalTime = 1000 / animationSpeed;
    // Set the target values for the counters
    if (document.getElementById('facebook-count')) {
    const facebookTarget = 1000;
    const twitterTarget = 500;
    const instagramTarget = 2000;

    // Set the starting values for the counters
    let facebookCount = 0;
    let twitterCount = 0;
    let instagramCount = 0;

    // Set the animation speed and interval time
    const animationSpeed = 50; // Counter increment per interval
    const intervalTime = 1000 / animationSpeed; // 1000ms = 1s, divide by animation speed to get interval time

    // Define the counter update function
    function updateCounters() {
      // Check if the counters have reached their target values
      if (facebookCount >= facebookTarget && twitterCount >= twitterTarget && instagramCount >= instagramTarget) {
        clearInterval(interval); // Stop the interval
      } else {
        // Increase the counter values
        if (facebookCount < facebookTarget) {
          facebookCount += Math.ceil((facebookTarget - facebookCount) / animationSpeed);
        }
        if (twitterCount < twitterTarget) {
          twitterCount += Math.ceil((twitterTarget - twitterCount) / animationSpeed);
        }
        if (instagramCount < instagramTarget) {
          instagramCount += Math.ceil((instagramTarget - instagramCount) / animationSpeed);
        }

        // Update the counter elements with the new values
        document.getElementById("facebook-count").innerHTML = facebookCount;
        document.getElementById("twitter-count").innerHTML = twitterCount;
        document.getElementById("instagram-count").innerHTML = instagramCount;
      }
    }
  }
    // Start the interval to update the counters
    const interval = setInterval(updateCounters, intervalTime);
  //  change the color of navbar on scroll
    $(document).ready(function () {
      $(window).scroll(function () {
        var scroll = $(window).scrollTop();
        if (scroll > 500) {
          $(".nav").css("background", "rgba(211,211,211)");
          $(".nav").css("transition", "background 1s");
        }

        else {
          $(".nav").css("background", "white");
          $(".menu__link").css("color","white");
        }
      })
    })

    // <!--start script for image carousel -->
    if (document.querySelector('.carousel-inner')){
    const images = document.querySelectorAll('.carousel-inner img');

    let currentImageIndex = 0;
    images[currentImageIndex].classList.add('active');

    setInterval(() => {
      images[currentImageIndex].classList.remove('active');
      currentImageIndex = (currentImageIndex + 1) % images.length;
      images[currentImageIndex].classList.add('active');
    }, 5000);
  }
  // <!--end script for image carousel -->
