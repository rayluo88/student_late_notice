// Set default arrival time to current time
document.addEventListener('DOMContentLoaded', function() {
    const timeInput = document.getElementById('arrival_time');
    if (timeInput) {
        const now = new Date();
        const time = now.toTimeString().slice(0, 5);
        timeInput.value = time;
    }
});

// Basic form validation
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function(e) {
        const requiredFields = form.querySelectorAll('[required]');
        let valid = true;
        
        requiredFields.forEach(field => {
            if (!field.value.trim()) {
                valid = false;
                field.classList.add('is-invalid');
            } else {
                field.classList.remove('is-invalid');
            }
        });
        
        if (!valid) {
            e.preventDefault();
        }
    });
}); 