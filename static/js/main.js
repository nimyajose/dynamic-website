document.addEventListener("DOMContentLoaded", function() {
    let currentIndex = 0;
    const items = document.querySelectorAll('.carousel-item');
    const dots = document.querySelectorAll('.dot');

    function updateCarousel() {
        items.forEach((item, index) => {
            item.classList.remove('active', 'center');
            if (index === currentIndex) {
                item.classList.add('active');
                item.classList.add('center');
            } else if (index === (currentIndex - 1 + items.length) % items.length || index === (currentIndex + 1) % items.length) {
                item.classList.add('active');
            }
        });

        dots.forEach((dot, index) => {
            dot.classList.toggle('active', index === currentIndex);
        });

        // Move carousel
        document.querySelector('.carousel').style.transform = `translateX(-${currentIndex * 33.333}%)`;
    }

    // Event listeners for dots
    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            currentIndex = index;
            updateCarousel();
        });
    });

    // Auto-scroll or manual scroll logic can be added here
    updateCarousel(); // Initialize carousel
});
<script>
$(document).ready(function(){
    $(".event-carousel").owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        dots: true,
        autoplay: true,
        autoplayTimeout: 3000,
        autoplayHoverPause: true,
        center: true,
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 3
            }
        }
    });
});
</script>
